# -*- coding: utf-8 -*-
"""
service_refresh.py  -  Servico leve do KelTec Media Play

Unica funcao: quando o usuario fecha a janela de CONFIGURACOES do Kodi (OK/voltar)
e a tela atual e o MENU PRINCIPAL do add-on, atualiza o menu na hora para refletir
o novo status (servidor ativo, conta VIP, controle parental, itens visiveis...).

Observacoes:
  * Nao inicia proxy nem toca em nada do main.py (o proxy continua subindo pelo main).
  * Atualiza so quando a janela de configuracoes FECHA (nao em cada setSetting do
    proprio add-on), evitando laco de atualizacoes.
  * Se o menu foi atualizado pelo proprio add-on ha instantes (propriedade
    'keltec_menu_refreshed' na janela Home), nao atualiza de novo.
"""
import time

import xbmc
import xbmcgui

try:                                    # Python 3
    from urllib.parse import urlparse, parse_qs
except ImportError:                     # pragma: no cover
    from urlparse import urlparse, parse_qs

ADDON_URL = 'plugin://plugin.video.keltecmp-xtream/'
POLL_SECONDS = 1.0
PENDING_WINDOW = 120        # segundos para esperar o menu aparecer apos fechar as configuracoes
SKIP_IF_REFRESHED = 5       # nao repete se o add-on ja atualizou ha menos de 5s


def _on_main_menu():
    """True se a lista exibida agora e o menu principal do add-on."""
    path = xbmc.getInfoLabel('Container.FolderPath') or ''
    if not path.startswith(ADDON_URL):
        return False
    try:
        mode = (parse_qs(urlparse(path).query).get('mode') or ['main'])[0] or 'main'
    except Exception:
        mode = 'main'
    return mode in ('main', 'enter')


def _recently_refreshed():
    try:
        last = float(xbmcgui.Window(10000).getProperty('keltec_menu_refreshed') or 0)
        return (time.time() - last) < SKIP_IF_REFRESHED
    except Exception:
        return False


def run():
    monitor = xbmc.Monitor()
    settings_was_open = False
    pending_until = 0.0

    while not monitor.abortRequested():
        if monitor.waitForAbort(POLL_SECONDS):
            break
        try:
            settings_open = xbmc.getCondVisibility('Window.IsVisible(addonsettings)')
            if settings_open:
                settings_was_open = True
                continue

            if settings_was_open:               # acabou de fechar as configuracoes
                settings_was_open = False
                pending_until = time.time() + PENDING_WINDOW

            if pending_until:
                if time.time() > pending_until:
                    pending_until = 0.0
                    continue
                # configuracoes abertas a partir da ficha do add-on: espera a ficha fechar
                if xbmc.getCondVisibility('Window.IsVisible(addoninformation)'):
                    continue
                pending_until = 0.0
                if _on_main_menu() and not _recently_refreshed():
                    xbmc.log('[KelTec] Configuracoes fechadas: atualizando menu principal', xbmc.LOGINFO)
                    xbmc.executebuiltin('Container.Refresh')
        except Exception as e:
            xbmc.log('[KelTec] service_refresh: %s' % e, xbmc.LOGDEBUG)


if __name__ == '__main__':
    run()
