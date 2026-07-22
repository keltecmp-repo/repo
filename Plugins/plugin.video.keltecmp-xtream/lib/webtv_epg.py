# -*- coding: utf-8 -*-
"""
WebTV EPG - Guia de programacao para canais WebTV
Fontes: limaalef/BrazilTVEPG (epg.xml + claro.xml + globo.xml)
"""
import re, time, threading, json
import xbmc

EPG_URLS = [
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/epg.xml',
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/claro.xml',
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/globo.xml',
]
CACHE_TTL = 1800

_cache = {}
_cache_lock = threading.Lock()

CHANNEL_MAP = {
    'adultswim': 'Adult Swim HD',
    'amc': 'AMC HD',
    'animalplanet': 'ANIMAL PLANET HD',
    'aparecida': 'TV APARECIDA HD',
    'axn': 'AXN',
    'bandnews': 'BAND NEWS',
    'bandrj': 'BAND HD',
    'bandsp': 'BAND SPORTS HD',
    'bandsports': 'BAND SPORTS HD',
    'cancaonova': 'Canção Nova',
    'cartoonito': 'CARTOONITO',
    'cinemax': 'CINEMAX HD',
    'cnnbrasil': 'CNN BRASIL',
    'combate': 'combate',
    'cultura': 'TV Cultura SP_local',
    'discoverychannel': 'DISCOVERY CHANNEL HD',
    'discoverykids': 'DISCOVERY KIDS HD',
    'discoveryscience': 'DISCOVERY SCIENCE HD',
    'discoverytheather': 'DISCOVERY THEATER HD',
    'discoveryturbo': 'DISCOVERY TURBO HD',
    'discoveryworld': 'DISCOVERY WORLD HD',
    'discoveryhh': 'DISCOVERY HOME & HEALTH',
    'discoveryid': 'DISCOVERY ID',
    'espn': 'ESPN',
    'espn2': 'ESPN 2',
    'espn3': 'ESPN 3',
    'espn4': 'ESPN 4',
    'espn5': 'ESPN 5',
    'espn6': 'ESPN 6',
    'foodnetwork': 'FOOD NETWORK HD',
    'globosp': 'GLOBO SP',
    'gloob': 'gloob',
    'gnt': 'gnt',
    'hbo': 'HBO',
    'hbo2': 'HBO 2',
    'hbofamily': 'HBO FAMILY HD',
    'hboplus': 'HBO PLUS HD',
    'hboxtreme': 'HBO XTREME HD',
    'hbozone': 'HBO ZONE HD',
    'historia': 'HISTORY HD',
    'history': 'HISTORY HD',
    'hits': 'HITS HD',
    'megapix': 'MEGAPIX HD',
    'mgm': 'MGM HD',
    'multishow': 'MULTISHOW HD',
    'natgeo': 'NATIONAL GEOGRAPHIC HD',
    'natgeowild': 'NATIONAL GEOGRAPHIC WILD HD',
    'nickjr': 'Nick Jr.',
    'nickelodeon': 'NICKELODEON HD',
    'paramount': 'PARAMOUNT HD',
    'recordsp': 'RECORD SP',
    'recordrs': 'RECORD RS',
    'recordmg': 'RECORD MG',
    'recordrj': 'RECORD RJ',
    'redeuniao': 'Rede Gospel',
    'rgbtv': 'RGB TV',
    'rockinrio': 'Rock in Rio',
    'sbt': 'SBT SP HD',
    'seuhistory': 'HISTORY HD',
    'seumegapix': 'MEGAPIX HD',
    'seustar': 'STAR CHANNEL HD',
    'space': 'SPACE HD',
    'star': 'STAR CHANNEL HD',
    'starchannel': 'STAR CHANNEL HD',
    'studious': 'STUDIO UNIVERSAL HD',
    'syfy': 'SYFY HD',
    'tbs': 'TBS HD',
    'tcm': 'TCM HD',
    'telecineaction': 'Telecine Action',
    'telecinecult': 'Telecine Cult',
    'telecinefun': 'Telecine Fun',
    'telecinepipoca': 'Telecine Pipoca',
    'telecinepremium': 'Telecine Premium',
    'telecinetouch': 'Telecine Touch',
    'tnt': 'TNT HD',
    'tntseries': 'TNT SERIES HD',
    'tvlondrina': 'TV LONDRINA',
    'warnerchannel': 'WARNER CHANNEL',
    'woohoo': 'WooHoo',
    'band': 'BAND HD',
    'record': 'RECORD SP',
    'recordtv': 'RECORD SP',
    'globo': 'GLOBO SP',
    'sbt': 'SBT SP HD',
    'cartoonnetwork': 'CARTOON NETWORK',
    'globoam': 'GLOBO SP',
    'gloce': 'GLOBO SP',
    'globodf': 'GLOBO SP',
    'globoes': 'GLOBO SP',
    'globogo': 'GLOBO SP',
    'globomg': 'GLOBO SP',
    'globonews': 'GLOBONEWS',
    'globonovelas': 'GLOBO SP',
    'globopb': 'GLOBO SP',
    'globope': 'GLOBO SP',
    'globorj': 'GLOBO SP',
    'globors': 'GLOBO SP',
    'recordgo': 'RECORD SP',
    'recordmg': 'RECORD MG',
    'recordrj': 'RECORD RJ',
    'masterchef': 'MEGAPIX HD',
    'mtv': 'MTV HD',
    'ae': 'A&E',
    'discoverychannel': 'DISCOVERY HD',
    'discoveryhh': 'DISCOVERY HOME&HEALTH HD',
    'discoveryid': 'DISCOVERY ID',
    'globoce': 'GLOBO SP',
    'cartoonnetwork': 'CARTOON HD',
    'mtv': 'MTV',
    'sportynetplus1': 'SportyNet + 1',
    'sportynetplus2': 'SportyNet + 2',
    'sportynetplus3': 'SportyNet + 3',
    'ufcfightpass': 'UFC',
    'discoveryid': 'ID HD',
    'sonychannel': 'SONY CHANNEL',
    'redevida': 'REDE VIDA',
    'tvpaieterno': 'TV PAI ETERNO HD',
    'tntnovelas': 'TNT NOVELAS',
}

_epg_data = None

def _log(msg):
    xbmc.log('[WebTV-EPG] ' + msg, xbmc.LOGINFO)

def _fetch_epg(force=False):
    global _epg_data
    now = time.time()
    with _cache_lock:
        if not force and _epg_data and (now - _cache.get('epg_ts', 0)) < CACHE_TTL:
            return _epg_data
    try:
        import cloudscraper as _cs
        s = _cs.create_scraper()
    except Exception:
        import requests as _req
        s = _req.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0'})

    channels = {}
    programmes = {}
    for url in EPG_URLS:
        try:
            r = s.get(url, timeout=10)
            xml = r.text
            for ch_id, ch_name in re.findall(r'<channel id="([^"]+)">\s*<display-name[^>]*>([^<]+)</display-name>', xml):
                ch_key = ch_id.lower().replace('&amp;', '&')
                ch_name_clean = ch_name.replace('&amp;', '&')
                if ch_key not in channels:
                    channels[ch_key] = {'id': ch_id, 'name': ch_name_clean, 'source': url}
            for prog in re.findall(r'<programme start="([^"]+)" stop="([^"]+)" channel="([^"]+)">.*?<title[^>]*>([^<]*)</title>(?:\s*<sub-title[^>]*>([^<]*)</sub-title>)?(?:\s*<desc[^>]*>([^<]*)</desc>)?', xml, re.DOTALL):
                ch = prog[2].lower().replace('&amp;', '&')
                if ch not in programmes:
                    programmes[ch] = []
                programmes[ch].append({
                    'start': prog[0],
                    'stop': prog[1],
                    'title': prog[3].strip(),
                    'subtitle': prog[4].strip() if prog[4] else '',
                    'desc': prog[5].strip() if prog[5] else '',
                })
        except Exception as e:
            _log('Erro ao baixar %s: %s' % (url, e))

    _epg_data = {'channels': channels, 'programmes': programmes}
    with _cache_lock:
        _cache['epg_ts'] = now
    _log('EPG carregado: %d canais, %d com programacao' % (len(channels), len(programmes)))
    return _epg_data

def _parse_epg_time(ts):
    try:
        from datetime import datetime, timezone, timedelta
        import calendar
        dt_str = ts.strip()
        dt = datetime.strptime(dt_str[:14], '%Y%m%d%H%M%S')
        if len(dt_str) > 14:
            tz_str = dt_str[14:].strip()
            sign = 1 if tz_str[0] == '+' else -1
            h, m = int(tz_str[1:3]), int(tz_str[3:5])
            offset = timedelta(hours=sign*h, minutes=sign*m)
            dt = dt.replace(tzinfo=timezone(offset))
        else:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except Exception:
        return 0

def _resolve_epg_id(channel_id):
    epg_id = CHANNEL_MAP.get(channel_id)
    if epg_id:
        return epg_id.lower()
    return channel_id.lower()

def _get_programmes_for_channel(channel_id):
    epg = _fetch_epg()
    if not epg:
        return []
    epg_id = _resolve_epg_id(channel_id)
    progs = epg.get('programmes', {}).get(epg_id, [])
    if not progs:
        for ch_key, ch_info in epg.get('channels', {}).items():
            if channel_id in ch_key or ch_key in channel_id:
                progs = epg.get('programmes', {}).get(ch_key, [])
                break
    return progs

def get_current_programme(channel_id):
    progs = _get_programmes_for_channel(channel_id)
    now = time.time()
    for p in progs:
        start_ts = _parse_epg_time(p['start'])
        stop_ts = _parse_epg_time(p['stop'])
        if start_ts <= now < stop_ts:
            return p
    return None

def get_next_programme(channel_id):
    progs = _get_programmes_for_channel(channel_id)
    now = time.time()
    for p in progs:
        start_ts = _parse_epg_time(p['start'])
        if start_ts > now:
            return p
    return None

def get_current_programme_info(channel_id):
    progs = _get_programmes_for_channel(channel_id)
    now = time.time()
    for p in progs:
        start_ts = _parse_epg_time(p['start'])
        stop_ts = _parse_epg_time(p['stop'])
        if start_ts <= now < stop_ts:
            try:
                from datetime import datetime as _dt
                start_str = _dt.fromtimestamp(start_ts).strftime('%H:%M')
                stop_str = _dt.fromtimestamp(stop_ts).strftime('%H:%M')
            except Exception:
                start_str = stop_str = ''
            return p['title'], start_str, stop_str, p.get('desc', ''), p.get('subtitle', '')
    return None, None, None, None, None

def get_epg_text(channel_id, max_rows=6):
    progs = _get_programmes_for_channel(channel_id)
    now = time.time()
    grid = []
    current_name = ''
    show_count = 0
    found_now = False
    for p in progs:
        start_ts = _parse_epg_time(p['start'])
        stop_ts = _parse_epg_time(p['stop'])
        if stop_ts <= now:
            continue
        try:
            from datetime import datetime as _dt
            start_str = _dt.fromtimestamp(start_ts).strftime('%H:%M')
        except Exception:
            start_str = ''
        title = p['title']
        is_now = start_ts <= now < stop_ts
        if is_now:
            found_now = True
            current_name = title
            if grid:
                grid.append('')
            grid.append('[COLOR gold]--- AGORA ---[/COLOR]')
            grid.append('[COLOR lime]>>[/COLOR] [COLOR white]%s[/COLOR]  [COLOR gold]%s[/COLOR]' % (start_str, title))
            grid.append('[COLOR gold]----------------------------[/COLOR]')
            show_count += 1
        elif found_now and start_ts > now:
            if show_count >= max_rows:
                break
            grid.append('   [COLOR gray]%s[/COLOR]  %s' % (start_str, title))
            show_count += 1
    return '\n'.join(grid), current_name, ''

def epg_is_ready():
    global _epg_data
    return _epg_data is not None and (time.time() - _cache.get('epg_ts', 0)) < CACHE_TTL

def get_channel_count():
    epg = _fetch_epg()
    if not epg:
        return 0
    return len(epg.get('channels', {}))
