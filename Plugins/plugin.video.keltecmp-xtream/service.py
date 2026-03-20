# -*- coding: utf-8 -*-
"""
SERVICE.PY - Inicia servidor F4MTESTER automaticamente
Coloque em: service.py (raiz do addon)
"""

import xbmc
import xbmcaddon
import threading
import sys
import os

# Adiciona pasta resources/lib ao path
addon = xbmcaddon.Addon()
addon_path = xbmc.translatePath(addon.getAddonInfo('path'))
lib_path = os.path.join(addon_path, 'resources', 'lib')
sys.path.insert(0, lib_path)

# Log inicial
xbmc.log("[KelTec F4M] Iniciando serviço...", xbmc.LOGINFO)

# Inicia servidor F4MTESTER em thread separada
try:
    from f4m_proxy import server_run
    
    threading.Thread(target=server_run, daemon=True).start()
    
    xbmc.log("[KelTec F4M] ✅ Servidor F4MTESTER iniciado na porta 8088", xbmc.LOGINFO)
    
except ImportError as e:
    xbmc.log(f"[KelTec F4M] ❌ Erro ao importar f4m_proxy: {e}", xbmc.LOGERROR)
except Exception as e:
    xbmc.log(f"[KelTec F4M] ❌ Erro ao iniciar servidor: {e}", xbmc.LOGERROR)

# Mantém o serviço vivo
monitor = xbmc.Monitor()

while not monitor.abortRequested():
    if monitor.waitForAbort(10):
        break

# Encerra
xbmc.log("[KelTec F4M] Serviço encerrado", xbmc.LOGINFO)