from flask import Flask, request, Response, jsonify
import urllib.parse
import requests
import binascii
import os
import re
import time
import logging
import sys
import warnings
from urllib.parse import urljoin
from requests.exceptions import ConnectionError, RequestException
from urllib3.exceptions import IncompleteRead
from doh import DNSOverrideDoH

# ============================================
# SILENCIAMENTO EXTREMO - NENHUM LOG APARECE
# ============================================

# Desativa warnings
warnings.filterwarnings("ignore")

# 1. Desativa completamente o sistema de logging
logging.basicConfig(level=logging.CRITICAL)
logging.disable(logging.CRITICAL)

# 2. Desativa todos os loggers conhecidos
for name in list(logging.Logger.manager.loggerDict.keys()):
    try:
        logging.getLogger(name).disabled = True
    except:
        pass

# 3. Silencia loggers específicos
for logger_name in [
    'werkzeug', 'flask', 'flask.app', 'flask.cli',
    'urllib3', 'urllib3.connectionpool', 'urllib3.connection',
    'urllib3.response', 'urllib3.util.retry',
    'requests', 'requests.packages.urllib3',
    'dns', 'dns.resolver', 'dns.rdtypes',
    'http.client', 'chardet', 'charset_normalizer'
]:
    try:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.CRITICAL)
        logger.disabled = True
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
    except:
        pass

# 4. Remove todos os handlers do root logger
root_logger = logging.getLogger()
for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)

# 5. Configura ambiente para não gerar logs
os.environ['WERKZEUG_RUN_MAIN'] = 'true'
os.environ['FLASK_ENV'] = 'production'
os.environ['FLASK_DEBUG'] = '0'
os.environ['WERKZEUG_DEBUG_PIN'] = 'off'

# 6. Redireciona stdout e stderr para null
class NullDevice:
    def write(self, *args, **kwargs):
        pass
    def flush(self, *args, **kwargs):
        pass
    def close(self, *args, **kwargs):
        pass

# Salva os originais
_original_stdout = sys.stdout
_original_stderr = sys.stderr

# Redireciona
sys.stdout = NullDevice()
sys.stderr = NullDevice()

# 7. Substitui a função print original
_original_print = print
def null_print(*args, **kwargs):
    pass
import builtins
builtins.print = null_print

# 8. Desativa o output do Flask no console
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# ============================================
# FIM DO SILENCIAMENTO
# ============================================

PORT = 8088

# Cria o app com debug desativado
app = Flask(__name__)
app.debug = False
app.config['PROPAGATE_EXCEPTIONS'] = False

# Desativa completamente os logs do Flask
app.logger.disabled = True
app.logger.handlers = []

# Desativa o logger do werkzeug
werkzeug_log = logging.getLogger('werkzeug')
werkzeug_log.disabled = True
werkzeug_log.handlers = []

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

IP_CACHE_TS = {}
IP_CACHE_MP4 = {}
AGENT_OF_CHAOS = {}
COUNT_CLEAR = {}

def get_ip():
    forwarded_for = request.headers.get("X-Forwarded-For")
    real_ip = request.headers.get("X-Real-IP")
    if forwarded_for:
        ip = forwarded_for.split(",")[0].strip()
    elif real_ip:
        ip = real_ip
    else:
        ip = request.remote_addr
    return ip

def get_cache_key(client_ip: str, url: str) -> str:
    return f"{client_ip}:{url}"

def rewrite_m3u8_urls(playlist_content: str, base_url: str) -> str:
    def replace_url(match):
        segment_url = match.group(0).strip()
        if segment_url.startswith('#') or not segment_url or segment_url == '/':
            return segment_url
        try:
            absolute_url = urljoin(base_url + '/', segment_url)
            if not (absolute_url.endswith('.ts') or '/hl' in absolute_url.lower() or absolute_url.endswith('.m3u8')):
                return segment_url
            scheme = request.scheme
            host = request.host
            proxied_url = f"{scheme}://{host}/hlsretry?url={urllib.parse.quote(absolute_url)}"
            return proxied_url
        except ValueError:
            return segment_url

    return re.sub(r'^(?!#)\S+', replace_url, playlist_content, flags=re.MULTILINE)

def stream_response(response, client_ip, url, headers, sess):
    cache_key = get_cache_key(client_ip, url) if any(ext in url.lower() for ext in ['.mp4', '.m3u8']) else client_ip
    mode_ts = False

    def generate_chunks():
        nonlocal mode_ts
        bytes_read = 0
        try:
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    bytes_read += len(chunk)
                    if '.mp4' in url.lower():
                        IP_CACHE_MP4.setdefault(cache_key, []).append(chunk)
                        if len(IP_CACHE_MP4[cache_key]) > 20:
                            IP_CACHE_MP4[cache_key].pop(0)
                    elif '.ts' in url.lower() or '/hl' in url.lower():
                        mode_ts = True
                        IP_CACHE_TS.setdefault(cache_key, []).append(chunk)
                        if len(IP_CACHE_TS[cache_key]) > 20:
                            IP_CACHE_TS[cache_key].pop(0)
                    yield chunk
        except (IncompleteRead, ConnectionError):
            cache = IP_CACHE_TS if mode_ts else IP_CACHE_MP4
            for chunk in cache.get(cache_key, [])[-5:]:
                yield chunk
        finally:
            try:
                sess.close()
            except:
                pass

    return generate_chunks()

def stream_cache(client_ip, url):
    if url:
        cache_key = get_cache_key(client_ip, url) if any(ext in url.lower() for ext in ['.mp4', '.m3u8']) else client_ip
        if '.mp4' in url.lower():
            cache = IP_CACHE_MP4
        elif '.ts' in url.lower() or '/hl' in url.lower():
            cache = IP_CACHE_TS
        else:
            cache = None
        if cache:
            def generate_cached_chunks():
                if cache_key in cache:
                    for chunk in cache.get(cache_key, [])[-5:]:
                        yield chunk
            return generate_cached_chunks()
    return None

@app.route("/hlsretry")
def hls_retry():
    DNSOverrideDoH()
    url = request.args.get('url')
    client_ip = get_ip()
    cache_key = get_cache_key(client_ip, url) if url and any(x in url.lower() for x in ['.mp4', '.m3u8']) else client_ip

    if not url:
        return jsonify({"detail": "No URL provided"}), 400

    session = requests.Session()
    headers_master = dict(request.headers)
    original_headers = {}
    headers = {}
    for k, v in headers_master.items():
        if k.lower() == 'host':
            continue
        else:
            headers[k] = v
            original_headers[k] = v 
    max_retries = 7
    attempts = 0
    tried_without_range = False
    change_user_agent = False

    media_type = (
        'video/mp4' if '.mp4' in url.lower()
        else 'video/mp2t' if '.ts' in url.lower() or '/hl' in url.lower()
        else 'application/octet-stream'
    )
    response_headers = {}
    status = 200

    while attempts < max_retries:
        try:
            range_header = headers.get('Range')
            if '.mp4' in url.lower() and range_header and tried_without_range:
                headers.pop('Range', None)

            if AGENT_OF_CHAOS.get(cache_key) and not '.ts' in url.lower() and not '/hl' in url.lower():
                if not change_user_agent:
                    headers['User-Agent'] = original_headers.get('User-Agent', DEFAULT_USER_AGENT)
                else:
                    headers['User-Agent'] = AGENT_OF_CHAOS[cache_key]
            if '.ts' in url.lower() or '/hl' in url.lower():
                if change_user_agent or not headers.get('User-Agent'):
                    headers['User-Agent'] = binascii.b2a_hex(os.urandom(20))[:32]
                else:
                    headers['User-Agent'] = original_headers.get('User-Agent', DEFAULT_USER_AGENT)

            response = session.get(url, headers=headers, allow_redirects=True, stream=True, timeout=9)

            if response.status_code in (200, 206):
                if '.mp4' in url.lower() or '.m3u8' in url.lower():
                    url = response.url
                change_user_agent = False
                if client_ip in COUNT_CLEAR:
                    if COUNT_CLEAR.get(client_ip, 0) > 4:
                        try:
                            if cache_key in AGENT_OF_CHAOS:
                                del AGENT_OF_CHAOS[cache_key]
                            if cache_key in IP_CACHE_MP4:
                                del IP_CACHE_MP4[cache_key]
                            if cache_key in IP_CACHE_TS:
                                del IP_CACHE_TS[cache_key]
                        except:
                            pass
                if not client_ip in COUNT_CLEAR:
                    COUNT_CLEAR[client_ip] = 0
                elif int(COUNT_CLEAR.get(client_ip, 0) > 4):
                    COUNT_CLEAR[client_ip] = 0
                else:
                    if client_ip in COUNT_CLEAR:
                        COUNT_CLEAR[client_ip] = COUNT_CLEAR.get(client_ip, 0) + 1                    
                content_type = response.headers.get("content-type", "").lower()

                if "mpegurl" in content_type or ".m3u8" in url.lower():
                    base_url = url.rsplit('/', 1)[0]
                    playlist_content = response.content.decode('utf-8', errors='ignore')
                    rewritten = rewrite_m3u8_urls(playlist_content, base_url)
                    return Response(rewritten, content_type="application/x-mpegURL")
                
                if '/hl' in url.lower() and '_' in url.lower() and '.ts' in url.lower():
                    try:
                        seg_ = re.findall(r'_(.*?)\.ts', url)[0]
                        seg_before = f'_{seg_}.ts'
                        seg_after = f'_{str(int(seg_) + 1)}.ts'
                        url = url.replace(seg_before, seg_after)
                    except:
                        pass

                media_type = (
                    'video/mp4' if '.mp4' in url.lower()
                    else 'video/mp2t' if '.ts' in url.lower() or '/hl' in url.lower()
                    else response.headers.get("content-type", "application/octet-stream")
                )

                response_headers = {
                    k: v for k, v in response.headers.items()
                    if k.lower() in ['content-type', 'accept-ranges', 'content-range']
                }

                status = 206 if response.status_code == 206 else 200

                return Response(
                    stream_response(response, client_ip, url, headers, session),
                    headers=response_headers,
                    content_type=media_type,
                    status=status
                )

            elif response.status_code == 416 and range_header and not tried_without_range:
                tried_without_range = True
                continue
            else:
                change_user_agent = True
                AGENT_OF_CHAOS[cache_key] = binascii.b2a_hex(os.urandom(20))[:32]
                time.sleep(3)
                attempts += 1
                if '.ts' in url.lower() or '/hl' in url.lower() or '.mp4' in url.lower():
                    return Response(
                        stream_cache(client_ip, url),
                        headers=response_headers,
                        content_type=media_type,
                        status=status
                    )                       
        except RequestException:
            change_user_agent = True
            AGENT_OF_CHAOS[cache_key] = binascii.b2a_hex(os.urandom(20))[:32]
            time.sleep(3)
            attempts += 1
            if '.ts' in url.lower() or '/hl' in url.lower() or '.mp4' in url.lower():
                return Response(
                    stream_cache(client_ip, url),
                    headers=response_headers,
                    content_type=media_type,
                    status=status
                )              

    return jsonify({"detail": "Falha ao conectar após múltiplas tentativas"}), 502


@app.route("/tsdownloader")
def ts_downloader():
    DNSOverrideDoH()
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    headers_master = dict(request.headers)
    headers = {}
    for k, v in headers_master.items():
        if k.lower() == 'host':
            continue
        else:
            headers[k] = v 

    stop_ts = False
    last_url = ''

    def generate_ts():
        nonlocal last_url
        nonlocal stop_ts
        while not stop_ts:
            try:                
                if not last_url:
                    last_url = requests.get(url, headers=headers, allow_redirects=True, stream=True, timeout=5).url 
                with requests.get(last_url, headers=headers, stream=True, timeout=15) as response:
                    if response.status_code == 200:
                        for chunk in response.iter_content(chunk_size=4096):
                            if stop_ts:
                                return
                            if chunk:
                                try:
                                    yield chunk
                                except (ConnectionResetError, BrokenPipeError, GeneratorExit):
                                    stop_ts = True
                                    return
            except Exception:
                pass

    resp = Response(generate_ts(), content_type='video/mp2t')

    @resp.call_on_close
    def on_close():
        nonlocal stop_ts
        stop_ts = True

    return resp


@app.route("/")
def index():
    return jsonify({"message": "F4MTESTER PROXY v4.2.5"})


def server_run():
    # Suprime qualquer output restante
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            app.run(host='127.0.0.1', port=PORT, debug=False, use_reloader=False, threaded=True)
        except Exception:
            pass
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


# Restaura para o resto do programa (não deve afetar)
sys.stdout = _original_stdout
sys.stderr = _original_stderr