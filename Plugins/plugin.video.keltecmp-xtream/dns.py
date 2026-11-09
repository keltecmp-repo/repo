# -*- coding: utf-8 -*-
"""
DNS customizado KelTec (v2 - resolucao paralela e tolerante a falhas)

Problemas do resolvedor antigo (que faziam servidores Xtream "sumirem" da busca):
  * consultava 6 DNS em SEQUENCIA (1,5 s cada): com UDP/53 bloqueado levava ~9 s
    por host e a busca estourava o timeout antes do fallback para o DNS do sistema;
  * aceitava IPs de bloqueio (0.0.0.0 / paginas de bloqueio do OpenDNS);
  * guardava so o 1o IP: se esse IP estivesse fora do ar nao havia segunda chance;
  * dependendo do host, so o DNS da operadora (ou so um publico) resolve certo.

Agora:
  * todos os DNS publicos + o DNS do sistema sao consultados EM PARALELO;
  * os IPs de todos os resolvedores sao combinados (o cliente HTTP tenta um a um);
  * fallback DNS-over-HTTPS (1.1.1.1 / 8.8.8.8) quando UDP/53 esta bloqueado;
  * IPs de bloqueio sao descartados; falhas recentes entram em cache negativo curto;
  * invalidate_host(host) limpa o cache de um host (usado nas tentativas de retry).
"""
import socket
import struct
import random
import logging
import json
import time
import os
import threading
import xbmc
import xbmcaddon
import xbmcvfs
ADDON_ = xbmcaddon.Addon()
TRANSLATE_ = xbmcvfs.translatePath
profile = TRANSLATE_(ADDON_.getAddonInfo('profile'))
if not os.path.exists(profile):
    os.makedirs(profile)
CACHE_FILE = os.path.join(profile, 'dns_cache.json')


_DNS_PATCH_STATE = {'installed': False, 'original_getaddrinfo': socket.getaddrinfo, 'instance': None}

_MAX_IPS = 6
_UDP_TIMEOUT = 1.6        # por servidor DNS
_PHASE1_BUDGET = 1.8      # UDP publico + DNS do sistema (em paralelo)
_PHASE2_BUDGET = 2.6      # DNS-over-HTTPS (so se a fase 1 nao trouxe nada)
_GRACE = 0.35             # apos o 1o IP valido, espera um pouco pelos demais
_NEG_TTL = 20             # cache negativo (s)

# IPs de "bloqueio" devolvidos por DNS com filtro (nao sao o servidor real)
_BAD_IPS = {'0.0.0.0', '255.255.255.255'}
_BAD_PREFIXES = ('127.', '0.', '146.112.61.', '146.112.62.')


def _ip_ok(ip):
    if not ip or ip in _BAD_IPS:
        return False
    for p in _BAD_PREFIXES:
        if ip.startswith(p):
            return False
    return True


class customdns:
    def __init__(self, cache_file=CACHE_FILE, cache_ttl=3600):
        self.dns_server = [
            '94.140.14.140', # adguard
            '94.140.14.141', # adguard
            '208.67.222.222',# OpenDNS
            '208.67.220.220',# OpenDNS
            '1.1.1.1',       # Cloudflare
            '8.8.8.8'        # Google DNS
        ]
        # DNS-over-HTTPS (usam IP no URL: nao dependem de DNS para conectar)
        self.doh_urls = [
            'https://1.1.1.1/dns-query?name={host}&type=A',
            'https://8.8.8.8/resolve?name={host}&type=A',
        ]
        self.original_getaddrinfo = _DNS_PATCH_STATE.get('original_getaddrinfo', socket.getaddrinfo)
        self.cache_file = cache_file
        self.cache_ttl = cache_ttl  # Tempo de expiração em segundos
        self._lock = threading.RLock()
        self._neg = {}              # host -> expira (cache negativo)
        self._sys_failed = {}       # host -> True se o DNS do sistema ja tentou e falhou
        self.cache = self._load_cache()
        self.debug_mode = False
        self.mode_logger = False

        # Override DNS only once per runtime
        if not _DNS_PATCH_STATE.get('installed'):
            _DNS_PATCH_STATE['original_getaddrinfo'] = socket.getaddrinfo
            socket.getaddrinfo = self._resolver
            _DNS_PATCH_STATE['installed'] = True
            _DNS_PATCH_STATE['instance'] = self
        elif _DNS_PATCH_STATE.get('instance') is None:
            _DNS_PATCH_STATE['instance'] = self

    # ------------------------------------------------------------------
    # Cache
    # ------------------------------------------------------------------
    def _load_cache(self):
        """Carrega o cache do arquivo JSON, se existir"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r') as f:
                    cache = json.load(f)
                current_time = time.time()
                out = {}
                for domain, data in cache.items():
                    if data.get('expires', 0) <= current_time:
                        continue
                    ips = [i for i in (data.get('ips') or [data.get('ip')]) if _ip_ok(i)]
                    if ips:
                        out[domain] = {'ip': ips[0], 'ips': ips, 'expires': data['expires']}
                return out
            return {}
        except Exception as e:
            logging.error("Erro ao carregar cache: {}".format(e))
            return {}

    def _save_cache(self):
        """Salva o cache no arquivo JSON (escrita atomica, thread-safe)"""
        try:
            with self._lock:
                tmp = self.cache_file + '.tmp'
                with open(tmp, 'w') as f:
                    json.dump(self.cache, f, indent=2)
                os.replace(tmp, self.cache_file)
        except Exception as e:
            logging.error("Erro ao salvar cache: {}".format(e))

    def invalidate(self, host):
        """Remove um host do cache (IP antigo/quebrado) e do cache negativo."""
        try:
            with self._lock:
                changed = self.cache.pop(host, None) is not None
                self._neg.pop(host, None)
            if changed:
                self._save_cache()
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Utilitarios
    # ------------------------------------------------------------------
    def is_valid_ipv4(self, ip):
        try:
            socket.inet_aton(ip)
            return True
        except (socket.error, TypeError):
            return False

    def is_valid_ipv6(self, ip):
        try:
            if hasattr(socket, 'inet_pton'):
                socket.inet_pton(socket.AF_INET6, ip)
                return True
            return False
        except (socket.error, TypeError):
            return False

    def _build_dns_query(self, domain, transaction_id=None):
        if transaction_id is None:
            transaction_id = random.randint(0, 65535)
        flags = 0x0100
        questions = 1
        header = struct.pack('>HHHHHH', transaction_id, flags, questions, 0, 0, 0)

        try:
            labels = domain.encode('idna').split(b'.')
        except Exception:
            labels = domain.encode('utf-8', 'ignore').split(b'.')
        qname = b''.join(bytes([len(p)]) + p for p in labels if p) + b'\x00'

        qtype = 1  # A record
        qclass = 1  # IN
        question = qname + struct.pack('>HH', qtype, qclass)
        return header + question

    @staticmethod
    def _skip_name(data, offset):
        """Avanca ate depois de um nome DNS (labels e/ou ponteiro de compressao)."""
        n = len(data)
        while offset < n:
            ln = data[offset]
            if ln == 0:
                return offset + 1
            if ln & 0xC0 == 0xC0:
                return offset + 2
            offset += ln + 1
        return offset

    def _parse_dns_response(self, data, transaction_id=None):
        """Retorna a lista de IPs (registros A) validos da resposta."""
        ips = []
        try:
            if len(data) < 12:
                return ips
            tid, flags, qd, an = struct.unpack('>HHHH', data[:8])
            if transaction_id is not None and tid != transaction_id:
                return ips
            if (flags & 0x000F) != 0:        # rcode != NOERROR (NXDOMAIN, SERVFAIL...)
                return ips
            offset = 12
            for _ in range(qd):
                offset = self._skip_name(data, offset) + 4
            for _ in range(an):
                offset = self._skip_name(data, offset)
                rtype, rclass, ttl, rdlength = struct.unpack('>HHIH', data[offset:offset + 10])
                offset += 10
                if rtype == 1 and rdlength == 4:
                    ip = '.'.join(map(str, struct.unpack('>BBBB', data[offset:offset + 4])))
                    if _ip_ok(ip) and ip not in ips:
                        ips.append(ip)
                offset += rdlength
        except Exception:
            pass
        return ips

    # ------------------------------------------------------------------
    # Consultas individuais
    # ------------------------------------------------------------------
    def _query_udp(self, domain, dns_custom):
        """Consulta um servidor DNS por UDP. Devolve lista de IPs."""
        s = None
        try:
            tid = random.randint(0, 65535)
            query = self._build_dns_query(domain, tid)
            if self.is_valid_ipv6(dns_custom):
                s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
                addr = (dns_custom, 53, 0, 0)
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (dns_custom, 53)
            s.settimeout(_UDP_TIMEOUT)
            s.sendto(query, addr)
            data, _ = s.recvfrom(1024)
            return self._parse_dns_response(data, tid)
        except Exception as e:
            if self.mode_logger:
                logging.error("Erro ao resolver {} com {}: {}".format(domain, dns_custom, e))
            return []
        finally:
            try:
                if s:
                    s.close()
            except Exception:
                pass

    def _query_doh(self, domain, url_tpl):
        """DNS-over-HTTPS (JSON). Funciona mesmo com UDP/53 bloqueado."""
        try:
            import urllib.request
            req = urllib.request.Request(url_tpl.format(host=domain),
                                         headers={'accept': 'application/dns-json',
                                                  'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=2.4) as r:
                j = json.loads(r.read().decode('utf-8'))
            ips = []
            for a in (j.get('Answer') or []):
                if a.get('type') == 1:
                    ip = str(a.get('data') or '').strip()
                    if self.is_valid_ipv4(ip) and _ip_ok(ip) and ip not in ips:
                        ips.append(ip)
            return ips
        except Exception as e:
            if self.mode_logger:
                logging.error("DoH falhou {}: {}".format(domain, e))
            return []

    def _query_system(self, domain):
        """DNS do sistema/operadora (resolve nomes que os publicos nao conhecem)."""
        try:
            infos = self.original_getaddrinfo(domain, None, socket.AF_INET, socket.SOCK_STREAM)
            ips = []
            for info in infos:
                ip = info[4][0]
                if _ip_ok(ip) and ip not in ips:
                    ips.append(ip)
            return ips
        except Exception:
            return []

    # ------------------------------------------------------------------
    # Resolucao paralela
    # ------------------------------------------------------------------
    def resolve_all(self, domain):
        """Devolve lista de IPs (ate _MAX_IPS) combinando todos os resolvedores."""
        domain = (domain or '').strip('.')
        now = time.time()
        with self._lock:
            ent = self.cache.get(domain)
            if ent:
                if ent['expires'] > now:
                    return list(ent.get('ips') or [ent['ip']])
                self.cache.pop(domain, None)
            neg = self._neg.get(domain)
            if neg and neg > now:
                return []

        pub = []                   # IPs dos DNS publicos (ordem de chegada)
        sysips = []                # IPs do DNS do sistema/operadora
        lock = threading.Lock()
        first_evt = threading.Event()
        pending = [0]
        sys_done = [False]

        def _add(ips, is_sys):
            if not ips:
                return
            with lock:
                dst = sysips if is_sys else pub
                for ip in ips:
                    if ip not in dst:
                        dst.append(ip)
                first_evt.set()

        def _worker(fn, is_sys, *args):
            try:
                _add(fn(*args), is_sys)
            finally:
                with lock:
                    pending[0] -= 1
                    if is_sys:
                        sys_done[0] = True

        def _launch(fn, is_sys, *args):
            with lock:
                pending[0] += 1
            threading.Thread(target=_worker, args=(fn, is_sys) + args, daemon=True).start()

        # Fase 1: DNS publicos (UDP) + DNS do sistema, todos ao mesmo tempo
        for srv in self.dns_server:
            _launch(self._query_udp, False, domain, srv)
        _launch(self._query_system, True, domain)

        def _wait(budget):
            end = time.time() + budget
            while time.time() < end:
                with lock:
                    nothing_left = pending[0] <= 0
                if nothing_left:
                    return
                if first_evt.is_set():
                    # ja temos IP: janela para juntar os demais resolvedores. Se so o
                    # DNS do sistema respondeu, espera mais pelos publicos (preferidos:
                    # a operadora pode devolver IP de pagina de bloqueio).
                    with lock:
                        only_sys = (not pub)
                    t_end = min(end, time.time() + (0.9 if only_sys else _GRACE))
                    while time.time() < t_end:
                        with lock:
                            if pending[0] <= 0:
                                return
                        time.sleep(0.03)
                    return
                time.sleep(0.03)

        _wait(_PHASE1_BUDGET)

        # Fase 2: DoH (UDP/53 bloqueado e sistema sem resposta)
        if not first_evt.is_set():
            for u in self.doh_urls:
                _launch(self._query_doh, False, domain, u)
            _wait(_PHASE2_BUDGET)

        with lock:
            ips = (pub + [i for i in sysips if i not in pub])[:_MAX_IPS]
            self._sys_failed[domain] = bool(sys_done[0] and not sysips)

        with self._lock:
            if ips:
                self.cache[domain] = {'ip': ips[0], 'ips': ips,
                                      'expires': time.time() + self.cache_ttl}
                self._neg.pop(domain, None)
            else:
                self._neg[domain] = time.time() + _NEG_TTL
        if ips:
            self._save_cache()
            if self.mode_logger:
                logging.debug("Resolved {} to {}".format(domain, ips))
        return ips

    def resolve(self, domain, dns_custom=None):
        """Compatibilidade: devolve um unico IP."""
        ips = self.resolve_all(domain)
        return ips[0] if ips else None

    def _resolver(self, host, port, *args, **kwargs):
        try:
            if host is None or isinstance(host, bytes):
                return self.original_getaddrinfo(host, port, *args, **kwargs)
            if self.is_valid_ipv4(host) or self.is_valid_ipv6(host):
                if self.mode_logger:
                    logging.debug("Bypass: {} já é IP".format(host))
                return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (host, port))]
            # localhost / nomes sem ponto (rede local) -> resolvedor do sistema
            if '.' not in host.strip('.'):
                return self.original_getaddrinfo(host, port, *args, **kwargs)

            ips = self.resolve_all(host)
            if ips:
                return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (ip, port)) for ip in ips]

            if self._sys_failed.get(host.strip('.')):
                # sistema ja tentou e falhou; nao repete (evita esperar duas vezes)
                raise socket.gaierror(socket.EAI_NONAME, 'Name or service not known')
            if self.mode_logger:
                logging.warning("Falha ao resolver {}, fallback para getaddrinfo".format(host))
        except socket.gaierror:
            raise
        except Exception as e:
            if self.mode_logger:
                logging.error("Erro no resolver para {}: {}".format(host, e))

        return self.original_getaddrinfo(host, port, *args, **kwargs)


def invalidate_host(host):
    """Limpa o cache DNS de um host (ex.: apos falha de conexao) para forcar nova resolucao."""
    try:
        inst = _DNS_PATCH_STATE.get('instance')
        if inst and host:
            inst.invalidate(str(host).strip('.'))
    except Exception:
        pass
