# -*- coding: utf-8 -*-
# SERVER_LOADER_VERSION = "5.0"
"""
Modulo de Carregamento de Servidores v5.0
==========================================
Parser JSON proprio - nao usa json.loads pois o Kodi tem um bug
onde ValueError nao esta no escopo do modulo json, causando NameError.
"""

import os
import re
import sys
import time
import xbmc
import xbmcvfs
import xml.etree.ElementTree as ET

# Silencia loggers que vazam URLs nos logs do Kodi
try:
    import logging as _log
    _log.getLogger('urllib3').setLevel(_log.CRITICAL)
    _log.getLogger('urllib3.connectionpool').setLevel(_log.CRITICAL)
    _log.getLogger('requests').setLevel(_log.CRITICAL)
    _log.getLogger('root').setLevel(_log.CRITICAL)
except Exception:
    pass

try:
    from lib import servers_config
    HAS_LOCAL_CONFIG = True
except ImportError:
    HAS_LOCAL_CONFIG = False
    xbmc.log("[ServerLoader v5.0] lib/servers_config.py nao encontrado", xbmc.LOGWARNING)


# ===========================================================================
# PARSER JSON PROPRIO
# Nao depende do modulo json do Python (que causa NameError no Kodi).
# Usa apenas re e operacoes de string.
# ===========================================================================

def _get_str(block, key):
    m = re.search(r'"' + key + r'"\s*:\s*"([^"]*)"', block)
    return m.group(1) if m else ''

def _get_int(block, key, default=0):
    m = re.search(r'"' + key + r'"\s*:\s*(\d+)', block)
    return int(m.group(1)) if m else default

def _get_bool(block, key, default=True):
    m = re.search(r'"' + key + r'"\s*:\s*(true|false)', block, re.IGNORECASE)
    return m.group(1).lower() == 'true' if m else default

def _extract_blocks(text):
    """Extrai blocos {} de dentro do array servers: [...].
    Usa bracket_depth para nao parar prematuramente em ] internos.
    """
    sm = re.search(r'"servers"\s*:\s*\[', text)
    if not sm:
        return []
    tail = text[sm.end():]
    depth = 0          # profundidade de chaves {}
    bracket_depth = 1  # ja estamos dentro do [ principal
    start = -1
    blocks = []
    in_str = False
    esc = False
    for i, c in enumerate(tail):
        if esc:
            esc = False
            continue
        if c == '\\' and in_str:
            esc = True
            continue
        if c == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if c == '{':
            if depth == 0:
                start = i
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0 and start != -1:
                blocks.append(tail[start:i+1])
                start = -1
        elif c == '[':
            bracket_depth += 1
        elif c == ']':
            bracket_depth -= 1
            if bracket_depth == 0:
                break  # fim do array servers
    return blocks

def parse_server_json(text):
    """
    Faz parse do JSON de servidores sem usar json.loads.
    Retorna (dict, True) ou (None, False).
    """
    try:
        if isinstance(text, (bytes, bytearray)):
            text = text.decode('utf-8-sig', errors='ignore')
        text = text.strip()
        if text and ord(text[0]) == 0xFEFF:
            text = text[1:]

        # Extrai debug_mode da raiz
        dm = re.search(r'"debug_mode"\s*:\s*(true|false)', text, re.IGNORECASE)
        debug_mode = dm.group(1).lower() == 'true' if dm else False

        # Extrai servidores
        servers = []
        for block in _extract_blocks(text):
            srv_id = _get_int(block, 'id')
            if srv_id == 0:
                continue
            if not _get_bool(block, 'enabled', True):
                continue
            url      = _get_str(block, 'url')
            username = _get_str(block, 'username')
            password = _get_str(block, 'password')
            if url and username and password:
                servers.append({
                    'id':       srv_id,
                    'name':     _get_str(block, 'name') or 'Servidor',
                    'url':      url,
                    'username': username,
                    'password': password,
                    'priority': _get_int(block, 'priority', 999),
                    'source':   'remote'
                })

        return {'debug_mode': debug_mode, 'servers': servers}, True

    except BaseException as e:
        xbmc.log("[ServerLoader v5.0] Erro no parser: " + str(e), xbmc.LOGERROR)
        return None, False


# ===========================================================================
# SERVER LOADER CLASS
# ===========================================================================

class ServerLoader:
    """Carrega e gerencia servidores de multiplas fontes."""

    def __init__(self, addon, profile_dir):
        xbmc.log("[ServerLoader v5.0] inicializado", xbmc.LOGINFO)
        self.addon = addon
        self.profile_dir = profile_dir
        self.cache_file = os.path.join(profile_dir, 'remote_servers_cache.json')

        if HAS_LOCAL_CONFIG:
            self.config = servers_config.CONFIG
            self.remote_url  = self.config.get('remote_config_url', '')
            self.cache_ttl   = self.config.get('remote_cache_ttl', 3600)
            self.prefer_remote = self.config.get('prefer_remote', True)
            self.override_user = self.config.get('override_user_config', False)
            self.allow_user  = self.config.get('allow_user_servers', True)
        else:
            self.remote_url  = ''
            self.cache_ttl   = 3600
            self.prefer_remote = False
            self.override_user = False
            self.allow_user  = True

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    def _is_debug(self):
        """Le debug_mode do cache. Padrao: False."""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    raw = f.read()
                dm = re.search(r'"debug_mode"\s*:\s*(true|false)', raw, re.IGNORECASE)
                return dm.group(1).lower() == 'true' if dm else False
        except Exception:
            pass
        return False

    def log(self, message, level=xbmc.LOGINFO):
        if level == xbmc.LOGDEBUG and not self._is_debug():
            return
        xbmc.log("[ServerLoader] " + str(message), level)

    # ------------------------------------------------------------------
    # Ponto de entrada
    # ------------------------------------------------------------------

    def get_all_servers(self):
        all_servers = []

        if self.remote_url and self.prefer_remote:
            remote = self._load_remote_servers()
            if remote:
                all_servers.extend(remote)
                self.log("Servidores remotos: " + str(len(remote)))

        if HAS_LOCAL_CONFIG:
            local = self._load_local_servers()
            if local:
                all_servers.extend(local)
                self.log("Servidores locais: " + str(len(local)))

        if self.allow_user and not self.override_user:
            user = self._load_user_servers()
            if user:
                all_servers.extend(user)
                self.log("Servidores do usuario: " + str(len(user)))

        # Remove duplicatas
        seen = set()
        unique = []
        for s in all_servers:
            key = s.get('url', '') + '|' + s.get('username', '')
            if key not in seen and s.get('url') and s.get('username'):
                seen.add(key)
                unique.append(s)

        unique.sort(key=lambda x: x.get('priority', 999))
        self.log("Total de servidores unicos carregados: " + str(len(unique)))
        return unique

    # ------------------------------------------------------------------
    # Fontes
    # ------------------------------------------------------------------

    def _load_local_servers(self):
        if not HAS_LOCAL_CONFIG:
            return []
        try:
            servers = servers_config.get_servidores()
            for s in servers:
                s['source'] = 'local'
            return servers
        except Exception as e:
            self.log("Erro ao carregar servidores locais: " + str(e), xbmc.LOGERROR)
            return []

    def _load_remote_servers(self):
        if not self.remote_url:
            return []
        if self._is_cache_valid():
            cached = self._load_from_cache()
            # Se o cache tem servidores validos, usa. Senao redownload.
            if len(cached) > 0:
                self.log("Usando cache de servidores remotos")
                return cached
            self.log("Cache invalido ou vazio, redownload forcado")
        try:
            self.log("Atualizando lista de servidores...")
            import requests as _req
            r = _req.get(self.remote_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            r.raise_for_status()
            _raw = r.content
            _txt = _raw.decode("utf-8-sig", errors="ignore") if isinstance(_raw, (bytes, bytearray)) else _raw
            _blocos = _extract_blocks(_txt)
            xbmc.log("[ServerLoader-DIAG] blocos=" + str(len(_blocos)) + " inicio=" + repr(_txt[:60]), xbmc.LOGINFO)
            data, ok = parse_server_json(_raw)
            if ok and data and data.get('servers'):
                servers = data['servers']
                debug_mode = data.get('debug_mode', False)
                self._save_to_cache(servers, debug_mode)
                self.log("Servidores carregados: " + str(len(servers)))
                return servers
            else:
                self.log("Nenhum servidor encontrado no arquivo remoto", xbmc.LOGWARNING)
                return self._load_from_cache()
        except Exception as e:
            self.log("Falha ao atualizar servidores remotos.", xbmc.LOGERROR)
            return self._load_from_cache()

    def _load_user_servers(self):
        servers = []
        for i in range(1, 6):
            url    = self.addon.getSetting('server' + str(i) + '_url') or ''
            user   = self.addon.getSetting('server' + str(i) + '_user') or ''
            passwd = self.addon.getSetting('server' + str(i) + '_pass') or ''
            name   = self.addon.getSetting('server' + str(i) + '_name') or ''
            if url and user and passwd:
                if not name.strip():
                    try:
                        name = url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
                    except Exception:
                        name = 'Servidor ' + str(i)
                servers.append({
                    'id': i + 100, 'name': name, 'url': url,
                    'username': user, 'password': passwd,
                    'priority': i + 100, 'source': 'user'
                })
        return servers

    # ------------------------------------------------------------------
    # Cache - usa re em vez de json para leitura tambem
    # ------------------------------------------------------------------

    def _is_cache_valid(self):
        if not os.path.exists(self.cache_file):
            return False
        try:
            return (time.time() - os.path.getmtime(self.cache_file)) < self.cache_ttl
        except Exception:
            return False

    def _load_from_cache(self):
        """Le cache usando re para nao depender do modulo json."""
        try:
            if not os.path.exists(self.cache_file):
                return []
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                raw = f.read()
            data, ok = parse_server_json(raw)
            if ok and data and data.get('servers'):
                return data['servers']
        except Exception:
            pass
        return []

    def _save_to_cache(self, servers, debug_mode=False):
        """Salva cache como JSON gerado manualmente (sem modulo json)."""
        try:
            if not os.path.exists(self.profile_dir):
                os.makedirs(self.profile_dir)

            def esc(s):
                return str(s).replace('\\', '\\\\').replace('"', '\\"')

            lines = ['{\n']
            lines.append('  "debug_mode": ' + ('true' if debug_mode else 'false') + ',\n')
            lines.append('  "timestamp": ' + str(int(time.time())) + ',\n')
            lines.append('  "servers": [\n')
            for idx, s in enumerate(servers):
                comma = '' if idx == len(servers) - 1 else ','
                lines.append('    {\n')
                lines.append('      "id": '       + str(s.get('id', 0))           + ',\n')
                lines.append('      "name": "'    + esc(s.get('name', ''))        + '",\n')
                lines.append('      "url": "'     + esc(s.get('url', ''))         + '",\n')
                lines.append('      "username": "' + esc(s.get('username', ''))   + '",\n')
                lines.append('      "password": "' + esc(s.get('password', ''))   + '",\n')
                lines.append('      "priority": ' + str(s.get('priority', 999))   + ',\n')
                lines.append('      "source": "'  + esc(s.get('source', 'remote'))+ '",\n')
                lines.append('      "enabled": true\n')
                lines.append('    }' + comma + '\n')
            lines.append('  ]\n')
            lines.append('}\n')

            with open(self.cache_file, 'w', encoding='utf-8') as f:
                f.writelines(lines)

            self.log("Cache salvo: " + str(len(servers)) + " servidores, debug_mode=" + str(debug_mode))
        except Exception as e:
            self.log("Erro ao salvar cache: " + str(e), xbmc.LOGERROR)