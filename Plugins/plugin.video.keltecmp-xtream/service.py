# -*- coding: utf-8 -*-
"""
SERVICE.PY - Inicia servidor proxy nativo KelTec (sem dependência de f4mTester)
"""

import xbmc
import xbmcaddon
import threading
import sys
import os

addon = xbmcaddon.Addon()
addon_path = xbmc.translatePath(addon.getAddonInfo('path'))
sys.path.insert(0, addon_path)

xbmc.log("[KelTec Proxy] Iniciando serviço...", xbmc.LOGINFO)

try:
    from app import server_run, PORT

    threading.Thread(target=server_run, daemon=True).start()

    xbmc.log(f"[KelTec Proxy] ✅ Servidor nativo iniciado na porta {PORT}", xbmc.LOGINFO)

except ImportError as e:
    xbmc.log(f"[KelTec Proxy] ❌ Erro ao importar app: {e}", xbmc.LOGERROR)
except Exception as e:
    xbmc.log(f"[KelTec Proxy] ❌ Erro ao iniciar servidor: {e}", xbmc.LOGERROR)

# Mantém o serviço vivo
monitor = xbmc.Monitor()
while not monitor.abortRequested():
    if monitor.waitForAbort(10):
        break

xbmc.log("[KelTec Proxy] Serviço encerrado", xbmc.LOGINFO)
