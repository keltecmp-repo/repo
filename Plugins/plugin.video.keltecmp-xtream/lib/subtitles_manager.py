# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

try:
    from kodi_six import xbmc, xbmcaddon, xbmcvfs
except ImportError:
    import xbmc
    import xbmcaddon
    import xbmcvfs

try:
    import requests as _req
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

_HAS_KODI = (xbmc is not None)
_DEFAULT_TIMEOUT = 20
_API_TEMPLATE = 'https://opensubtitles.stremio.homes/{lang}/ai-translated=false%7Cfrom=all%7CCauto-adjustment=true'
_USER_AGENT = 'KelTecMediaPlay/3.0'


# ---------------------------------------------------------------------------
# Helpers internos (substitutos do módulo common)
# ---------------------------------------------------------------------------

def _log(msg, level=None):
    if _HAS_KODI:
        lvl = level if level is not None else xbmc.LOGDEBUG
        xbmc.log('[KelTec-Subs] {}'.format(msg), lvl)


def _log_debug(msg):
    _log(msg, xbmc.LOGDEBUG)


def _get_addon(addon=None):
    if addon is not None:
        return addon
    try:
        return xbmcaddon.Addon()
    except Exception:
        return None


def _ensure_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except Exception:
        pass
    return path


def _make_session():
    if not _HAS_REQUESTS:
        return None
    s = _req.Session()
    s.headers.update({'User-Agent': _USER_AGENT})
    return s


def _get_setting_bool(setting_id, default=True, addon=None):
    addon = _get_addon(addon)
    if addon is None:
        return default
    try:
        return addon.getSetting(setting_id) == 'true'
    except Exception:
        return default


def _get_setting_enum_value(setting_id, options, default, addon=None):
    addon = _get_addon(addon)
    if addon is None:
        return default
    try:
        idx = int(addon.getSetting(setting_id) or '0')
        idx = max(0, min(idx, len(options) - 1))
        return options[idx]
    except Exception:
        return default


# ---------------------------------------------------------------------------
# Cache / diretório de legendas
# ---------------------------------------------------------------------------

def _get_subtitle_dir(addon=None):
    addon = _get_addon(addon)
    if addon is None:
        return _ensure_dir(os.path.join(os.getcwd(), 'subtitles'))
    profile_dir = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
    return _ensure_dir(os.path.join(profile_dir, 'subtitles'))


def clear_subtitles_cache(addon=None):
    addon = _get_addon(addon)
    subtitle_dir = _get_subtitle_dir(addon)
    removed = 0
    try:
        if os.path.isdir(subtitle_dir):
            for filename in os.listdir(subtitle_dir):
                path = os.path.join(subtitle_dir, filename)
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                        removed += 1
                except Exception as exc:
                    _log('Falha ao remover {}: {}'.format(path, exc), xbmc.LOGWARNING)
    except Exception as exc:
        _log('Erro limpando cache: {}'.format(exc), xbmc.LOGWARNING)
    return removed


def get_subtitle_language_candidates(addon=None):
    addon = _get_addon(addon)
    preferred = _get_setting_enum_value('idioma_legenda', ['pt-br', 'en', 'es'], 'pt-br', addon=addon)
    fallback = _get_setting_enum_value('fallback_legenda', ['', 'pt-pt', 'en', 'es'], '', addon=addon)
    candidates = []
    for code in (preferred, fallback):
        if code and code not in candidates:
            candidates.append(code)
    return candidates or ['pt-br']


# ---------------------------------------------------------------------------
# API Stremio
# ---------------------------------------------------------------------------

def build_subtitles_api_url(imdb_id, media_type, lang, season=None, episode=None):
    base = _API_TEMPLATE.format(lang=lang)
    if media_type == 'series' and season and episode:
        return '{}/subtitles/series/{}:{}:{}.json'.format(base, imdb_id, season, episode)
    return '{}/subtitles/movie/{}.json'.format(base, imdb_id)


def fetch_subtitles_metadata(imdb_id, media_type, lang, season=None, episode=None, session=None):
    session = session or _SESSION
    url = build_subtitles_api_url(imdb_id, media_type, lang, season=season, episode=episode)
    _log('URL: {}'.format(url), xbmc.LOGINFO)
    response = session.get(url, timeout=_DEFAULT_TIMEOUT)
    response.raise_for_status()
    payload = response.json()
    subtitles = payload.get('subtitles') or []
    _log('API retornou {} legenda(s) para {} imdb={}'.format(len(subtitles), lang, imdb_id), xbmc.LOGINFO)
    return subtitles


def download_subtitle(url, destination_path, session=None):
    session = session or _SESSION
    response = session.get(url, timeout=_DEFAULT_TIMEOUT)
    response.raise_for_status()
    with open(destination_path, 'wb') as fh:
        fh.write(response.content)
    _log('Download OK: {}'.format(os.path.basename(destination_path)), xbmc.LOGINFO)
    return destination_path


# ---------------------------------------------------------------------------
# Interface principal: busca e baixa automaticamente (sem menu)
# ---------------------------------------------------------------------------

def get_and_download_subtitles(imdb_id, media_type, season=None, episode=None,
                                addon=None, clear_before=True):
    addon = _get_addon(addon)
    if not imdb_id or not media_type:
        _log_debug('Busca ignorada: imdb_id ou media_type ausente.')
        return []

    if media_type == 'series' and (not season or not episode):
        _log_debug('Busca para serie ignorada: season/episode ausentes.')
        return []

    if not _get_setting_bool('legendasauto', True, addon=addon):
        _log_debug('Legendas automaticas desativadas pelo usuario.')
        return []

    if clear_before and _get_setting_bool('limparlegendas', True, addon=addon):
        clear_subtitles_cache(addon)

    candidates = get_subtitle_language_candidates(addon)
    local_paths = []

    for lang in candidates:
        try:
            subtitles = fetch_subtitles_metadata(
                imdb_id, media_type, lang,
                season=season, episode=episode,
                session=_SESSION,
            )
        except Exception as exc:
            _log('Erro consultando {} para {}: {}'.format(lang, imdb_id, exc), xbmc.LOGWARNING)
            continue

        if not subtitles:
            _log_debug('Nenhuma legenda para {} em {}.'.format(imdb_id, lang))
            continue

        for idx, sub in enumerate(subtitles):
            if idx >= 1:
                break
            url = sub.get('url')
            if not url:
                continue
            dest = os.path.join(
                _get_subtitle_dir(addon),
                'sub_{}_{}.vtt'.format(lang.replace('-', '_'), idx))
            try:
                download_subtitle(url, dest, session=_SESSION)
                local_paths.append(dest)
            except Exception as exc:
                _log('Falha ao baixar {}: {}'.format(url, exc), xbmc.LOGWARNING)

        if local_paths:
            _log_debug('Legendas obtidas com idioma {}.'.format(lang))
            return local_paths

    return []


def get_stremio_subtitle(imdb_id, season=None, episode=None, lang='pt-br', addon=None):
    media_type = 'series' if season and episode else 'movie'
    try:
        subtitles = fetch_subtitles_metadata(
            imdb_id, media_type, lang,
            season=season, episode=episode,
            session=_SESSION,
        )
        if not subtitles:
            _log('Nenhuma legenda para {}'.format(imdb_id))
            return None
        url = subtitles[0].get('url')
        if not url:
            return None
        dest = os.path.join(
            _get_subtitle_dir(addon),
            '{}_{}.vtt'.format(imdb_id, lang))
        return download_subtitle(url, dest, session=_SESSION)
    except Exception as exc:
        _log('Erro subtitle: {}'.format(exc), xbmc.LOGWARNING)
        return None


# ---------------------------------------------------------------------------
# Sessao global
# ---------------------------------------------------------------------------
_SESSION = _make_session() if _HAS_REQUESTS else None


# ---------------------------------------------------------------------------
# Compatibilidade: get_subtitles_manager() retorna um wrapper de objeto
# para nao quebrar chamadas existentes em main.py
# ---------------------------------------------------------------------------

class _SubtitlesCompat:
    """Wrapper de compatibilidade para codigo legado que usa get_subtitles_manager()."""

    def __init__(self, addon):
        self._addon = addon

    def get_and_download(self, imdb_id, media_type, season=None, episode=None):
        return get_and_download_subtitles(
            imdb_id, media_type,
            season=season, episode=episode,
            addon=self._addon, clear_before=False)

    def prompt_and_download(self, imdb_id=None, media_type=None,
                             season=None, episode=None, display_title=None,
                             **kwargs):
        _log('prompt_and_download chamado — delegando para get_and_download_subtitles')
        paths = get_and_download_subtitles(
            imdb_id=imdb_id or kwargs.get('imdb_id'),
            media_type=media_type or kwargs.get('media_type'),
            season=season, episode=episode,
            addon=self._addon, clear_before=False)
        return paths[0] if paths else ''

    def clear_cache(self):
        return clear_subtitles_cache(self._addon)


def get_subtitles_manager(addon, profile_dir=None):
    if not _HAS_REQUESTS:
        if _HAS_KODI:
            xbmc.log('[KelTec-Subs] requests nao disponivel.', xbmc.LOGWARNING)
        return None
    try:
        return _SubtitlesCompat(addon)
    except Exception as exc:
        if _HAS_KODI:
            xbmc.log('[KelTec-Subs] Erro ao criar manager: {}'.format(exc), xbmc.LOGERROR)
        return None
