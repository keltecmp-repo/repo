# -*- coding: utf-8 -*-
"""
Pluto TV EPG Engine — Converte Pluto TV em EPG XMLTV para PVR.
Enriquecimento TMDB com cache persistente para posters/notas/generos.
"""
import json, os, time, re, threading, xml.etree.ElementTree as ET
import urllib.parse
import xbmc, xbmcvfs

ADDON_ID = 'plugin.video.keltecmp-xtream'
LOG_TAG = '[PlutoEPG]'
_CACHE_DIR = None
_TMDB_CACHE = {}
_TMDB_CACHE_LOCK = threading.Lock()
_TMDB_CACHE_PATH = None

def _log(msg):
    xbmc.log(f'{LOG_TAG} {msg}', xbmc.LOGINFO)

def _get_cache_dir():
    global _CACHE_DIR
    if _CACHE_DIR is None:
        addon = __import__('xbmcaddon').Addon(ADDON_ID)
        profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
        _CACHE_DIR = os.path.join(profile, 'pluto_epg_cache')
        if not os.path.exists(_CACHE_DIR):
            os.makedirs(_CACHE_DIR)
    return _CACHE_DIR

def _get_tmdb_cache_path():
    global _TMDB_CACHE_PATH
    if _TMDB_CACHE_PATH is None:
        _TMDB_CACHE_PATH = os.path.join(_get_cache_dir(), 'tmdb_programs.json')
    return _TMDB_CACHE_PATH

def _load_tmdb_cache():
    path = _get_tmdb_cache_path()
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save_tmdb_cache():
    path = _get_tmdb_cache_path()
    try:
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(_TMDB_CACHE, f, ensure_ascii=False)
        os.replace(tmp, path)
    except Exception as e:
        _log(f'Erro ao salvar cache TMDB: {e}')

def _xml_escape(s):
    if not s: return ''
    s = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    s = s.replace('"', '&quot;').replace("'", '&apos;')
    return s

def _ts_to_xmltv(ts):
    t = time.gmtime(ts)
    return time.strftime('%Y%m%d%H%M%S', t) + ' +0000'

def enrich_programs_tmdb(programs, tmdb_helper=None, now_ts=None, window_start=None, window_end=None):
    loaded = _load_tmdb_cache()
    with _TMDB_CACHE_LOCK:
        _TMDB_CACHE.update(loaded)
    needs_save = False
    if now_ts is None:
        now_ts = time.time()
    if window_start is None:
        window_start = now_ts - 86400
    if window_end is None:
        window_end = now_ts + 172800
    unique_titles = set()
    for prog_list in programs.values():
        for p in prog_list:
            title = p.get('title', '')
            if not title or title in _TMDB_CACHE:
                continue
            try:
                ts = p.get('start', None)
                if ts is None:
                    ts = p.get('timestamp', p.get(0, None))
                if ts is not None:
                    ts = float(ts)
                    if ts < window_start - 7200 or ts > window_end:
                        continue
            except (ValueError, TypeError, IndexError):
                pass
            unique_titles.add(title)
    if unique_titles and tmdb_helper:
        for title in list(unique_titles)[:300]:
            if title in _TMDB_CACHE:
                continue
            meta = {}
            try:
                result = tmdb_helper.process_tv_metadata(title)
                if result and result.get('title'):
                    meta = {
                        'poster': result.get('poster', ''),
                        'rating': result.get('rating', 0),
                        'year': result.get('year', 0),
                        'genre': (result.get('genre') or [''])[0] if isinstance(result.get('genre'), list) else (result.get('genre') or ''),
                        'plot': result.get('plot', ''),
                        'cast': (result.get('cast') or [])[:5],
                        'director': (result.get('director') or [''])[0] if isinstance(result.get('director'), list) else (result.get('director') or ''),
                    }
                else:
                    result = tmdb_helper.process_movie_metadata(title)
                    if result and result.get('title'):
                        meta = {
                            'poster': result.get('poster', ''),
                            'rating': result.get('rating', 0),
                            'year': result.get('year', 0),
                            'genre': (result.get('genre') or [''])[0] if isinstance(result.get('genre'), list) else (result.get('genre') or ''),
                            'plot': result.get('plot', ''),
                            'cast': (result.get('cast') or [])[:5],
                            'director': (result.get('director') or [''])[0] if isinstance(result.get('director'), list) else (result.get('director') or ''),
                        }
            except Exception:
                meta = {}
            with _TMDB_CACHE_LOCK:
                _TMDB_CACHE[title] = meta
            needs_save = True
    if needs_save:
        _save_tmdb_cache()
    return _TMDB_CACHE

def build_pvr_channels(data, region_code=None):
    channels = []
    regions = data.get('regions', {})
    for rcode, region in regions.items():
        if region_code and rcode != region_code:
            continue
        for ch_id, ch in region.get('channels', {}).items():
            name = ch.get('name', ch_id) or ch_id
            logo = ch.get('logo', '') or ''
            group = ch.get('group', 'Pluto TV')
            chno = ch.get('chno', '')
            tvg_id = f'pluto.{ch_id}'
            label = f'{chno} | {name}' if chno else name
            channels.append({
                'name': label,
                'url': f'plugin://plugin.video.keltecmp-xtream/?mode=pluto_tv_play&channel_id={urllib.parse.quote(ch_id)}',
                'tvg_id': tvg_id,
                'tvg_name': name,
                'logo': logo,
                'group': group,
                'chno': chno,
            })
    return channels

def build_epg_xml(data, tmdb_cache=None, region_code=None):
    root = ET.Element('tv')
    regions = data.get('regions', {})
    added_channels = set()
    now = time.time()
    for rcode, region in regions.items():
        if region_code and rcode != region_code:
            continue
        for ch_id, ch in region.get('channels', {}).items():
            tvg_id = f'pluto.{ch_id}'
            ch_el = ET.SubElement(root, 'channel', {'id': tvg_id})
            dn = ET.SubElement(ch_el, 'display-name')
            ch_name = str(ch.get('name', ch_id) or ch_id)
            dn.text = ch_name
            ch_logo = str(ch.get('logo', '') or '')
            ch_desc = str(ch.get('description', '') or '')
            if ch_logo:
                ch_el.set('icon', ch_logo)
            programs = ch.get('programs', [])
            chno = str(ch.get('chno', '') or '')
            for idx, prog in enumerate(programs):
                try:
                    start_ts = float(prog[0])
                except (IndexError, ValueError):
                    continue
                end_idx = idx + 1
                if end_idx < len(programs):
                    try:
                        end_ts = float(programs[end_idx][0])
                    except (ValueError, IndexError):
                        end_ts = start_ts + 1800
                else:
                    end_ts = start_ts + 1800
                if end_ts < now - 86400 or start_ts > now + 172800:
                    continue
                try:
                    title = str(prog[1]) if len(prog) > 1 else ''
                except Exception:
                    title = ''
                subtitle = str(prog[2]) if len(prog) > 2 else ''
                desc = str(prog[3]) if len(prog) > 3 and prog[3] else ''
                if not title:
                    continue
                prog_el = ET.SubElement(root, 'programme', {
                    'channel': tvg_id,
                    'start': _ts_to_xmltv(start_ts),
                    'stop': _ts_to_xmltv(end_ts),
                })
                title_el = ET.SubElement(prog_el, 'title')
                title_el.text = str(title)
                if subtitle:
                    sub_el = ET.SubElement(prog_el, 'sub-title')
                    sub_el.text = str(subtitle)
                desc_el = None
                if desc:
                    desc_el = ET.SubElement(prog_el, 'desc')
                    desc_el.text = str(desc)
                tmdb_meta = None
                if tmdb_cache and title in tmdb_cache:
                    tmdb_meta = tmdb_cache[title]
                # fallback: channel logo + channel desc when TMDB unavailable
                tmdb_poster = ''
                tmdb_plot = ''
                tmdb_rating = 0
                tmdb_genre = ''
                tmdb_year = 0
                tmdb_cast = []
                tmdb_director = ''
                if tmdb_meta:
                    try:
                        tmdb_poster = str(tmdb_meta.get('poster', '') or '')
                    except Exception:
                        pass
                    try:
                        tmdb_rating = tmdb_meta.get('rating') or 0
                    except Exception:
                        pass
                    try:
                        tmdb_genre = str(tmdb_meta.get('genre', '') or '')
                    except Exception:
                        pass
                    try:
                        tmdb_year = tmdb_meta.get('year') or 0
                    except Exception:
                        pass
                    try:
                        tmdb_plot = str(tmdb_meta.get('plot', '') or '')
                    except Exception:
                        pass
                    try:
                        tmdb_cast = list(tmdb_meta.get('cast', []) or [])
                    except Exception:
                        pass
                    try:
                        tmdb_director = str(tmdb_meta.get('director', '') or '')
                    except Exception:
                        pass
                prog_icon = tmdb_poster or ch_logo
                if prog_icon:
                    ET.SubElement(prog_el, 'icon', {'src': prog_icon})
                # desc: TMDB plot > original desc > channel description
                final_plot = tmdb_plot or desc or ch_desc
                if final_plot:
                    if desc_el is None:
                        desc_el = ET.SubElement(prog_el, 'desc')
                    desc_el.text = final_plot
                if tmdb_genre:
                    ET.SubElement(prog_el, 'category', {'lang': 'en'}).text = tmdb_genre
                if tmdb_year:
                    ET.SubElement(prog_el, 'date').text = str(tmdb_year)
                if tmdb_rating:
                    sr = ET.SubElement(prog_el, 'star-rating')
                    ET.SubElement(sr, 'points').text = str(tmdb_rating)
                if tmdb_cast or tmdb_director:
                    cred = ET.SubElement(prog_el, 'credits')
                    if tmdb_director:
                        ET.SubElement(cred, 'director').text = tmdb_director
                    for actor in tmdb_cast:
                        ET.SubElement(cred, 'actor').text = str(actor)
    return root

def export_pvr_files(channels, epg_root, m3u_path, epg_path):
    m3u_lines = ['#EXTM3U']
    for ch in channels:
        try:
            name = str(ch.get('name', 'Unknown') or 'Unknown')
            tvg_id = str(ch.get('tvg_id', '') or '')
            logo = str(ch.get('logo', '') or '')
            group = str(ch.get('group', 'Pluto TV') or 'Pluto TV')
            chno = str(ch.get('chno', '') or '')
            url = str(ch.get('url', '') or '')
        except Exception:
            continue
        attrs = [f'tvg-id="{tvg_id}"', f'tvg-name="{name}"']
        if logo:
            attrs.append(f'tvg-logo="{logo}"')
        if group:
            attrs.append(f'group-title="{group}"')
        if chno:
            attrs.append(f'tvg-chno="{chno}"')
        m3u_lines.append(f'#EXTINF:-1 {" ".join(attrs)},{name}')
        m3u_lines.append(url)
    try:
        tmp = m3u_path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            f.write('\n'.join(m3u_lines))
        os.replace(tmp, m3u_path)
    except Exception as e:
        _log(f'Erro M3U: {e}')
        return False
    try:
        tmp = epg_path + '.tmp'
        ET.ElementTree(epg_root).write(tmp, encoding='utf-8', xml_declaration=True)
        os.replace(tmp, epg_path)
    except Exception as e:
        _log(f'Erro EPG: {e}')
        return False
    _log(f'Exportados {len(channels)} canais Pluto TV para PVR')
    return True
