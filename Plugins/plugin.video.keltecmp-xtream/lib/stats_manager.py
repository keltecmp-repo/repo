# -*- coding: utf-8 -*-
# ============================================================================
# KELTEC MEDIA PLAY - DASHBOARD DE ESTATISTICAS v1.0
# ============================================================================
# Arquivo: lib/stats_manager.py
#
# FUNCIONALIDADES:
#   - Total de horas assistidas (filmes, series, ao vivo)
#   - Generos mais assistidos (usa dados TMDB ja em cache)
#   - Top 5 conteudos mais assistidos
#   - Streaks de visualizacao (dias consecutivos)
#   - Distribuicao por tipo (live / movie / series)
#   - Hora do dia preferida para assistir
#   - Exibicao no menu do Kodi como tela de estatisticas
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
    """
    Calcula e exibe estatisticas de visualizacao a partir do WatchHistory.

    Uso:
        sm = StatsManager(profile_dir, watch_history)
        sm.show_dashboard(addon_handle)
    """

    # Duracao estimada em minutos por tipo (para calcular horas sem timestamp fim)
    _DURATION_ESTIMATE = {
        'live':   60,   # 1h estimada por canal ao vivo
        'movie':  110,  # 1h50 estimada por filme
        'series': 45,   # 45min estimada por episodio
    }

    def __init__(self, profile_dir, watch_history=None, tmdb_cache=None):
        """
        profile_dir   : caminho do PROFILE_DIR do Kodi (para salvar stats extras)
        watch_history : instancia do WatchHistory do main.py
        tmdb_cache    : dict de cache TMDB em memoria (opcional, para enriquecer generos)
        """
        self._profile_dir   = profile_dir
        self._wh            = watch_history
        self._tmdb_cache    = tmdb_cache or {}
        self._stats_file    = os.path.join(profile_dir, 'keltec_stats_extra.json')

    # -- Dados brutos ------------------------------------_____________________

    def _get_all_items(self):
        """Retorna todos os itens do historico como lista de dicts."""
        if not self._wh:
            return []
        try:
            return self._wh.get_all() or []
        except Exception as e:
            _log(f'Erro ao obter historico: {e}')
            return []

    # -- Calculos principais ------------------------------------______________

    def compute(self):
        """
        Calcula todas as estatisticas e retorna um dict com os resultados.
        Seguro contra erros - nunca lanca excecao.
        """
        items = self._get_all_items()
        result = {
            'total_items':   0,
            'total_minutes': 0,
            'by_type':       {'live': 0, 'movie': 0, 'series': 0},
            'top_titles':    [],
            'top_genres':    [],
            'streak_days':   0,
            'best_hour':     None,
            'first_watch':   None,
            'last_watch':    None,
        }

        if not items:
            return result

        try:
            result['total_items'] = len(items)

            # -- Contagem por tipo ------------------------------------________
            type_counter = Counter()
            title_counter = Counter()
            hour_counter  = Counter()
            days_seen     = set()
            timestamps    = []

            for it in items:
                stype = it.get('stype', 'live')
                name  = it.get('name', '')
                ts    = it.get('timestamp', 0)

                type_counter[stype] += 1
                if name:
                    title_counter[name] += 1
                if ts:
                    timestamps.append(ts)
                    try:
                        t = time.localtime(ts)
                        hour_counter[t.tm_hour] += 1
                        days_seen.add(time.strftime('%Y-%m-%d', t))
                    except Exception:
                        pass

            result['by_type'] = {
                'live':   type_counter.get('live', 0),
                'movie':  type_counter.get('movie', 0),
                'series': type_counter.get('series', 0),
            }

            # -- Horas estimadas ------------------------------------__________
            total_min = 0
            for stype, count in type_counter.items():
                total_min += count * self._DURATION_ESTIMATE.get(stype, 60)
            result['total_minutes'] = total_min

            # -- Top titulos ------------------------------------______________
            result['top_titles'] = [
                {'name': n, 'count': c}
                for n, c in title_counter.most_common(5)
            ]

            # -- Hora preferida ------------------------------------___________
            if hour_counter:
                best_h = hour_counter.most_common(1)[0][0]
                result['best_hour'] = best_h

            # -- Streak de dias consecutivos __________________________________
            result['streak_days'] = self._calc_streak(days_seen)

            # -- Primeira e ultima visualizacao _______________________________
            if timestamps:
                result['first_watch'] = min(timestamps)
                result['last_watch']  = max(timestamps)

            # -- Generos (via cache TMDB) ------------------------------------_
            result['top_genres'] = self._extract_top_genres(items)

        except Exception as e:
            _log(f'Erro ao computar stats: {e}')

        return result

    def _calc_streak(self, days_set):
        """
        Calcula o streak atual de dias consecutivos assistindo.
        Considera "hoje" e dias anteriores contiguos.
        """
        if not days_set:
            return 0
        try:
            sorted_days = sorted(days_set, reverse=True)
            today_str   = time.strftime('%Y-%m-%d')
            # Streak comeca so se assistiu hoje ou ontem
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

    def _extract_top_genres(self, items, top_n=5):
        """
        Extrai generos mais assistidos cruzando o historico com o cache TMDB.
        Retorna lista de {'genre': str, 'count': int}.
        """
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

    # -- Formatacao de exibicao ------------------------------------___________

    @staticmethod
    def _fmt_hours(minutes):
        """Converte minutos em string legivel: '2h 30min' ou '145h'."""
        if minutes < 60:
            return f'{minutes}min'
        h = minutes // 60
        m = minutes % 60
        if m:
            return f'{h}h {m}min'
        return f'{h}h'

    @staticmethod
    def _fmt_date(ts):
        """Formata timestamp em DD/MM/YYYY."""
        if not ts:
            return '-'
        try:
            return time.strftime('%d/%m/%Y', time.localtime(ts))
        except Exception:
            return '-'

    @staticmethod
    def _fmt_hour(h):
        """Formata hora no padrao BR: 22:00."""
        if h is None:
            return '-'
        return f'{h:02d}:00'

    @staticmethod
    def _bar(value, total, width=10, fill='_', empty='_'):
        """Gera barra de progresso de texto."""
        if total == 0:
            return empty * width
        filled = int(round(value / total * width))
        return fill * filled + empty * (width - filled)

    # -- Exibicao no Kodi ------------------------------------_________________

    def show_dashboard(self, addon_handle, addon_icon=None, addon_fanart=None):
        """
        Exibe o dashboard de estatisticas como lista de itens no Kodi.
        Cada linha e um item nao reproduzivel - so visual.
        """
        if not _HAS_KODI:
            return

        stats = self.compute()
        items_raw = self._get_all_items()

        SEP   = '[B][COLOR orange] | [/COLOR][/B]'
        BRAND = '[B][COLOR white]KeTec[/COLOR] [COLOR crimson]Media Play[/COLOR][/B]'

        icon_use   = addon_icon   or 'DefaultFile.png'
        fanart_use = addon_fanart or ''

        def _li(label, plot='', icon=None):
            """Cria ListItem nao reproduzivel para o dashboard."""
            li = xbmcgui.ListItem(label=label)
            li.setProperty('IsPlayable', 'false')
            li.setArt({
                'icon':   icon or icon_use,
                'thumb':  icon or icon_use,
                'fanart': fanart_use,
            })
            if plot:
                try:
                    li.setInfo('video', {'plot': plot, 'title': label})
                except Exception:
                    pass
            return li

        def _add(label, plot='', icon=None, url=''):
            li = _li(label, plot, icon)
            xbmcplugin.addDirectoryItem(
                handle=addon_handle,
                url=url or 'plugin://dummy',
                listitem=li,
                isFolder=False
            )

        # ____________________________________________________________________
        # CABECALHO
        # ____________________________________________________________________
        _add(
            f'{BRAND}{SEP}[B][COLOR gold][ STATS ] Dashboard de Estatisticas[/COLOR][/B]',
            plot='Resumo completo de visualizacoes do KelTec Media Play.'
        )

        # Linha vazia visual
        _add('[COLOR dimgray]------------------------------------[/COLOR]')

        # ____________________________________________________________________
        # RESUMO GERAL
        # ____________________________________________________________________
        total_h  = self._fmt_hours(stats['total_minutes'])
        total_it = stats['total_items']

        _add(
            f'[B][COLOR deepskyblue]>>[/COLOR]  Total assistido:[/B]  [COLOR gold]{total_h}[/COLOR]'
            f'  [COLOR dimgray]({total_it} reproducoes)[/COLOR]',
            plot=(
                f'Tempo estimado total assistido: [B]{total_h}[/B]\n'
                f'Total de reproducoes: {total_it}\n\n'
                f'[COLOR gray](Estimativa: filmes ~110min, series ~45min, ao vivo ~60min)[/COLOR]'
            )
        )

        # ____________________________________________________________________
        # DISTRIBUICAO POR TIPO
        # ____________________________________________________________________
        by_type = stats['by_type']
        live_n  = by_type.get('live', 0)
        movie_n = by_type.get('movie', 0)
        ser_n   = by_type.get('series', 0)
        total_t = max(live_n + movie_n + ser_n, 1)

        live_bar  = self._bar(live_n,  total_t)
        movie_bar = self._bar(movie_n, total_t)
        ser_bar   = self._bar(ser_n,   total_t)

        _add('[COLOR dimgray]------------------------------------[/COLOR]')
        _add(
            f'[B][COLOR cyan][TV] Ao Vivo:[/COLOR][/B]  [COLOR cyan]{live_bar}[/COLOR] {live_n}',
            plot=f'Canais ao vivo assistidos: {live_n} vezes\n'
                 f'({int(live_n/total_t*100)}% do total)'
        )
        _add(
            f'[B][COLOR gold][VOD] Filmes:[/COLOR][/B]  [COLOR gold]{movie_bar}[/COLOR] {movie_n}',
            plot=f'Filmes assistidos: {movie_n} vezes\n'
                 f'({int(movie_n/total_t*100)}% do total)'
        )
        _add(
            f'[B][COLOR lime][SER] Series:[/COLOR][/B]  [COLOR lime]{ser_bar}[/COLOR] {ser_n}',
            plot=f'Episodios de series assistidos: {ser_n} vezes\n'
                 f'({int(ser_n/total_t*100)}% do total)'
        )

        # ____________________________________________________________________
        # TOP 5 TITULOS
        # ____________________________________________________________________
        if stats['top_titles']:
            _add('[COLOR dimgray]------------------------------------[/COLOR]')
            _add('[B][COLOR gold]--- Mais Assistidos ---[/COLOR][/B]')
            medals = ['[COLOR gold]1.[/COLOR]', '[COLOR silver]2.[/COLOR]', '[COLOR orange]3.[/COLOR]', '4.', '5.']
            for i, t in enumerate(stats['top_titles']):
                medal = medals[i] if i < len(medals) else f'{i+1}.'
                _add(
                    f'  {medal}  [B]{t["name"]}[/B]'
                    f'  [COLOR dimgray]({t["count"]}x)[/COLOR]',
                    plot=f'"{t["name"]}" foi assistido {t["count"]} vez(es).'
                )

        # ____________________________________________________________________
        # GENEROS FAVORITOS
        # ____________________________________________________________________
        if stats['top_genres']:
            _add('[COLOR dimgray]------------------------------------[/COLOR]')
            _add('[B][COLOR white]--- Generos Favoritos ---[/COLOR][/B]')
            max_g = stats['top_genres'][0]['count'] if stats['top_genres'] else 1
            for g in stats['top_genres']:
                bar = self._bar(g['count'], max_g, width=8)
                _add(
                    f'  [COLOR orange]{bar}[/COLOR]  [B]{g["genre"]}[/B]'
                    f'  [COLOR dimgray]({g["count"]})[/COLOR]',
                    plot=f'Genero "{g["genre"]}" - {g["count"]} conteudo(s) assistido(s).'
                )

        # ____________________________________________________________________
        # STREAK E HABITOS
        # ____________________________________________________________________
        _add('[COLOR dimgray]------------------------------------[/COLOR]')

        streak = stats['streak_days']
        if streak >= 7:
            streak_color = 'gold'
            streak_emoji = '[FUE]'
        elif streak >= 3:
            streak_color = 'lime'
            streak_emoji = '[BOA]'
        elif streak >= 1:
            streak_color = 'deepskyblue'
            streak_emoji = '[OK]'
        else:
            streak_color = 'gray'
            streak_emoji = '[---]'

        _add(
            f'[B][COLOR white]{streak_emoji}  Streak atual:[/COLOR][/B]'
            f'  [COLOR {streak_color}][B]{streak} dia(s) consecutivo(s)[/B][/COLOR]',
            plot=(
                f'Voce assistiu por [B]{streak} dia(s) seguido(s)[/B]!\n\n'
                + ('INCRIVEL! Continue assim!' if streak >= 7 else
                   'Boa sequencia!' if streak >= 3 else
                   'Comecando bem!' if streak >= 1 else
                   'Nenhum dia consecutivo recente.')
            )
        )

        best_h = stats.get('best_hour')
        if best_h is not None:
            period = ('manha' if 6 <= best_h < 12 else
                      'tarde' if 12 <= best_h < 18 else
                      'noite' if 18 <= best_h < 24 else
                      'madrugada')
            _add(
                f'[B][COLOR deepskyblue][HR][/COLOR]  Hora favorita:[/B]'
                f'  [COLOR deepskyblue]{self._fmt_hour(best_h)}[/COLOR]'
                f'  [COLOR gray]({period})[/COLOR]',
                plot=f'Voce costuma assistir mais as [B]{self._fmt_hour(best_h)}[/B] ({period}).'
            )

        # ____________________________________________________________________
        # PRIMEIRA / ULTIMA VISUALIZACAO
        # ____________________________________________________________________
        first = self._fmt_date(stats.get('first_watch'))
        last  = self._fmt_date(stats.get('last_watch'))
        if first != '-':
            _add(
                f'[B][COLOR white][CAL]  Periodo:[/COLOR][/B]'
                f'  [COLOR gray]{first}[/COLOR]'
                f'  [COLOR orange]-[/COLOR]'
                f'  [COLOR gray]{last}[/COLOR]',
                plot=f'Primeira visualizacao registrada: {first}\nUltima visualizacao: {last}'
            )

        # ____________________________________________________________________
        # RODAPE
        # ____________________________________________________________________
        _add('[COLOR dimgray]------------------------------------[/COLOR]')
        _add(
            '[COLOR dimgray]  Estatisticas baseadas no historico local do add-on[/COLOR]',
            plot='Os dados sao calculados a partir do historico de reproducao armazenado localmente.'
        )

        xbmcplugin.setContent(addon_handle, 'files')
        xbmcplugin.endOfDirectory(addon_handle)


# ____________________________________________________________________________
# FACTORY FUNCTION
# ____________________________________________________________________________

def get_stats_manager(profile_dir, watch_history=None, tmdb_cache=None):
    """
    Retorna instancia de StatsManager.
    Nunca lanca excecao - retorna None em caso de erro.
    """
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
