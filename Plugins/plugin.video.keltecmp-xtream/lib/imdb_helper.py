# -*- coding: utf-8 -*-
import json
import time
import re

try:
    import xbmc
    _KODI = True
except ImportError:
    _KODI = False

_API_URL = 'https://graphql.prod.api.imdb.a2z.com/'
_HEADERS = {
    'Referer': 'https://www.imdb.com/',
    'Origin': 'https://www.imdb.com',
    'Content-Type': 'application/json',
}
_CACHE = {}
_CACHE_TTL = 86400

def _log(msg):
    if _KODI:
        xbmc.log(f'[IMDB] {msg}', xbmc.LOGINFO)

def _gql_min(q):
    return re.sub(r' {4}', '', q)

_FETCH_QUERY = '''
query($id: ID!) {
    title(id: $id) {
        id
        titleText { text }
        plot { plotText { plainText } }
        primaryImage { url }
        releaseDate { year month day }
        ratingsSummary { aggregateRating voteCount }
        certificate { rating }
        titleGenres { genres { genre { text } } }
        directors: credits(first: 5, filter: { categories: ["director"] }) {
            edges { node { name { nameText { text } } } }
        }
        writers: credits(first: 5, filter: { categories: ["writer"] }) {
            edges { node { name { nameText { text } } } }
        }
        cast: credits(first: 10, filter: { categories: ["actor", "actress"] }) {
            edges {
                node {
                    ... on Cast {
                        name { nameText { text } primaryImage { url } }
                        characters { name }
                    }
                }
            }
        }
        latestTrailer {
            id
        }
    }
}
'''

_TRAILER_FRAGMENT = '''
fragment SharedVideoAllPlaybackUrls on Video {
    playbackURLs {
        displayName { value }
        videoMimeType
        url
    }
}
'''

_TRAILER_QUERY = '''
query VideoPlayback($viconst: ID!) {
    video(id: $viconst) {
        ...SharedVideoAllPlaybackUrls
    }
}
''' + _TRAILER_FRAGMENT

def _http_post_json(url, payload, headers, timeout=15):
    try:
        import requests
        r = requests.post(url, json=payload, headers=headers, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except ImportError:
        data = json.dumps(payload).encode('utf-8')
        import urllib.request, urllib.error
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8'))


def fetch_imdb_data(imdb_id):
    if not imdb_id or not imdb_id.startswith('tt'):
        return None
    now = time.time()
    cached = _CACHE.get(imdb_id)
    if cached and (now - cached['_ts']) < _CACHE_TTL:
        return cached['data']
    try:
        payload = {
            'query': _gql_min(_FETCH_QUERY),
            'variables': {'id': imdb_id}
        }
        raw = _http_post_json(_API_URL, payload, _HEADERS)
    except Exception as e:
        _log(f'fetch_imdb_data({imdb_id}) erro: {e}')
        if cached:
            return cached['data']
        return None

    title = raw.get('data', {}).get('title')
    if not title:
        return None

    rating = title.get('ratingsSummary') or {}
    cert = title.get('certificate') or {}
    genres = title.get('titleGenres') or {}
    directors = title.get('directors') or {}
    writers = title.get('writers') or {}
    cast_raw = title.get('cast') or {}
    release = title.get('releaseDate') or {}

    trailer_raw = title.get('latestTrailer') or {}
    trailer_id = trailer_raw.get('id') if trailer_raw else None

    result = {
        'title':       (title.get('titleText') or {}).get('text', ''),
        'plot':        (title.get('plot') or {}).get('plotText') or {},
        'poster':      (title.get('primaryImage') or {}).get('url', ''),
        'year':        release.get('year', ''),
        'rating':      rating.get('aggregateRating'),
        'votes':       rating.get('voteCount'),
        'certificate': cert.get('rating', ''),
        'genres':      [g['genre']['text'] for g in genres.get('genres', [])],
        'directors':   [
            e['node']['name']['nameText']['text']
            for e in directors.get('edges', [])
        ],
        'writers':     [
            e['node']['name']['nameText']['text']
            for e in writers.get('edges', [])
        ],
        'cast':        [
            {
                'name':    e['node']['name']['nameText']['text'],
                'role':    (e['node'].get('characters') or [{}])[0].get('name', ''),
                'thumb':   (e['node']['name'].get('primaryImage') or {}).get('url', ''),
            }
            for e in cast_raw.get('edges', [])
        ],
        'trailer_id':  trailer_id,
    }

    _CACHE[imdb_id] = {'data': result, '_ts': now}
    return result


def fetch_imdb_rating(imdb_id):
    data = fetch_imdb_data(imdb_id)
    if data:
        return {
            'rating': data.get('rating'),
            'votes':  data.get('votes'),
            'certificate': data.get('certificate'),
        }
    return None


def fetch_imdb_trailer_url(imdb_id):
    if not imdb_id or not imdb_id.startswith('tt'):
        return None
    now = time.time()
    cache_key = f'{imdb_id}_trailer'
    cached = _CACHE.get(cache_key)
    if cached and (now - cached['_ts']) < _CACHE_TTL:
        return cached['data']

    # First, get the trailer video ID from the title query
    data = fetch_imdb_data(imdb_id)
    if not data:
        return None
    trailer_id = data.get('trailer_id')
    if not trailer_id:
        return None

    # Now fetch the actual playback URL
    try:
        payload = {
            'query': _gql_min(_TRAILER_QUERY),
            'variables': {'viconst': trailer_id}
        }
        raw = _http_post_json(_API_URL, payload, _HEADERS)
    except Exception as e:
        _log(f'fetch_imdb_trailer_url({imdb_id}) erro: {e}')
        return None

    video = raw.get('data', {}).get('video')
    if not video:
        return None

    playback_urls = video.get('playbackURLs', [])
    if not playback_urls:
        return None

    # Pick the best quality MP4
    # Prefer 1080p, then 720p, then highest available
    mp4s = []
    for pu in playback_urls:
        if pu.get('videoMimeType') != 'MP4':
            continue
        name = (pu.get('displayName') or {}).get('value', '')
        url = pu.get('url', '')
        if not url:
            continue
        quality = 0
        if '1080' in name:
            quality = 1080
        elif '720' in name:
            quality = 720
        elif '480' in name:
            quality = 480
        elif '360' in name:
            quality = 360
        mp4s.append({'quality': quality, 'url': url})

    if not mp4s:
        return None

    mp4s.sort(key=lambda x: x['quality'], reverse=True)
    result_url = mp4s[0]['url']

    _CACHE[cache_key] = {'data': result_url, '_ts': now}
    return result_url


def clear_cache():
    _CACHE.clear()
