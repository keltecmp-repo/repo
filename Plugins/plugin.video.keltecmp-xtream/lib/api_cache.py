# -*- coding: utf-8 -*-
"""Cache persistente para API do servidor Xtream.

Armazena respostas JSON em disco com TTL configurável.
Usa escrita atômica (.tmp + rename) para evitar corrupção.
Thread-safe via threading.Lock.
"""

import os
import json
import time
import threading
from typing import Optional

try:
    import xbmc
    _KODI = True
except ImportError:
    _KODI = False

from lib.crypto_util import obfuscate_blob, deobfuscate_blob


def _log(msg: str) -> None:
    if _KODI:
        xbmc.log(f'[ApiCache] {msg}', xbmc.LOGDEBUG)
    else:
        print(f'[ApiCache] {msg}')


class ApiCache:
    """Cache JSON persistente em disco com TTL.

    Uso:
        cache = ApiCache(profile_dir, ttl=300)
        data = cache.get('live_categories')
        if data is None:
            data = fetch_from_api()
            cache.set('live_categories', data)
    """

    def __init__(self, profile_dir: str, filename: str = 'api_cache.json', ttl: int = 300):
        self._path = os.path.join(profile_dir, filename)
        self._ttl = ttl
        self._lock = threading.Lock()
        self._data: Optional[dict] = None
        self._loaded = False

    def _load(self) -> dict:
        if self._loaded and self._data is not None:
            return self._data
        with self._lock:
            if self._loaded and self._data is not None:
                return self._data
            try:
                if os.path.exists(self._path):
                    with open(self._path, 'r', encoding='utf-8') as f:
                        _content = f.read()
                    if _content.startswith('{'):
                        self._data = json.loads(_content)
                    else:
                        _raw = deobfuscate_blob(_content)
                        self._data = json.loads(_raw) if _raw else {}
                else:
                    self._data = {}
            except Exception as e:
                _log(f'Erro ao carregar cache: {e}')
                self._data = {}
            self._loaded = True
        return self._data

    def get(self, key: str) -> object:
        data = self._load()
        entry = data.get(key)
        if not entry:
            return None
        if time.time() - entry.get('ts', 0) > self._ttl:
            return None
        return entry.get('data')

    def set(self, key: str, value: object) -> None:
        data = self._load()
        with self._lock:
            data[key] = {'ts': time.time(), 'data': value}
            self._flush()

    def _flush(self) -> None:
        try:
            tmp = self._path + '.tmp'
            _protected = obfuscate_blob(json.dumps(self._data, ensure_ascii=False))
            with open(tmp, 'w', encoding='utf-8') as f:
                f.write(_protected)
            os.replace(tmp, self._path)
        except Exception as e:
            _log(f'Erro ao salvar cache: {e}')

    def invalidate(self, key: Optional[str] = None) -> None:
        data = self._load()
        with self._lock:
            if key:
                data.pop(key, None)
            else:
                data.clear()
            self._flush()

    @property
    def size(self) -> int:
        data = self._load()
        return len(data)

    def clear_expired(self) -> int:
        data = self._load()
        now = time.time()
        expired = [k for k, v in data.items() if now - v.get('ts', 0) > self._ttl]
        if expired:
            with self._lock:
                for k in expired:
                    data.pop(k, None)
                self._flush()
        return len(expired)
