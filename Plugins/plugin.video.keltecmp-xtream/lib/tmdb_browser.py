# -*- coding: utf-8 -*-
"""
TMDB Browser v3.0 - KelTec Media Play
=======================================
Busca em TODOS os servidores em paralelo.
Metadados completos com InfoTagVideo (Kodi 21+).
Sem emojis - compativel com todos os skins.
"""

import re, json, time, os, threading, hashlib

try:
    import requests as _req_lib
    _tmdb_browser_session = _req_lib.Session()
    _tmdb_browser_session.headers['Connection'] = 'keep-alive'
    def _http_get(url, params=None, headers=None, timeout=18):
        h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        if headers:
            h.update(headers)
        r = _tmdb_browser_session.get(url, params=params, headers=h, timeout=timeout)
        r.raise_for_status()
        return r.json()
except ImportError:
    import urllib.request, urllib.parse as _uparse
    def _http_get(url, params=None, headers=None, timeout=18):
        if params:
            url = url + '?' + _uparse.urlencode(params)
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8'))

try:
    import xbmc, xbmcgui, xbmcaddon, xbmcvfs
except ImportError:
    pass

# Acelerador: cache em disco dos catalogos dos servidores
try:
    from . import accelerator as _accelerator
except Exception:
    try:
        import accelerator as _accelerator
    except Exception:
        _accelerator = None

# Normalizacao/pontuacao de titulos compartilhada com a busca TMDB
try:
    from .search_match import (
        normalize_title as _sm_normalize_title,
        score_titles as _sm_score_titles,
        is_year_token as _sm_is_year_token,
    )
except Exception:
    try:
        from search_match import (
            normalize_title as _sm_normalize_title,
            score_titles as _sm_score_titles,
            is_year_token as _sm_is_year_token,
        )
    except Exception:
        _sm_normalize_title = None
        _sm_score_titles = None
        _sm_is_year_token = None

# Invalida o cache DNS de um host quando a conexao falha (IP velho/quebrado)
try:
    from dns import invalidate_host as _dns_invalidate
except Exception:
    def _dns_invalidate(host):
        return None

# Tabela rapida p/ remover acentos no pre-filtro de titulos (catalogos grandes)
def _build_fold_table():
    import unicodedata
    tbl = {}
    for cp in range(0xC0, 0x250):
        ch = chr(cp)
        base = unicodedata.normalize('NFKD', ch)[:1]
        if base and base.isascii() and base.isalpha():
            tbl[cp] = base.lower()
    tbl[0xDF] = 'ss'
    return tbl
_FOLD_TABLE = _build_fold_table()

# User-Agents alternativos: alguns paineis Xtream bloqueiam UA de navegador
_ALT_UAS = (
    'VLC/3.0.20 LibVLC/3.0.20',
    'IPTVSmartersPro',
    'okhttp/4.9.3',
)

TMDB_API_BASE   = 'https://api.themoviedb.org/3'
TMDB_IMAGE_BASE = 'https://image.tmdb.org/t/p'
IMG_POSTER  = 'w500'
IMG_FANART  = 'original'
IMG_PROFILE = 'w185'
IMG_THUMB   = 'w300'

# Menus de navegacao
TMDB_MOVIE_MENUS = [
    ('Filmes Populares',              'discover_movies_popular'),
    ('Lancamentos - Em Cartaz',       'discover_movies_now_playing'),
    ('Lancamentos - Em Breve',        'discover_movies_upcoming'),
    ('Filmes Mais Votados',           'discover_movies_top_rated'),
    ('Filmes por Genero',             'tmdb_movie_genres'),
    ('Buscar Filme por Titulo',       'tmdb_search_movie'),
]

TMDB_TV_MENUS = [
    ('Series Populares',              'discover_tv_popular'),
    ('Lancamentos - Hoje no Ar',      'discover_tv_airing_today'),
    ('Lancamentos - Em Exibicao',     'discover_tv_on_the_air'),
    ('Series Mais Votadas',           'discover_tv_top_rated'),
    ('Series por Genero',             'tmdb_tv_genres'),
    ('Buscar Serie por Titulo',       'tmdb_search_tv'),
]

# Chaves de roteamento que build_menu passa para a URL
TMDB_ROUTING_KEYS = {
    'tmdb_id', 'tmdb_type', 'tmdb_title', 'tmdb_year',
    'genre_id', 'page', 'query',
    'category_id', 'cat_name', 'endpoint', 'series_id',
    'plot', 'col_name', 'col_data',
    'server_url', 'server_user', 'server_pass', 'server_name',
}


# ── Cache ──────────────────────────────────────────────────────────────

class _Cache:
    def __init__(self, cache_dir, hours=6):
        self.dir = cache_dir or '/tmp'
        self.hours = hours
        self._mem = {}
        if cache_dir and not os.path.exists(cache_dir):
            try: os.makedirs(cache_dir)
            except Exception: pass

    def _path(self, key):
        # Usa hash MD5 da chave completa para evitar colisao por truncamento
        # (truncar em 100 chars cortava o with_genres=XX fazendo todos os generos
        #  compartilharem o mesmo arquivo de cache e retornarem o mesmo conteudo)
        safe = re.sub(r'[^\w]', '_', key)[:40]
        hsh  = hashlib.md5(key.encode('utf-8')).hexdigest()[:16]
        return os.path.join(self.dir, f'tmdb_{safe}_{hsh}.json')

    def get(self, key):
        if key in self._mem:
            ts, v = self._mem[key]
            if time.time() - ts < self.hours * 3600:
                return v
        try:
            p = self._path(key)
            if os.path.exists(p):
                with open(p, 'r', encoding='utf-8') as f:
                    obj = json.load(f)
                if time.time() - obj['_ts'] < self.hours * 3600:
                    self._mem[key] = (obj['_ts'], obj['d'])
                    return obj['d']
        except Exception: pass
        return None

    def set(self, key, value):
        self._mem[key] = (time.time(), value)
        try:
            with open(self._path(key), 'w', encoding='utf-8') as f:
                json.dump({'_ts': time.time(), 'd': value}, f, ensure_ascii=False)
        except Exception: pass


# ── Browser ───────────────────────────────────────────────────────────

class TMDBBrowser:

    def __init__(self, api_key, language='pt-BR', cache_dir=None, cache_hours=6):
        self.api_key  = api_key
        self.language = language
        self.cache    = _Cache(cache_dir, cache_hours)

    # ── API ─────────────────────────────────────────────────────────

    def _get(self, endpoint, extra=None):
        p = {'api_key': self.api_key, 'language': self.language}
        if extra:
            p.update(extra)
        key = endpoint + '|' + '|'.join(f'{k}={v}' for k, v in sorted(p.items()))
        cached = self.cache.get(key)
        if cached is not None:
            return cached
        try:
            data = _http_get(f'{TMDB_API_BASE}/{endpoint}', params=p)
            self.cache.set(key, data)
            return data
        except Exception as e:
            xbmc.log(f'[KelTec-TMDBv3] API {endpoint}: {e}', xbmc.LOGWARNING)
            return None

    def img(self, path, size=IMG_POSTER):
        return f'{TMDB_IMAGE_BASE}/{size}{path}' if path else ''

    # Mapa de generos TMDB (evita chamada extra de API por item na listagem)
    _GENRE_MAP = {
        28:'Acao',35:'Comedia',80:'Crime',99:'Documentario',18:'Drama',
        10751:'Familia',14:'Fantasia',36:'Historia',27:'Terror',10402:'Musica',
        9648:'Misterio',10749:'Romance',878:'Ficcao Cientifica',10770:'Cinema TV',
        53:'Suspense',10752:'Guerra',37:'Faroeste',
        10759:'Acao e Aventura',16:'Animacao',10762:'Infantil',10763:'Noticias',
        10764:'Reality',10765:'Sci-Fi e Fantasia',10766:'Novela',10767:'Talk Show',
        10768:'Guerra e Politica'
    }

    def _norm(self, m):
        year  = (m.get('release_date') or m.get('first_air_date') or '')[:4]
        title = m.get('title') or m.get('name') or m.get('original_title') or ''
        ttype = 'movie' if ('title' in m and 'name' not in m) or m.get('media_type') == 'movie' else 'tv'
        # Converte genre_ids para nomes usando mapa local (sem chamada extra de API)
        genre_ids = m.get('genre_ids', [])
        genre_str = ', '.join(self._GENRE_MAP.get(gid, '') for gid in genre_ids if gid in self._GENRE_MAP)
        return {
            'tmdb_id':   m.get('id', 0),
            'tmdb_type': ttype,
            'title':     title,
            'original_title': (m.get('original_title') or m.get('original_name') or ''),
            'original_language': m.get('original_language', ''),
            'year':      year,
            'plot':      m.get('overview', ''),
            'rating':    round(float(m.get('vote_average') or 0), 1),
            'votes':     m.get('vote_count', 0),
            'popularity': float(m.get('popularity') or 0),
            'genre':     genre_str,
            'icon':      self.img(m.get('poster_path')),
            'fanart':    self.img(m.get('backdrop_path'), IMG_FANART),
        }

    # ── Listas ──────────────────────────────────────────────────────

    _API_PAGE_SIZE = 20

    def _fetch_multi_page(self, ep, params, items_per_page=50):
        """
        Fetch multiple TMDB API pages to reach items_per_page.
        Returns (items_list, total_api_pages)
        """
        page = params.get('page', 1)
        # Calculate which API pages we need: for display page N, we need
        # to fetch enough API pages to cover N * items_per_page items.
        # API returns 20 items/page. We need ceil(items_per_page / 20) pages.
        apis_per_display = -(-items_per_page // self._API_PAGE_SIZE)  # ceil division
        start_api_page = (page - 1) * apis_per_display + 1

        all_results = []
        total_api_pages = 1
        for i in range(apis_per_display):
            p = start_api_page + i
            p_params = dict(params, page=p)
            data = self._get(ep, p_params)
            if not data:
                break
            all_results.extend(data.get('results', []))
            total_api_pages = max(total_api_pages, int(data.get('total_pages', 1)))
            # If this was the last available page, stop
            if p >= total_api_pages:
                break

        sliced = all_results[:items_per_page]
        total_display_pages = -(-total_api_pages // apis_per_display)  # ceil
        return sliced, total_display_pages

    def get_movies(self, list_type='popular', page=1, genre_id=None, items_per_page=50):
        ep_map = {'popular':'movie/popular','now_playing':'movie/now_playing',
                  'upcoming':'movie/upcoming','top_rated':'movie/top_rated'}
        params = {'page': page}
        if list_type == 'genre' and genre_id:
            ep = 'discover/movie'
            params.update({
                'with_genres':    genre_id,
                'sort_by':        'popularity.desc',
                'vote_count.gte': 50,
            })
        else:
            ep = ep_map.get(list_type)
            if not ep: return [], 1
        results, total_pages = self._fetch_multi_page(ep, params, items_per_page)
        if list_type == 'genre' and genre_id:
            gid = int(genre_id)
            results = [m for m in results if gid in (m.get('genre_ids') or [])]
        return [self._norm(m) for m in results], total_pages

    def get_tv(self, list_type='popular', page=1, genre_id=None, items_per_page=50):
        ep_map = {'popular':'tv/popular','airing_today':'tv/airing_today',
                  'on_the_air':'tv/on_the_air','top_rated':'tv/top_rated'}
        params = {'page': page}
        if list_type == 'genre' and genre_id:
            ep = 'discover/tv'
            params.update({
                'with_genres':    genre_id,
                'sort_by':        'popularity.desc',
                'vote_count.gte': 30,
            })
        else:
            ep = ep_map.get(list_type)
            if not ep: return [], 1
        results, total_pages = self._fetch_multi_page(ep, params, items_per_page)
        if list_type == 'genre' and genre_id:
            gid = int(genre_id)
            results = [t for t in results if gid in (t.get('genre_ids') or [])]
        return [self._norm(t) for t in results], total_pages

    def search_movies(self, query, page=1, year=None):
        params = {'query': query, 'page': page}
        if year and str(year).isdigit():
            params['year'] = int(year)
        data = self._get('search/movie', params)
        if not data: return [], 1
        return [self._norm(m) for m in data.get('results', [])], int(data.get('total_pages', 1))

    def search_tv(self, query, page=1, year=None):
        params = {'query': query, 'page': page}
        if year and str(year).isdigit():
            params['first_air_date_year'] = int(year)
        data = self._get('search/tv', params)
        if not data: return [], 1
        return [self._norm(t) for t in data.get('results', [])], int(data.get('total_pages', 1))

    def get_movie_genres(self):
        d = self._get('genre/movie/list')
        return d.get('genres', []) if d else []

    def get_tv_genres(self):
        d = self._get('genre/tv/list')
        return d.get('genres', []) if d else []

    # ── Detalhes completos ───────────────────────────────────────────

    def get_full_movie_details(self, tmdb_id):
        """
        Retorna dict completo para filme:
        title, year, plot, tagline, rating, votes, runtime,
        genres, studio, director, cast, trailer,
        collection (name + parts), similar, icon, fanart
        """
        key = f'fmov_{tmdb_id}'
        cached = self.cache.get(key)
        if cached: return cached

        data = self._get(
            f'movie/{tmdb_id}',
            {'append_to_response': 'credits,videos,similar,release_dates'}
        )
        if not data: return None

        # Elenco (15 primeiros)
        cast = []
        for a in data.get('credits', {}).get('cast', [])[:15]:
            cast.append({
                'name':      a.get('name', ''),
                'character': a.get('character', ''),
                'thumb':     self.img(a.get('profile_path'), IMG_PROFILE),
                'order':     a.get('order', 99),
            })

        # Crew: diretores + roteiristas
        crew = data.get('credits', {}).get('crew', [])
        directors  = [c['name'] for c in crew if c.get('job') == 'Director']
        writers    = [c['name'] for c in crew if c.get('job') in ('Screenplay','Writer','Story')][:3]

        # Trailer (primeiro trailer ou teaser do YouTube)
        trailer = ''
        for v in data.get('videos', {}).get('results', []):
            if v.get('site') == 'YouTube':
                if v.get('type') == 'Trailer' and not trailer:
                    trailer = f"plugin://plugin.video.youtube/play/?video_id={v['key']}"
                elif v.get('type') == 'Teaser' and not trailer:
                    trailer = f"plugin://plugin.video.youtube/play/?video_id={v['key']}"

        # Classificacao indicativa
        certification = ''
        for rel in data.get('release_dates', {}).get('results', []):
            if rel.get('iso_3166_1') in ('BR', 'US'):
                for rd in rel.get('release_dates', []):
                    if rd.get('certification'):
                        certification = rd['certification']
                        break
                if certification:
                    break

        # Colecao
        collection = None
        col_raw = data.get('belongs_to_collection')
        if col_raw and col_raw.get('id'):
            col_data = self._get(f"collection/{col_raw['id']}")
            if col_data:
                parts = sorted(
                    [self._norm(p) for p in col_data.get('parts', []) if p.get('id')],
                    key=lambda x: x.get('year') or '9999'
                )
                collection = {
                    'id':     col_raw['id'],
                    'name':   col_raw.get('name', ''),
                    'poster': self.img(col_raw.get('poster_path')),
                    'parts':  parts,
                }

        # Similares (12)
        similar = [self._norm(m) for m in data.get('similar', {}).get('results', [])[:12]]

        result = {
            'tmdb_id':        data.get('id'),
            'tmdb_type':      'movie',
            'title':          data.get('title', ''),
            'original_title': data.get('original_title', ''),
            'year':           (data.get('release_date') or '')[:4],
            'release_date':   data.get('release_date', ''),
            'plot':           data.get('overview', ''),
            'tagline':        data.get('tagline', ''),
            'rating':         round(float(data.get('vote_average') or 0), 1),
            'votes':          data.get('vote_count', 0),
            'runtime':        data.get('runtime', 0),
            'genres':         [g['name'] for g in data.get('genres', [])],
            'genre_ids':      [g['id']   for g in data.get('genres', [])],
            'studio':         (data.get('production_companies') or [{}])[0].get('name', ''),
            'country':        (data.get('production_countries') or [{}])[0].get('iso_3166_1', ''),
            'director':       ', '.join(directors),
            'writer':         ', '.join(writers),
            'certification':  certification,
            'cast':           cast,
            'trailer':        trailer,
            'collection':     collection,
            'similar':        similar,
            'icon':           self.img(data.get('poster_path')),
            'fanart':         self.img(data.get('backdrop_path'), IMG_FANART),
            'thumb':          self.img(data.get('backdrop_path'), IMG_THUMB),
            'popularity':     data.get('popularity', 0),
            'imdb_id':        data.get('imdb_id', ''),
            'homepage':       data.get('homepage', ''),
        }
        self.cache.set(key, result)
        return result

    def get_full_tv_details(self, tmdb_id):
        """
        Retorna dict completo para serie:
        title, year, plot, rating, votes, seasons_count,
        genres, networks, creator, cast, trailer, similar
        """
        key = f'ftv_{tmdb_id}'
        cached = self.cache.get(key)
        if cached: return cached

        data = self._get(
            f'tv/{tmdb_id}',
            {'append_to_response': 'credits,videos,similar,content_ratings,external_ids'}
        )
        if not data: return None

        cast = []
        for a in data.get('credits', {}).get('cast', [])[:15]:
            cast.append({
                'name':      a.get('name', ''),
                'character': a.get('character', ''),
                'thumb':     self.img(a.get('profile_path'), IMG_PROFILE),
            })

        trailer = ''
        for v in data.get('videos', {}).get('results', []):
            if v.get('site') == 'YouTube' and v.get('type') in ('Trailer', 'Teaser'):
                trailer = f"plugin://plugin.video.youtube/play/?video_id={v['key']}"
                break

        # Classificacao
        certification = ''
        for cr in data.get('content_ratings', {}).get('results', []):
            if cr.get('iso_3166_1') == 'BR':
                certification = cr.get('rating', '')
                break
        if not certification:
            for cr in data.get('content_ratings', {}).get('results', []):
                if cr.get('iso_3166_1') == 'US':
                    certification = cr.get('rating', '')
                    break

        similar = [self._norm(t) for t in data.get('similar', {}).get('results', [])[:12]]

        result = {
            'tmdb_id':        data.get('id'),
            'tmdb_type':      'tv',
            'title':          data.get('name', ''),
            'original_title': data.get('original_name', ''),
            'year':           (data.get('first_air_date') or '')[:4],
            'release_date':   data.get('first_air_date', ''),
            'plot':           data.get('overview', ''),
            'tagline':        data.get('tagline', ''),
            'rating':         round(float(data.get('vote_average') or 0), 1),
            'votes':          data.get('vote_count', 0),
            'seasons_count':  data.get('number_of_seasons', 0),
            'episodes_count': data.get('number_of_episodes', 0),
            'status':         data.get('status', ''),
            'genres':         [g['name'] for g in data.get('genres', [])],
            'genre_ids':      [g['id']   for g in data.get('genres', [])],
            'networks':       [n['name'] for n in data.get('networks', [])],
            'country':        (data.get('origin_country') or [''])[0],
            'creator':        ', '.join(c['name'] for c in data.get('created_by', [])),
            'certification':  certification,
            'cast':           cast,
            'trailer':        trailer,
            'similar':        similar,
            'icon':           self.img(data.get('poster_path')),
            'fanart':         self.img(data.get('backdrop_path'), IMG_FANART),
            'thumb':          self.img(data.get('backdrop_path'), IMG_THUMB),
            'homepage':       data.get('homepage', ''),
            'imdb_id':        (data.get('external_ids') or {}).get('imdb_id', ''),
        }
        self.cache.set(key, result)
        return result

#________________________________________________________________________________    

    def discover_movies(self, with_genres=None, page=1, sort_by='popularity.desc', items_per_page=50):
        """
        Busca filmes por gênero usando discover/movie
        """
        params = {
            'page': page,
            'sort_by': sort_by,
            'vote_count.gte': 50
        }
        if with_genres:
            params['with_genres'] = with_genres
        
        results, total_pages = self._fetch_multi_page('discover/movie', params, items_per_page)
        
        movies = []
        for m in results:
            genre_ids = m.get('genre_ids', [])
            if with_genres and int(with_genres) not in genre_ids:
                continue
            movies.append({
                'tmdb_id': m.get('id'),
                'title': m.get('title', ''),
                'year': (m.get('release_date') or '')[:4],
                'rating': round(float(m.get('vote_average') or 0), 1),
                'icon': self.img(m.get('poster_path')),
                'fanart': self.img(m.get('backdrop_path'), 'original'),
                'plot': m.get('overview', ''),
            })
        
        return movies, total_pages
        
    def discover_tv(self, with_genres=None, page=1, sort_by='popularity.desc', items_per_page=50):
        """
        Busca séries por gênero usando discover/tv
        """
        params = {
            'page': page,
            'sort_by': sort_by,
            'vote_count.gte': 30
        }
        if with_genres:
            params['with_genres'] = with_genres
        
        results, total_pages = self._fetch_multi_page('discover/tv', params, items_per_page)
        
        shows = []
        for t in results:
            genre_ids = t.get('genre_ids', [])
            if with_genres and int(with_genres) not in genre_ids:
                continue
            
            shows.append({
                'tmdb_id': t.get('id'),
                'title': t.get('name', ''),
                'year': (t.get('first_air_date') or '')[:4],
                'rating': round(float(t.get('vote_average') or 0), 1),
                'icon': self.img(t.get('poster_path')),
                'fanart': self.img(t.get('backdrop_path'), 'original'),
                'plot': t.get('overview', ''),
            })
        
        return shows, total_pages


    # ── Busca em todos os servidores (paralela) ──────────────────────

    def find_in_all_servers(self, title, tmdb_type, servers, progress_cb=None, tmdb_year='', cancel_event=None, max_wait=None, max_workers=None, request_timeout=None):
        """
        Busca em TODOS os servidores Xtream em paralelo (todos sao consultados).
        progress_cb(pct, msg) - callback opcional para DialogProgress
        tmdb_year - ano do TMDB para penalizar resultados com ano diferente
        cancel_event - threading.Event: quando setado, interrompe a busca
        max_wait - piso de tempo total (s); o prazo real cresce automaticamente
                   para dar tempo de consultar TODOS os servidores.
        max_workers - maximo de servidores consultados ao mesmo tempo (default 6).
        request_timeout - timeout por requisicao HTTP (default 5s).

        Retorna lista de dicts ordenada por match_score desc (resultados de todos
        os servidores que contem o titulo).
        """
        if not servers:
            return []

        results      = []
        results_lock = threading.Lock()
        total        = len(servers)
        done_count   = [0]

        if max_workers is None:
            max_workers = 6
        try:
            max_workers = max(1, min(int(max_workers), max(1, total)))
        except Exception:
            max_workers = 6

        if request_timeout is None:
            request_timeout = 5.0
        try:
            request_timeout = max(2.0, float(request_timeout))
        except Exception:
            request_timeout = 5.0

        if max_wait is None:
            max_wait = 0.0
        try:
            max_wait = max(0.0, float(max_wait))
        except Exception:
            max_wait = 0.0

        UA   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        _sem = threading.BoundedSemaphore(max_workers)

        # Normalizacoes do titulo calculadas UMA vez (evita re-normalizar o titulo
        # da query para cada item do catalogo — grande ganho em TV Box fracos).
        _q_norm  = _norm_title(title)
        _q_lower = title.lower().strip()
        # Tokens do titulo (sem acento/pontuacao/artigos) p/ pre-filtro tolerante:
        # "Pantera Negra: Wakanda" casa com "Pantera Negra - Wakanda" e "Ação" com "Acao".
        _q_tokens_all = [t for t in _q_norm.split() if t]
        # "Duna 2021" deve pre-filtrar por "Duna" (o ano e tratado no score).
        _q_tokens = ([t for t in _q_tokens_all
                      if not (_sm_is_year_token and _sm_is_year_token(t))]
                     or _q_tokens_all)

        def _finish(srv):
            with results_lock:
                done_count[0] += 1
                if progress_cb and not (cancel_event and cancel_event.is_set()):
                    pct = int(10 + 85 * done_count[0] / total)
                    try:
                        progress_cb(pct, f'Verificado {done_count[0]}/{total}: {(srv.get("name") or "Servidor").strip()}')
                    except Exception:
                        pass

        def _search_one(srv):
            try:
                if cancel_event and cancel_event.is_set():
                    return
                with _sem:
                    if cancel_event and cancel_event.is_set():
                        return
                    _search_one_worker(srv)
            except Exception as e:
                xbmc.log(f'[KelTec-TMDBv3] {(srv.get("name") or "Servidor").strip()}: {type(e).__name__}: {e}', xbmc.LOGWARNING)
            finally:
                _finish(srv)

        def _search_one_worker(srv):
            s_url  = (srv.get('url') or '').strip().rstrip('/')
            s_user = (srv.get('username') or srv.get('user') or '').strip()
            s_pass = (srv.get('password') or srv.get('pass') or '').strip()
            s_name = (srv.get('name') or 'Servidor').strip()

            if not s_url or not s_user or not s_pass:
                return

            endpoint = 'get_vod_streams' if tmdb_type == 'movie' else 'get_series'
            api_url  = f'{s_url}/player_api.php'
            params   = {'username': s_user, 'password': s_pass, 'action': endpoint}
            data     = None
            ctimeout = min(3.0, request_timeout)

            # -- Acelerador: catalogo em cache em disco (evita rebaixar tudo) --
            _from_cache = False
            if _accelerator is not None:
                try:
                    _cached = _accelerator.load_catalog(s_url, tmdb_type)
                except Exception:
                    _cached = None
                if isinstance(_cached, list) and _cached:
                    data = _cached
                    _from_cache = True

            if not _from_cache:
                # Sessao propria por worker: requests.Session nao e thread-safe
                # quando compartilhada por muitos threads simultaneos.
                session = None
                try:
                    session = _req_lib.Session()
                except Exception:
                    session = None
                try:
                    if cancel_event and cancel_event.is_set():
                        return
                    if session is not None:
                        resp = session.get(api_url, params=params,
                                           headers={'User-Agent': UA},
                                           timeout=(ctimeout, request_timeout))
                        resp.raise_for_status()
                        data = resp.json()
                    else:
                        import urllib.request, urllib.parse as _up
                        full_url = api_url + '?' + _up.urlencode(params)
                        req = urllib.request.Request(full_url, headers={'User-Agent': UA})
                        with urllib.request.urlopen(req, timeout=request_timeout) as r:
                            data = json.loads(r.read().decode('utf-8'))
                except Exception as _e1:
                    if cancel_event and cancel_event.is_set():
                        return
                    # 2a tentativa: limpa o cache DNS do host (IP velho/bloqueado), forca
                    # nova resolucao em paralelo (publico + sistema + DoH) e troca o UA.
                    try:
                        import urllib.request, urllib.parse as _up
                        _host = _up.urlparse(api_url).hostname or ''
                        _dns_invalidate(_host)       # proxima busca ja resolve de novo
                        full_url = api_url + '?' + _up.urlencode(params)
                        data = None
                        # Timeout (servidor lento/offline) nao melhora repetindo na hora:
                        # evita somar ~2x o tempo em servidores mortos.
                        _tname = type(_e1).__name__
                        if 'Timeout' in _tname or isinstance(_e1, TimeoutError):
                            raise RuntimeError('timeout')
                        for _ua in _ALT_UAS[:2]:
                            if cancel_event and cancel_event.is_set():
                                return
                            try:
                                req = urllib.request.Request(full_url, headers={'User-Agent': _ua})
                                with urllib.request.urlopen(req, timeout=request_timeout) as r:
                                    data = json.loads(r.read().decode('utf-8'))
                                if isinstance(data, list):
                                    break
                            except Exception as _e2:
                                data = None
                                # 401/403/406 = painel recusou o UA -> tenta o proximo UA;
                                # qualquer outro erro de rede: nao insiste.
                                if getattr(_e2, 'code', None) in (401, 403, 406, 429, 512):
                                    continue
                                break
                    except Exception:
                        data = None
                finally:
                    if session is not None:
                        try:
                            session.close()
                        except Exception:
                            pass
                # Grava o catalogo baixado no disco (acelera as proximas buscas)
                if _accelerator is not None and isinstance(data, list) and data:
                    try:
                        _accelerator.save_catalog(s_url, tmdb_type, data)
                    except Exception:
                        pass

            if not data or not isinstance(data, list):
                return

            # Limite de resultados por servidor (ainda coleta de TODOS os servidores)
            _max_per_srv = 12
            _found_srv   = 0

            for _idx, item in enumerate(data):
                # Checa cancelamento periodicamente (mantem UI responsiva)
                if _idx % 250 == 0:
                    if cancel_event and cancel_event.is_set():
                        return

                raw  = (item.get('name') or '').strip()
                if not raw:
                    continue
                _rl = raw.lower()
                if _q_lower not in _rl:
                    if not _q_tokens:
                        continue
                    _rf = _rl.translate(_FOLD_TABLE)
                    if not all(_t in _rf for _t in _q_tokens):
                        continue
                sc   = _match_with_year(title, raw, tmdb_year, q_norm=_q_norm)
                if sc < 0.60:  # threshold elevado — filtra titulos parciais
                    continue

                sid = str(item.get('stream_id') or item.get('series_id') or '')
                if not sid:
                    continue

                if tmdb_type == 'movie':
                    ext   = item.get('container_extension') or 'mp4'
                    stype = item.get('stream_type') or 'movie'
                    url   = f'{s_url}/{stype}/{s_user}/{s_pass}/{sid}.{ext}'
                    icon  = item.get('stream_icon') or ''
                    ctype = 'movie'
                else:
                    url   = ''
                    info  = item.get('info') or {}
                    icon  = info.get('cover_big') or info.get('movie_image') or item.get('cover') or ''
                    ctype = 'tvshow'

                dup = f'{s_url}|{sid}'
                with results_lock:
                    if not any(f'{r["server_url"]}|{r["stream_id"]}' == dup for r in results):
                        results.append({
                            'title':        raw,
                            'url':          url,
                            'icon':         icon,
                            'content_type': ctype,
                            'stream_id':    sid,
                            'match_score':  sc,
                            'tmdb_type':    tmdb_type,
                            'server_name':  s_name,
                            'server_url':   s_url,
                            'server_user':  s_user,
                            'server_pass':  s_pass,
                        })
                        _found_srv += 1
                        if _found_srv >= _max_per_srv:
                            break

        if cancel_event and cancel_event.is_set():
            return []

        threads = []
        for s in servers:
            if cancel_event and cancel_event.is_set():
                break
            t = threading.Thread(target=_search_one, args=(s,), daemon=True)
            t.start()
            threads.append(t)

        # Prazo para consultar TODOS os servidores: cada um leva no maximo ~2x o
        # timeout (requisicao + fallback), dividido pelas ondas do pool de workers.
        waves  = -(-total // max_workers)  # divisao arredondada para cima
        needed = (request_timeout * 2.0 + 2.5) * waves + 4.0
        deadline = time.time() + max(max_wait, needed)

        for t in threads:
            if cancel_event and cancel_event.is_set():
                break
            remaining = deadline - time.time()
            if remaining > 0:
                t.join(timeout=remaining)
            else:
                break

        alive = sum(1 for t in threads if t.is_alive())
        if alive:
            xbmc.log(f'[KelTec-TMDBv3] retornando cedo: {alive} servidor(es) ainda respondendo', xbmc.LOGINFO)

        with results_lock:
            results.sort(key=lambda x: (-x['match_score'], x['title'].lower()))
        return results

# ── Fuzzy match ────────────────────────────────────────────────────────

def _norm_title(t):
    """Titulo comparavel (delegado ao modulo compartilhado quando disponivel)."""
    if _sm_normalize_title is not None:
        try:
            return _sm_normalize_title(t)
        except Exception:
            pass
    import unicodedata
    t = (t or '').lower().strip()
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    # Remove artigos pt/en/es
    for a in [r'\bthe\b',r'\ba\b',r'\ban\b',r'\bo\b',r'\bos\b',r'\bas\b',
              r'\bum\b',r'\buma\b',r'\bel\b',r'\bla\b',r'\blos\b',r'\blas\b']:
        t = re.sub(a, ' ', t)
    t = re.sub(r'[^\w\s]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def _match(a, b):
    """
    Matching por palavras inteiras (com tolerancia a erros de digitacao).
    'a' e 'b' ja chegam normalizados por _norm_title.

    Regras:
      1. Exato / prefixo recebem prioridade maxima.
      2. Todas as palavras relevantes da query sao comparadas como palavras
         inteiras (evita 'Ava' casar com 'Avatar').
      3. Anos isolados sao ignorados quando ha outras palavras.
      4. Score final combina cobertura, precisao, Jaccard e proximidade
         de tamanho. Sem nenhuma palavra em comum, tenta similaridade
         global (typos leves) e descarta o resto.
    """
    if not a or not b:
        return 0.0

    if _sm_score_titles is not None:
        try:
            return _sm_score_titles({'tokens': a.split(), 'year': ''}, [b])
        except Exception:
            pass

    if a == b:
        return 1.0

    wa = a.split()
    wb = b.split()
    if not wa or not wb:
        return 0.0

    if _sm_is_year_token is not None:
        _filtered = [w for w in wa if not _sm_is_year_token(w)]
        if _filtered:
            wa = _filtered
        _filtered = [w for w in wb if not _sm_is_year_token(w)]
        if _filtered:
            wb = _filtered

    q_core = ' '.join(wa)
    c_core = ' '.join(wb)
    if q_core == c_core:
        return 1.0
    if c_core.startswith(q_core + ' '):
        return 0.95
    if q_core.startswith(c_core + ' '):
        return 0.92

    sa, sb = set(wa), set(wb)
    matched = sa & sb
    if not matched:
        from difflib import SequenceMatcher
        ratio = SequenceMatcher(None, q_core, c_core).ratio()
        return 0.72 * ratio if (ratio >= 0.84 and min(len(q_core), len(c_core)) >= 4) else 0.0

    coverage  = len(matched) / len(sa)
    precision = len(matched) / len(sb)
    jaccard   = len(matched) / len(sa | sb)
    len_ratio = min(len(wa), len(wb)) / max(len(wa), len(wb))
    score = coverage * 0.45 + precision * 0.15 + jaccard * 0.15 + len_ratio * 0.15

    if wa[0] == wb[0]:
        score += 0.05
    if (len(wa[0]) >= 4 and len(wb[0]) >= 4 and wa[0][:4] == wb[0][:4]):
        score += 0.03
    return min(1.0, score)


def _match_with_year(query_title, xtream_title, tmdb_year='', q_norm=None):
    """
    Match com bonus/penalidade de ano.
    Se o titulo do Xtream contem um ano que diverge do ano TMDB, penaliza.
    Se nao contem ano, usa o score normal.
    q_norm - titulo da query ja normalizado (opcional, evita re-normalizar
             o mesmo titulo milhares de vezes em aparelhos fracos).
    """
    base = _match(q_norm if q_norm is not None else _norm_title(query_title), _norm_title(xtream_title))
    if not base or not tmdb_year or not str(tmdb_year).isdigit():
        return base

    # Extrai ano do titulo Xtream (ex: "Avatar (2022)", "Avatar 2022")
    years_found = __import__('re').findall(r'\b(19|20)\d{2}\b', xtream_title)
    if not years_found:
        return base  # sem ano no titulo Xtream — nao penaliza

    xtream_year = int(years_found[-1])
    diff = abs(int(tmdb_year) - int(xtream_year))

    if diff == 0:
        return min(1.0, base + 0.05)   # bonus: ano exato
    elif diff == 1:
        return base                     # tolerancia de 1 ano (release vs lancamento BR)
    elif diff <= 3:
        return base * 0.85             # penalidade leve
    else:
        return base * 0.50             # penalidade forte (provavelmente titulo diferente)


# ── Factory ────────────────────────────────────────────────────────────

def get_tmdb_browser(addon):
    try:
        api_key = addon.getSetting('tmdb_api_key') or ''
        if not api_key:
            xbmc.log('[KelTec-TMDBv3] Sem API Key TMDB.', xbmc.LOGWARNING)
            return None
        lang      = addon.getSetting('tmdb_language') or 'pt-BR'
        profile   = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
        cache_dir = os.path.join(profile, 'tmdb_browser_cache')
        return TMDBBrowser(api_key=api_key, language=lang,
                           cache_dir=cache_dir, cache_hours=6)
    except Exception as e:
        xbmc.log(f'[KelTec-TMDBv3] Erro: {e}', xbmc.LOGERROR)
        return None
