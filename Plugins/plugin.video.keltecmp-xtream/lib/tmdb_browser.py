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
    def _http_get(url, params=None, headers=None, timeout=18):
        h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        if headers:
            h.update(headers)
        r = _req_lib.get(url, params=params, headers=h, timeout=timeout)
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
            except: pass

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
        except: pass
        return None

    def set(self, key, value):
        self._mem[key] = (time.time(), value)
        try:
            with open(self._path(key), 'w', encoding='utf-8') as f:
                json.dump({'_ts': time.time(), 'd': value}, f, ensure_ascii=False)
        except: pass


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
            'year':      year,
            'plot':      m.get('overview', ''),
            'rating':    round(float(m.get('vote_average') or 0), 1),
            'votes':     m.get('vote_count', 0),
            'genre':     genre_str,
            'icon':      self.img(m.get('poster_path')),
            'fanart':    self.img(m.get('backdrop_path'), IMG_FANART),
        }

    # ── Listas ──────────────────────────────────────────────────────

    def get_movies(self, list_type='popular', page=1, genre_id=None):
        ep_map = {'popular':'movie/popular','now_playing':'movie/now_playing',
                  'upcoming':'movie/upcoming','top_rated':'movie/top_rated'}
        params = {'page': page}
        if list_type == 'genre' and genre_id:
            ep = 'discover/movie'
            # Exige que o genero escolhido seja o PRIMARIO (primeiro da lista)
            # vote_count minimo evita filmes obscuros que distorcem a lista
            params.update({
                'with_genres':    genre_id,       # deve conter este genero
                'sort_by':        'popularity.desc',
                'vote_count.gte': 50,             # minimo de votos (evita lixo)
            })
        else:
            ep = ep_map.get(list_type)
            if not ep: return [], 1
        data = self._get(ep, params)
        if not data: return [], 1
        results = data.get('results', [])
        # Filtro pos-requisicao: se buscando por genero, garante que o genero
        # escolhido esta na lista de generos do item (TMDB pode trazer hybridos)
        if list_type == 'genre' and genre_id:
            gid = int(genre_id)
            results = [m for m in results if gid in (m.get('genre_ids') or [])]
        return [self._norm(m) for m in results], int(data.get('total_pages', 1))

    def get_tv(self, list_type='popular', page=1, genre_id=None):
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
        data = self._get(ep, params)
        if not data: return [], 1
        results = data.get('results', [])
        if list_type == 'genre' and genre_id:
            gid = int(genre_id)
            results = [t for t in results if gid in (t.get('genre_ids') or [])]
        return [self._norm(t) for t in results], int(data.get('total_pages', 1))

    def search_movies(self, query, page=1):
        data = self._get('search/movie', {'query': query, 'page': page})
        if not data: return [], 1
        return [self._norm(m) for m in data.get('results', [])], int(data.get('total_pages', 1))

    def search_tv(self, query, page=1):
        data = self._get('search/tv', {'query': query, 'page': page})
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
            {'append_to_response': 'credits,videos,similar,content_ratings'}
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
        }
        self.cache.set(key, result)
        return result

#________________________________________________________________________________    

    def discover_movies(self, with_genres=None, page=1, sort_by='popularity.desc'):
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
        
        data = self._get('discover/movie', params)
        if not data:
            return [], 1
        
        results = data.get('results', [])
        total_pages = int(data.get('total_pages', 1))
        
        movies = []
        for m in results:
            # Verifica se o gênero está presente (filtro extra)
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
        
    def discover_tv(self, with_genres=None, page=1, sort_by='popularity.desc'):
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
        
        data = self._get('discover/tv', params)
        if not data:
            return [], 1
        
        results = data.get('results', [])
        total_pages = int(data.get('total_pages', 1))
        
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

    def find_in_all_servers(self, title, tmdb_type, servers, progress_cb=None, tmdb_year=''):
        """
        Busca em TODOS os servidores Xtream em paralelo.
        progress_cb(pct, msg) - callback opcional para DialogProgress
        tmdb_year - ano do TMDB para penalizar resultados com ano diferente

        Retorna lista de dicts ordenada por match_score desc.
        """
        if not servers:
            return []

        results      = []
        results_lock = threading.Lock()
        total        = len(servers)
        done_count   = [0]

        UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

        def _search_one(srv):
            s_url  = (srv.get('url') or '').strip().rstrip('/')
            s_user = (srv.get('username') or srv.get('user') or '').strip()
            s_pass = (srv.get('password') or srv.get('pass') or '').strip()
            s_name = (srv.get('name') or 'Servidor').strip()

            if not s_url or not s_user or not s_pass:
                with results_lock:
                    done_count[0] += 1
                return

            try:
                # Tenta ambos: com e sem porta explicita
                endpoint = 'get_vod_streams' if tmdb_type == 'movie' else 'get_series'
                api_url  = f'{s_url}/player_api.php'
                params   = {'username': s_user, 'password': s_pass, 'action': endpoint}

                try:
                    import requests as _r
                    resp = _r.get(api_url, params=params,
                                  headers={'User-Agent': UA}, timeout=22)
                    resp.raise_for_status()
                    data = resp.json()
                except Exception:
                    # Fallback: urllib
                    import urllib.request, urllib.parse as _up
                    full_url = api_url + '?' + _up.urlencode(params)
                    req = urllib.request.Request(full_url,
                                                  headers={'User-Agent': UA})
                    with urllib.request.urlopen(req, timeout=22) as r:
                        data = json.loads(r.read().decode('utf-8'))

                if not data or not isinstance(data, list):
                    return

                q = _norm_title(title)

                for item in data:
                    raw  = (item.get('name') or '').strip()
                    sc   = _match_with_year(title, raw, tmdb_year)
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

            except Exception as e:
                xbmc.log(f'[KelTec-TMDBv3] {s_name}: {type(e).__name__}: {e}', xbmc.LOGWARNING)
            finally:
                with results_lock:
                    done_count[0] += 1
                    if progress_cb:
                        pct = int(10 + 85 * done_count[0] / total)
                        progress_cb(pct, f'Verificado {done_count[0]}/{total}: {s_name}')

        threads  = [threading.Thread(target=_search_one, args=(s,), daemon=True) for s in servers]
        deadline = time.time() + 35
        for t in threads:
            t.start()
        for t in threads:
            remaining = max(0.3, deadline - time.time())
            t.join(timeout=remaining)

        results.sort(key=lambda x: (-x['match_score'], x['title'].lower()))
        return results[:25]

def get_full_movie_details_by_title(self, title):
    """Busca detalhes completos de um filme pelo título"""
    try:
        search_result = self.search_movies(title)
        if search_result and search_result[0]:
            return self.get_full_movie_details(search_result[0].get('tmdb_id'))
    except:
        pass
    return None

def get_full_tv_details_by_title(self, title):
    """Busca detalhes completos de uma série pelo título"""
    try:
        search_result = self.search_tv(title)
        if search_result and search_result[0]:
            return self.get_full_tv_details(search_result[0].get('tmdb_id'))
    except:
        pass
    return None

# ── Fuzzy match ────────────────────────────────────────────────────────

def _norm_title(t):
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
    Matching por palavras inteiras — evita falsos positivos tipo 'Ava'/'Atar'
    para a query 'Avatar'.
    Regras:
      1. Match exato → 1.0
      2. Todas as palavras da query devem aparecer como PALAVRAS INTEIRAS no
         resultado (nao como substrings). Se alguma faltar → penaliza forte.
      3. Score final = Jaccard ponderado pelo ratio de tamanho dos titulos.
    """
    if not a or not b: return 0.0
    if a == b: return 1.0

    wa = a.split()   # palavras da query normalizada
    wb = b.split()   # palavras do resultado normalizado
    if not wa or not wb: return 0.0

    sa, sb = set(wa), set(wb)

    # Quantas palavras da query aparecem como palavras inteiras no resultado?
    matched = sa & sb
    coverage = len(matched) / len(sa)   # 1.0 = todas as palavras da query presentes

    # Se nenhuma palavra da query aparece como palavra inteira → descarta
    if coverage == 0:
        return 0.0

    # Se a query tem 1 palavra e ela NAO aparece como palavra inteira → 0
    # (evita 'Ava'→'Avatar', 'Ko'→'Kodi', etc.)
    if len(wa) == 1 and coverage < 1.0:
        return 0.0

    # Jaccard nas palavras
    j = len(sa & sb) / len(sa | sb)

    # Penaliza resultados muito mais longos que a query
    # (preserva sequencias/continuacoes mas rejeita resultados completamente
    #  diferentes que so compartilham uma palavra genérica)
    len_ratio = min(len(wa), len(wb)) / max(len(wa), len(wb))

    # Bonus se os primeiros 4 chars batem (mesmo inicio de titulo)
    bonus = 0.08 if (len(a) >= 4 and len(b) >= 4 and a[:4] == b[:4]) else 0

    # Score = cobertura da query (peso 50%) + Jaccard (30%) + ratio tamanho (20%)
    score = coverage * 0.5 + j * 0.3 + len_ratio * 0.2 + bonus
    return min(1.0, score)


def _match_with_year(query_title, xtream_title, tmdb_year=''):
    """
    Match com bonus/penalidade de ano.
    Se o titulo do Xtream contem um ano que diverge do ano TMDB, penaliza.
    Se nao contem ano, usa o score normal.
    """
    base = _match(_norm_title(query_title), _norm_title(xtream_title))
    if not base or not tmdb_year or not str(tmdb_year).isdigit():
        return base

    # Extrai ano do titulo Xtream (ex: "Avatar (2022)", "Avatar 2022")
    import re as _re
    years_found = _re.findall(r'\b(19|20)\d{2}\b', xtream_title)
    if not years_found:
        return base  # sem ano no titulo Xtream — nao penaliza

    xtream_year = int(years_found[-1] + _re.findall(r'\b(?:19|20)(\d{2})\b', xtream_title)[-1] if False else years_found[-1])
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
