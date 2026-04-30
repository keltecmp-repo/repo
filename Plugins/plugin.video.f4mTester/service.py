import xbmc
import xbmcaddon
import xbmcvfs
import threading
import socket
import time
import os
import tempfile

def _get_kodi_temp_dir():
    try:
        tmp = xbmcvfs.translatePath('special://temp/')
        if tmp and os.path.isdir(tmp):
            return tmp
    except Exception:
        pass
    try:
        tmp = tempfile.gettempdir()
        if tmp and os.path.isdir(tmp):
            return tmp
    except Exception:
        pass
    return os.path.dirname(os.path.abspath(__file__))

_PORT_FILE = os.path.join(_get_kodi_temp_dir(), 'f4mtester_port.tmp')

def _read_port():
    try:
        with open(_PORT_FILE, 'r') as f:
            return int(f.read().strip())
    except Exception:
        return 8088

# Inicia o servidor numa thread separada
def _start_server():
    try:
        from app import server_run
        server_run()
    except Exception as e:
        xbmc.log('[f4mTester] ERRO fatal no servidor: %s' % str(e), xbmc.LOGERROR)

t = threading.Thread(target=_start_server)
t.daemon = True
t.start()

# Aguarda o servidor estar realmente respondendo
# Le a porta do ARQUIVO (atualizado pelo server_run apos bind bem-sucedido)
def _wait_server_ready(timeout=15):
    deadline = time.time() + timeout
    port = 8088
    while time.time() < deadline:
        # Re-le a porta a cada tentativa -- o server_run atualiza o arquivo
        # apos o bind bem-sucedido, entao eventualmente pegaremos a porta certa
        port = _read_port()
        try:
            s = socket.create_connection(('127.0.0.1', port), timeout=0.5)
            s.close()
            xbmc.log('[f4mTester] Proxy pronto na porta %d' % port, xbmc.LOGINFO)
            return True
        except Exception:
            time.sleep(0.5)
    xbmc.log('[f4mTester] AVISO: proxy nao respondeu em %ds (porta=%d)' % (timeout, port), xbmc.LOGWARNING)
    return False

_wait_server_ready()

# Mantém o addon vivo
monitor = xbmc.Monitor()
while not monitor.abortRequested():
    if monitor.waitForAbort(5):
        break

xbmc.log('[f4mTester] Servico encerrado.', xbmc.LOGINFO)