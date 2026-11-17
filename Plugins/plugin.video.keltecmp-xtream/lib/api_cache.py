# -*- coding: utf-8 -*-
"""Cache persistente para a API do servidor Xtream (v2 - leve para pouca RAM).

O que mudou em relacao a versao anterior
----------------------------------------
* Antes: UM unico api_cache.json com TODAS as respostas, carregado inteiro na
  RAM e REGRAVADO (json.dumps + ofuscacao byte a byte em Python puro) a cada
  `set()`. Com catalogos de dezenas de milhares de itens isso custava centenas
  de MB de RAM e varios segundos de CPU a cada consulta.
* Agora: um arquivo comprimido (zlib) por chave, escrito de forma atomica e
  lido sob demanda. Nada fica na RAM aqui, e um `set()` grava so a propria
  resposta. O diretorio e mantido dentro de um limite de arquivos/bytes.

A interface publica (get / set / invalidate / size / clear_expired) e igual.

Tambem inclui `BoundedCache`, um dicionario com limite de entradas e de itens
totais (LRU), para substituir caches em memoria que nunca eram esvaziados.
"""

import os
import json
import time
import zlib
import hashlib
import threading
from collections import OrderedDict
from typing import Optional

try:
    import xbmc
    _KODI = True
except ImportError:
    _KODI = False

_MAGIC = b'KTA2'
_XOR_KEY = bytes.fromhex('9d41c7e2b86a35f01c7bd4a9e3582f66')   # ofuscacao leve do cabecalho
_MAX_FILES = 48
_MAX_BYTES = 40 * 1024 * 1024


def _log(msg: str) -> None:
    if _KODI:
        xbmc.log(f'[ApiCache] {msg}', xbmc.LOGDEBUG)
    else:
        print(f'[ApiCache] {msg}')


def _scramble_head(data: bytes, n: int = 48) -> bytes:
    """XOR nos primeiros bytes: o arquivo deixa de ser um zlib legivel por
    qualquer ferramenta, sem custo de CPU (nao percorre o arquivo todo)."""
    head = bytes(b ^ _XOR_KEY[i % len(_XOR_KEY)] for i, b in enumerate(data[:n]))
    return head + data[n:]


class ApiCache:
    """Cache JSON persistente em disco com TTL (um arquivo por chave).

    Uso:
        cache = ApiCache(profile_dir, ttl=300)
        data = cache.get('live_categories')
        if data is None:
            data = fetch_from_api()
            cache.set('live_categories', data)
    """

    def __init__(self, profile_dir: str, filename: str = 'api_cache.json', ttl: int = 300):
        self._dir = os.path.join(profile_dir, 'api_cache')
        self._legacy = os.path.join(profile_dir, filename)
        self._ttl = ttl
        self._lock = threading.Lock()
        self._ready = False

    # -- infraestrutura ----------------------------------------------------
    def _ensure(self) -> bool:
        if self._ready:
            return True
        try:
            os.makedirs(self._dir, exist_ok=True)
        except Exception as e:
            _log(f'sem diretorio de cache: {e}')
            return False
        # remove o api_cache.json antigo (podia ter dezenas de MB)
        for p in (self._legacy, self._legacy + '.tmp'):
            try:
                if os.path.exists(p):
                    os.remove(p)
            except Exception:
                pass
        self._ready = True
        return True

    def _path(self, key: str) -> str:
        h = hashlib.md5(str(key).encode('utf-8')).hexdigest()
        return os.path.join(self._dir, h + '.kta')

    # -- API publica -------------------------------------------------------
    def get(self, key: str) -> object:
        if not self._ensure():
            return None
        p = self._path(key)
        try:
            st = os.stat(p)
        except OSError:
            return None
        if time.time() - st.st_mtime > self._ttl:
            return None
        try:
            with open(p, 'rb') as f:
                blob = f.read()
            if blob[:4] != _MAGIC:
                return None
            raw = zlib.decompress(_scramble_head(blob[4:]))
            return json.loads(raw.decode('utf-8'))
        except Exception as e:
            _log(f'cache ilegivel ({e}); descartado')
            try:
                os.remove(p)
            except Exception:
                pass
            return None

    def set(self, key: str, value: object) -> None:
        if not self._ensure():
            return
        p = self._path(key)
        tmp = '%s.%d.%d.tmp' % (p, os.getpid(), threading.get_ident())
        try:
            raw = json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
            blob = _MAGIC + _scramble_head(zlib.compress(raw, 1))   # nivel 1: rapido em CPU fraca
            del raw
            with self._lock:
                with open(tmp, 'wb') as f:
                    f.write(blob)
                os.replace(tmp, p)
            self._trim()
        except Exception as e:
            _log(f'Erro ao salvar cache: {e}')
            try:
                if os.path.exists(tmp):
                    os.remove(tmp)
            except Exception:
                pass

    def _files(self):
        out = []
        try:
            for fn in os.listdir(self._dir):
                if fn.endswith('.kta'):
                    fp = os.path.join(self._dir, fn)
                    st = os.stat(fp)
                    out.append((st.st_mtime, st.st_size, fp))
        except Exception:
            pass
        return out

    def _trim(self) -> None:
        files = self._files()
        total = sum(s for _, s, _ in files)
        if len(files) <= _MAX_FILES and total <= _MAX_BYTES:
            return
        files.sort()
        for mtime, size, fp in files:
            if len(files) <= _MAX_FILES and total <= _MAX_BYTES:
                break
            try:
                os.remove(fp)
                total -= size
                files = [f for f in files if f[2] != fp]
            except Exception:
                pass

    def invalidate(self, key: Optional[str] = None) -> None:
        if not self._ensure():
            return
        with self._lock:
            if key:
                try:
                    os.remove(self._path(key))
                except Exception:
                    pass
            else:
                for _, _, fp in self._files():
                    try:
                        os.remove(fp)
                    except Exception:
                        pass

    @property
    def size(self) -> int:
        if not self._ensure():
            return 0
        return len(self._files())

    def clear_expired(self) -> int:
        if not self._ensure():
            return 0
        now = time.time()
        n = 0
        for mtime, _, fp in self._files():
            if now - mtime > self._ttl:
                try:
                    os.remove(fp)
                    n += 1
                except Exception:
                    pass
        return n


class BoundedCache:
    """Dicionario LRU com limite de entradas e de itens totais.

    Compativel com o uso de `_JSON_CACHE` (get / [] / clear / pop / in / len).
    As funcoes `max_entries` e `max_items` sao reavaliadas a cada insercao,
    entao o limite acompanha o perfil de RAM (ver accel_engine).
    """

    def __init__(self, max_entries=8, max_items=120000):
        self._d = OrderedDict()
        self._sizes = {}
        self._lock = threading.RLock()
        self._max_entries = max_entries
        self._max_items = max_items

    @staticmethod
    def _val(v, fn):
        try:
            return int(fn() if callable(fn) else fn)
        except Exception:
            return 8

    @staticmethod
    def _weight(entry) -> int:
        data = entry.get('data') if isinstance(entry, dict) else entry
        try:
            return len(data) if isinstance(data, (list, dict)) else 1
        except Exception:
            return 1

    def get(self, key, default=None):
        with self._lock:
            if key in self._d:
                self._d.move_to_end(key)
                return self._d[key]
        return default

    def __getitem__(self, key):
        with self._lock:
            self._d.move_to_end(key)
            return self._d[key]

    def __setitem__(self, key, value):
        with self._lock:
            self._d[key] = value
            self._d.move_to_end(key)
            self._sizes[key] = self._weight(value)
            self._evict()

    def _evict(self):
        max_e = max(1, self._val(None, self._max_entries))
        max_i = max(1000, self._val(None, self._max_items))
        while len(self._d) > 1 and (len(self._d) > max_e or sum(self._sizes.values()) > max_i):
            k, _ = self._d.popitem(last=False)
            self._sizes.pop(k, None)

    def pop(self, key, *default):
        with self._lock:
            self._sizes.pop(key, None)
            return self._d.pop(key, *default)

    def clear(self):
        with self._lock:
            self._d.clear()
            self._sizes.clear()

    def __contains__(self, key):
        return key in self._d

    def __len__(self):
        return len(self._d)

    def keys(self):
        with self._lock:
            return list(self._d.keys())
