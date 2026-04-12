# -*- coding: utf-8 -*-
"""
KelTec Media Play — Proxy Local de Stream v2.0
================================================
Servidor HTTP leve que roda em 127.0.0.1:8089.

Função:
  Recebe requisições do Kodi VideoPlayer com um token opaco,
  descriptografa o token para obter a URL real do servidor,
  e faz o proxy transparente dos bytes de vídeo.

Resultado no kodi.log:
  VideoPlayer::OpenFile: http://127.0.0.1:8089/stream?token=XXXX
  (a URL real com credenciais NUNCA aparece no log)

Endpoints:
  GET /stream?token=<TOKEN>      → proxy de filmes/séries/lives
  GET /health                    → health check (retorna OK)
  GET /stop                      → encerra o servidor

TOKEN:
  base64url( xor( json({"url": "...", "ua": "..."}), KEY ) )
  Gerado por gerar_token() no main.py — mesma chave _CACHE_KEY.
"""

import sys
import os
import socket
import threading
import base64
import json
import time

try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse, parse_qs, urlencode, quote
    import urllib.request as _urllib_req
except ImportError:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
    from urlparse import urlparse, parse_qs
    import urllib2 as _urllib_req

# ── Configuração ─────────────────────────────────────────────────────────────
PROXY_HOST = '127.0.0.1'
PROXY_PORT = 8089                    # Porta diferente do F4M (8088)
CHUNK_SIZE = 64 * 1024               # 64 KB por chunk
CONNECT_TIMEOUT = 15                 # segundos para conectar ao servidor
READ_TIMEOUT    = 30                 # segundos para ler dados

# Mesma chave do módulo de proteção no main.py
# IMPORTANTE: troque para o mesmo valor que _CACHE_KEY no main.py
_KEY = b'KT#2025!SecureMP'

USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/127.0.0.0 Safari/537.36'
)

# ── Cifra XOR (igual ao main.py) ─────────────────────────────────────────────
def _xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def _decode_token(token: str) -> dict:
    """Descriptografa token e retorna dict com 'url' (e opcionalmente 'ua')."""
    try:
        # Normaliza base64url → base64 padrão
        padded = token + '=' * (-len(token) % 4)
        cifrado = base64.b64decode(padded.replace('-', '+').replace('_', '/'))
        raw = _xor(cifrado, _KEY)
        return json.loads(raw.decode('utf-8'))
    except Exception:
        return {}

def gerar_token(url: str, ua: str = '') -> str:
    """
    Gera um token opaco para a URL.
    Use esta função no main.py para criar a URL de proxy:
        token = gerar_token(url_real)
        url_proxy = f'http://127.0.0.1:{PROXY_PORT}/stream?token={token}'
    """
    payload = json.dumps({'url': url, 'ua': ua or USER_AGENT},
                         ensure_ascii=False).encode('utf-8')
    cifrado = _xor(payload, _KEY)
    token = base64.b64encode(cifrado).decode('ascii')
    # Converte para base64url (seguro em querystring sem encoding)
    return token.replace('+', '-').replace('/', '_').rstrip('=')


# ── Handler HTTP ──────────────────────────────────────────────────────────────
class ProxyHandler(BaseHTTPRequestHandler):

    # Silencia logs do servidor HTTP (não aparece no kodi.log)
    def log_message(self, fmt, *args):
        pass

    def log_error(self, fmt, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path   = parsed.path.rstrip('/')

        if path == '/health':
            self._respond_text(200, 'OK')
            return

        if path == '/stop':
            self._respond_text(200, 'Stopping')
            threading.Thread(target=self.server.shutdown, daemon=True).start()
            return

        if path == '/stream':
            params = parse_qs(parsed.query)
            token  = params.get('token', [''])[0]
            if not token:
                self._respond_text(400, 'Token ausente')
                return
            self._proxy_stream(token)
            return

        self._respond_text(404, 'Not found')

    def _respond_text(self, code, msg):
        body = msg.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _proxy_stream(self, token):
        """
        Descriptografa o token, conecta ao servidor real e faz proxy
        transparente dos bytes — suporta Range requests (seek do player).
        """
        info = _decode_token(token)
        real_url = info.get('url', '')
        ua       = info.get('ua', USER_AGENT)

        if not real_url:
            self._respond_text(400, 'Token inválido')
            return

        # Monta headers para o servidor real
        req_headers = {
            'User-Agent': ua,
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }

        # Repassa Range do Kodi (necessário para seek funcionar)
        range_hdr = self.headers.get('Range', '')
        if range_hdr:
            req_headers['Range'] = range_hdr

        try:
            req = _urllib_req.Request(real_url, headers=req_headers)
            resp = _urllib_req.urlopen(req, timeout=CONNECT_TIMEOUT)
        except Exception as e:
            self._respond_text(502, f'Erro ao conectar: {e}')
            return

        # Determina status de resposta
        status = resp.getcode()
        if range_hdr and status == 200:
            status = 206  # Partial Content se houve Range mas servidor ignorou

        # Cabeçalhos de resposta ao Kodi
        self.send_response(status)

        content_type   = resp.headers.get('Content-Type',   'video/mp4')
        content_length = resp.headers.get('Content-Length', '')
        content_range  = resp.headers.get('Content-Range',  '')
        accept_ranges  = resp.headers.get('Accept-Ranges',  'bytes')

        self.send_header('Content-Type',   content_type)
        self.send_header('Accept-Ranges',  accept_ranges)
        if content_length:
            self.send_header('Content-Length', content_length)
        if content_range:
            self.send_header('Content-Range', content_range)
        self.end_headers()

        # Stream dos dados em chunks
        try:
            while True:
                chunk = resp.read(CHUNK_SIZE)
                if not chunk:
                    break
                self.wfile.write(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass  # Kodi parou a reprodução — normal
        except Exception:
            pass
        finally:
            try:
                resp.close()
            except Exception:
                pass


# ── Servidor ──────────────────────────────────────────────────────────────────
class ThreadedProxyServer(HTTPServer):
    """HTTPServer com threads por requisição (suporta múltiplos streams)."""
    allow_reuse_address = True

    def process_request(self, request, client_address):
        t = threading.Thread(
            target=self._handle_request_noblock,
            args=(request, client_address),
            daemon=True
        )
        t.start()

    def _handle_request_noblock(self, request, client_address):
        try:
            self.finish_request(request, client_address)
        except Exception:
            pass
        finally:
            self.shutdown_request(request)


def esta_rodando(port=PROXY_PORT):
    """Verifica se o proxy já está rodando na porta."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((PROXY_HOST, port))
        s.close()
        return result == 0
    except Exception:
        return False


def iniciar_servidor():
    """Inicia o servidor proxy. Bloqueia até encerrado."""
    if esta_rodando():
        return  # Já está rodando

    try:
        server = ThreadedProxyServer((PROXY_HOST, PROXY_PORT), ProxyHandler)
        server.serve_forever()
    except OSError:
        pass  # Porta ocupada


# ── Entry point (quando chamado como subprocess) ──────────────────────────────
if __name__ == '__main__':
    iniciar_servidor()
