# -*- coding: utf-8 -*-
"""
service_refresh.py  -  Servico leve do KelTec Media Play

Deixa o add-on "dinamico" sem precisar reabrir menus:

  1. Fechou as CONFIGURACOES do Kodi (OK/voltar) estando no menu principal
     -> atualiza o menu principal na hora (servidor ativo, conta VIP, parental...).
  2. PAROU (ou terminou) uma reproducao e voltou para uma tela dinamica do add-on
     (menu principal, historico, estatisticas, favoritos)
     -> atualiza a tela na hora (contadores, "ultimos vistos", etc.).
  3. PAROU (ou terminou) uma reproducao -> avisa o painel VIP que o usuario voltou a
     "navegando" (idle), sem esperar o proximo heartbeat.

Observacoes:
  * Sobe o proxy nativo KPN (porta 8090) UMA vez, no boot do Kodi, para que nenhum clique
    (play de Xtream/WebTV) precise iniciar ou reiniciar o proxy. O main.py so inicia o proxy
    como fallback, se a porta estiver fechada.
  * So atualiza quando a janela de configuracoes FECHA ou quando a reproducao ACABA
    (nao a cada setSetting do proprio add-on), evitando laco de atualizacoes.
  * Se o add-on atualizou a tela ha instantes (propriedade 'keltec_menu_refreshed' na
    janela Home), nao atualiza de novo.
"""
import sys
import threading
import time

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

try:                                    # Python 3
    from urllib.parse import urlparse, parse_qs
except ImportError:                     # pragma: no cover
    from urlparse import urlparse, parse_qs

ADDON_ID = 'plugin.video.keltecmp-xtream'
ADDON_URL = 'plugin://plugin.video.keltecmp-xtream/'
POLL_SECONDS = 0.5
PENDING_WINDOW = 120        # segundos para esperar o menu aparecer apos fechar as configuracoes
SKIP_IF_REFRESHED = 3       # nao repete se o add-on ja atualizou ha menos de 3s
PLAY_SETTLE = 0.3           # espera o Kodi sair da tela cheia do video antes de atualizar
PLAY_PENDING_MAX = 20       # desiste se a tela nao assentar em 20s

# Telas que mudam com a reproducao (historico, contadores, ultimos vistos...)
DYNAMIC_AFTER_PLAY = ('main', 'enter', 'history_menu', 'history', 'stats_dashboard',
                      'favorites_menu')


def _container_mode():
    """Modo (?mode=) da lista do add-on exibida agora; None se nao for o add-on."""
    path = xbmc.getInfoLabel('Container.FolderPath') or ''
    if not path.startswith(ADDON_URL):
        return None
    try:
        return (parse_qs(urlparse(path).query).get('mode') or ['main'])[0] or 'main'
    except Exception:
        return 'main'


def _on_main_menu():
    """True se a lista exibida agora e o menu principal do add-on."""
    return _container_mode() in ('main', 'enter')


def _recently_refreshed():
    try:
        last = float(xbmcgui.Window(10000).getProperty('keltec_menu_refreshed') or 0)
        return (time.time() - last) < SKIP_IF_REFRESHED
    except Exception:
        return False


def _report_idle():
    """Avisa o painel VIP: reproducao acabou -> usuario voltou a 'navegando'. Roda em thread."""
    try:
        addon = xbmcaddon.Addon(ADDON_ID)
        path = xbmcvfs.translatePath(addon.getAddonInfo('path'))
        if path not in sys.path:
            sys.path.insert(0, path)
        profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
        from lib.session_manager import report_content_standalone
        report_content_standalone(profile, 'idle')
    except Exception as e:
        xbmc.log('[KelTec] service_refresh: idle: %s' % e, xbmc.LOGDEBUG)


def _do_refresh(reason):
    try:
        xbmcgui.Window(10000).setProperty('keltec_menu_refreshed', str(time.time()))
    except Exception:
        pass
    xbmc.log('[KelTec] %s: atualizando tela' % reason, xbmc.LOGINFO)
    xbmc.executebuiltin('Container.Refresh')


class _PlayerWatcher(xbmc.Player):
    """Avisa o laco principal quando uma reproducao termina (stop, fim ou erro)."""
    def __init__(self):
        xbmc.Player.__init__(self)
        self.ended_at = 0.0

    def onPlayBackStopped(self):
        self.ended_at = time.time()

    def onPlayBackEnded(self):
        self.ended_at = time.time()

    def onPlayBackError(self):
        self.ended_at = time.time()


KPN_PORT = 8090


def _port_open(port, timeout=0.2):
    import socket
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(timeout)
        r = sk.connect_ex(('127.0.0.1', port))
        sk.close()
        return r == 0
    except Exception:
        return False


def _start_kpn_proxy():
    """Inicia o proxy nativo (kpn.py) uma unica vez, se a porta ainda estiver livre."""
    try:
        if _port_open(KPN_PORT):
            return
        addon = xbmcaddon.Addon(ADDON_ID)
        path = xbmcvfs.translatePath(addon.getAddonInfo('path'))
        if path not in sys.path:
            sys.path.insert(0, path)
        from kpn import server_run
        threading.Thread(target=server_run, args=(KPN_PORT,), daemon=True,
                         name='KelTecStreamProxy').start()
        xbmc.log('[KelTec] service_refresh: proxy KPN iniciado na porta %d' % KPN_PORT, xbmc.LOGINFO)
    except Exception as e:
        xbmc.log('[KelTec] service_refresh: proxy KPN: %s' % e, xbmc.LOGWARNING)


def run():
    _start_kpn_proxy()
    monitor = xbmc.Monitor()
    player = _PlayerWatcher()
    settings_was_open = False
    pending_until = 0.0

    while not monitor.abortRequested():
        if monitor.waitForAbort(POLL_SECONDS):
            break
        try:
            # ---------- reproducao terminou: atualiza telas dinamicas ----------
            if player.ended_at:
                elapsed = time.time() - player.ended_at
                if xbmc.getCondVisibility('Player.HasMedia'):
                    player.ended_at = 0.0           # ja comecou outra (ex.: proximo episodio)
                elif elapsed > PLAY_PENDING_MAX:
                    player.ended_at = 0.0
                elif elapsed >= PLAY_SETTLE and \
                        not xbmc.getCondVisibility('Window.IsActive(fullscreenvideo)'):
                    player.ended_at = 0.0
                    threading.Thread(target=_report_idle, daemon=True).start()
                    if _container_mode() in DYNAMIC_AFTER_PLAY and not _recently_refreshed():
                        _do_refresh('Reproducao encerrada')

            # ---------- configuracoes fechadas: atualiza o menu principal ----------
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
                    _do_refresh('Configuracoes fechadas')
        except Exception as e:
            xbmc.log('[KelTec] service_refresh: %s' % e, xbmc.LOGDEBUG)


if __name__ == '__main__':
    run()
