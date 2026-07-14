# -*- coding: utf-8 -*-
"""
Pluto TV nativo — sem dependencia externa (SlyGuy).
Canais gratis ao vivo com EPG, regioes e grupos.
"""
import json, gzip, time, uuid, io, os, threading, re as _re
from urllib.parse import urlencode, quote as _quote, quote_plus
from collections import OrderedDict

import requests as _req
_pluto_session = _req.Session()
_pluto_session.headers['Connection'] = 'keep-alive'
import xbmc, xbmcgui, xbmcplugin, xbmcvfs
try:
    from urllib3.util.ssl_ import create_urllib3_context
    import ssl, urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except Exception:
    pass

PLUTO_DATA_URL = 'https://i.mjh.nz/PlutoTV/.channels.json.gz'
PLUTO_BOOT_URL = 'https://boot.pluto.tv/v4/start'
PLUTO_STITCHER = 'https://cfd-v4-service-channel-stitcher-use1-1.prd.pluto.tv/v2/stitch/hls/channel/{id}/master.m3u8?{params}&jwt={token}&masterJWTPassthrough=true&includeExtendedEvents=true'
UUID_NAMESPACE = '122e1611-0232-4336-bf43-e054c8ecd0d5'
ALT_UA = 'otg/1.5.1 (AppleTv Apple TV 4; tvOS16.0; appletv.client) libcurl/7.58.0 OpenSSL/1.0.2o zlib/1.2.11 clib/1.8.56'
CACHE_TTL = 300
JWT_TTL = 1800

_cache = {}
_cache_lock = threading.Lock()
_ADDON_HANDLE = None

def _set_handle(handle):
    global _ADDON_HANDLE
    _ADDON_HANDLE = handle

def _log(msg):
    xbmc.log('[PlutoTV] ' + msg, xbmc.LOGINFO)

_RE_EMOJI = _re.compile(
    '[\U0001F000-\U0001FFFF\U00002000-\U000020FF\U00002100-\U0000214F'
    '\U00002190-\U000021FF\U00002300-\U000023FF\U00002400-\U0000243F'
    '\U00002440-\U000024FF\U000025A0-\U000025FF\U00002600-\U000026FF'
    '\U00002700-\U000027BF\U0000FE00-\U0000FE0F\U0001F600-\U0001F64F'
    '\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF'
    '\U00002702-\U000027B0\U000024C2-\U000025B7\U000025B6-\U000025C0'
    '\U000025C0-\U000025FE\U00002602-\U0000266F\U0000267F-\U0000267F'
    '\U00002693-\U000026D3\U0000266D-\U0000266F\U00002934-\U00002935'
    '\U00002B05-\U00002B07\U00002B55-\U00002B59\U00003030-\U00003030'
    '\U0000303D-\U0000303D\U00003297-\U00003299\U0001F004-\U0001F004'
    ']+', _re.UNICODE)

def _sanitize(text):
    text = _RE_EMOJI.sub('', text)
    text = text.replace('\u2500', '-').replace('\u2550', '-')
    text = text.replace('\u2588', '#').replace('\u2592', '#')
    text = ''.join(c if ord(c) < 0x10000 and c not in '\u2018\u2019\u201c\u201d' else "'" if c in "\u2018\u2019" else '"' if c in "\u201c\u201d" else c for c in text)
    return text.strip()

# ---------------------------------------------------------------------------
# Data fetching
# ---------------------------------------------------------------------------

def _fetch_data(force=False):
    global _cache
    now = time.time()
    with _cache_lock:
        if not force and _cache.get('data') and (now - _cache.get('data_ts', 0)) < CACHE_TTL:
            return _cache['data']
    try:
        r = _pluto_session.get(PLUTO_DATA_URL, timeout=15, verify=False)
        r.raise_for_status()
        raw = gzip.decompress(r.content)
        data = json.loads(raw.decode('utf-8'))
        with _cache_lock:
            _cache['data'] = data
            _cache['data_ts'] = now
        _log('Dados carregados: %d regioes' % len(data.get('regions', {})))
        return data
    except Exception as e:
        _log('Erro ao buscar dados: %s' % e)
        with _cache_lock:
            return _cache.get('data')

def _get_jwt(force=False):
    now = time.time()
    with _cache_lock:
        if not force and _cache.get('jwt') and (now - _cache.get('jwt_ts', 0)) < JWT_TTL:
            return _cache['jwt']
    device_id = str(uuid.uuid3(uuid.UUID(UUID_NAMESPACE), str(uuid.getnode())))
    params = {
        'deviceId': device_id, 'deviceMake': 'Chrome', 'deviceType': 'web',
        'deviceVersion': '114.0.0', 'deviceModel': 'web', 'DNT': '0',
        'appName': 'web', 'appVersion': '7.2.0-57e9a96fe7f66354de7957efff20f469e6772404',
        'serverSideAds': 'false', 'drmCapabilities': 'widevine:L3',
        'clientID': device_id, 'clientModelNumber': '1.0.0',
    }
    try:
        r = _pluto_session.get(PLUTO_BOOT_URL, params=params, timeout=10, verify=False)
        r.raise_for_status()
        j = r.json()
        result = (j['stitcherParams'], j['sessionToken'])
        with _cache_lock:
            _cache['jwt'] = result
            _cache['jwt_ts'] = now
        return result
    except Exception as e:
        _log('Erro JWT: %s' % e)
        with _cache_lock:
            return _cache.get('jwt', (None, None))

# ---------------------------------------------------------------------------
# Menu builders
# ---------------------------------------------------------------------------

def _add_item(label, url, thumb='', fanart='', plot='', folder=True, playable=False, label2='', genre=''):
    li = xbmcgui.ListItem(label=label)
    art = {}
    if thumb: art['thumb'] = thumb
    if fanart: art['fanart'] = fanart
    if art: li.setArt(art)
    if label2:
        li.setLabel2(label2)
    if plot:
        try:
            tag = li.getVideoInfoTag()
            tag.setPlot(plot)
            if label2:
                tag.setPlotOutline(label2)
            if genre:
                tag.setGenre(genre)
            tag.setTitle(label)
            tag.setMediaType('tvshow')
        except Exception:
            li.setInfo('video', {'plot': plot, 'genre': genre, 'title': label})
    if playable:
        li.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=_ADDON_HANDLE, url=url, listitem=li, isFolder=folder)

def _end(content_type=''):
    if content_type:
        xbmcplugin.setContent(_ADDON_HANDLE, content_type)
        xbmcplugin.addSortMethod(_ADDON_HANDLE, xbmcplugin.SORT_METHOD_UNSORTED)
        xbmcplugin.addSortMethod(_ADDON_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_ADDON_HANDLE)

# ---------------------------------------------------------------------------
# Menu: Regions
# ---------------------------------------------------------------------------

def menu_regions():
    data = _fetch_data()
    if not data:
        xbmcgui.Dialog().notification('Pluto TV', 'Erro ao carregar dados.')
        _end(); return
    regions = data.get('regions', {})
    for code in sorted(regions, key=lambda c: (regions[c].get('sort', 9), regions[c].get('name', ''))):
        r = regions[code]
        ch_count = len(r.get('channels', {}))
        region_name = _sanitize(r.get('name', code))
        label = '%s (%d)' % (region_name, ch_count)
        url = 'plugin://plugin.video.keltecmp-xtream/?mode=pluto_tv_region&region_code=%s' % _quote(code)
        _add_item(label, url, thumb=r.get('logo', ''), fanart=r.get('logo', ''),
                  plot='[B]%s[/B] - %d canais\n%s' % (region_name, ch_count, _sanitize(r.get('description', ''))))
    _end('files')

# ---------------------------------------------------------------------------
# Menu: Groups (within a region) or direct channels
# ---------------------------------------------------------------------------

def menu_groups(region_code):
    data = _fetch_data()
    if not data:
        _end(); return
    regions = data.get('regions', {})
    region = regions.get(region_code)
    if not region:
        _end(); return
    channels = region.get('channels', {})
    groups = OrderedDict()
    for ch_id, ch in channels.items():
        g = ch.get('group', 'Other')
        if g not in groups: groups[g] = []
        groups[g].append(ch_id)
    if not groups:
        _end(); return
    # If only one group or groups disabled, show channels directly
    if len(groups) == 1:
        menu_channels(region_code, 'ALL')
        return
    all_count = sum(len(v) for v in groups.values())
    url_all = 'plugin://plugin.video.keltecmp-xtream/?mode=pluto_tv_channels&region_code=%s&group=ALL' % _quote(region_code)
    region_logo = region.get('logo', '')
    _add_item('All (%d)' % all_count, url_all, thumb=region_logo, fanart=region_logo,
              plot='[B]%s[/B] - Todos os %d canais' % (region.get('name', ''), all_count))
    for gname in groups:
        count = len(groups[gname])
        display_name = _sanitize(gname)
        first_ch = channels.get(groups[gname][0], {}) if groups[gname] else {}
        thumb = first_ch.get('logo', '')
        fanart = first_ch.get('art', '') or first_ch.get('logo', '')
        url_g = 'plugin://plugin.video.keltecmp-xtream/?mode=pluto_tv_channels&region_code=%s&group=%s' % (_quote(region_code), _quote(gname))
        _add_item('%s (%d)' % (display_name, count), url_g, thumb=thumb, fanart=fanart,
                  plot='[B]%s[/B] - %d canais\nRegiao: %s' % (display_name, count, region.get('name', '')),
                  genre=display_name)
    _end('files')

# ---------------------------------------------------------------------------
# Menu: Channels
# ---------------------------------------------------------------------------

def _build_epg(programs, now_ts, max_rows=10):
    grid = []
    current_name = ''
    for idx, row in enumerate(programs[:max_rows]):
        try:
            start = float(row[0])
            if start > now_ts + 7200:
                break
            from datetime import datetime as _dt
            start_t = _dt.fromtimestamp(start).strftime('%H:%M')
            title = _sanitize(row[1])
            if idx + 1 < len(programs):
                try:
                    end_t = _dt.fromtimestamp(float(programs[idx + 1][0])).strftime('%H:%M')
                except Exception:
                    end_t = ''
            else:
                end_t = ''
            is_now = start <= now_ts
            if is_now:
                try:
                    nxt = float(programs[idx + 1][0])
                    is_now = now_ts < nxt
                except (IndexError, Exception):
                    is_now = now_ts - start < 3600
            if is_now:
                current_name = title
                time_range = '%s-%s' % (start_t, end_t) if end_t else start_t
                grid.append('[COLOR gold]--- AGORA ---[/COLOR]')
                grid.append('[COLOR lime]>>[/COLOR] [COLOR white]%s[/COLOR]  [COLOR gold]%s[/COLOR]' % (time_range, title))
                grid.append('[COLOR gold]----------------------------[/COLOR]')
            else:
                time_range = start_t + ('-' + end_t if end_t else '')
                grid.append('   [COLOR gray]%s[/COLOR]  %s' % (time_range, title))
        except Exception:
            pass
    return '\n'.join(grid), current_name

def menu_channels(region_code, group_name=None):
    data = _fetch_data()
    if not data:
        _end(); return
    region = data.get('regions', {}).get(region_code)
    if not region:
        _end(); return
    channels = region.get('channels', {})
    show_chno = True
    now_ts = time.time()
    items = []
    for ch_id in sorted(channels, key=lambda c: (channels[c].get('chno', 999) if show_chno else channels[c].get('name', ''))):
        ch = channels[ch_id]
        if group_name and group_name != 'ALL' and ch.get('group') != group_name:
            continue
        chno = ch.get('chno', '')
        name = _sanitize(ch.get('name', ch_id))
        group = _sanitize(ch.get('group', ''))
        label = '%s | %s' % (chno, name) if show_chno and chno else name
        epg_text, current_prog = _build_epg(ch.get('programs', []), now_ts)
        plot = epg_text if epg_text else ''
        prog_line = current_prog if current_prog else ''
        label2 = '>> %s' % current_prog if current_prog else ''
        desc = _sanitize(ch.get('description', ''))
        if desc:
            plot += '\n\n[COLOR dimgray]%s[/COLOR]' % desc
        if not plot:
            plot = '[B]%s - %s[/B]' % (region.get('name', ''), group)
        play_url = 'plugin://plugin.video.keltecmp-xtream/?mode=pluto_tv_play&channel_id=%s' % _quote(ch_id)
        _add_item(label, play_url, thumb=ch.get('logo', ''), fanart=ch.get('art', ''),
                  plot=plot, folder=False, playable=True, label2=label2, genre=group)
    _end('tvshows')

# ---------------------------------------------------------------------------
# Playback
# ---------------------------------------------------------------------------

def sync_to_pvr(region_code=None):
    addon = __import__('xbmcaddon').Addon('plugin.video.keltecmp-xtream')
    profile = __import__('xbmcvfs').translatePath(addon.getAddonInfo('profile'))
    dp = xbmcgui.DialogProgress()
    label = 'Pluto TV - PVR'
    if region_code: label += ' [%s]' % region_code
    dp.create(label, 'Carregando dados dos canais...')
    data = _fetch_data()
    if not data or dp.iscanceled():
        if dp.iscanceled(): dp.close()
        else: xbmcgui.Dialog().notification('Pluto TV', 'Erro ao carregar dados', xbmcgui.NOTIFICATION_ERROR)
        return
    try:
        from lib.pluto_epg import build_pvr_channels, build_epg_xml, enrich_programs_tmdb, export_pvr_files
        from lib.pvr_manager import _configure_pvr_instance, is_pvr_installed, prompt_install_pvr
    except Exception as e:
        _log(f'Erro ao importar modulos EPG: {e}')
        dp.close()
        xbmcgui.Dialog().notification('Pluto TV', 'Erro interno', xbmcgui.NOTIFICATION_ERROR)
        return
    if not is_pvr_installed():
        dp.close()
        prompt_install_pvr()
        if not is_pvr_installed():
            return
        dp.create(label, 'Carregando dados dos canais...')
    dp.update(10, 'Construindo lista de canais...')
    channels = build_pvr_channels(data, region_code=region_code)
    if not channels:
        dp.close()
        xbmcgui.Dialog().notification('Pluto TV', 'Nenhum canal encontrado', xbmcgui.NOTIFICATION_WARNING)
        return
    dp.update(20, 'Carregando cache TMDB...')
    try:
        from lib.pluto_epg import _load_tmdb_cache
        tmdb_cache = _load_tmdb_cache()
    except Exception:
        tmdb_cache = None
    dp.update(40, 'Montando XMLTV da programacao...')
    epg_root = build_epg_xml(data, tmdb_cache=tmdb_cache, region_code=region_code)
    if dp.iscanceled(): dp.close(); return
    dp.update(60, 'Exportando arquivos M3U e EPG...')
    m3u_path = os.path.join(profile, 'pluto_pvr.m3u8')
    epg_path = os.path.join(profile, 'pluto_epg.xml')
    ok = export_pvr_files(channels, epg_root, m3u_path, epg_path)
    if not ok:
        dp.close()
        xbmcgui.Dialog().notification('Pluto TV', 'Falha ao exportar', xbmcgui.NOTIFICATION_ERROR)
        return
    dp.update(80, 'Configurando PVR (instancia 3)...\nAcesse TV > Guia de Programacao')
    ok_cfg = _configure_pvr_instance(m3u_path, epg_path, instance=3, instance_name='Pluto TV')
    if ok_cfg:
        try:
            __import__('xbmc').executebuiltin('UpdateLocalAddons')
        except Exception:
            pass
        dp.update(100, 'Pronto!')
        xbmc.sleep(300)
        dp.close()
        xbmcgui.Dialog().notification('Pluto TV',
            f'{len(channels)} canais sincronizados!',
            xbmcgui.NOTIFICATION_INFO, 3000)
        yes = xbmcgui.Dialog().yesno('Pluto TV', f'{len(channels)} canais exportados.\nDeseja abrir a Guia de Programacao?')
        if yes:
            xbmc.sleep(2000)
            xbmc.executebuiltin('ActivateWindow(TVGuide)')
    else:
        dp.close()
        xbmcgui.Dialog().notification('Pluto TV', 'Falha ao configurar PVR', xbmcgui.NOTIFICATION_ERROR)
    _log(f'PVR sync: {len(channels)} canais Pluto TV')

def _find_channel(data, channel_id):
    for r in data.get('regions', {}).values():
        ch = r.get('channels', {}).get(channel_id)
        if ch:
            return ch
    return None

def _find_region_for_channel(data, channel_id):
    for code, r in data.get('regions', {}).items():
        if channel_id in r.get('channels', {}):
            return r
    return None

def play_channel(channel_id):
    data = _fetch_data()
    if not data:
        xbmcplugin.setResolvedUrl(_ADDON_HANDLE, False, xbmcgui.ListItem())
        return
    channel = _find_channel(data, channel_id)
    if not channel:
        xbmcplugin.setResolvedUrl(_ADDON_HANDLE, False, xbmcgui.ListItem())
        return
    name = channel.get('name', channel_id)
    thumb = channel.get('logo', '')
    fanart = channel.get('art', '') or thumb
    group = _sanitize(channel.get('group', ''))
    desc = _sanitize(channel.get('description', ''))
    params, jwt = _get_jwt()
    if not params or not jwt:
        xbmcplugin.setResolvedUrl(_ADDON_HANDLE, False, xbmcgui.ListItem())
        return
    headers = {}
    for src in (data, _find_region_for_channel(data, channel_id), channel):
        if src:
            headers.update(src.get('headers', {}))
    headers.setdefault('User-Agent', ALT_UA)
    headers.setdefault('Origin', 'https://pluto.tv')
    headers.setdefault('Referer', 'https://pluto.tv/')
    pluto_url = PLUTO_STITCHER.format(id=channel_id, params=params, token=jwt)
    try:
        from kpn import get_port
        _port = get_port() or 8090
    except Exception:
        _port = 8090
    proxy_url = 'http://127.0.0.1:%d/hlsproxy?url=%s&h=%s' % (
        _port, quote_plus(pluto_url), quote_plus(json.dumps(headers)))
    li = xbmcgui.ListItem(label=name, path=proxy_url)
    try:
        tag = li.getVideoInfoTag()
        tag.setTitle(name)
        tag.setMediaType('video')
        if group:
            tag.setGenre(group)
        if desc:
            tag.setPlot(desc)
    except Exception:
        li.setInfo('video', {'title': name, 'plot': desc or '', 'genre': group or ''})
    li.setArt({'thumb': thumb, 'fanart': fanart, 'poster': thumb, 'icon': thumb})
    li.setProperty('IsPlayable', 'true')
    li.setProperty('inputstream', 'inputstream.adaptive')
    li.setProperty('inputstream.adaptive.manifest_config',
        '{"hls_ignore_endlist":true,"hls_fix_mediasequence":true,"hls_fix_discsequence":true}')
    li.setProperty('inputstream.adaptive.live_delay', '15')
    li.setProperty('inputstream.adaptive.audio_persist', 'true')
    li.setContentLookup(False)
    li.setMimeType('application/vnd.apple.mpegurl')
    xbmcplugin.setResolvedUrl(_ADDON_HANDLE, True, li)
    _log('Reproduzindo (proxy HLS): %s' % name)
