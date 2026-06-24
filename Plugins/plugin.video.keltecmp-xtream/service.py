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

# Mantém o serviço vivo e encerra sessão VIP no shutdown
monitor = xbmc.Monitor()
while not monitor.abortRequested():
    if monitor.waitForAbort(10):
        break

# Kodi está fechando — encerra sessão VIP corretamente
try:
    from lib.session_manager import end_session
    from lib.vip_manager import get_vip_manager, _clear_token as _vip_clear_token
    _addon_path = xbmc.translatePath(addon.getAddonInfo('profile'))
    # Envia action=end para servidor liberar o dispositivo
    end_session(_addon_path)
    xbmc.log("[KelTec Proxy] Sessão VIP encerrada no shutdown", xbmc.LOGINFO)
except Exception as _se:
    xbmc.log(f"[KelTec Proxy] Erro ao encerrar sessão: {_se}", xbmc.LOGINFO)

xbmc.log("[KelTec Proxy] Serviço encerrado", xbmc.LOGINFO)
