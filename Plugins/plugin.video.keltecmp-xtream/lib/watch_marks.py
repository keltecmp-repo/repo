# -*- coding: utf-8 -*-
"""
watch_marks.py - etiquetas de VISTO / EM ANDAMENTO para filmes e episodios.

Arquivo: watch_marks.json (pasta de dados do add-on)
    {"v": {chave: {"s": "done"|"part", "p": pos_s, "d": dur_s, "t": timestamp,
                    "sk": chave_da_serie, "se": temporada, "ep": episodio, "ti": titulo}},
     "tot": {chave_da_serie: total_de_episodios_conhecido}}

Quem grava: o servico (service_refresh.py) acompanha o player e chama record_from_player().
Quem avisa o que esta tocando: a skin IBO e o menu classico (set_now) antes de iniciar a reproducao.
Quem le: a skin IBO (etiquetas) e o menu classico.
"""
import json
import os
import re
import threading
import time

from lib.my_list import norm, _profile, _log

FILE_NAME = 'watch_marks.json'
NOW_PROP = 'keltec.now'
DONE_PCT = 0.90          # >= 90% do video = visto
MIN_PCT = 0.03           # menos de 3% (e < 60 s) = nao conta como iniciado
MIN_SEC = 60
_LOCK = threading.Lock()
_C = {'mtime': -1.0, 'data': None}


def _path():
    return os.path.join(_profile(), FILE_NAME)


def _load(force=False):
    now = time.time()
    if not force and _C['data'] is not None and now - _C.get('chk', 0.0) < 0.8:
        return _C['data']
    _C['chk'] = now
    p = _path()
    try:
        mt = os.path.getmtime(p) if os.path.isfile(p) else 0.0
    except OSError:
        mt = 0.0
    if not force and _C['data'] is not None and mt == _C['mtime']:
        return _C['data']
    d = {'v': {}, 'tot': {}}
    if mt:
        try:
            with open(p, 'r', encoding='utf-8') as fh:
                raw = json.load(fh)
            if isinstance(raw, dict):
                d['v'] = raw.get('v') or {}
                d['tot'] = raw.get('tot') or {}
        except Exception as exc:  # noqa: BLE001
            _log('watch_marks: %s' % exc)
    _C['data'], _C['mtime'] = d, mt
    return d


def _save(d):
    p = _path()
    tmp = p + '.tmp'
    try:
        with _LOCK:
            with open(tmp, 'w', encoding='utf-8') as fh:
                json.dump(d, fh, ensure_ascii=False)
            os.replace(tmp, p)
        _C['data'] = d
        try:
            _C['mtime'] = os.path.getmtime(p)
        except OSError:
            _C['mtime'] = -1.0
    except Exception as exc:  # noqa: BLE001
        _log('watch_marks gravar: %s' % exc)


# ============================================================================ CHAVES
_TAIL_RE = re.compile(r'(?:\s*\[(?:visto|continuar[^\]]*|em andamento[^\]]*|completa)\]|\s*[\(\[]\s*(?:19|20)\d{2}\s*[\)\]]|\s+\*\s*\d+(?:[.,]\d+)?|\s+\u2605.*|\s+(?:4k|uhd|fhd|hd|sd)\b)+\s*$', re.I)


def base_title(title):
    """Titulo sem ano '(2021)', nota '*7.5', estrela de Minha Lista e qualidade: mesma chave em qualquer lista
    (servidor, TMDB, busca, animes, novelas)."""
    t = title or ''
    for _ in range(3):
        n = _TAIL_RE.sub('', t)
        if n == t:
            break
        t = n
    return t


def movie_key(title):
    return 'm|' + norm(base_title(title))


def series_key(title):
    return norm(base_title(title))


def ep_key(series_title, season, episode):
    return 'e|%s|%d|%d' % (series_key(series_title), int(season or 0), int(episode or 0))


def parse_se(label, season=None, episode=None):
    """(temporada, episodio) pelos campos do item ou pelo rotulo 'T1 E5', 'S01E05', '1x05', 'Cap. 12'."""
    try:
        s, e = int(season or 0), int(episode or 0)
    except (TypeError, ValueError):
        s, e = 0, 0
    lab = label or ''
    if not (s and e):
        m = (re.search(r'\bT\s*(\d{1,2})\s*[-. ]?\s*E\s*(\d{1,4})', lab, re.I)
             or re.search(r'\bS\s*(\d{1,2})\s*[-. ]?\s*E\s*(\d{1,4})', lab, re.I)
             or re.search(r'\b(\d{1,2})x(\d{1,4})\b', lab, re.I))
        if m:
            s, e = s or int(m.group(1)), e or int(m.group(2))
    if not e:
        m = (re.search(r'\bE(?:p|pis[oó]dio)?\.?\s*(\d{1,4})\b', lab, re.I)
             or re.search(r'cap[ií]tulo\s*(\d{1,4})|cap\.?\s*(\d{1,4})', lab, re.I)
             or re.match(r'\s*(\d{1,4})\s*[-.)]', lab))
        if m:
            e = int([g for g in m.groups() if g][0])
    return s, e


def item_key(label, series_title='', season=None, episode=None):
    """Chave do item: episodio (se ha serie) ou filme."""
    if series_title:
        s, e = parse_se(label, season, episode)
        if e:
            return ep_key(series_title, s, e)
        return 'x|%s|%s' % (series_key(series_title), norm(label))
    return movie_key(label)


# ============================================================================ "TOCANDO AGORA"
def set_now(key, title='', series_title='', season=0, episode=0, kind='movie', total=0):
    """Anota (na janela Home) o que sera reproduzido. O servico usa quando o player iniciar."""
    try:
        import xbmcgui
        xbmcgui.Window(10000).setProperty(NOW_PROP, json.dumps({
            'k': key, 'ti': title, 'st': series_title, 'se': season, 'ep': episode,
            'kind': kind, 'tot': total, 'at': time.time()}, ensure_ascii=False))
    except Exception as exc:  # noqa: BLE001
        _log('set_now: %s' % exc)


def get_now(max_age=180):
    try:
        import xbmcgui
        w = xbmcgui.Window(10000)
        raw = w.getProperty(NOW_PROP)
        if not raw:
            return None
        d = json.loads(raw)
        if time.time() - float(d.get('at') or 0) > max_age:
            return None
        return d
    except Exception:  # noqa: BLE001
        return None


def clear_now():
    try:
        import xbmcgui
        xbmcgui.Window(10000).clearProperty(NOW_PROP)
    except Exception:  # noqa: BLE001
        pass


# ============================================================================ GRAVAR
def record(key, pos, dur, meta=None, force_done=False):
    """Grava o progresso. Retorna 'done' | 'part' | ''."""
    if not key:
        return ''
    try:
        pos, dur = float(pos or 0), float(dur or 0)
    except (TypeError, ValueError):
        return ''
    if force_done or (dur > 0 and pos / dur >= DONE_PCT):
        status = 'done'
    elif pos >= MIN_SEC or (dur > 0 and pos / dur >= MIN_PCT):
        status = 'part'
    else:
        return ''
    d = _load(force=True)
    old = d['v'].get(key) or {}
    if status == 'part' and old.get('s') == 'done':
        status_keep = True              # rever um item ja visto nao tira o "visto"
    else:
        status_keep = False
    if not status_keep:
        ent = {'s': status, 'p': int(pos), 'd': int(dur), 't': int(time.time())}
        m = meta or {}
        for src, dst in (('st', 'sk'), ('se', 'se'), ('ep', 'ep'), ('ti', 'ti')):
            if m.get(src):
                ent[dst] = series_key(m[src]) if src == 'st' else m[src]
        d['v'][key] = ent
    else:
        d['v'][key]['t'] = int(time.time())
    if meta and meta.get('st') and meta.get('tot'):
        d['tot'][series_key(meta['st'])] = int(meta['tot'])
    _save(d)
    return status


def record_from_player(pos, dur, ended=False):
    now = get_now(max_age=6 * 3600)
    if not now:
        return ''
    return record(now.get('k'), pos, dur, meta=now, force_done=ended)


# ============================================================================ CONSULTA
def status_of(key):
    """('done'|'part'|'', pct 0-100)."""
    e = _load().get('v', {}).get(key)
    if not e:
        return '', 0
    pct = 100 if e.get('s') == 'done' else (int(100 * e.get('p', 0) / e['d']) if e.get('d') else 0)
    return e.get('s', ''), pct


def set_total(series_title, total):
    """Guarda o total de episodios (conhecido ao abrir a serie)."""
    if not series_title or not total:
        return
    d = _load()
    k = series_key(series_title)
    if d['tot'].get(k) != int(total):
        d = _load(force=True)
        d['tot'][k] = int(total)
        _save(d)


def series_progress(series_title):
    """{'done': n, 'part': n, 'total': n, 'state': 'done'|'part'|''}."""
    d = _load()
    sk = series_key(series_title)
    done = part = 0
    for e in d['v'].values():
        if e.get('sk') == sk:
            if e.get('s') == 'done':
                done += 1
            else:
                part += 1
    total = int(d['tot'].get(sk) or 0)
    if not (done or part):
        state = ''
    elif total and done >= total:
        state = 'done'
    else:
        state = 'part'
    return {'done': done, 'part': part, 'total': total, 'state': state}


def episode_tag(status, pct):
    """(texto, estado) da etiqueta de um episodio/filme."""
    if status == 'done':
        return 'VISTO', 'done'
    if status == 'part':
        return ('CONTINUAR %d%%' % pct) if pct else 'CONTINUAR', 'part'
    return '', ''


def series_tag(title):
    """(texto, estado, pct) da etiqueta da capa de uma serie."""
    p = series_progress(title)
    if p['state'] == 'done':
        return 'COMPLETA', 'done', 100
    if p['state'] == 'part':
        if p['total']:
            return 'EM ANDAMENTO %d/%d' % (p['done'], p['total']), 'part', int(100 * p['done'] / p['total'])
        n = p['done'] + p['part']
        return 'EM ANDAMENTO %d ep.' % n, 'part', 0
    return '', '', 0


def last_for_series(series_title):
    """Marca mais recente (maior timestamp) dos episodios da serie, ou None."""
    sk = series_key(series_title)
    best = None
    for e in _load()['v'].values():
        if e.get('sk') == sk and (best is None or e.get('t', 0) > best.get('t', 0)):
            best = e
    return best


def next_episode_index(keys):
    """Dada a lista de chaves dos episodios (em ordem), indice do que o usuario deve ver agora:
    o primeiro 'part'; senao o primeiro depois do ultimo 'done'; senao 0."""
    d = _load()['v']
    last_done = -1
    for i, k in enumerate(keys):
        e = d.get(k)
        if e and e.get('s') == 'part':
            return i
        if e and e.get('s') == 'done':
            last_done = i
    return min(last_done + 1, len(keys) - 1) if last_done >= 0 and keys else 0


def clear_all():
    _save({'v': {}, 'tot': {}})
