# -*- coding: utf-8 -*-
# ============================================================================
# KELTEC MEDIA PLAY - DASHBOARD DE ESTATISTICAS v2.0
# ============================================================================
# Arquivo: lib/stats_manager.py
#
# FUNCIONALIDADES:
#   - Total de horas assistidas (filmes, series, ao vivo)
#   - Dias unicos com atividade + media por dia
#   - Top 5 conteudos mais assistidos
#   - Top 3 por tipo (ao vivo, filmes, series)
#   - Generos mais assistidos (usa dados TMDB ja em cache)
#   - Streak de dias consecutivos
#   - Hora do dia e dia da semana preferidos
#   - Atividade mensal (ultimos 6 meses)
#   - Distribuicao por tipo com barras e horas estimadas
# ============================================================================

import json
import time
import os
from collections import Counter

try:
    import xbmc
    import xbmcgui
    import xbmcplugin
    import xbmcaddon
    _HAS_KODI = True
except ImportError:
    _HAS_KODI = False


def _log(msg):
    if _HAS_KODI:
        xbmc.log(f'[KelTec-Stats] {msg}', xbmc.LOGDEBUG)


# ____________________________________________________________________________
class StatsManager:

    _DURATION_ESTIMATE = {
        'live':   60,
        'movie':  110,
        'series': 45,
    }

    _DOW_NAMES = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']

    def __init__(self, profile_dir, watch_history=None, tmdb_cache=None):
        self._profile_dir   = profile_dir
        self._wh            = watch_history
        self._tmdb_cache    = tmdb_cache or {}
        self._stats_file    = os.path.join(profile_dir, 'keltec_stats_extra.json')

    def _get_all_items(self):
        if not self._wh:
            return []
        try:
            return self._wh.get_all() or []
        except Exception as e:
            _log(f'Erro ao obter historico: {e}')
            return []

    # -- Calculos principais ------------------------------------------------

    def compute(self):
        items = self._get_all_items()
        result = {
            'total_items':   0,
            'total_minutes': 0,
            'by_type':       {'live': 0, 'movie': 0, 'series': 0},
            'minutes_by_type': {'live': 0, 'movie': 0, 'series': 0},
            'top_titles':    [],
            'top_genres':    [],
            'streak_days':   0,
            'unique_days':   0,
            'avg_per_day':   0,
            'best_hour':     None,
            'best_dow':      None,
            'monthly':       [],
            'top_by_type':   {'live': [], 'movie': [], 'series': []},
            'first_watch':   None,
            'last_watch':    None,
        }

        if not items:
            return result

        try:
            result['total_items'] = len(items)

            type_counter   = Counter()
            title_counter  = Counter()
            live_counter   = Counter()
            movie_counter  = Counter()
            series_counter = Counter()
            hour_counter   = Counter()
            dow_counter    = Counter()
            days_seen      = set()
            timestamps     = []

            for it in items:
                stype = it.get('stype', 'live')
                name  = it.get('name', '')
                ts    = it.get('timestamp', 0)

                type_counter[stype] += 1
                if name:
                    title_counter[name] += 1
                    if stype == 'live':
                        live_counter[name] += 1
                    elif stype == 'movie':
                        movie_counter[name] += 1
                    elif stype == 'series':
                        series_counter[name] += 1
                if ts:
                    timestamps.append(ts)
                    try:
                        t = time.localtime(ts)
                        hour_counter[t.tm_hour] += 1
                        dow_counter[t.tm_wday]  += 1
                        days_seen.add(time.strftime('%Y-%m-%d', t))
                    except Exception:
                        pass

            result['by_type'] = {
                'live':   type_counter.get('live', 0),
                'movie':  type_counter.get('movie', 0),
                'series': type_counter.get('series', 0),
            }

            total_min = 0
            min_by_type = {}
            for stype in ('live', 'movie', 'series'):
                c = type_counter.get(stype, 0)
                m = c * self._DURATION_ESTIMATE.get(stype, 60)
                min_by_type[stype] = m
                total_min += m
            result['total_minutes'] = total_min
            result['minutes_by_type'] = min_by_type

            result['top_titles'] = [
                {'name': n, 'count': c}
                for n, c in title_counter.most_common(5)
            ]

            result['top_by_type'] = {
                'live':   [{'name': n, 'count': c} for n, c in live_counter.most_common(3)],
                'movie':  [{'name': n, 'count': c} for n, c in movie_counter.most_common(3)],
                'series': [{'name': n, 'count': c} for n, c in series_counter.most_common(3)],
            }

            if hour_counter:
                result['best_hour'] = hour_counter.most_common(1)[0][0]

            if dow_counter:
                result['best_dow'] = dow_counter.most_common(1)[0][0]

            result['streak_days'] = self._calc_streak(days_seen)
            result['unique_days'] = len(days_seen)

            if result['unique_days'] > 0:
                result['avg_per_day'] = round(result['total_items'] / result['unique_days'], 1)

            if timestamps:
                result['first_watch'] = min(timestamps)
                result['last_watch']  = max(timestamps)

            result['monthly'] = self._calc_monthly(items)
            result['top_genres'] = self._extract_top_genres(items)

        except Exception as e:
            _log(f'Erro ao computar stats: {e}')

        return result

    def _calc_streak(self, days_set):
        if not days_set:
            return 0
        try:
            sorted_days = sorted(days_set, reverse=True)
            today_str   = time.strftime('%Y-%m-%d')
            if sorted_days[0] not in (today_str,
                                      time.strftime('%Y-%m-%d',
                                                    time.localtime(time.time() - 86400))):
                return 0
            streak = 1
            for i in range(1, len(sorted_days)):
                prev = time.strptime(sorted_days[i - 1], '%Y-%m-%d')
                curr = time.strptime(sorted_days[i],     '%Y-%m-%d')
                diff = (time.mktime(prev) - time.mktime(curr)) / 86400
                if abs(diff - 1) < 0.1:
                    streak += 1
                else:
                    break
            return streak
        except Exception:
            return 0

    def _calc_monthly(self, items):
        monthly = Counter()
        try:
            for it in items:
                ts = it.get('timestamp', 0)
                if ts:
                    try:
                        t = time.localtime(ts)
                        key = time.strftime('%Y-%m', t)
                        monthly[key] += 1
                    except Exception:
                        pass
        except Exception as e:
            _log(f'Erro ao calcular mensal: {e}')
        if not monthly:
            return []
        sorted_keys = sorted(monthly.keys(), reverse=True)[:6]
        if not sorted_keys:
            return []
        max_c = monthly[sorted_keys[0]]
        return [
            {
                'label': time.strftime('%b/%y', time.strptime(k + '-01', '%Y-%m-%d')),
                'count': monthly[k],
                'pct': int(monthly[k] / max_c * 100) if max_c else 0,
            }
            for k in sorted_keys
        ]

    def _extract_top_genres(self, items, top_n=5):
        genre_counter = Counter()
        try:
            for it in items:
                name  = it.get('name', '')
                stype = it.get('stype', '')
                if stype == 'live' or not name:
                    continue
                cache_key = f"{'movie' if stype == 'movie' else 'series'}_{name}"
                cached = self._tmdb_cache.get(cache_key, {})
                genre_str = cached.get('genre', '')
                if genre_str:
                    for g in genre_str.split(','):
                        g = g.strip()
                        if g:
                            genre_counter[g] += 1
        except Exception as e:
            _log(f'Erro ao extrair generos: {e}')

        return [{'genre': g, 'count': c} for g, c in genre_counter.most_common(top_n)]

    # -- Formatacao de exibicao ---------------------------------------------

    @staticmethod
    def _fmt_hours(minutes):
        if minutes < 60:
            return f'{minutes}min'
        h = minutes // 60
        m = minutes % 60
        if m:
            return f'{h}h {m}min'
        return f'{h}h'

    @staticmethod
    def _fmt_date(ts):
        if not ts:
            return '-'
        try:
            return time.strftime('%d/%m/%Y', time.localtime(ts))
        except Exception:
            return '-'

    @staticmethod
    def _fmt_hour(h):
        if h is None:
            return '-'
        return f'{h:02d}:00'

    @staticmethod
    def _bar(value, total, width=10):
        if total == 0:
            return f'[COLOR gray]{"-" * width}[/COLOR]'
        filled = int(round(value / total * width))
        return f'[COLOR gold]{"#" * filled}[/COLOR][COLOR dimgray]{"-" * (width - filled)}[/COLOR]'

    @staticmethod
    def _pct(value, total):
        if total <= 0:
            return 0
        return int(round(value / total * 100))

    # -- Exibicao no Kodi ---------------------------------------------------

    def show_dashboard(self, addon_handle, addon_icon=None, addon_fanart=None):
        if not _HAS_KODI:
            return

        stats = self.compute()

        SEP   = '[B][COLOR orange] | [/COLOR][/B]'
        BRAND = '[B][COLOR white]KeTec[/COLOR] [COLOR crimson]Media Play[/COLOR][/B]'

        icon_use   = addon_icon   or 'DefaultFile.png'
        fanart_use = addon_fanart or ''

        def _li(label, plot=''):
            li = xbmcgui.ListItem(label=label)
            li.setProperty('IsPlayable', 'false')
            li.setArt({
                'icon':   icon_use,
                'thumb':  icon_use,
                'fanart': fanart_use,
            })
            if plot:
                try:
                    li.setInfo('video', {'plot': plot, 'title': label})
                except Exception:
                    pass
            return li

        def _add(label, plot=''):
            li = _li(label, plot)
            xbmcplugin.addDirectoryItem(
                handle=addon_handle,
                url='plugin://dummy',
                listitem=li,
                isFolder=False
            )

        def _section(title):
            _add(f'[B][COLOR gold]--- {title} ---[/COLOR][/B]')

        def _sep():
            _add(f'[COLOR dimgray]{"-" * 36}[/COLOR]')

        # =====================================================================
        # HEADER
        # =====================================================================
        _add(
            f'{BRAND}{SEP}[B][COLOR gold]Dashboard de Estatisticas[/COLOR][/B]'
        )
        _sep()

        total_it  = stats['total_items']
        total_h   = self._fmt_hours(stats['total_minutes'])
        unique_d  = stats['unique_days']
        avg_day   = stats['avg_per_day']

        _add(
            f'[B]Total assistido:[/B]  [COLOR gold]{total_h}[/COLOR]'
            f'  [COLOR dimgray]({total_it} reproducoes)[/COLOR]'
        )
        if unique_d > 0:
            _add(
                f'[B]Dias com atividade:[/B]  [COLOR deepskyblue]{unique_d}[/COLOR]'
                f'  [COLOR dimgray](media: {avg_day}/dia)[/COLOR]'
            )

        first = self._fmt_date(stats.get('first_watch'))
        last  = self._fmt_date(stats.get('last_watch'))
        if first != '-':
            _add(
                f'[B]Periodo:[/B]  [COLOR gray]{first}[/COLOR]'
                f'  [COLOR orange]a[/COLOR]'
                f'  [COLOR gray]{last}[/COLOR]'
            )

        # =====================================================================
        # DISTRIBUICAO POR TIPO
        # =====================================================================
        _sep()
        _section('POR TIPO')
        _sep()

        by_type    = stats['by_type']
        min_by_type = stats['minutes_by_type']
        live_n     = by_type.get('live', 0)
        movie_n    = by_type.get('movie', 0)
        ser_n      = by_type.get('series', 0)
        total_t    = max(live_n + movie_n + ser_n, 1)

        if live_n:
            bar = self._bar(live_n, total_t)
            hh = self._fmt_hours(min_by_type.get('live', 0))
            _add(
                f'[B][COLOR cyan]TV[/COLOR][/B] {bar} [B]{live_n}[/B]'
                f'  [COLOR dimgray]{hh}[/COLOR]'
                f'  [COLOR gray]({self._pct(live_n, total_t)}%)[/COLOR]'
            )
        if movie_n:
            bar = self._bar(movie_n, total_t)
            hh = self._fmt_hours(min_by_type.get('movie', 0))
            _add(
                f'[B][COLOR gold]VOD[/COLOR][/B] {bar} [B]{movie_n}[/B]'
                f'  [COLOR dimgray]{hh}[/COLOR]'
                f'  [COLOR gray]({self._pct(movie_n, total_t)}%)[/COLOR]'
            )
        if ser_n:
            bar = self._bar(ser_n, total_t)
            hh = self._fmt_hours(min_by_type.get('series', 0))
            _add(
                f'[B][COLOR lime]SER[/COLOR][/B] {bar} [B]{ser_n}[/B]'
                f'  [COLOR dimgray]{hh}[/COLOR]'
                f'  [COLOR gray]({self._pct(ser_n, total_t)}%)[/COLOR]'
            )

        # =====================================================================
        # TOP 5 MAIS ASSISTIDOS
        # =====================================================================
        if stats['top_titles']:
            _sep()
            _section('TOP 5 MAIS ASSISTIDOS')
            _sep()
            medals = ['[COLOR gold]1[/COLOR]', '[COLOR silver]2[/COLOR]',
                      '[COLOR orange]3[/COLOR]', '4', '5']
            for i, t in enumerate(stats['top_titles']):
                medal = medals[i] if i < len(medals) else f'{i+1}'
                _add(
                    f'  {medal}. [B]{t["name"]}[/B]'
                    f'  [COLOR dimgray]({t["count"]}x)[/COLOR]'
                )

        # =====================================================================
        # TOP 3 POR TIPO
        # =====================================================================
        top_by_type = stats['top_by_type']
        has_any_top = any(v for v in top_by_type.values())

        if has_any_top:
            _sep()
            _section('TOP 3 POR TIPO')
            _sep()

            if top_by_type['live']:
                _add(f'[B][COLOR cyan]Ao Vivo:[/COLOR][/B]')
                for i, t in enumerate(top_by_type['live']):
                    _add(
                        f'   {i+1}. [B]{t["name"]}[/B]'
                        f'  [COLOR dimgray]({t["count"]}x)[/COLOR]'
                    )

            if top_by_type['movie']:
                _add(f'[B][COLOR gold]Filmes:[/COLOR][/B]')
                for i, t in enumerate(top_by_type['movie']):
                    _add(
                        f'   {i+1}. [B]{t["name"]}[/B]'
                        f'  [COLOR dimgray]({t["count"]}x)[/COLOR]'
                    )

            if top_by_type['series']:
                _add(f'[B][COLOR lime]Series:[/COLOR][/B]')
                for i, t in enumerate(top_by_type['series']):
                    _add(
                        f'   {i+1}. [B]{t["name"]}[/B]'
                        f'  [COLOR dimgray]({t["count"]}x)[/COLOR]'
                    )

        # =====================================================================
        # GENEROS
        # =====================================================================
        if stats['top_genres']:
            _sep()
            _section('GENEROS FAVORITOS')
            _sep()
            max_g = stats['top_genres'][0]['count'] if stats['top_genres'] else 1
            for g in stats['top_genres']:
                bar = self._bar(g['count'], max_g, width=8)
                _add(
                    f'  {bar}  [B]{g["genre"]}[/B]'
                    f'  [COLOR dimgray]({g["count"]})[/COLOR]'
                )

        # =====================================================================
        # HABITOS
        # =====================================================================
        _sep()
        _section('HABITOS')
        _sep()

        streak = stats['streak_days']
        if streak >= 7:
            streak_color = 'gold'
        elif streak >= 3:
            streak_color = 'lime'
        elif streak >= 1:
            streak_color = 'deepskyblue'
        else:
            streak_color = 'gray'

        _add(
            f'[B]Streak:[/B]  [COLOR {streak_color}]{streak} dia(s) consecutivo(s)[/COLOR]'
        )

        best_h = stats.get('best_hour')
        if best_h is not None:
            period = ('manha' if 6 <= best_h < 12 else
                      'tarde' if 12 <= best_h < 18 else
                      'noite' if 18 <= best_h < 24 else
                      'madrugada')
            _add(
                f'[B]Horario favorito:[/B]'
                f'  [COLOR deepskyblue]{self._fmt_hour(best_h)}[/COLOR]'
                f'  [COLOR gray]({period})[/COLOR]'
            )

        best_dow = stats.get('best_dow')
        if best_dow is not None and 0 <= best_dow <= 6:
            _add(
                f'[B]Dia favorito:[/B]'
                f'  [COLOR deepskyblue]{self._DOW_NAMES[best_dow]}[/COLOR]'
            )

        # =====================================================================
        # ATIVIDADE MENSAL
        # =====================================================================
        monthly = stats.get('monthly', [])
        if monthly:
            _sep()
            _section('ATIVIDADE MENSAL')
            _sep()
            for m in monthly:
                bar = self._bar(m['count'], monthly[0]['count'], width=6)
                _add(
                    f'  [B]{m["label"]}[/B]  {bar}'
                    f'  [B]{m["count"]}[/B]'
                    f'  [COLOR dimgray]({m["pct"]}%)[/COLOR]'
                )

        # =====================================================================
        # FOOTER
        # =====================================================================
        _sep()
        _add(
            f'[COLOR dimgray]Estatisticas baseadas no historico local[/COLOR]'
        )

        xbmcplugin.setContent(addon_handle, 'files')
        xbmcplugin.endOfDirectory(addon_handle)


# ____________________________________________________________________________
# FACTORY FUNCTION
# ____________________________________________________________________________

def get_stats_manager(profile_dir, watch_history=None, tmdb_cache=None):
    try:
        return StatsManager(
            profile_dir=profile_dir,
            watch_history=watch_history,
            tmdb_cache=tmdb_cache,
        )
    except Exception as e:
        if _HAS_KODI:
            xbmc.log(f'[KelTec-Stats] Erro ao criar StatsManager: {e}', xbmc.LOGERROR)
        return None
