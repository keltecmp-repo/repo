# -*- coding: utf-8 -*-
"""
Módulo de Carregamento de Servidores - VERSÃO JSON
====================================================

Gerencia servidores de três fontes:
1. Arquivo local (lib/servers_config.py) - servidores pré-definidos
2. Arquivo remoto (JSON ou XML hospedado) - servidores atualizáveis
3. Configurações do usuário (settings.xml) - servidores personalizados

Prioridade: Remoto > Local > Usuário (configurável)

**NOVIDADE:** Suporte a JSON (mais simples e confiável que XML)
"""

import os
import json
import time
import xbmc
import xbmcvfs
import xml.etree.ElementTree as ET

try:
    # Tenta importar a configuração local de servidores
    from lib import servers_config
    HAS_LOCAL_CONFIG = True
except ImportError:
    HAS_LOCAL_CONFIG = False
    xbmc.log("[ServerLoader] lib/servers_config.py não encontrado - usando apenas config manual", xbmc.LOGWARNING)


class ServerLoader:
    """Carrega e gerencia servidores de múltiplas fontes"""
    
    def __init__(self, addon, profile_dir):
        self.addon = addon
        self.profile_dir = profile_dir
        self.cache_file = os.path.join(profile_dir, 'remote_servers_cache.json')
        
        # Configurações
        if HAS_LOCAL_CONFIG:
            self.config = servers_config.CONFIG
            self.remote_url = self.config.get('remote_config_url', '')
            self.cache_ttl = self.config.get('remote_cache_ttl', 3600)
            self.prefer_remote = self.config.get('prefer_remote', True)
            self.override_user = self.config.get('override_user_config', False)
            self.allow_user = self.config.get('allow_user_servers', True)
        else:
            self.remote_url = ''
            self.cache_ttl = 3600
            self.prefer_remote = False
            self.override_user = False
            self.allow_user = True
    
    def log(self, message, level=xbmc.LOGINFO):
        """Helper para logging"""
        xbmc.log(f"[ServerLoader] {message}", level)
    
    def get_all_servers(self):
        """
        Retorna todos os servidores de todas as fontes, ordenados por prioridade
        
        Ordem de carregamento (configurável):
        1. Servidores remotos (se prefer_remote=True)
        2. Servidores locais (se disponíveis)
        3. Servidores do usuário (se allow_user=True)
        """
        all_servers = []
        
        # 1. Carrega servidores remotos (se configurado)
        if self.remote_url and self.prefer_remote:
            remote_servers = self._load_remote_servers()
            if remote_servers:
                all_servers.extend(remote_servers)
                self.log(f"Carregados {len(remote_servers)} servidores remotos")
        
        # 2. Carrega servidores locais (se disponíveis)
        if HAS_LOCAL_CONFIG:
            local_servers = self._load_local_servers()
            if local_servers:
                all_servers.extend(local_servers)
                self.log(f"Carregados {len(local_servers)} servidores locais")
        
        # 3. Carrega servidores do usuário (se permitido)
        if self.allow_user and not self.override_user:
            user_servers = self._load_user_servers()
            if user_servers:
                all_servers.extend(user_servers)
                self.log(f"Carregados {len(user_servers)} servidores do usuário")
        
        # Remove duplicatas (baseado em URL + USERNAME)
        # IMPORTANTE: Mesma URL com usuários diferentes = servidores diferentes!
        seen = set()
        unique_servers = []
        for server in all_servers:
            url = server.get('url', '')
            username = server.get('username', '')
            # Chave única: URL + USERNAME
            key = f"{url}|{username}"
            
            if url and username and key not in seen:
                seen.add(key)
                unique_servers.append(server)
                self.log(f"  ✅ Adicionado: {server.get('name', '?')} ({url} + {username})", xbmc.LOGDEBUG)
            else:
                if not url or not username:
                    self.log(f"  ❌ Ignorado: {server.get('name', '?')} - URL ou USERNAME vazio", xbmc.LOGWARNING)
                else:
                    self.log(f"  ⚠️ Duplicado: {server.get('name', '?')} - Mesma URL+USERNAME", xbmc.LOGWARNING)
        
        # Ordena por prioridade (menor = mais prioritário)
        unique_servers.sort(key=lambda x: x.get('priority', 999))
        
        self.log(f"Total de servidores únicos carregados: {len(unique_servers)}")
        
        # Debug: mostra todos os servidores carregados
        for srv in unique_servers:
            self.log(f"  [{srv.get('priority', '?')}] {srv.get('name', 'Sem nome')} - {srv.get('source', '?')}", xbmc.LOGDEBUG)
        
        return unique_servers
    
    def _load_local_servers(self):
        """Carrega servidores do arquivo local lib/servers_config.py"""
        if not HAS_LOCAL_CONFIG:
            return []
        
        try:
            servers = servers_config.get_servidores()
            self.log(f"Servidores locais carregados: {len(servers)}")
            # Adiciona marcador de origem
            for server in servers:
                server['source'] = 'local'
            return servers
        except Exception as e:
            self.log(f"Erro ao carregar servidores locais: {e}", xbmc.LOGERROR)
            return []
    
    def _load_remote_servers(self):
        """
        Carrega servidores do arquivo remoto (JSON ou XML) com cache
        
        Detecta automaticamente o formato:
        - URL termina com .json → JSON
        - URL termina com .xml → XML
        - Caso contrário, tenta JSON primeiro, depois XML
        """
        if not self.remote_url:
            return []
        
        # Verifica se tem cache válido
        if self._is_cache_valid():
            self.log("Usando cache de servidores remotos")
            return self._load_from_cache()
        
        # Cache inválido ou inexistente, baixa do servidor
        try:
            self.log(f"Baixando servidores remotos de: {self.remote_url}")
            import requests
            
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(self.remote_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Detecta formato automaticamente
            servers = None
            
            # Tenta JSON primeiro (mais confiável)
            if self.remote_url.endswith('.json') or 'json' in self.remote_url.lower():
                self.log("Detectado formato JSON")
                servers = self._parse_remote_json(response.text)
            elif self.remote_url.endswith('.xml'):
                self.log("Detectado formato XML")
                servers = self._parse_remote_xml(response.content)
            else:
                # Tenta JSON primeiro
                self.log("Formato não detectado, tentando JSON...")
                servers = self._parse_remote_json(response.text)
                
                if not servers:
                    self.log("JSON falhou, tentando XML...")
                    servers = self._parse_remote_xml(response.content)
            
            if servers:
                # Salva no cache
                self._save_to_cache(servers)
                self.log(f"✅ Servidores remotos carregados: {len(servers)}")
                
                # Log detalhado dos servidores
                for srv in servers:
                    self.log(f"  → {srv.get('name', '?')} (ID: {srv.get('id', '?')})", xbmc.LOGDEBUG)
                
                return servers
            else:
                self.log("❌ Nenhum servidor encontrado no arquivo remoto", xbmc.LOGWARNING)
                return []
                
        except Exception as e:
            self.log(f"❌ Erro ao carregar servidores remotos: {e}", xbmc.LOGERROR)
            import traceback
            self.log(f"Traceback: {traceback.format_exc()}", xbmc.LOGDEBUG)
            # Tenta usar cache antigo como fallback
            return self._load_from_cache()
    
    def _parse_remote_json(self, json_text):
        """
        Parse JSON e retorna lista de servidores
        
        Formato esperado:
        {
            "servers": [
                {
                    "id": 1,
                    "name": "Servidor Principal",
                    "url": "http://example.com",
                    "username": "user",
                    "password": "pass",
                    "priority": 1,
                    "enabled": true
                }
            ]
        }
        """
        try:
            data = json.loads(json_text)
            servers = []
            
            # Suporta tanto {"servers": [...]} quanto [...]
            server_list = data.get('servers', data) if isinstance(data, dict) else data
            
            if not isinstance(server_list, list):
                self.log(f"Formato JSON inválido: esperado lista, recebido {type(server_list)}", xbmc.LOGERROR)
                return []
            
            for srv_data in server_list:
                try:
                    # Verifica se está habilitado
                    enabled = srv_data.get('enabled', True)
                    if not enabled:
                        self.log(f"Servidor {srv_data.get('name', '?')} desabilitado", xbmc.LOGDEBUG)
                        continue
                    
                    server = {
                        'id': int(srv_data.get('id', 0)),
                        'name': srv_data.get('name', 'Servidor'),
                        'url': srv_data.get('url', ''),
                        'username': srv_data.get('username', ''),
                        'password': srv_data.get('password', ''),
                        'priority': int(srv_data.get('priority', 999)),
                        'source': 'remote'
                    }
                    
                    # Valida campos obrigatórios
                    if server['url'] and server['username'] and server['password']:
                        servers.append(server)
                        self.log(f"✅ Servidor JSON carregado: {server['name']} (ID: {server['id']})", xbmc.LOGDEBUG)
                    else:
                        self.log(f"❌ Servidor {server['name']} ignorado - campos vazios", xbmc.LOGWARNING)
                        
                except Exception as e:
                    self.log(f"Erro ao parsear servidor JSON: {e}", xbmc.LOGERROR)
                    continue
            
            self.log(f"Parse JSON completo: {len(servers)} servidores válidos")
            return servers
            
        except json.JSONDecodeError as e:
            self.log(f"Erro ao decodificar JSON: {e}", xbmc.LOGERROR)
            return []
        except Exception as e:
            self.log(f"Erro inesperado ao parsear JSON: {e}", xbmc.LOGERROR)
            return []
    
    def _parse_remote_xml(self, xml_content):
        """
        Parse XML e retorna lista de servidores (mantido para compatibilidade)
        """
        try:
            root = ET.fromstring(xml_content)
            servers = []
            
            for server_elem in root.findall('server'):
                try:
                    enabled = server_elem.findtext('enabled', 'true').lower() == 'true'
                    if not enabled:
                        continue
                    
                    server = {
                        'id': int(server_elem.findtext('id', '0')),
                        'name': server_elem.findtext('n', 'Servidor'),
                        'url': server_elem.findtext('url', ''),
                        'username': server_elem.findtext('username', ''),
                        'password': server_elem.findtext('password', ''),
                        'priority': int(server_elem.findtext('priority', '999')),
                        'source': 'remote'
                    }
                    
                    # Valida campos obrigatórios
                    if server['url'] and server['username'] and server['password']:
                        servers.append(server)
                        self.log(f"✅ Servidor XML carregado: {server['name']} (ID: {server['id']})", xbmc.LOGDEBUG)
                    else:
                        self.log(f"❌ Servidor {server['name']} ignorado - campos vazios", xbmc.LOGWARNING)
                        
                except Exception as e:
                    self.log(f"Erro ao parsear servidor XML: {e}", xbmc.LOGERROR)
                    continue
            
            self.log(f"Parse XML completo: {len(servers)} servidores válidos")
            return servers
            
        except ET.ParseError as e:
            self.log(f"Erro ao parsear XML: {e}", xbmc.LOGERROR)
            return []
        except Exception as e:
            self.log(f"Erro inesperado ao parsear XML: {e}", xbmc.LOGERROR)
            return []
    
    def _load_user_servers(self):
        """Carrega servidores configurados pelo usuário no settings.xml"""
        servers = []
        
        for i in range(1, 6):
            url = self.addon.getSetting(f'server{i}_url') or ''
            user = self.addon.getSetting(f'server{i}_user') or ''
            passwd = self.addon.getSetting(f'server{i}_pass') or ''
            name = self.addon.getSetting(f'server{i}_name') or ''
            
            if url and user and passwd:
                # Nome automático se vazio
                if not name or not name.strip():
                    try:
                        domain = url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
                        name = f"{domain}"
                    except:
                        name = f"Servidor {i}"
                
                servers.append({
                    'id': i + 100,  # IDs 101-105 para servidores do usuário
                    'name': name,
                    'url': url,
                    'username': user,
                    'password': passwd,
                    'priority': i + 100,  # Menor prioridade que pré-definidos
                    'source': 'user'
                })
        
        return servers
    
    def _is_cache_valid(self):
        """Verifica se o cache de servidores remotos ainda é válido"""
        if not os.path.exists(self.cache_file):
            return False
        
        try:
            # Verifica idade do arquivo
            mtime = os.path.getmtime(self.cache_file)
            age = time.time() - mtime
            is_valid = age < self.cache_ttl
            
            if is_valid:
                self.log(f"Cache válido (idade: {int(age)}s / TTL: {self.cache_ttl}s)")
            else:
                self.log(f"Cache expirado (idade: {int(age)}s / TTL: {self.cache_ttl}s)")
            
            return is_valid
        except Exception as e:
            self.log(f"Erro ao verificar cache: {e}", xbmc.LOGERROR)
            return False
    
    def _load_from_cache(self):
        """Carrega servidores do cache"""
        try:
            if not os.path.exists(self.cache_file):
                return []
            
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            servers = data.get('servers', [])
            self.log(f"Carregados {len(servers)} servidores do cache")
            return servers
        except Exception as e:
            self.log(f"Erro ao carregar cache: {e}", xbmc.LOGERROR)
            return []
    
    def _save_to_cache(self, servers):
        """Salva servidores no cache"""
        try:
            # Garante que o diretório existe
            if not os.path.exists(self.profile_dir):
                os.makedirs(self.profile_dir)
            
            cache_data = {
                'timestamp': time.time(),
                'servers': servers
            }
            
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            
            self.log(f"Cache salvo: {len(servers)} servidores")
        except Exception as e:
            self.log(f"Erro ao salvar cache: {e}", xbmc.LOGERROR)