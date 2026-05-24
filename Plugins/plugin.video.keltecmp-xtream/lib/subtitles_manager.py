# -*- coding: utf-8 -*-
# ============================================================================
# KELTEC MEDIA PLAY - LEGENDAS AUTOMATICAS v2.0
# ============================================================================
# Arquivo: lib/subtitles_manager.py
#
# COMO USAR: Nao requer configuracao. Funciona anonimamente.
# Para mais downloads (sem limite diario), configure API Key em:
#   https://www.opensubtitles.com/en/consumers
#
# APIs suportadas:
#   1. OpenSubtitles REST v1 (com API key pessoal)
#   2. OpenSubtitles XML-RPC (anonimo - sem configuracao)
# ============================================================================

import os
import time
import threading

try:
    import requests as _req
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

try:
    import xmlrpc.client as _xmlrpc
    _HAS_XMLRPC = True
except ImportError:
    _HAS_XMLRPC = False

try:
    import xbmc
    import xbmcgui
    _HAS_KODI = True
except ImportError:
    _HAS_KODI = False

# -- Constantes ----------------------------------------------------------------
_OS_REST_BASE    = 'https://api.opensubtitles.com/api/v1'
_OS_XMLRPC_URL   = 'https://opensubtitles-v3.strem.io/xml-rpc'
# User-agent aprovado pelo OpenSubtitles para testes/apps Kodi
_OS_USER_AGENT   = 'KelTecMediaPlay v2.0'
_CACHE_TTL       = 86400 * 7  # 7 dias

# Mapeamento idioma -> codigo
_LANG_MAP = {
    'Portugues (Brasil)':   {'rest': 'pt-BR', 'xmlrpc': 'pob'},
    'Portugues (Portugal)': {'rest': 'pt-PT', 'xmlrpc': 'por'},
    'Ingles':               {'rest': 'en',    'xmlrpc': 'eng'},
    'Espanhol':             {'rest': 'es',    'xmlrpc': 'spa'},
    'Frances':              {'rest': 'fr',    'xmlrpc': 'fre'},
    'Italiano':             {'rest': 'it',    'xmlrpc': 'ita'},
    'Alemao':               {'rest': 'de',    'xmlrpc': 'ger'},
}
_LANG_NAMES = list(_LANG_MAP.keys())
SUBTITLE_LANG_NAMES = _LANG_NAMES


def _log(msg, level=None):
    if _HAS_KODI:
        lvl = level if level is not None else xbmc.LOGDEBUG
        xbmc.log(f'[KelTec-Subs] {msg}', lvl)


# -----------------------------------------------------------------------------
class SubtitlesManager:
    """
    Busca e baixa legendas via OpenSubtitles.
    Modo 1 (preferido): REST API v1 com API key pessoal do usuario.
    Modo 2 (fallback):  XML-RPC anonimo - funciona sem configuracao.
    """

    def __init__(self, addon, profile_dir):
        self._addon       = addon
        self._profile_dir = profile_dir
        self._cache_dir   = os.path.join(profile_dir, 'subtitles_cache')
        self._xmlrpc_token = None
        self._xmlrpc_ts    = 0
        self._lock         = threading.Lock()
        self._ensure_cache_dir()

    def _ensure_cache_dir(self):
        try:
            if not os.path.exists(self._cache_dir):
                os.makedirs(self._cache_dir)
        except Exception:
            pass

    def _get_api_key(self):
        """
        Retorna API key do OpenSubtitles.
        Prioridade:
          1. Settings do KelTec (campo opensubtitles_api_key)
          2. Settings do add-on oficial service.subtitles.opensubtitles.com
          3. Settings do add-on OpenSubtitles legado
        """
        try:
            # 1. Chave configurada diretamente no KelTec
            key = (self._addon.getSetting('opensubtitles_api_key') or '').strip()
            if key:
                return key
        except Exception:
            pass
        try:
            # 2. Add-on oficial OpenSubtitles.com (novo)
            import xbmcaddon as _xa
            os_addon = _xa.Addon('service.subtitles.opensubtitles.com')
            key = (os_addon.getSetting('APIKey') or '').strip()
            if key:
                _log('API key lida do add-on service.subtitles.opensubtitles.com')
                return key
        except Exception:
            pass
        try:
            # 3. Add-on OpenSubtitles legado
            import xbmcaddon as _xa
            os_addon = _xa.Addon('service.subtitles.opensubtitles')
            key = (os_addon.getSetting('OSUser') or '').strip()
            # Legado usa usuario/senha, nao API key - retorna vazio
        except Exception:
            pass
        return ''

    def _get_os_credentials(self):
        """
        Retorna (username, password) do add-on OpenSubtitles para XML-RPC autenticado.
        Login autenticado tem limite diario maior que anonimo.
        """
        try:
            import xbmcaddon as _xa
            os_addon = _xa.Addon('service.subtitles.opensubtitles.com')
            user = (os_addon.getSetting('OSuser') or '').strip()
            pwd  = (os_addon.getSetting('OSpass') or '').strip()
            if user and pwd:
                return user, pwd
        except Exception:
            pass
        return '', ''

    def _get_lang_pref(self):
        """
        Retorna (rest_code, xmlrpc_code, display_name) do idioma preferido.
        NAO adiciona fallbacks automaticos - o usuario escolheu um idioma especifico.
        """
        try:
            idx = int(self._addon.getSetting('subtitle_lang') or '0')
            key = _LANG_NAMES[idx] if idx < len(_LANG_NAMES) else _LANG_NAMES[0]
        except Exception:
            key = _LANG_NAMES[0]
        pref = _LANG_MAP[key]
        return pref['rest'], pref['xmlrpc'], key

    # -- XMLRPC (anonimo - sem API key) ----------------------------------------

    def _xmlrpc_login(self):
        """
        Login no OpenSubtitles XML-RPC.
        Usa credenciais do add-on oficial se disponivel (mais downloads/dia).
        Fallback para login anonimo.
        """
        if not _HAS_XMLRPC:
            return None
        now = time.time()
        if self._xmlrpc_token and (now - self._xmlrpc_ts) < 800:
            return self._xmlrpc_token
        try:
            user, pwd = self._get_os_credentials()
            proxy  = _xmlrpc.ServerProxy(_OS_XMLRPC_URL, allow_none=True)
            result = proxy.LogIn(user, pwd, 'pt-BR', _OS_USER_AGENT)
            if result.get('status', '').startswith('200'):
                self._xmlrpc_token = result.get('token', '')
                self._xmlrpc_ts    = now
                _log(f'XML-RPC login OK ({"autenticado" if user else "anonimo"})')
                return self._xmlrpc_token
            _log(f'XML-RPC login falhou: {result.get("status")}', xbmc.LOGWARNING if _HAS_KODI else None)
        except Exception as e:
            _log(f'XML-RPC login erro: {e}')
        return None

    def _search_xmlrpc(self, title, year=0, xmlrpc_lang='pob', imdb_id=None):
        """Busca via XML-RPC anonimo. Retorna lista normalizada."""
        token = self._xmlrpc_login()
        if not token:
            return []
        try:
            proxy = _xmlrpc.ServerProxy(_OS_XMLRPC_URL, allow_none=True)
            queries = []
            # Busca por IMDB ID (mais precisa)
            if imdb_id:
                clean_imdb = imdb_id.replace('tt', '')
                queries.append({'sublanguageid': xmlrpc_lang, 'imdbid': clean_imdb})
            # Busca por titulo + ano
            query_str = f'{title} {year}' if year else title
            queries.append({'sublanguageid': xmlrpc_lang, 'query': query_str})
            # Fallback ingles
            if xmlrpc_lang != 'eng':
                queries.append({'sublanguageid': 'eng', 'query': query_str})

            result = proxy.SearchSubtitles(token, queries)
            if result.get('status', '').startswith('200'):
                data = result.get('data', [])
                if not isinstance(data, list):
                    return []
                subs = []
                seen = set()
                for item in data:
                    fid = item.get('IDSubtitleFile', '')
                    if fid in seen:
                        continue
                    seen.add(fid)
                    lang = item.get('SubLanguageID', '')
                    # Normaliza codigo de idioma
                    lang_display = {'pob': 'PT-BR', 'por': 'PT-PT', 'eng': 'EN',
                                    'spa': 'ES',   'fre': 'FR',   'ita': 'IT',
                                    'ger': 'DE'}.get(lang, lang.upper())
                    subs.append({
                        'file_id':     fid,
                        'download_url': item.get('SubDownloadLink', ''),
                        'file_name':   item.get('SubFileName', ''),
                        'language':    lang_display,
                        'downloads':   int(item.get('SubDownloadsCnt', 0) or 0),
                        'rating':      float(item.get('SubRating', 0) or 0),
                        'hearing_impaired': item.get('SubHearingImpaired', '0') == '1',
                        'source':      'xmlrpc',
                    })
                return subs
        except Exception as e:
            _log(f'XML-RPC search erro: {e}')
        return []

    # -- REST v1 (com API key) -------------------------------------------------

    def _search_rest(self, title, year=0, rest_langs=None, imdb_id=None, tmdb_id=None):
        """Busca via REST API v1. Requer API key valida."""
        if not _HAS_REQUESTS:
            return []
        api_key = self._get_api_key()
        if not api_key:
            return []
        if rest_langs is None:
            rest_langs = ['pt-BR', 'en']
        try:
            params = {
                'query':          title,
                'languages':      ','.join(rest_langs),
                'order_by':       'download_count',
                'order_direction':'desc',
                'per_page':       '20',
            }
            if year:
                params['year'] = str(year)
            if imdb_id:
                params['imdb_id'] = imdb_id.replace('tt', '')
            if tmdb_id:
                params['tmdb_id'] = str(tmdb_id)

            resp = _req.get(
                f'{_OS_REST_BASE}/subtitles',
                headers={
                    'Content-Type': 'application/json',
                    'Accept':       'application/json',
                    'Api-Key':      api_key,
                    'User-Agent':   _OS_USER_AGENT,
                },
                params=params,
                timeout=12
            )
            if resp.status_code == 401:
                _log('API key invalida (401). Use sua chave em opensubtitles.com/en/consumers',
                     xbmc.LOGWARNING if _HAS_KODI else None)
                return []
            if resp.status_code != 200:
                _log(f'REST search: HTTP {resp.status_code}')
                return []

            subs = []
            for item in resp.json().get('data', []):
                attrs = item.get('attributes', {})
                files = attrs.get('files', [])
                if not files:
                    continue
                lang = attrs.get('language', '')
                lang_display = {'pt-BR': 'PT-BR', 'pt-PT': 'PT-PT',
                                'en': 'EN', 'es': 'ES'}.get(lang, lang.upper())
                subs.append({
                    'file_id':     files[0].get('file_id', ''),
                    'download_url': '',
                    'file_name':   files[0].get('file_name', ''),
                    'language':    lang_display,
                    'downloads':   attrs.get('download_count', 0),
                    'rating':      attrs.get('ratings', 0),
                    'hearing_impaired': attrs.get('hearing_impaired', False),
                    'source':      'rest',
                })
            return subs
        except Exception as e:
            _log(f'REST search erro: {e}')
        return []

    # -- Download --------------------------------------------------------------

    def _download(self, sub, filename=None):
        """Baixa legenda e salva no cache. Retorna caminho local."""
        file_id  = str(sub.get('file_id', ''))
        dl_url   = sub.get('download_url', '')
        fname    = filename or sub.get('file_name', 'legenda.srt')

        ext = '.srt'
        if fname.endswith('.ass') or fname.endswith('.ssa'):
            ext = '.ass'
        elif fname.endswith('.sub'):
            ext = '.sub'

        cache_path = os.path.join(self._cache_dir, f'{file_id}{ext}')
        if os.path.exists(cache_path):
            mtime = os.path.getmtime(cache_path)
            if time.time() - mtime < _CACHE_TTL:
                _log(f'Cache hit: {os.path.basename(cache_path)}')
                return cache_path

        # XML-RPC: download direto pela URL
        if dl_url and sub.get('source') == 'xmlrpc':
            return self._download_direct(dl_url, cache_path, file_id)

        # REST: solicita link de download
        if sub.get('source') == 'rest' and file_id:
            return self._download_rest(file_id, cache_path)

        return ''

    def _download_direct(self, url, cache_path, file_id):
        """Download direto (XML-RPC retorna URL direta)."""
        if not _HAS_REQUESTS:
            return ''
        try:
            # URL do XML-RPC e comprimida em gzip
            resp = _req.get(url, timeout=20, stream=True)
            if resp.status_code != 200:
                return ''
            import gzip, io
            raw = b''
            for chunk in resp.iter_content(8192):
                raw += chunk
            # Tenta descomprimir gzip
            try:
                content = gzip.decompress(raw)
            except Exception:
                content = raw
            with open(cache_path, 'wb') as f:
                f.write(content)
            _log(f'Download OK: {os.path.basename(cache_path)}', xbmc.LOGINFO if _HAS_KODI else None)
            return cache_path
        except Exception as e:
            _log(f'Erro download direto: {e}')
        return ''

    def _download_rest(self, file_id, cache_path):
        """Download via REST API (requer solicitar link primeiro)."""
        if not _HAS_REQUESTS:
            return ''
        api_key = self._get_api_key()
        if not api_key:
            return ''
        try:
            resp = _req.post(
                f'{_OS_REST_BASE}/download',
                json={'file_id': int(file_id)},
                headers={'Api-Key': api_key, 'User-Agent': _OS_USER_AGENT,
                         'Content-Type': 'application/json'},
                timeout=12
            )
            if resp.status_code != 200:
                return ''
            link = resp.json().get('link', '')
            if not link:
                return ''
            dl = _req.get(link, timeout=20, stream=True)
            if dl.status_code != 200:
                return ''
            with open(cache_path, 'wb') as f:
                for chunk in dl.iter_content(8192):
                    f.write(chunk)
            _log(f'REST download OK: {os.path.basename(cache_path)}', xbmc.LOGINFO if _HAS_KODI else None)
            return cache_path
        except Exception as e:
            _log(f'Erro REST download: {e}')
        return ''

    # -- Interface principal ---------------------------------------------------

    def prompt_and_download(self, title, year=0, imdb_id=None, tmdb_id=None,
                            media_type='movie', tmdb_title=None):
        """
        Interface completa: busca no idioma SELECIONADO apenas,
        filtra resultados pelo idioma, exibe menu e baixa a legenda.

        Parametros:
          title       : titulo do item no servidor (pode estar em PT ou EN)
          tmdb_title  : titulo em PT-BR do TMDB (mais preciso para busca)
          imdb_id     : ID IMDB para busca precisa (ex: 'tt1234567')
          tmdb_id     : ID TMDB para busca precisa
        """
        if not _HAS_KODI:
            return ''
        if not (_HAS_REQUESTS or _HAS_XMLRPC):
            return ''

        rest_code, xmlrpc_code, lang_name = self._get_lang_pref()
        api_key = self._get_api_key()

        # Usa titulo PT-BR do TMDB se disponivel - busca mais precisa
        search_title = tmdb_title or title

        # Limpa titulo de tags IPTV como [Dual], [Leg], (2026), etc.
        import re as _re
        clean_title = _re.sub(
            r'\s*[\[\(][^\]\)]*[\]\)]\s*|\s*\(?\d{4}\)?\s*$', '', search_title
        ).strip()

        _log(f'Buscando legendas: "{clean_title}" ({year}) lang={xmlrpc_code} imdb={imdb_id}',
             xbmc.LOGINFO if _HAS_KODI else None)

        xbmcgui.Dialog().notification(
            'KelTec - Legendas',
            f'Buscando [{lang_name}]: {clean_title[:35]}',
            xbmcgui.NOTIFICATION_INFO, 2000
        )

        subs = []

        # 1. REST API com chave (mais precisa, filtra por idioma na query)
        if api_key:
            subs = self._search_rest(
                clean_title, year, [rest_code], imdb_id, tmdb_id)
            _log(f'REST [{rest_code}]: {len(subs)} resultado(s)',
                 xbmc.LOGINFO if _HAS_KODI else None)

        # 2. XML-RPC com credenciais/anonimo
        if not subs and _HAS_XMLRPC:
            subs = self._search_xmlrpc(
                clean_title, year, xmlrpc_code, imdb_id)
            _log(f'XML-RPC [{xmlrpc_code}]: {len(subs)} resultado(s)',
                 xbmc.LOGINFO if _HAS_KODI else None)

        # 3. Se nao achou, tenta com titulo original (ingles) no mesmo idioma
        if not subs and tmdb_title and clean_title != title:
            alt_title = _re.sub(
                r'\s*[\[\(][^\]\)]*[\]\)]\s*|\s*\(?\d{4}\)?\s*$', '', title
            ).strip()
            if api_key:
                subs = self._search_rest(
                    alt_title, year, [rest_code], imdb_id, tmdb_id)
            if not subs and _HAS_XMLRPC:
                subs = self._search_xmlrpc(
                    alt_title, year, xmlrpc_code, imdb_id)
            if subs:
                _log(f'Achou com titulo alternativo: "{alt_title}"',
                     xbmc.LOGINFO if _HAS_KODI else None)

        # Filtra SOMENTE o idioma selecionado
        _LANG_CODE_MAP = {
            'pt-BR': ['PT-BR', 'pob', 'pb'],
            'pt-PT': ['PT-PT', 'PT', 'por', 'pt'],
            'en':    ['EN', 'eng'],
            'es':    ['ES', 'spa'],
            'fr':    ['FR', 'fre'],
            'it':    ['IT', 'ita'],
            'de':    ['DE', 'ger'],
        }
        accepted = [c.upper() for c in _LANG_CODE_MAP.get(rest_code, [rest_code.upper()])]
        subs_filtered = [s for s in subs
                         if s.get('language', '').upper() in accepted]

        # Se filtrou tudo, usa lista original com aviso
        if not subs_filtered and subs:
            _log(f'Nenhum resultado em [{rest_code}], mostrando todos',
                 xbmc.LOGWARNING if _HAS_KODI else None)
            subs_filtered = subs

        if not subs_filtered:
            xbmcgui.Dialog().notification(
                'Legendas',
                f'Sem legendas em {lang_name} para: {clean_title[:30]}',
                xbmcgui.NOTIFICATION_WARNING, 3000
            )
            return ''

        # Ordena por downloads (mais populares primeiro)
        subs_filtered.sort(key=lambda x: x.get('downloads', 0), reverse=True)

        # Monta menu de selecao
        options = []
        for s in subs_filtered[:20]:
            lang = s['language']
            rel  = (s.get('file_name') or '')
            # Exibe so o nome do release, sem extensao
            rel  = _re.sub(r'\.(srt|ass|sub|ssa)$', '', rel, flags=_re.IGNORECASE)[:48]
            dl   = s.get('downloads', 0)
            hi   = ' [CC]' if s.get('hearing_impaired') else ''
            options.append(f'[{lang}]{hi}  {rel}  ({dl} dl)')
        options.append('[COLOR gray]Reproduzir sem legenda[/COLOR]')

        choice = xbmcgui.Dialog().select(
            f'Legendas [{lang_name}] - {clean_title[:30]}', options)
        if choice < 0 or choice >= len(subs_filtered):
            return ''

        selected = subs_filtered[choice]

        xbmcgui.Dialog().notification(
            'Legendas', 'Baixando...', xbmcgui.NOTIFICATION_INFO, 1500)

        path = self._download(selected, selected.get('file_name', ''))
        if path:
            xbmcgui.Dialog().notification(
                'Legendas', f'[{selected["language"]}] Carregada!',
                xbmcgui.NOTIFICATION_INFO, 2500)
        else:
            xbmcgui.Dialog().notification(
                'Legendas', 'Falha ao baixar. Tente outra opcao.',
                xbmcgui.NOTIFICATION_ERROR, 2500)
        return path

    def clear_cache(self):
        """Limpa cache de legendas."""
        try:
            removed = 0
            for f in os.listdir(self._cache_dir):
                if f.endswith(('.srt', '.ass', '.sub', '.ssa')):
                    os.remove(os.path.join(self._cache_dir, f))
                    removed += 1
            _log(f'Cache limpo: {removed} arquivo(s).')
            return True
        except Exception as e:
            _log(f'Erro ao limpar cache: {e}')
            return False


def get_subtitles_manager(addon, profile_dir):
    if not (_HAS_REQUESTS or _HAS_XMLRPC):
        if _HAS_KODI:
            xbmc.log('[KelTec-Subs] requests/xmlrpc nao disponivel.', xbmc.LOGWARNING)
        return None
    try:
        return SubtitlesManager(addon, profile_dir)
    except Exception as e:
        if _HAS_KODI:
            xbmc.log(f'[KelTec-Subs] Erro: {e}', xbmc.LOGERROR)
        return None