# -*- coding: utf-8 -*-
# =============================================================================
# KELTEC MEDIA PLAY - LEGENDAS v3.0
# =============================================================================
# Arquivo: lib/subtitles_manager.py
#
# v3.0 - Reescrita completa:
#   * Usa a mesma API Stremio do OnePlay:
#       https://opensubtitles-v3.strem.io/{lang}/...
#   * Sem API key, sem XML-RPC, sem limite diário
#   * Download direto de .vtt (sem descompressão)
#   * Menu de seleção exibe o TÍTULO EM PORTUGUÊS (tmdb_title)
#   * Suporte a fallback de idioma (pt-br → pt-pt → en)
#   * Cache local por 7 dias
# =============================================================================

from __future__ import unicode_literals

import os
import time
import hashlib

try:
    import requests as _req
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

try:
    from kodi_six import xbmc, xbmcgui, xbmcvfs
except ImportError:
    try:
        import xbmc
        import xbmcgui
        import xbmcvfs
    except ImportError:
        xbmc = xbmcgui = xbmcvfs = None

_HAS_KODI = (xbmc is not None)

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

# Mesma URL base usada pelo OnePlay
_STREMIO_BASE = (
    'https://opensubtitles-v3.strem.io'
    '/{lang}'
    '/ai-translated=false%7Cfrom=all%7CCauto-adjustment=true'
)
_USER_AGENT = 'KelTecMediaPlay v3.0'
_CACHE_TTL  = 86400 * 7   # 7 dias

# Idiomas suportados: nome exibido -> código da API Stremio
_LANG_OPTIONS = [
    ('Português (Brasil)',   'pt-br'),
    ('Português (Portugal)', 'pt-pt'),
    ('Inglês',               'en'),
    ('Espanhol',             'es'),
    ('Francês',              'fr'),
    ('Italiano',             'it'),
    ('Alemão',               'de'),
]
SUBTITLE_LANG_NAMES = [name for name, _ in _LANG_OPTIONS]


def _log(msg, level=None):
    if _HAS_KODI:
        lvl = level if level is not None else xbmc.LOGDEBUG
        xbmc.log('[KelTec-Subs] {}'.format(msg), lvl)


# ---------------------------------------------------------------------------
# Classe principal
# ---------------------------------------------------------------------------

class SubtitlesManager:
    """
    Busca e baixa legendas via API Stremio (opensubtitles-v3.strem.io).
    Mesma API usada pelo addon OnePlay — sem API key, sem limite diário.
    """

    def __init__(self, addon, profile_dir):
        self._addon       = addon
        self._cache_dir   = os.path.join(profile_dir, 'subtitles_cache')
        self._session     = None
        self._ensure_cache_dir()

    # ------------------------------------------------------------------
    # Helpers internos
    # ------------------------------------------------------------------

    def _ensure_cache_dir(self):
        try:
            if not os.path.exists(self._cache_dir):
                os.makedirs(self._cache_dir)
        except Exception:
            pass

    def _get_session(self):
        if self._session is None:
            if not _HAS_REQUESTS:
                return None
            self._session = _req.Session()
            self._session.headers.update({'User-Agent': _USER_AGENT})
        return self._session

    def _get_lang_pref(self):
        """
        Retorna (display_name, lang_code) do idioma preferido nas configurações.
        """
        try:
            idx = int(self._addon.getSetting('subtitle_lang') or '0')
            idx = max(0, min(idx, len(_LANG_OPTIONS) - 1))
        except Exception:
            idx = 0
        return _LANG_OPTIONS[idx]

    def _get_fallback_lang(self):
        """
        Retorna código do idioma de fallback (configuração 'fallback_legenda').
        Valores: 0=Nenhum, 1=pt-pt, 2=en, 3=es
        """
        fallback_codes = ['', 'pt-pt', 'en', 'es']
        try:
            idx = int(self._addon.getSetting('fallback_legenda') or '0')
            idx = max(0, min(idx, len(fallback_codes) - 1))
            return fallback_codes[idx]
        except Exception:
            return ''

    def _cache_path(self, imdb_id, lang, media_type, season=None, episode=None):
        """Gera caminho de cache único para cada combinação de parâmetros."""
        if media_type == 'series':
            key = '{}_{}_{}_s{}e{}'.format(imdb_id, lang, media_type, season, episode)
        else:
            key = '{}_{}'.format(imdb_id, lang)
        hashed = hashlib.md5(key.encode('utf-8')).hexdigest()[:12]
        return os.path.join(self._cache_dir, '{}.vtt'.format(hashed))

    # ------------------------------------------------------------------
    # API Stremio — idêntica ao OnePlay
    # ------------------------------------------------------------------

    def _build_api_url(self, lang, imdb_id, media_type, season=None, episode=None):
        """
        Monta a URL da API Stremio.
        Mesma lógica de build_subtitles_api_url() do OnePlay.
        """
        base = _STREMIO_BASE.format(lang=lang)
        if media_type == 'series':
            return '{}/subtitles/series/{}:{}:{}.json'.format(
                base, imdb_id, season, episode)
        return '{}/subtitles/movie/{}.json'.format(base, imdb_id)

    def _fetch_subtitle_list(self, lang, imdb_id, media_type,
                              season=None, episode=None):
        """
        Busca lista de legendas na API Stremio.
        Retorna lista de dicts com 'url', 'lang', e opcionalmente 'id'.
        """
        session = self._get_session()
        if not session:
            return []

        url = self._build_api_url(lang, imdb_id, media_type,
                                   season=season, episode=episode)
        _log('[Subs] URL: {}'.format(url), xbmc.LOGINFO if _HAS_KODI else None)
        try:
            resp = session.get(url, timeout=15)
            _log('[Subs] HTTP {}: {}'.format(resp.status_code, url[:80]),
                 xbmc.LOGINFO if _HAS_KODI else None)
            resp.raise_for_status()
            data = resp.json()
            subs = data.get('subtitles') or []
            _log('[Subs] API retornou {} legenda(s) para lang={} imdb={}'.format(
                len(subs), lang, imdb_id),
                xbmc.LOGINFO if _HAS_KODI else None)
            return subs
        except Exception as exc:
            _log('[Subs] Erro ao buscar legendas [{}] imdb={}: {}'.format(lang, imdb_id, exc),
                 xbmc.LOGWARNING if _HAS_KODI else None)
            return []

    def _download_vtt(self, subtitle_url, dest_path):
        """
        Baixa um arquivo .vtt diretamente para dest_path.
        Mesma lógica de download_subtitle() do OnePlay.
        """
        session = self._get_session()
        if not session:
            return False
        try:
            resp = session.get(subtitle_url, timeout=20)
            resp.raise_for_status()
            with open(dest_path, 'wb') as fh:
                fh.write(resp.content)
            _log('Download OK: {}'.format(os.path.basename(dest_path)),
                 xbmc.LOGINFO if _HAS_KODI else None)
            return True
        except Exception as exc:
            _log('Erro ao baixar {}: {}'.format(subtitle_url, exc),
                 xbmc.LOGWARNING if _HAS_KODI else None)
            return False

    # ------------------------------------------------------------------
    # Interface de alto nível: busca automática (sem menu)
    # ------------------------------------------------------------------

    def get_and_download(self, imdb_id, media_type,
                          season=None, episode=None):
        """
        Busca e baixa a melhor legenda disponível SEM exibir menu.
        Retorna lista de caminhos locais (pode ter vários idiomas como fallback).
        Compatível com a chamada feita em default.py / get_and_download_subtitles().
        """
        if not imdb_id or not media_type:
            return []
        if media_type == 'series' and (
                season in (None, '') or episode in (None, '')):
            return []

        lang_name, primary_lang = self._get_lang_pref()
        fallback_lang = self._get_fallback_lang()

        candidates = [primary_lang]
        if fallback_lang and fallback_lang != primary_lang:
            candidates.append(fallback_lang)

        local_paths = []
        for lang in candidates:
            subs = self._fetch_subtitle_list(
                lang, imdb_id, media_type,
                season=season, episode=episode)
            if not subs:
                continue

            # Tenta baixar até 2 legendas para este idioma
            downloaded = 0
            for idx, sub in enumerate(subs):
                sub_url = sub.get('url')
                if not sub_url:
                    continue
                dest = os.path.join(
                    self._cache_dir,
                    'sub_{}_{}.vtt'.format(lang.replace('-', '_'), idx))
                if self._download_vtt(sub_url, dest):
                    local_paths.append(dest)
                    downloaded += 1
                if downloaded >= 2:
                    break

            if local_paths:
                _log('Legendas obtidas para idioma={}'.format(lang),
                     xbmc.LOGINFO if _HAS_KODI else None)
                return local_paths  # Sucesso no primeiro idioma disponível

        return local_paths

    # ------------------------------------------------------------------
    # Interface de alto nível: busca com menu de seleção
    # ------------------------------------------------------------------

    def prompt_and_download(self, imdb_id, media_type,
                             season=None, episode=None,
                             display_title=None):
        """
        Exibe menu de seleção de legenda e baixa a escolhida.

        Parâmetros:
          imdb_id       : ID IMDB (ex: 'tt1234567')
          media_type    : 'movie' ou 'series'
          season        : número da temporada (séries)
          episode       : número do episódio (séries)
          display_title : título em PT para exibir no menu
                          (use o título do TMDB em português)

        Retorna: caminho local do .vtt baixado, ou '' se cancelado/falha.
        """
        if not _HAS_KODI:
            return ''
        if not _HAS_REQUESTS:
            return ''

        lang_name, primary_lang = self._get_lang_pref()
        fallback_lang           = self._get_fallback_lang()

        # Título para exibir no cabeçalho do menu
        header_title = display_title or imdb_id or 'Legenda'
        # Trunca para caber no menu do Kodi
        header_short = header_title[:40]

        # Notifica que está buscando
        xbmcgui.Dialog().notification(
            'KelTec - Legendas',
            'Buscando [{}]: {}...'.format(lang_name, header_short),
            xbmcgui.NOTIFICATION_INFO, 2000)

        # ----- Busca na API -----
        subs = self._fetch_subtitle_list(
            primary_lang, imdb_id, media_type,
            season=season, episode=episode)

        # Fallback de idioma
        if not subs and fallback_lang and fallback_lang != primary_lang:
            _log('Sem resultados em {}. Tentando fallback {}.'.format(
                primary_lang, fallback_lang))
            subs = self._fetch_subtitle_list(
                fallback_lang, imdb_id, media_type,
                season=season, episode=episode)
            if subs:
                lang_name = fallback_lang.upper()

        if not subs:
            xbmcgui.Dialog().notification(
                'Legendas',
                'Nenhuma legenda encontrada para: {}'.format(header_short),
                xbmcgui.NOTIFICATION_WARNING, 3000)
            return ''

        # ----- Monta opções do menu -----
        # Cada item da API Stremio pode ter: url, lang, id, fps, ...
        # O campo 'id' costuma ser algo como "sub_12345" (sem título legível).
        # Usamos o display_title (PT-BR do TMDB) como título fixo —
        # assim SEMPRE aparece o nome em português no menu,
        # independente do que a API retornar.

        options = []
        for idx, sub in enumerate(subs[:30]):
            sub_lang = (sub.get('lang') or sub.get('language') or
                        primary_lang).upper().replace('-', '-')
            fps_raw  = sub.get('fps') or sub.get('framerate') or ''
            fps_str  = '  {:.3g}fps'.format(float(fps_raw)) if fps_raw else ''

            # Título exibido: sempre o título PT do TMDB + numeração
            option_text = '[{}]  {}  #{}{}'.format(
                sub_lang,
                header_title[:42],
                idx + 1,
                fps_str
            )
            options.append(option_text)

        options.append('[COLOR gray]Reproduzir sem legenda[/COLOR]')

        # ----- Exibe menu -----
        choice = xbmcgui.Dialog().select(
            'Legendas [{}] — {}'.format(lang_name, header_short),
            options)

        # Cancelou ou escolheu "sem legenda"
        if choice < 0 or choice >= len(subs):
            return ''

        selected_url = subs[choice].get('url', '')
        if not selected_url:
            return ''

        # ----- Baixa a legenda escolhida -----
        xbmcgui.Dialog().notification(
            'Legendas', 'Baixando...', xbmcgui.NOTIFICATION_INFO, 1500)

        dest = os.path.join(
            self._cache_dir,
            'selected_{}_{}.vtt'.format(
                (imdb_id or 'unknown').replace('tt', ''),
                primary_lang.replace('-', '_')))

        ok = self._download_vtt(selected_url, dest)
        if ok:
            xbmcgui.Dialog().notification(
                'Legendas',
                '[{}] Carregada!'.format(lang_name),
                xbmcgui.NOTIFICATION_INFO, 2500)
            return dest
        else:
            xbmcgui.Dialog().notification(
                'Legendas',
                'Falha ao baixar. Tente outra opção.',
                xbmcgui.NOTIFICATION_ERROR, 3000)
            return ''

    # ------------------------------------------------------------------
    # Utilitários
    # ------------------------------------------------------------------

    def clear_cache(self):
        """Remove todos os arquivos .vtt do cache."""
        removed = 0
        try:
            for fname in os.listdir(self._cache_dir):
                if fname.endswith('.vtt'):
                    try:
                        os.remove(os.path.join(self._cache_dir, fname))
                        removed += 1
                    except Exception:
                        pass
        except Exception as exc:
            _log('Erro ao limpar cache: {}'.format(exc))
        _log('Cache limpo: {} arquivo(s).'.format(removed))
        return removed


# ---------------------------------------------------------------------------
# Fábrica pública
# ---------------------------------------------------------------------------

def get_subtitles_manager(addon, profile_dir):
    """
    Retorna instância de SubtitlesManager, ou None se requests não disponível.
    """
    if not _HAS_REQUESTS:
        if _HAS_KODI:
            xbmc.log('[KelTec-Subs] requests não disponível.',
                     xbmc.LOGWARNING)
        return None
    try:
        return SubtitlesManager(addon, profile_dir)
    except Exception as exc:
        if _HAS_KODI:
            xbmc.log('[KelTec-Subs] Erro ao criar manager: {}'.format(exc),
                     xbmc.LOGERROR)
        return None