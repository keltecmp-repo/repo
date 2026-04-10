# -*- coding: utf-8 -*-
"""
TMDB Helper - Integração Completa com The Movie Database
=========================================================

Fornece metadados ricos para filmes, séries e episódios:
- Posters em HD
- Fanart em 4K
- Plots detalhados em português
- Ratings (IMDb, TMDB)
- Elenco e diretor
- Trailers
- Gêneros, ano, duração

Autor: KelTec Media Play
"""

import os
import json
import time
import re
import threading
import requests
from datetime import datetime, timedelta

try:
    from kodi_six import xbmc, xbmcaddon, xbmcvfs
except ImportError:
    import xbmc
    import xbmcaddon
    import xbmcvfs


class TMDBHelper:
    """Helper para integração com TMDB API"""
    
    # URLs da API
    BASE_URL = "https://api.themoviedb.org/3"
    IMAGE_BASE_URL = "https://image.tmdb.org/t/p"
    YOUTUBE_BASE_URL = "https://www.youtube.com/watch?v="
    
    # Tamanhos de imagem
    POSTER_SIZE = "w500"      # Poster médio (boa qualidade)
    FANART_SIZE = "original"  # Fanart máxima qualidade
    PROFILE_SIZE = "w185"     # Fotos de elenco
    
    def __init__(self, api_key, cache_dir, language='pt-BR', cache_days=7):
        """
        Inicializa o TMDB Helper
        
        Args:
            api_key: Chave da API TMDB (gratuita em themoviedb.org)
            cache_dir: Diretório para cache local
            language: Idioma dos metadados (pt-BR padrão)
            cache_days: Dias para expirar cache (7 padrão)
        """
        self.api_key = api_key
        self.cache_dir = cache_dir
        self.language = language
        self.cache_days = cache_days
        self.cache_file = os.path.join(cache_dir, 'tmdb_cache.json')
        self._cache_lock = threading.Lock()
        self.cache = self._load_cache()
        
        # Garante que diretório existe
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
    
    def log(self, message, level=xbmc.LOGINFO):
        """Log helper"""
        xbmc.log(f"[TMDB] {message}", level)
    
    # =========================
    # CACHE
    # =========================
    
    def _load_cache(self):
        """Carrega cache do disco"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            self.log(f"Erro ao carregar cache: {e}", xbmc.LOGWARNING)
        return {}
    
    def _save_cache(self):
        """Salva cache no disco"""
        try:
            with self._cache_lock:
                cache_copy = dict(self.cache)
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_copy, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.log(f"Erro ao salvar cache: {e}", xbmc.LOGERROR)
    
    def _is_cache_valid(self, cache_entry):
        """Verifica se entrada do cache ainda é válida"""
        if 'cached_at' not in cache_entry:
            return False
        
        cached_date = datetime.fromtimestamp(cache_entry['cached_at'])
        expire_date = cached_date + timedelta(days=self.cache_days)
        return datetime.now() < expire_date
    
    def _get_from_cache(self, cache_key):
        """Busca no cache (retorna None se não existir ou expirado)"""
        if cache_key in self.cache:
            entry = self.cache[cache_key]
            if self._is_cache_valid(entry):
                self.log(f"Cache hit: {cache_key}")
                return entry
            else:
                self.log(f"Cache expirado: {cache_key}")
                del self.cache[cache_key]
        return None
    
    def _add_to_cache(self, cache_key, data):
        """Adiciona ao cache"""
        data['cached_at'] = time.time()
        self.cache[cache_key] = data
        self._save_cache()
    
    # =========================
    # REQUISIÇÕES API
    # =========================
    
    def _request(self, endpoint, params=None):
        """Faz requisição à API TMDB"""
        if params is None:
            params = {}
        
        params['api_key'] = self.api_key
        params['language'] = self.language
        
        url = f"{self.BASE_URL}/{endpoint}"
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.log(f"Erro na requisição TMDB: {e}", xbmc.LOGERROR)
            return None
    
    # =========================
    # LIMPEZA DE TÍTULOS
    # =========================
    
    def _clean_title(self, title):
        """
        Limpa título para busca mais eficiente
        
        Remove:
        - Ano entre parênteses
        - Qualidade (HD, 4K, etc.)
        - Extras como [Dublado], (Legendado)
        - Caracteres especiais
        """
        # Remove ano (1999), [2020], etc.
        title = re.sub(r'[\(\[]?\d{4}[\)\]]?', '', title)
        
        # Remove qualidade
        title = re.sub(r'\b(HD|4K|720p|1080p|BluRay|WEB-DL|DVDRip)\b', '', title, flags=re.IGNORECASE)
        
        # Remove extras
        title = re.sub(r'[\(\[]?(Dublado|Legendado|Dual|Nacional)[\)\]]?', '', title, flags=re.IGNORECASE)
        
        # Remove múltiplos espaços
        title = re.sub(r'\s+', ' ', title)
        
        return title.strip()
    
    def _extract_year(self, title):
        """Extrai ano do título se existir"""
        match = re.search(r'\((\d{4})\)', title)
        if match:
            return int(match.group(1))
        return None
    
    # =========================
    # BUSCA
    # =========================
    
    def search_movie(self, title, year=None):
        """
        Busca filme por título
        
        Returns:
            dict com id, title, year, poster_path, etc.
            None se não encontrar
        """
        cache_key = f"search_movie_{title}_{year or 'any'}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        # Limpa título
        clean = self._clean_title(title)
        
        # Busca
        params = {'query': clean}
        if year:
            params['year'] = year
        
        data = self._request('search/movie', params)
        
        if data and data.get('results'):
            # Pega primeiro resultado
            result = data['results'][0]
            self._add_to_cache(cache_key, result)
            self.log(f"Filme encontrado: {result.get('title')} ({result.get('release_date', '')[:4]})")
            return result
        
        self.log(f"Filme não encontrado: {title}", xbmc.LOGWARNING)
        return None
    
    def search_tv(self, title, year=None):
        """
        Busca série por título
        
        Returns:
            dict com id, name, first_air_date, poster_path, etc.
            None se não encontrar
        """
        cache_key = f"search_tv_{title}_{year or 'any'}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        # Limpa título
        clean = self._clean_title(title)
        
        # Busca
        params = {'query': clean}
        if year:
            params['first_air_date_year'] = year
        
        data = self._request('search/tv', params)
        
        if data and data.get('results'):
            result = data['results'][0]
            self._add_to_cache(cache_key, result)
            self.log(f"Série encontrada: {result.get('name')} ({result.get('first_air_date', '')[:4]})")
            return result
        
        self.log(f"Série não encontrada: {title}", xbmc.LOGWARNING)
        return None
    
    # =========================
    # DETALHES COMPLETOS
    # =========================
    
    def get_movie_details(self, movie_id):
        """
        Busca detalhes completos do filme
        
        Inclui: credits (elenco), videos (trailers)
        """
        cache_key = f"movie_{movie_id}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        data = self._request(f'movie/{movie_id}', {
            'append_to_response': 'credits,videos'
        })
        
        if data:
            self._add_to_cache(cache_key, data)
            return data
        return None
    
    def get_tv_details(self, tv_id):
        """
        Busca detalhes completos da série
        
        Inclui: credits, videos
        """
        cache_key = f"tv_{tv_id}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        data = self._request(f'tv/{tv_id}', {
            'append_to_response': 'credits,videos'
        })
        
        if data:
            self._add_to_cache(cache_key, data)
            return data
        return None
    
    def get_episode_details(self, tv_id, season, episode):
        """
        Busca detalhes de episódio específico
        
        Inclui: nome, plot, poster, data de exibição
        """
        cache_key = f"episode_{tv_id}_s{season}e{episode}"
        cached = self._get_from_cache(cache_key)
        if cached:
            return cached
        
        data = self._request(f'tv/{tv_id}/season/{season}/episode/{episode}')
        
        if data:
            self._add_to_cache(cache_key, data)
            return data
        return None
    
    # =========================
    # PROCESSAMENTO DE METADADOS
    # =========================
    
    def get_image_url(self, path, size='original'):
        """Monta URL completa de imagem"""
        if not path:
            return ''
        return f"{self.IMAGE_BASE_URL}/{size}{path}"
    
    def get_youtube_url(self, key):
        """Monta URL do YouTube"""
        if not key:
            return ''
        return f"{self.YOUTUBE_BASE_URL}{key}"
    
    def process_movie_metadata(self, title, year=None):
        """
        Busca e processa metadados completos de filme
        
        Returns:
            dict com todos os metadados processados
        """
        # Tenta extrair ano do título se não foi fornecido
        if not year:
            year = self._extract_year(title)
        
        # Busca filme
        search_result = self.search_movie(title, year)
        if not search_result:
            return None
        
        movie_id = search_result.get('id')
        
        # Busca detalhes completos
        details = self.get_movie_details(movie_id)
        if not details:
            return None
        
        # Processa metadados
        metadata = {
            'tmdb_id': movie_id,
            'title': details.get('title', ''),
            'original_title': details.get('original_title', ''),
            'year': details.get('release_date', '')[:4] if details.get('release_date') else '',
            'rating': details.get('vote_average', 0),
            'votes': details.get('vote_count', 0),
            'plot': details.get('overview', ''),
            'tagline': details.get('tagline', ''),
            'runtime': details.get('runtime', 0),  # minutos
            'poster': self.get_image_url(details.get('poster_path'), self.POSTER_SIZE),
            'fanart': self.get_image_url(details.get('backdrop_path'), self.FANART_SIZE),
            'genres': [g['name'] for g in details.get('genres', [])],
            'studio': details.get('production_companies', [{}])[0].get('name', '') if details.get('production_companies') else '',
        }
        
        # Elenco (primeiros 5)
        credits = details.get('credits', {})
        cast = credits.get('cast', [])[:5]
        metadata['cast'] = [
            {
                'name': actor['name'],
                'character': actor.get('character', ''),
                'thumb': self.get_image_url(actor.get('profile_path'), self.PROFILE_SIZE)
            }
            for actor in cast
        ]
        
        # Diretor
        crew = credits.get('crew', [])
        directors = [c['name'] for c in crew if c.get('job') == 'Director']
        metadata['director'] = ', '.join(directors) if directors else ''
        
        # Trailer (primeiro vídeo do YouTube)
        videos = details.get('videos', {}).get('results', [])
        youtube_videos = [v for v in videos if v.get('site') == 'YouTube']
        if youtube_videos:
            metadata['trailer'] = self.get_youtube_url(youtube_videos[0]['key'])
        else:
            metadata['trailer'] = ''
        
        return metadata
    
    def process_tv_metadata(self, title, year=None):
        """
        Busca e processa metadados completos de série
        
        Returns:
            dict com todos os metadados processados
        """
        if not year:
            year = self._extract_year(title)
        
        search_result = self.search_tv(title, year)
        if not search_result:
            return None
        
        tv_id = search_result.get('id')
        
        details = self.get_tv_details(tv_id)
        if not details:
            return None
        
        metadata = {
            'tmdb_id': tv_id,
            'title': details.get('name', ''),
            'original_title': details.get('original_name', ''),
            'year': details.get('first_air_date', '')[:4] if details.get('first_air_date') else '',
            'rating': details.get('vote_average', 0),
            'votes': details.get('vote_count', 0),
            'plot': details.get('overview', ''),
            'tagline': details.get('tagline', ''),
            'seasons': details.get('number_of_seasons', 0),
            'episodes': details.get('number_of_episodes', 0),
            'status': details.get('status', ''),  # Em exibição, Finalizada, etc.
            'poster': self.get_image_url(details.get('poster_path'), self.POSTER_SIZE),
            'fanart': self.get_image_url(details.get('backdrop_path'), self.FANART_SIZE),
            'genres': [g['name'] for g in details.get('genres', [])],
            'networks': [n['name'] for n in details.get('networks', [])],
        }
        
        # Elenco
        credits = details.get('credits', {})
        cast = credits.get('cast', [])[:5]
        metadata['cast'] = [
            {
                'name': actor['name'],
                'character': actor.get('character', ''),
                'thumb': self.get_image_url(actor.get('profile_path'), self.PROFILE_SIZE)
            }
            for actor in cast
        ]
        
        # Criadores
        creators = details.get('created_by', [])
        metadata['creator'] = ', '.join([c['name'] for c in creators]) if creators else ''
        
        # Trailer
        videos = details.get('videos', {}).get('results', [])
        youtube_videos = [v for v in videos if v.get('site') == 'YouTube']
        if youtube_videos:
            metadata['trailer'] = self.get_youtube_url(youtube_videos[0]['key'])
        else:
            metadata['trailer'] = ''
        
        return metadata
    
    def process_episode_metadata(self, tv_title, season, episode):
        """
        Busca metadados de episódio específico
        
        Returns:
            dict com metadados do episódio
        """
        # Busca série primeiro
        search_result = self.search_tv(tv_title)
        if not search_result:
            return None
        
        tv_id = search_result.get('id')
        
        # Busca episódio
        ep_details = self.get_episode_details(tv_id, season, episode)
        if not ep_details:
            return None
        
        metadata = {
            'episode_name': ep_details.get('name', ''),
            'episode_number': ep_details.get('episode_number', episode),
            'season_number': ep_details.get('season_number', season),
            'air_date': ep_details.get('air_date', ''),
            'rating': ep_details.get('vote_average', 0),
            'plot': ep_details.get('overview', ''),
            'poster': self.get_image_url(ep_details.get('still_path'), self.POSTER_SIZE),
        }
        
        return metadata
    
    # =========================
    # FORMATAÇÃO PARA KODI
    # =========================
    
    def format_movie_for_kodi(self, metadata):
        """
        Formata metadados de filme para InfoLabel do Kodi
        
        Returns:
            dict pronto para li.setInfo('video', {...})
        """
        if not metadata:
            return {}
        
        info = {
            'title': metadata.get('title', ''),
            'originaltitle': metadata.get('original_title', ''),
            'year': int(metadata.get('year', 0)) if metadata.get('year') else 0,
            'rating': float(metadata.get('rating', 0)),
            'votes': str(metadata.get('votes', 0)),
            'plot': metadata.get('plot', ''),
            'tagline': metadata.get('tagline', ''),
            'duration': int(metadata.get('runtime', 0)) * 60,  # Kodi usa segundos
            'genre': ', '.join(metadata.get('genres', [])),
            'studio': metadata.get('studio', ''),
            'director': metadata.get('director', ''),
            'mediatype': 'movie',
        }
        
        # Cast (formato Kodi)
        if metadata.get('cast'):
            info['cast'] = [actor['name'] for actor in metadata['cast']]
            info['castandrole'] = [(actor['name'], actor['character']) for actor in metadata['cast']]
        
        return info
    
    def format_tv_for_kodi(self, metadata):
        """
        Formata metadados de série para InfoLabel do Kodi
        """
        if not metadata:
            return {}
        
        info = {
            'title': metadata.get('title', ''),
            'tvshowtitle': metadata.get('title', ''),
            'originaltitle': metadata.get('original_title', ''),
            'year': int(metadata.get('year', 0)) if metadata.get('year') else 0,
            'rating': float(metadata.get('rating', 0)),
            'votes': str(metadata.get('votes', 0)),
            'plot': metadata.get('plot', ''),
            'tagline': metadata.get('tagline', ''),
            'genre': ', '.join(metadata.get('genres', [])),
            'studio': ', '.join(metadata.get('networks', [])),
            'season': metadata.get('seasons', 0),
            'episode': metadata.get('episodes', 0),
            'status': metadata.get('status', ''),
            'mediatype': 'tvshow',
        }
        
        if metadata.get('cast'):
            info['cast'] = [actor['name'] for actor in metadata['cast']]
            info['castandrole'] = [(actor['name'], actor['character']) for actor in metadata['cast']]
        
        return info
    
    def format_episode_for_kodi(self, metadata, tv_metadata=None):
        """
        Formata metadados de episódio para InfoLabel do Kodi
        """
        if not metadata:
            return {}
        
        info = {
            'title': metadata.get('episode_name', ''),
            'season': int(metadata.get('season_number', 0)),
            'episode': int(metadata.get('episode_number', 0)),
            'aired': metadata.get('air_date', ''),
            'rating': float(metadata.get('rating', 0)),
            'plot': metadata.get('plot', ''),
            'mediatype': 'episode',
        }
        
        # Adiciona info da série se disponível
        if tv_metadata:
            info['tvshowtitle'] = tv_metadata.get('title', '')
            info['year'] = int(tv_metadata.get('year', 0)) if tv_metadata.get('year') else 0
        
        return info


def get_tmdb_helper(addon):
    """
    Factory function para criar TMDBHelper
    
    Lê configurações do settings.xml do add-on
    """
    try:
        # Importa xbmcvfs dentro da função para garantir que está disponível
        import xbmcvfs
        
        api_key = addon.getSetting('tmdb_api_key') or ''
        enabled = addon.getSetting('tmdb_enabled') == 'true'
        language = addon.getSetting('tmdb_language') or 'pt-BR'
        cache_days = int(addon.getSetting('tmdb_cache_days') or '7')
        
        xbmc.log(f"[TMDB] Configurações lidas: enabled={enabled}, has_key={bool(api_key)}, language={language}, cache_days={cache_days}", xbmc.LOGINFO)
        
        if not enabled:
            xbmc.log("[TMDB] TMDB desabilitado nas configurações", xbmc.LOGINFO)
            return None
        
        if not api_key:
            xbmc.log("[TMDB] API Key não configurada", xbmc.LOGWARNING)
            return None
        
        profile_dir = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
        
        xbmc.log(f"[TMDB] Inicializando com API Key: {api_key[:8]}... e cache em: {profile_dir}", xbmc.LOGINFO)
        
        return TMDBHelper(api_key, profile_dir, language, cache_days)
        
    except Exception as e:
        xbmc.log(f"[TMDB] Erro ao inicializar: {e}", xbmc.LOGERROR)
        import traceback
        xbmc.log(f"[TMDB] Traceback: {traceback.format_exc()}", xbmc.LOGERROR)
        return None