# -*- coding: utf-8 -*-
"""
WebTV EPG - Guia de programacao para canais WebTV   [KelTec-EPG] v2
Fontes: limaalef/BrazilTVEPG (epg.xml + claro.xml + globo.xml)
        + URLs extras opcionais (Configuracoes > Links das Fontes > "EPG extra").

v2 (correcao de canais sem EPG, ex.: Record e MTV):
  * Os nomes do CHANNEL_MAP nao batiam com os IDs reais das fontes (ex.: o mapa pedia
    'RECORD SP' e a fonte publica 'Record SP_local' / 'RECORD - Sao Paulo').
    Agora cada canal aceita uma LISTA de candidatos e a busca e normalizada
    (sem acento/maiuscula/espaco/&/'HD'/'_local').
  * Se o 1o candidato nao tem programacao futura, usa o proximo (ex.: Record: epg.xml -> claro.xml).
  * Programas ja encerrados nao sao mais guardados (menos memoria) e duplicados entre
    arquivos sao removidos.
  * Falha de download nao fica em cache por 30 min (tenta de novo em 2 min).
  * MTV: nenhuma das fontes publica a grade da MTV Brasil. Para ter EPG dela, informe
    uma URL XMLTV extra nas Configuracoes (campo "EPG extra") - o mapa ja esta pronto.
"""
import re, time, threading, json, unicodedata, os
from html import unescape
import xbmc

EPG_URLS = [
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/epg.xml',
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/claro.xml',
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/globo.xml',
    'https://raw.githubusercontent.com/limaalef/BrazilTVEPG/main/maissbt.xml',   # SBT / +SBT (625 KB)
]
CACHE_TTL = 1800        # EPG carregado com sucesso (memoria)
RETRY_TTL = 120         # nada carregou: tenta de novo logo
KEEP_PAST = 3600        # guarda programas encerrados ha ate 1h
DISK_CACHE_TTL = 6 * 3600   # cache em disco persiste entre navegacoes/restarts
ADDON_ID = 'plugin.video.keltecmp-xtream'

_cache = {}
_cache_lock = threading.Lock()
_fetch_lock = threading.Lock()

# Valor = nome do canal no EPG ou TUPLA de candidatos (ordem de preferencia).
# A comparacao ignora acento, maiuscula, espaco, '&', 'HD' e '_local'.
CHANNEL_MAP = {
    'adultswim': 'Adult Swim HD',
    'ae': 'A&E',
    'amc': 'AMC HD',
    'animalplanet': 'ANIMAL PLANET HD',
    'aparecida': 'TV APARECIDA HD',
    'axn': 'AXN',
    'band': 'BAND HD',
    'bandnews': 'BAND NEWS',
    'bandrj': 'BAND HD',
    'bandsp': 'BAND SPORTS HD',
    'bandsports': 'BAND SPORTS HD',
    'cancaonova': 'Canção Nova',
    'cartoonito': 'CARTOONITO',
    'cartoonnetwork': 'CARTOON HD',
    'cinemax': 'CINEMAX HD',
    'cnnbrasil': 'CNN BRASIL',
    'combate': ('COMBATE HD', 'combate'),
    'cultura': 'TV Cultura SP_local',
    'discoverychannel': 'DISCOVERY HD',
    'discoveryhh': 'DISCOVERY HOME&HEALTH HD',
    'discoveryid': 'ID HD',
    'discoverykids': 'DISCOVERY KIDS HD',
    'discoveryscience': 'DISCOVERY SCIENCE HD',
    'discoverytheather': 'DISCOVERY THEATER HD',
    'discoveryturbo': 'DISCOVERY TURBO HD',
    'discoveryworld': 'DISCOVERY WORLD HD',
    'espn': 'ESPN',
    'espn2': 'ESPN 2',
    'espn3': 'ESPN 3',
    'espn4': 'ESPN 4',
    'espn5': 'ESPN 5',
    'espn6': 'ESPN 6',
    'foodnetwork': 'FOOD NETWORK HD',
    'globo': 'GLOBO SP',
    'globoam': 'GLOBO SP',
    'globoce': 'GLOBO SP',
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
    'globosp': 'GLOBO SP',
    'gloce': 'GLOBO SP',
    'gloob': 'gloob',
    'gnt': 'gnt',
    'hbo': 'HBO',
    'hbo2': 'HBO2',
    'hbofamily': 'HBO Family',
    'hbomundi': 'HBO Mundi',
    'hboplus': ('HBO+', 'HBO Plus HD'),
    'hbopop': 'HBO Pop',
    'hbosignature': 'HBO Signature',
    'hboxtreme': 'HBO Xtreme',
    'hbozone': 'HBO ZONE HD',
    'historia': ('HISTORY', 'HISTORY HD'),
    'history': ('HISTORY', 'HISTORY HD'),
    'history2': 'HISTORY 2',
    'hits': 'HITS HD',
    'masterchef': 'MEGAPIX HD',
    'megapix': 'MEGAPIX HD',
    'mgm': 'MGM HD',
    'mtv': ('MTV HD', 'MTV', 'MTV Brasil'),
    'multishow': 'MULTISHOW HD',
    'natgeo': 'NATIONAL GEOGRAPHIC HD',
    'natgeowild': 'NATIONAL GEOGRAPHIC WILD HD',
    'nickelodeon': 'NICKELODEON HD',
    'nickjr': 'Nick Jr.',
    'paramount': 'PARAMOUNT HD',
    'record': ('Record SP_local', 'RECORD - Sao Paulo'),
    'recordgo': ('Record SP_local', 'RECORD - Sao Paulo'),
    'recordmg': ('Record SP_local', 'RECORD - Sao Paulo'),
    'recordnews': ('RECORD NEWS', 'Record News'),
    'recordrj': ('Record SP_local', 'RECORD - Sao Paulo'),
    'recordrs': ('Record SP_local', 'RECORD - Sao Paulo'),
    'recordsp': ('Record SP_local', 'RECORD - Sao Paulo'),
    'recordtv': ('Record SP_local', 'RECORD - Sao Paulo'),
    'redetv': ('Rede TV! SP_local', 'REDE TV! São Paulo'),
    'redeuniao': 'Rede Gospel',
    'redevida': 'REDE VIDA',
    'rgbtv': 'RGB TV',
    'rockinrio': 'Rock in Rio',
    'sbt': ('SBT São Paulo', 'SBT'),
    'sbtsp': ('SBT São Paulo', 'SBT'),
    'sbtkids': '+SBT Kids',
    'maissbtkids': '+SBT Kids',
    'sbtnovelas': '+SBT Novelas',
    'maissbtnovelas': '+SBT Novelas',
    'sbtshowdomilhao': '+SBT Show do Milhão',
    'maissbtshowdomilhao': '+SBT Show do Milhão',
    'showdomilhao': '+SBT Show do Milhão',
    'sbtnews': ('SBT NEWS HD', 'SBT News'),
    'seuhistory': ('HISTORY', 'HISTORY HD'),
    'seumegapix': 'MEGAPIX HD',
    'seustar': 'STAR CHANNEL HD',
    'sonychannel': 'SONY CHANNEL',
    'space': 'SPACE HD',
    'sportynetplus1': 'SportyNet + 1',
    'sportynetplus2': 'SportyNet + 2',
    'sportynetplus3': 'SportyNet + 3',
    'star': 'STAR CHANNEL HD',
    'starchannel': 'STAR CHANNEL HD',
    'studious': 'STUDIO UNIVERSAL HD',
    'syfy': 'SYFY HD',
    'tbs': 'TBS HD',
    'tcm': ('TCM BR', 'TCM HD'),
    'telecineaction': 'Telecine Action',
    'telecinecult': 'Telecine Cult',
    'telecinefun': 'Telecine Fun',
    'telecinepipoca': 'Telecine Pipoca',
    'telecinepremium': 'Telecine Premium',
    'telecinetouch': 'Telecine Touch',
    'tnt': 'TNT HD',
    'tntnovelas': 'TNT NOVELAS',
    'tntseries': 'TNT SERIES HD',
    'tvlondrina': 'TV LONDRINA',
    'tvpaieterno': 'TV PAI ETERNO HD',
    'ufcfightpass': 'UFC',
    'warnerchannel': 'WARNER CHANNEL',
    'woohoo': ('WOOHOO HD', 'WooHoo'),
}

# Canais regionais / variantes: quando o ID do site nao existe no EPG, usa a grade da praca principal.
# (id normalizado casa com a regex -> candidatos). A 1a regra que casar vale.
FAMILY_RULES = [
    (r'^(mais)?sbt.*kids',                ('+SBT Kids',)),
    (r'^(mais)?sbt.*novelas',             ('+SBT Novelas',)),
    (r'^(mais)?sbt.*(showdomilhao|milhao)', ('+SBT Show do Milhão',)),
    (r'^sbt.*news',                       ('SBT NEWS HD', 'SBT News')),
    (r'^sbt',                             ('SBT São Paulo', 'SBT')),
    (r'^record.*news',                    ('RECORD NEWS', 'Record News')),
    (r'^record',                          ('Record SP_local', 'RECORD - Sao Paulo')),
    (r'^globo(?!news|play|novelas|internacional)', ('GLOBO SP', 'Globo SP_local')),
    (r'^band(?!news|sports)',             ('BAND HD', 'Band SP_local')),
    (r'^redetv',                          ('Rede TV! SP_local', 'REDE TV! São Paulo')),
]

_epg_data = None


def _log(msg):
    xbmc.log('[WebTV-EPG] ' + msg, xbmc.LOGINFO)


def _epg_enabled():
    """Opcao nas configuracoes: desativar o EPG dos canais WebTV (1/2/3)."""
    try:
        import xbmcaddon
        raw = xbmcaddon.Addon(ADDON_ID).getSetting('webtv_epg_enabled')
        return str(raw or 'true').strip().lower() not in ('false', '0', 'off', 'no')
    except Exception:
        return True


def _extra_urls():
    try:
        import xbmcaddon
        raw = xbmcaddon.Addon(ADDON_ID).getSetting('webtv_epg_extra_url') or ''
    except Exception:
        raw = ''
    out = []
    for part in re.split(r'[\s;|,]+', raw.strip()):
        if part.lower().startswith(('http://', 'https://')):
            out.append(part)
    return out


# ---------------------------------------------------------------------------
# Normalizacao / resolucao de nomes
# ---------------------------------------------------------------------------
def _norm(text):
    text = unescape(str(text or ''))
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]', '', text.lower())


def _variants(n):
    """n normalizado -> [n, sem 'local', sem 'hd', sem ambos] (sem repetir, sem vazios)."""
    out = [n]
    for suf in ('local', 'hd'):
        for v in list(out):
            if v.endswith(suf) and len(v) > len(suf) + 1:
                out.append(v[:-len(suf)])
    res = []
    for v in out:
        if v and v not in res:
            res.append(v)
    return res


def _build_index(programmes):
    """{nome normalizado (e variantes): [chaves do canal]}. Nome exato vem antes."""
    index = {}

    def add(n, key):
        lst = index.setdefault(n, [])
        if key not in lst:
            lst.append(key)
    for key in programmes:
        add(_norm(key), key)
    for key in programmes:
        for v in _variants(_norm(key)):
            add(v, key)
    return index


def _ts(p):
    """Timestamps ja calculados no carregamento (ou calcula na hora)."""
    s = p.get('_s')
    if s is None:
        s = p['_s'] = _parse_epg_time(p['start'])
    e = p.get('_e')
    if e is None:
        e = p['_e'] = _parse_epg_time(p['stop'])
    return s, e


def _candidates(channel_id):
    cid = (channel_id or '').strip()
    val = CHANNEL_MAP.get(cid) or CHANNEL_MAP.get(cid.lower())
    cands = []
    if isinstance(val, (list, tuple)):
        cands.extend(val)
    elif val:
        cands.append(val)
    cands.append(cid)
    n = _norm(cid)
    for rx, fam in FAMILY_RULES:
        if re.match(rx, n):
            cands.extend(fam)
            break
    return cands


def _resolve_epg_id(channel_id):
    """Compatibilidade: primeiro candidato em minusculas."""
    return _candidates(channel_id)[0].lower()


def _lookup(epg, name):
    """Todas as chaves do EPG que casam com `name` (exato primeiro)."""
    programmes = epg.get('programmes', {})
    out = []
    key = str(name).lower().replace('&amp;', '&')
    if key in programmes:
        out.append(key)
    index = epg.get('index') or {}
    n = _norm(name)
    for v in [n] + _variants(n):
        for k in index.get(v, []):
            if k not in out:
                out.append(k)
    return out


def _rank(progs, now):
    """2 = tem programa no ar agora, 1 = so futuro, 0 = so passado/vazio."""
    best = 0
    for p in progs:
        s, e = _ts(p)
        if s <= now < e:
            return 2
        if e > now:
            best = 1
    return best


def _resolve_key(epg, channel_id):
    """Chave do canal no EPG (ou None). Resultado em cache dentro do proprio EPG."""
    memo = epg.setdefault('resolved', {})
    if channel_id in memo:
        return memo[channel_id]
    now = time.time()
    programmes = epg.get('programmes', {})
    found = []
    for cand in _candidates(channel_id):
        for k in _lookup(epg, cand):
            if k not in found:
                found.append(k)
    if not found:                         # ultimo recurso: nome parecido
        n = _norm(channel_id)
        if len(n) >= 3:
            hits = sorted((len(nk), nk, k) for nk, ks in (epg.get('index') or {}).items()
                          for k in ks if nk.startswith(n) or (len(n) >= 4 and n in nk)
                          or (len(nk) >= 4 and nk in n))
            found = [k for _l, _nk, k in hits]
    best, best_rank = None, -1
    for k in found:                       # melhor situacao primeiro; empate = ordem de preferencia
        r = _rank(programmes.get(k, []), now)
        if r > best_rank:
            best, best_rank = k, r
            if r == 2:
                break
    memo[channel_id] = best
    return best


# ---------------------------------------------------------------------------
# Download / parse
# ---------------------------------------------------------------------------
_PROG_RE = re.compile(
    r'<programme start="([^"]+)" stop="([^"]+)" channel="([^"]+)">.*?<title[^>]*>([^<]*)</title>'
    r'(?:\s*<sub-title[^>]*>([^<]*)</sub-title>)?(?:\s*<desc[^>]*>([^<]*)</desc>)?', re.DOTALL)
_CHAN_RE = re.compile(r'<channel id="([^"]+)">\s*<display-name[^>]*>([^<]+)</display-name>')


# ---------------------------------------------------------------------------
# Cache em disco (persiste entre navegacoes e reinicios do Kodi)
# ---------------------------------------------------------------------------
def _disk_cache_path():
    try:
        import xbmcaddon, xbmcvfs
        prof = xbmcvfs.translatePath(xbmcaddon.Addon(ADDON_ID).getAddonInfo('profile'))
        os.makedirs(prof, exist_ok=True)
        return os.path.join(prof, 'webtv_epg_cache.json')
    except Exception:
        return None


def _load_disk_cache():
    p = _disk_cache_path()
    if not p:
        return None
    try:
        if os.path.exists(p) and (time.time() - os.path.getmtime(p)) < DISK_CACHE_TTL:
            with open(p, 'r', encoding='utf-8') as f:
                obj = json.load(f)
            if obj and obj.get('channels') and obj.get('programmes') is not None:
                obj.setdefault('index', _build_index(obj['programmes']))
                obj.setdefault('resolved', {})
                return obj
    except Exception:
        pass
    return None


def _save_disk_cache(data):
    p = _disk_cache_path()
    if not p:
        return
    try:
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except Exception:
        pass


def _fetch_epg(force=False):
    global _epg_data
    # Respeita a opcao das configuracoes: EPG dos WebTV desativado.
    if not _epg_enabled():
        return None
    now = time.time()
    with _cache_lock:
        if not force and _epg_data is not None and (now - _cache.get('epg_ts', 0)) < _cache.get('ttl', CACHE_TTL):
            return _epg_data
    # Tenta o cache em disco (rapido, sem rede) antes de baixar
    if not force and _epg_data is None:
        disk = _load_disk_cache()
        if disk is not None:
            with _cache_lock:
                _epg_data = disk
                _cache['epg_ts'] = time.time()
                _cache['ttl'] = CACHE_TTL
            _log('EPG carregado do cache em disco: %d canais' % len(disk.get('channels', {})))
            return _epg_data
    with _fetch_lock:                     # evita 2 downloads simultaneos (tela + thread de aquecimento)
        now = time.time()
        with _cache_lock:
            if not force and _epg_data is not None and (now - _cache.get('epg_ts', 0)) < _cache.get('ttl', CACHE_TTL):
                return _epg_data
        try:
            import cloudscraper as _cs
            s = _cs.create_scraper()
        except Exception:
            import requests as _req
            s = _req.Session()
        s.headers.update({'User-Agent': 'Mozilla/5.0'})

        channels = {}
        per_src = {}      # canal -> {indice_da_fonte: {inicio: programa}}
        limit = now - KEEP_PAST
        for src_i, url in enumerate(list(EPG_URLS) + _extra_urls()):
            try:
                r = s.get(url, timeout=(10, 40))
                if r.status_code != 200:
                    _log('HTTP %s em %s' % (r.status_code, url))
                    continue
                xml = r.content.decode('utf-8', 'replace')
                for ch_id, ch_name in _CHAN_RE.findall(xml):
                    ch_key = unescape(ch_id).lower()
                    if ch_key not in channels:
                        channels[ch_key] = {'id': unescape(ch_id), 'name': unescape(ch_name), 'source': url}
                for prog in _PROG_RE.findall(xml):
                    st, en = _parse_epg_time(prog[0]), _parse_epg_time(prog[1])
                    if not st or not en or en < limit or not unescape(prog[3]).strip():
                        continue          # sem hora valida, ja encerrado ou sem titulo
                    ch = unescape(prog[2]).lower()
                    per_src.setdefault(ch, {}).setdefault(src_i, {})[st] = {
                        'start': prog[0], 'stop': prog[1], '_s': st, '_e': en,
                        'title': unescape(prog[3]).strip(),
                        'subtitle': unescape(prog[4]).strip() if prog[4] else '',
                        'desc': unescape(prog[5]).strip() if prog[5] else '',
                    }
            except Exception as e:
                _log('Erro ao baixar %s: %s' % (url, e))
            xml = None

        # Um canal pode existir em varios arquivos com grades diferentes: nao mistura.
        # Usa a 1a fonte (na ordem da lista) que tem programa no ar agora; senao a 1a com futuro.
        flat = {}
        for ch, srcs in per_src.items():
            lists = [[d[k] for k in sorted(d)] for _i, d in sorted(srcs.items())]
            flat[ch] = max(lists, key=lambda l: _rank(l, now)) if len(lists) > 1 else lists[0]
        per_src = None
        if not flat and _epg_data and _epg_data.get('programmes'):
            # nada carregou: mantem o EPG anterior e tenta de novo em breve
            with _cache_lock:
                _cache['epg_ts'] = time.time()
                _cache['ttl'] = RETRY_TTL
            _log('Falha ao atualizar o EPG; mantido o anterior')
            return _epg_data

        data = {'channels': channels, 'programmes': flat, 'index': _build_index(flat), 'resolved': {}}
        with _cache_lock:
            _epg_data = data
            _cache['epg_ts'] = time.time()
            _cache['ttl'] = CACHE_TTL if flat else RETRY_TTL
        if flat:
            _save_disk_cache(data)
        _log('EPG carregado: %d canais, %d com programacao' % (len(channels), len(flat)))
        return data


def _parse_epg_time(ts):
    try:
        from datetime import datetime, timezone, timedelta
        dt_str = ts.strip()
        dt = datetime.strptime(dt_str[:14], '%Y%m%d%H%M%S')
        if len(dt_str) > 14:
            tz_str = dt_str[14:].strip()
            sign = 1 if tz_str[0] == '+' else -1
            h, m = int(tz_str[1:3]), int(tz_str[3:5])
            offset = timedelta(hours=sign * h, minutes=sign * m)
            dt = dt.replace(tzinfo=timezone(offset))
        else:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except Exception:
        return 0


_bg_started = False
_bg_lock = threading.Lock()


def start_background_fetch():
    """Dispara o download do EPG em segundo plano, sem travar o menu."""
    global _bg_started
    with _bg_lock:
        if _bg_started:
            return
        _bg_started = True

    def _run():
        try:
            _fetch_epg()
        except Exception:
            pass
    threading.Thread(target=_run, daemon=True).start()


def _get_programmes_for_channel(channel_id, block=True):
    # Comportamento original: baixa o EPG (bloqueante) para a grade aparecer
    # ja na primeira abertura da categoria. Se desativado nas configuracoes,
    # retorna vazio na hora (menu rapido, sem EPG).
    if not _epg_enabled():
        return []
    epg = _fetch_epg()
    if not epg:
        return []
    key = _resolve_key(epg, channel_id)
    return epg.get('programmes', {}).get(key, []) if key else []


def get_current_programme(channel_id):
    now = time.time()
    for p in _get_programmes_for_channel(channel_id):
        s, e = _ts(p)
        if s <= now < e:
            return p
    return None


def get_next_programme(channel_id):
    now = time.time()
    for p in _get_programmes_for_channel(channel_id):
        if _ts(p)[0] > now:
            return p
    return None


def get_current_programme_info(channel_id):
    now = time.time()
    for p in _get_programmes_for_channel(channel_id):
        start_ts, stop_ts = _ts(p)
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
        start_ts, stop_ts = _ts(p)
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
    return _epg_data is not None and (time.time() - _cache.get('epg_ts', 0)) < _cache.get('ttl', CACHE_TTL)


def get_channel_count():
    epg = _fetch_epg()
    if not epg:
        return 0
    return len(epg.get('channels', {}))