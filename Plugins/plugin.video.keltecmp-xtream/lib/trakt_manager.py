# -*- coding: utf-8 -*-
# ============================================================================
# KELTEC MEDIA PLAY - TRAKT.TV INTEGRATION MODULE v2.0
# ============================================================================
# Arquivo: lib/trakt_manager.py
#
# COMO USAR:
#   Nao precisa configurar nada. So clicar em "Conectar Trakt" no menu,
#   ir em trakt.tv/activate no browser e digitar o codigo exibido.
#
# FUNCIONALIDADES:
#   - Autenticacao via Device Flow sem configuracao manual
#   - Credenciais do KelTec embutidas como padrao
#   - Scrobble automatico ao reproduzir filmes e series
#   - Sincronizacao de historico local para o Trakt
#   - Watchlist: ver, adicionar e remover itens
#   - Renovacao automatica de token expirado
# ============================================================================

import time
import threading

try:
    import requests as _req
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

try:
    import xbmc
    import xbmcgui
    import xbmcaddon
    _HAS_KODI = True
except ImportError:
    _HAS_KODI = False

# Credenciais padrao do app KelTec no Trakt (registrado pelo desenvolvedor)
# O usuario nao precisa criar sua propria conta de desenvolvedor.
_DEFAULT_CLIENT_ID     = '7790012fe4684af427bc39b712a1050c4e813ed0edec72d46fbce0dd1dc4fedb'
_DEFAULT_CLIENT_SECRET = '2f3bcc98ed7bc2f2a5a337267c1d4c0734886e6db8c220dd9d2a6e7156c716d1'

_TRAKT_BASE         = 'https://api.trakt.tv'
_TRAKT_API_VERSION  = '2'
_TRAKT_TOKEN_KEY    = 'trakt_access_token'
_TRAKT_REFRESH_KEY  = 'trakt_refresh_token'
_TRAKT_EXPIRY_KEY   = 'trakt_token_expiry'
_TRAKT_USERNAME_KEY = 'trakt_username'
_WATCHLIST_TTL      = 300

_scrobble_lock     = threading.Lock()
_watchlist_cache   = {}
_watchlist_cache_ts = 0


def _log(msg, level=None):
    if _HAS_KODI:
        lvl = level if level is not None else xbmc.LOGDEBUG
        xbmc.log(f'[KelTec-Trakt] {msg}', lvl)


class TraktManager:
    """
    Gerencia toda a integracao com o Trakt.tv para o KelTec Media Play.
    Nao requer configuracao manual - usa credenciais embutidas do app KelTec.
    """

    def __init__(self, addon):
        self._addon   = addon
        self._session = None
        self._client_id, self._client_secret = self._resolve_credentials()

    def _resolve_credentials(self):
        """Prioridade: settings do usuario > credenciais embutidas do KelTec."""
        try:
            uid = (self._addon.getSetting('trakt_client_id') or '').strip()
            sec = (self._addon.getSetting('trakt_client_secret') or '').strip()
            if uid and sec:
                return uid, sec
        except Exception:
            pass
        return _DEFAULT_CLIENT_ID, _DEFAULT_CLIENT_SECRET

    def _reload_credentials(self):
        self._client_id, self._client_secret = self._resolve_credentials()
        self._session = None

    def _get_session(self):
        if self._session is None:
            self._session = _req.Session()
        self._session.headers.update({
            'Content-Type':      'application/json',
            'trakt-api-version': _TRAKT_API_VERSION,
            'trakt-api-key':     self._client_id,
        })
        token = self._addon.getSetting(_TRAKT_TOKEN_KEY) or ''
        if token:
            self._session.headers['Authorization'] = f'Bearer {token}'
        else:
            self._session.headers.pop('Authorization', None)
        return self._session

    def _request(self, method, endpoint, data=None, timeout=12):
        if not _HAS_REQUESTS:
            return 0, None
        try:
            url  = f'{_TRAKT_BASE}/{endpoint.lstrip("/")  }'
            sess = self._get_session()
            if method == 'GET':
                resp = sess.get(url, timeout=timeout)
            elif method == 'POST':
                resp = sess.post(url, json=data, timeout=timeout)
            elif method == 'DELETE':
                resp = sess.delete(url, json=data, timeout=timeout)
            else:
                return 0, None
            if resp.status_code in (200, 201):
                try:
                    return resp.status_code, resp.json()
                except Exception:
                    return resp.status_code, {}
            return resp.status_code, None
        except Exception as e:
            _log(f'Erro HTTP {method} {endpoint}: {e}')
            return 0, None

    def _paged_request(self, endpoint, page=1, limit=60, params=None):
        """
        Requisicao GET com suporte a paginacao via headers do Trakt.
        Retorna (data_list, total_pages, total_items).
        O Trakt usa headers: X-Pagination-Page-Count, X-Pagination-Item-Count.
        """
        if not _HAS_REQUESTS:
            return [], 1, 0
        try:
            url  = f'{_TRAKT_BASE}/{endpoint.lstrip("/")}'
            sess = self._get_session()
            p = {'extended': 'full', 'page': page, 'limit': limit}
            if params:
                p.update(params)
            resp = sess.get(url, params=p, timeout=15)
            if resp.status_code not in (200, 201):
                _log(f'_paged_request {endpoint} -> {resp.status_code}')
                return [], 1, 0
            try:
                data = resp.json()
            except Exception:
                data = []
            # Le headers de paginacao do Trakt
            total_pages = int(resp.headers.get('X-Pagination-Page-Count', 1))
            total_items = int(resp.headers.get('X-Pagination-Item-Count', len(data) if data else 0))
            return (data if isinstance(data, list) else []), total_pages, total_items
        except Exception as e:
            _log(f'Erro _paged_request {endpoint}: {e}')
            return [], 1, 0

    def is_authenticated(self):
        token = self._addon.getSetting(_TRAKT_TOKEN_KEY) or ''
        if not token:
            return False
        try:
            expiry = int(self._addon.getSetting(_TRAKT_EXPIRY_KEY) or '0')
            if expiry and time.time() > expiry - 3600:
                self._refresh_token()
        except Exception:
            pass
        return bool(self._addon.getSetting(_TRAKT_TOKEN_KEY) or '')

    def _save_token(self, token_data):
        try:
            self._addon.setSetting(_TRAKT_TOKEN_KEY,   token_data.get('access_token', ''))
            self._addon.setSetting(_TRAKT_REFRESH_KEY, token_data.get('refresh_token', ''))
            expires_in = int(token_data.get('expires_in', 7776000))
            self._addon.setSetting(_TRAKT_EXPIRY_KEY,  str(int(time.time()) + expires_in))
            self._session = None
        except Exception as e:
            _log(f'Erro ao salvar token: {e}')

    def _save_username(self, access_token):
        try:
            if not _HAS_REQUESTS:
                return
            resp = _req.get(
                f'{_TRAKT_BASE}/users/me',
                headers={
                    'Content-Type':      'application/json',
                    'Authorization':     f'Bearer {access_token}',
                    'trakt-api-version': _TRAKT_API_VERSION,
                    'trakt-api-key':     self._client_id,
                },
                timeout=10
            )
            if resp.status_code == 200:
                username = resp.json().get('username', '')
                if username:
                    self._addon.setSetting(_TRAKT_USERNAME_KEY, username)
                    _log(f'Username salvo: {username}')
        except Exception as e:
            _log(f'Erro ao buscar username: {e}')

    def _refresh_token(self):
        refresh = self._addon.getSetting(_TRAKT_REFRESH_KEY) or ''
        if not refresh:
            return False
        _, data = self._request('POST', '/oauth/token', {
            'refresh_token': refresh,
            'client_id':     self._client_id,
            'client_secret': self._client_secret,
            'redirect_uri':  'urn:ietf:wg:oauth:2.0:oob',
            'grant_type':    'refresh_token',
        })
        if data and data.get('access_token'):
            self._save_token(data)
            return True
        return False

    def authenticate(self):
        """
        Fluxo Device Flow sem configuracao manual.
        1. Solicita device_code com credenciais embutidas do KelTec
        2. Mostra codigo para o usuario
        3. Usuario vai em trakt.tv/activate e digita o codigo
        4. Usuario volta e clica OK - verificacao imediata
        5. Fallback: colar Access Token manualmente
        """
        if not _HAS_KODI or not _HAS_REQUESTS:
            return False

        self._reload_credentials()

        try:
            resp = _req.post(
                f'{_TRAKT_BASE}/oauth/device/code',
                json={'client_id': self._client_id},
                headers={'Content-Type': 'application/json'},
                timeout=15
            )
        except Exception as e:
            xbmcgui.Dialog().ok(
                '[B][COLOR crimson]Trakt - Sem conexao[/COLOR][/B]',
                f'Nao foi possivel contatar o Trakt.\nErro: {e}\n\n'
                'Verifique sua conexao com a internet.'
            )
            return False

        if resp.status_code != 200:
            xbmcgui.Dialog().ok(
                '[B][COLOR crimson]Trakt - Erro[/COLOR][/B]',
                f'Resposta inesperada do Trakt: HTTP {resp.status_code}\n\n'
                'Tente novamente em alguns instantes.'
            )
            return False

        data        = resp.json()
        user_code   = data.get('user_code', '')
        device_code = data.get('device_code', '')

        xbmcgui.Dialog().ok(
            '[B][COLOR gold]Trakt - Conectar conta[/COLOR][/B]',
            '[B]Passo 1:[/B] Abra no navegador:\n'
            '[COLOR cyan][B]trakt.tv/activate[/B][/COLOR]\n\n'
            '[B]Passo 2:[/B] Digite este codigo:\n'
            f'[COLOR gold][B]   {user_code}   [/B][/COLOR]\n\n'
            '[B]Passo 3:[/B] Clique [B]Autorizar[/B] no site\n\n'
            '[COLOR dimgray]Feito isso, volte aqui e clique OK[/COLOR]'
        )

        authorized = False
        for tentativa in range(3):
            try:
                token_resp = _req.post(
                    f'{_TRAKT_BASE}/oauth/device/token',
                    json={
                        'code':          device_code,
                        'client_id':     self._client_id,
                        'client_secret': self._client_secret,
                        'grant_type':    'device_code',
                    },
                    timeout=12
                )
            except Exception as e:
                _log(f'Erro na verificacao {tentativa+1}: {e}')
                token_resp = None

            if token_resp and token_resp.status_code == 200:
                token_data   = token_resp.json()
                access_token = token_data.get('access_token', '')
                if access_token:
                    self._save_token(token_data)
                    self._save_username(access_token)
                    authorized = True
                    break

            if tentativa < 2:
                retry = xbmcgui.Dialog().yesno(
                    '[B][COLOR gold]Trakt - Verificando[/COLOR][/B]',
                    f'Codigo: [COLOR gold][B]{user_code}[/B][/COLOR]\n\n'
                    'Autorizacao ainda nao detectada.\n\n'
                    'Ja autorizou em [B]trakt.tv/activate[/B]?\n'
                    '[COLOR dimgray]SIM = verificar de novo  |  NAO = modo manual[/COLOR]'
                )
                if not retry:
                    break

        if not authorized:
            oferecer = xbmcgui.Dialog().yesno(
                'Trakt - Autorizacao nao detectada',
                'A autorizacao automatica nao funcionou.\n\n'
                'Deseja inserir o Access Token manualmente?\n'
                '[COLOR dimgray](Obtenha em trakt.tv/settings > Your API Apps)[/COLOR]'
            )
            if oferecer:
                authorized = self._authenticate_manual_token()

        if authorized:
            username = self._addon.getSetting(_TRAKT_USERNAME_KEY) or ''
            msg = f'Conectado como [B]{username}[/B]!' if username else 'Conta conectada!'
            xbmcgui.Dialog().notification('Trakt', msg, xbmcgui.NOTIFICATION_INFO, 3500)
            _log('Autenticado com sucesso.')
        else:
            xbmcgui.Dialog().notification(
                'Trakt', 'Autorizacao nao concluida.',
                xbmcgui.NOTIFICATION_WARNING, 3000
            )
        return authorized

    def _authenticate_manual_token(self):
        if not _HAS_KODI:
            return False
        xbmcgui.Dialog().ok(
            '[B][COLOR gold]Trakt - Token Manual[/COLOR][/B]',
            'Para obter seu Access Token:\n\n'
            '[B]1.[/B] Acesse: [COLOR cyan]trakt.tv/settings[/COLOR]\n'
            '[B]2.[/B] Va em: [B]Your API Apps[/B]\n'
            '[B]3.[/B] Clique no app KelTec -> [B]Authorize[/B]\n'
            '[B]4.[/B] Copie o [B]Access Token[/B] gerado\n\n'
            '[COLOR dimgray]Clique OK e cole o token no campo seguinte[/COLOR]'
        )
        keyboard = xbmc.Keyboard('', 'Cole seu Trakt Access Token aqui')
        keyboard.doModal()
        if not keyboard.isConfirmed():
            return False
        token = keyboard.getText().strip()
        if len(token) < 20:
            xbmcgui.Dialog().ok('Trakt', 'Token invalido ou muito curto.')
            return False
        try:
            self._addon.setSetting(_TRAKT_TOKEN_KEY,   token)
            self._addon.setSetting(_TRAKT_REFRESH_KEY, '')
            self._addon.setSetting(_TRAKT_EXPIRY_KEY,  str(int(time.time()) + 7776000))
            self._session = None
            return True
        except Exception as e:
            _log(f'Erro ao salvar token manual: {e}')
            return False

    def disconnect(self):
        try:
            for key in (_TRAKT_TOKEN_KEY, _TRAKT_REFRESH_KEY,
                        _TRAKT_EXPIRY_KEY, _TRAKT_USERNAME_KEY):
                self._addon.setSetting(key, '')
            self._session = None
        except Exception as e:
            _log(f'Erro ao desconectar: {e}')

    def _build_payload(self, title, year, progress, media_type, tmdb_id=None):
        payload = {'progress': round(float(progress), 1)}
        entry   = {'title': title}
        if year:
            entry['year'] = int(year)
        if tmdb_id:
            entry['ids'] = {'tmdb': int(tmdb_id)}
        if media_type == 'movie':
            payload['movie'] = entry
        else:
            payload['show'] = entry
        return payload

    def scrobble_start(self, title, year=0, progress=1.0,
                       media_type='movie', tmdb_id=None):
        if not self.is_authenticated():
            return False
        with _scrobble_lock:
            payload = self._build_payload(title, year, max(progress, 1.0),
                                          media_type, tmdb_id)
            code, _ = self._request('POST', '/scrobble/start', payload)
            ok = code in (200, 201)
            _log(f'scrobble/start [{media_type}] "{title}" -> {code}')
            return ok

    def scrobble_stop(self, title, year=0, progress=90.0,
                      media_type='movie', tmdb_id=None):
        if not self.is_authenticated():
            return False
        with _scrobble_lock:
            payload = self._build_payload(title, year, progress,
                                          media_type, tmdb_id)
            code, _ = self._request('POST', '/scrobble/stop', payload)
            ok = code in (200, 201)
            _log(f'scrobble/stop [{media_type}] "{title}" progress={progress:.0f}% -> {code}')
            return ok

    def get_watchlist(self, media_type='movies'):
        global _watchlist_cache, _watchlist_cache_ts
        if not self.is_authenticated():
            return []
        if (time.time() - _watchlist_cache_ts < _WATCHLIST_TTL
                and media_type in _watchlist_cache):
            return _watchlist_cache[media_type]
        # extended=full retorna metadados completos (titulo, ano, ids)
        _, data = self._request('GET', f'/sync/watchlist/{media_type}?extended=full')
        result = data if isinstance(data, list) else []
        _watchlist_cache[media_type] = result
        _watchlist_cache_ts = time.time()
        return result

    def add_to_watchlist(self, title, year=0, tmdb_id=None, media_type='movie'):
        if not self.is_authenticated():
            return False
        entry = {'title': title}
        if year:
            entry['year'] = int(year)
        if tmdb_id:
            entry['ids'] = {'tmdb': int(tmdb_id)}
        payload = {'movies': [entry]} if media_type == 'movie' else {'shows': [entry]}
        code, _ = self._request('POST', '/sync/watchlist', payload)
        ok = code in (200, 201)
        if ok:
            _watchlist_cache.clear()
        return ok

    def remove_from_watchlist(self, title, year=0, tmdb_id=None, media_type='movie'):
        if not self.is_authenticated():
            return False
        entry = {'title': title}
        if year:
            entry['year'] = int(year)
        if tmdb_id:
            entry['ids'] = {'tmdb': int(tmdb_id)}
        payload = {'movies': [entry]} if media_type == 'movie' else {'shows': [entry]}
        code, _ = self._request('POST', '/sync/watchlist/remove', payload)
        ok = code in (200, 201)
        if ok:
            _watchlist_cache.clear()
        return ok

    def sync_local_history(self, watch_history_items):
        if not self.is_authenticated():
            return False, 0
        movies, shows = [], []
        for item in watch_history_items:
            stype = item.get('stype', '')
            name  = item.get('name', '')
            ts    = item.get('timestamp', 0)
            if not name or stype == 'live':
                continue
            entry = {'title': name}
            try:
                entry['watched_at'] = time.strftime(
                    '%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(ts))
            except Exception:
                pass
            if stype == 'movie':
                movies.append(entry)
            elif stype == 'series':
                shows.append(entry)
        if not movies and not shows:
            return True, 0
        payload = {}
        if movies:
            payload['movies'] = movies
        if shows:
            payload['shows'] = shows
        code, resp = self._request('POST', '/sync/history', payload)
        added = 0
        if isinstance(resp, dict):
            added = (resp.get('added', {}).get('movies', 0) +
                     resp.get('added', {}).get('episodes', 0))
        ok = code in (200, 201)
        _log(f'sync_history: {len(movies)} filmes, {len(shows)} series -> {code}, {added} add')
        return ok, added

    def get_username(self):
        return self._addon.getSetting(_TRAKT_USERNAME_KEY) or ''

    # -- Sync pessoal (requer login) -------------------------------------------

    def _sync_request(self, path, limit=100):
        """Requisicao autenticada para endpoints /sync/."""
        if not self.is_authenticated():
            return []
        _, data = self._request('GET', f'/{path.lstrip("/")}?extended=full&limit={limit}')
        return data if isinstance(data, list) else []

    def get_collection(self, media_type='movies'):
        """Colecao pessoal (filmes/series marcados como coletados)."""
        path = 'sync/collection/movies' if media_type == 'movies' else 'sync/collection/shows'
        return self._sync_request(path)

    def get_watched_history(self, media_type='movies', limit=100):
        """Historico de reproducao do Trakt (o que ja assistiu)."""
        path = 'sync/history/movies' if media_type == 'movies' else 'sync/history/shows'
        return self._sync_request(path, limit=limit)

    def get_playback_progress(self, media_type='movies'):
        """Itens em progresso no Trakt (Continuar Assistindo). progress 5-95%."""
        if not self.is_authenticated():
            return []
        endpoint = 'movies' if media_type == 'movies' else 'episodes'
        _, data = self._request('GET', f'/sync/playback/{endpoint}?limit=50')
        if not isinstance(data, list):
            return []
        return [i for i in data if 5 <= float(i.get('progress', 0)) <= 95]

    def get_favorites(self, media_type='movies'):
        """Favoritos pessoais do Trakt."""
        path = 'sync/favorites/movies' if media_type == 'movies' else 'sync/favorites/shows'
        return self._sync_request(path)

    def get_ratings(self, media_type='movies', min_rating=1):
        """Filmes/series avaliados pelo usuario no Trakt."""
        path = 'sync/ratings/movies' if media_type == 'movies' else 'sync/ratings/shows'
        data = self._sync_request(path)
        if min_rating > 1:
            data = [i for i in data if i.get('rating', 0) >= min_rating]
        return data

    def get_recommendations(self, media_type='movies', limit=30):
        """Recomendacoes personalizadas (requer login). Baseadas no historico."""
        if not self.is_authenticated():
            return []
        path = 'movies' if media_type == 'movies' else 'shows'
        _, data = self._request('GET', f'/{path}/recommendations?extended=full&limit={limit}')
        return data if isinstance(data, list) else []

    def get_calendar_shows(self, days=7):
        """Episodios que estreiam nos proximos dias (requer login)."""
        if not self.is_authenticated():
            return []
        import time as _t
        start = _t.strftime('%Y-%m-%d')
        _, data = self._request('GET', f'/calendars/my/shows/{start}/{days}?extended=full')
        return data if isinstance(data, list) else []

    def get_calendar_movies(self, days=30):
        """Filmes com lancamento previsto nos proximos dias (requer login)."""
        if not self.is_authenticated():
            return []
        import time as _t
        start = _t.strftime('%Y-%m-%d')
        _, data = self._request('GET', f'/calendars/my/movies/{start}/{days}?extended=full')
        return data if isinstance(data, list) else []

    # -- Listas publicas (SEM necessidade de login) ----------------------------
    # Estas funcionam apenas com o client_id - o usuario nao precisa autenticar.

    def _public_request(self, endpoint, params=None):
        """
        Requisicao publica ao Trakt - apenas client_id, sem token.
        Retorna lista ou None. Sem paginacao (uso interno).
        """
        if not _HAS_REQUESTS:
            return None
        try:
            import requests as _r
            p = {'extended': 'full', 'limit': 30}
            if params:
                p.update(params)
            resp = _r.get(
                f'{_TRAKT_BASE}/{endpoint.lstrip("/")}',
                headers={
                    'Content-Type':      'application/json',
                    'trakt-api-version': _TRAKT_API_VERSION,
                    'trakt-api-key':     self._client_id,
                },
                params=p,
                timeout=15
            )
            if resp.status_code == 200:
                return resp.json()
            _log(f'public_request {endpoint} -> {resp.status_code}')
            return None
        except Exception as e:
            _log(f'Erro public_request {endpoint}: {e}')
            return None

    def _public_paged_request(self, endpoint, page=1, limit=60, params=None):
        """
        Requisicao publica paginada - apenas client_id, sem token.
        Retorna (data_list, total_pages, total_items).
        """
        if not _HAS_REQUESTS:
            return [], 1, 0
        try:
            import requests as _r
            p = {'extended': 'full', 'page': page, 'limit': limit}
            if params:
                p.update(params)
            resp = _r.get(
                f'{_TRAKT_BASE}/{endpoint.lstrip("/")}',
                headers={
                    'Content-Type':      'application/json',
                    'trakt-api-version': _TRAKT_API_VERSION,
                    'trakt-api-key':     self._client_id,
                },
                params=p,
                timeout=15
            )
            if resp.status_code not in (200, 201):
                _log(f'_public_paged_request {endpoint} -> {resp.status_code}')
                return [], 1, 0
            try:
                data = resp.json()
            except Exception:
                data = []
            total_pages = int(resp.headers.get('X-Pagination-Page-Count', 1))
            total_items = int(resp.headers.get('X-Pagination-Item-Count', len(data) if data else 0))
            return (data if isinstance(data, list) else []), total_pages, total_items
        except Exception as e:
            _log(f'Erro _public_paged_request {endpoint}: {e}')
            return [], 1, 0

    def get_trending(self, media_type='movies', limit=60, page=1):
        """Em Alta - nao requer login. Retorna (items, total_pages)."""
        data, pages, _ = self._public_paged_request(
            f'/{media_type}/trending', page=page, limit=limit)
        return data, pages

    def get_popular(self, media_type='movies', limit=60, page=1):
        """Populares - nao requer login. Retorna (items, total_pages)."""
        data, pages, _ = self._public_paged_request(
            f'/{media_type}/popular', page=page, limit=limit)
        return data, pages

    def get_most_watched(self, media_type='movies', period='weekly', limit=60, page=1):
        """Mais Assistidos - nao requer login. period: daily/weekly/monthly/yearly/all"""
        data, pages, _ = self._public_paged_request(
            f'/{media_type}/watched/{period}', page=page, limit=limit)
        return data, pages

    def get_most_anticipated(self, media_type='movies', limit=60, page=1):
        """Mais Aguardados - nao requer login."""
        data, pages, _ = self._public_paged_request(
            f'/{media_type}/anticipated', page=page, limit=limit)
        return data, pages

    def get_box_office(self, limit=10, page=1):
        """Bilheteria atual (apenas filmes) - nao requer login."""
        data, pages, _ = self._public_paged_request(
            '/movies/boxoffice', page=page, limit=limit)
        return data, pages

    def get_imdb_top250(self, media_type='movies', limit=60, page=1):
        """IMDB Top 250 via lista publica do Trakt (sem login). Com paginacao."""
        if media_type == 'movies':
            path = 'users/justin/lists/imdb-top-rated-movies/items/movies'
        else:
            path = 'users/justin/lists/imdb-top-rated-tv-shows/items/shows'
        data, pages, _ = self._public_paged_request(path, page=page, limit=limit)
        return data, pages

    def get_trakt_genres(self, media_type='movies'):
        """
        Retorna lista de generos do Trakt (sem login).
        media_type: 'movies' | 'shows'
        Endpoint correto: /genres/movies e /genres/shows
        Retorna lista de {'name': str, 'slug': str}
        """
        # Endpoint correto da API Trakt: /genres/{type}
        endpoint = f'/genres/{"movies" if media_type == "movies" else "shows"}'
        data = self._public_request(endpoint, params={})
        if isinstance(data, list) and data:
            return data
        # Fallback: lista estatica de generos principais caso a API falhe
        _fallback = {
            'movies': [
                {'name': 'Acao',        'slug': 'action'},
                {'name': 'Aventura',    'slug': 'adventure'},
                {'name': 'Animacao',    'slug': 'animation'},
                {'name': 'Comedia',     'slug': 'comedy'},
                {'name': 'Crime',       'slug': 'crime'},
                {'name': 'Documentario','slug': 'documentary'},
                {'name': 'Drama',       'slug': 'drama'},
                {'name': 'Fantasia',    'slug': 'fantasy'},
                {'name': 'Ficcao Cientifica', 'slug': 'science-fiction'},
                {'name': 'Horror',      'slug': 'horror'},
                {'name': 'Misterio',    'slug': 'mystery'},
                {'name': 'Romance',     'slug': 'romance'},
                {'name': 'Suspense',    'slug': 'thriller'},
                {'name': 'Faroeste',    'slug': 'western'},
                {'name': 'Familia',     'slug': 'family'},
                {'name': 'Historia',    'slug': 'history'},
                {'name': 'Musical',     'slug': 'music'},
                {'name': 'Guerra',      'slug': 'war'},
            ],
            'shows': [
                {'name': 'Acao',        'slug': 'action'},
                {'name': 'Aventura',    'slug': 'adventure'},
                {'name': 'Animacao',    'slug': 'animation'},
                {'name': 'Comedia',     'slug': 'comedy'},
                {'name': 'Crime',       'slug': 'crime'},
                {'name': 'Documentario','slug': 'documentary'},
                {'name': 'Drama',       'slug': 'drama'},
                {'name': 'Fantasia',    'slug': 'fantasy'},
                {'name': 'Ficcao Cientifica', 'slug': 'science-fiction'},
                {'name': 'Horror',      'slug': 'horror'},
                {'name': 'Misterio',    'slug': 'mystery'},
                {'name': 'Reality',     'slug': 'reality'},
                {'name': 'Suspense',    'slug': 'thriller'},
                {'name': 'Familia',     'slug': 'family'},
                {'name': 'Infantil',    'slug': 'kids'},
                {'name': 'Noticias',    'slug': 'news'},
                {'name': 'Talk Show',   'slug': 'talk-show'},
            ],
        }
        _log(f'get_trakt_genres: usando fallback para {media_type}')
        return _fallback.get(media_type, [])

    def get_by_genre(self, genre_slug, media_type='movies', limit=60, page=1, sort='popularity'):
        """
        Filmes/series filtrados por genero via Trakt.
        genre_slug: slug do genero (ex: 'action', 'comedy', 'drama')
        sort: popularity | revenue | release | viewers | collected | anticipated
        Retorna (items, total_pages).
        """
        path = f'/{media_type}/{sort}' if sort != 'popularity' else f'/{media_type}/popular'
        data, pages, _ = self._public_paged_request(
            path, page=page, limit=limit,
            params={'genres': genre_slug}
        )
        return data, pages

    @staticmethod
    def normalize_item(item):
        """
        Normaliza qualquer estrutura de resposta do Trakt para dict padrao.
        Suporta: trending, popular, watched, anticipated, boxoffice,
                 watchlist, collection, ratings, playback, list items.
        """
        if not isinstance(item, dict):
            return None

        # Estruturas possiveis:
        # trending/watched/anticipated: {watchers, movie:{...}} ou {watchers, show:{...}}
        # popular/recommendations:      {title, year, ids, ...}  (objeto direto)
        # watchlist/collection/ratings: {rank, type, movie:{...}} ou {rank, type, show:{...}}
        # list items:                   {rank, id, listed_at, type, movie:{...}}
        # playback:                     {progress, type, movie:{...}} ou {progress, type, episode:{...}}

        obj = None
        mtype = 'movie'

        # 1. Tenta extrair pelo campo 'movie' ou 'show' diretamente
        if 'movie' in item:
            obj   = item['movie']
            mtype = 'movie'
        elif 'show' in item:
            obj   = item['show']
            mtype = 'show'
        elif 'episode' in item and 'show' not in item:
            # playback de episodio sem show - pula
            return None

        # 2. Se nao achou, pode ser objeto direto (popular retorna lista de objetos)
        if obj is None:
            if item.get('ids') and item.get('title'):
                obj = item
                # Detecta tipo pelo campo 'number_of_seasons' ou 'runtime'
                mtype = 'show' if 'number_of_seasons' in item else 'movie'
            else:
                return None

        if not obj:
            return None

        ids = obj.get('ids', {})
        tmdb_id = ids.get('tmdb')
        if not tmdb_id:
            return None

        return {
            'title':      obj.get('title', ''),
            'year':       obj.get('year', 0),
            'tmdb_id':    tmdb_id,
            'imdb_id':    ids.get('imdb', ''),
            'slug':       ids.get('slug', ''),
            'overview':   obj.get('overview', ''),
            'rating':     obj.get('rating', 0),
            'genres':     obj.get('genres', []),
            'media_type': mtype,
            'watchers':   item.get('watchers', 0),
            'play_count': item.get('play_count', 0),
            'progress':   item.get('progress', 0),
            'user_rating': item.get('rating', 0),  # rating do usuario (em ratings)
        }


def get_trakt_manager(addon):
    if not _HAS_REQUESTS:
        _log('requests nao disponivel - Trakt desabilitado.')
        return None
    try:
        return TraktManager(addon)
    except Exception as e:
        _log(f'Erro ao criar TraktManager: {e}')
        return None
