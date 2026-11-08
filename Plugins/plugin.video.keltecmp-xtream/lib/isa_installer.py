# -*- coding: utf-8 -*-
"""
Instalador automatico do inputstream.adaptive (ISA).

Garante que o add-on de stream adaptativo esteja INSTALADO e HABILITADO
antes de reproduzir canais (WebTV 1/2/3), independente da skin ou do
dispositivo. Usado como fallback em tempo de execucao alem da dependencia
declarada no addon.xml.

Retorno: True se o ISA ficou pronto para uso, False caso contrario
(nesse caso o player padrao/ffmpegdirect e usado como fallback).
"""
import time

import xbmc
import xbmcgui

ISA_ID = 'inputstream.adaptive'


def _installed():
    try:
        return bool(xbmc.getCondVisibility('System.HasAddon(%s)' % ISA_ID))
    except Exception:
        return False


def _enabled():
    try:
        return bool(xbmc.getCondVisibility('System.AddonIsEnabled(%s)' % ISA_ID))
    except Exception:
        # Algumas versoes/plataformas nao expoem AddonIsEnabled: assume habilitado
        return _installed()


def _wait_for(check, timeout):
    """Aguarda `check()` retornar True, mantendo o Kodi responsivo."""
    mon = xbmc.Monitor()
    deadline = time.monotonic() + max(1.0, float(timeout))
    while time.monotonic() < deadline:
        if mon.abortRequested():
            break
        try:
            if check():
                return True
        except Exception:
            pass
        mon.waitForAbort(0.5)
    try:
        return bool(check())
    except Exception:
        return False


def ensure_inputstream_adaptive(timeout=40.0, notify=True):
    """
    Instala (se ausente) e habilita (se desabilitado) o inputstream.adaptive.

    A instalacao usa o repositorio oficial do Kodi (que acompanha o app) e
    e feita de forma assincrona; aqui aguardamos ate o add-on aparecer.
    """
    if _installed() and _enabled():
        return True

    if not _installed():
        try:
            xbmc.executebuiltin('InstallAddon(%s)' % ISA_ID)
        except Exception:
            pass
        if notify:
            try:
                xbmcgui.Dialog().notification(
                    'KelTec', 'Instalando inputstream.adaptive...',
                    xbmcgui.NOTIFICATION_INFO, 3000)
            except Exception:
                pass
        _wait_for(_installed, timeout)

    if _installed() and not _enabled():
        try:
            xbmc.executebuiltin('EnableAddon(%s)' % ISA_ID)
        except Exception:
            pass
        _wait_for(_enabled, min(float(timeout), 15.0))

    ok = _installed() and _enabled()
    if notify:
        try:
            if ok:
                xbmcgui.Dialog().notification(
                    'KelTec', 'inputstream.adaptive pronto.',
                    xbmcgui.NOTIFICATION_INFO, 2000)
            else:
                xbmcgui.Dialog().notification(
                    'KelTec', 'Falha ao ativar inputstream.adaptive. Usando player padrao.',
                    xbmcgui.NOTIFICATION_WARNING, 4000)
        except Exception:
            pass
    return ok
