# -*- coding: utf-8 -*-
"""
Módulo de histórico de reprodução para Xtream Universal.
Rastreia os últimos itens assistidos por tipo (live, movie, series).
Adaptado e integrado ao Xtream Universal.
"""
import json
import os
import time

import xbmcvfs
import xbmcaddon

from lib.crypto_util import obfuscate, deobfuscate, obfuscate_dict, deobfuscate_dict, hash_key

MAX_HISTORY = 50  # Máximo de itens no histórico


class WatchHistory:
    """Gerencia o histórico de reprodução dos últimos vistos."""

    def __init__(self, addon=None):
        if addon is None:
            addon = xbmcaddon.Addon()
        profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
        if not os.path.exists(profile):
            os.makedirs(profile)
        self._path = os.path.join(profile, 'watch_history.json')
        self._items = self._load()

    def _load(self):
        try:
            with open(self._path, 'r', encoding='utf-8') as f:
                _raw = json.load(f)
            if isinstance(_raw, list):
                for item in _raw:
                    if 'url' in item:
                        item['url'] = deobfuscate(item['url'])
                    if 'icon' in item:
                        item['icon'] = deobfuscate(item['icon'])
            return _raw
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return []

    def _save(self):
        _to_save = []
        for item in self._items:
            _copy = dict(item)
            if 'url' in _copy:
                _copy['url'] = obfuscate(_copy['url'])
            if 'icon' in _copy:
                _copy['icon'] = obfuscate(_copy['icon'])
            _to_save.append(_copy)
        tmp_file = self._path + '.tmp'
        try:
            with open(tmp_file, 'w', encoding='utf-8') as f:
                json.dump(_to_save, f, ensure_ascii=False)
                try:
                    f.flush()
                    os.fsync(f.fileno())
                except OSError:
                    pass
            os.replace(tmp_file, self._path)
        except Exception:
            pass

    def add(self, name, url, icon='', stype='live', extra=None):
        """
        Adiciona item ao histórico. Deduplica por name+stype, mais recente primeiro.
        stype: 'live', 'movie', 'series'
        """
        entry = {
            'name': name,
            'url': url,
            'icon': icon,
            'stype': stype,
            'timestamp': time.time(),
        }
        if extra and isinstance(extra, dict):
            entry.update(extra)

        # Remove entrada existente com mesmo nome+tipo
        self._items = [i for i in self._items
                       if not (i.get('name') == name and i.get('stype') == stype)]

        # Insere no início
        self._items.insert(0, entry)

        # Limita ao máximo
        self._items = self._items[:MAX_HISTORY]
        self._save()

    def get_all(self, stype=None):
        """Retorna histórico, opcionalmente filtrado por tipo."""
        if stype:
            return [i for i in self._items if i.get('stype') == stype]
        return list(self._items)

    def clear(self):
        """Limpa todo o histórico."""
        self._items = []
        self._save()

    def clear_by_type(self, stype):
        """Limpa histórico de um tipo específico."""
        self._items = [i for i in self._items if i.get('stype') != stype]
        self._save()

    def remove(self, name, stype=None):
        """Remove item específico do histórico."""
        if stype:
            self._items = [i for i in self._items
                           if not (i.get('name') == name and i.get('stype') == stype)]
        else:
            self._items = [i for i in self._items if i.get('name') != name]
        self._save()

    def count(self, stype=None):
        """Conta itens no histórico."""
        if stype:
            return len([i for i in self._items if i.get('stype') == stype])
        return len(self._items)


class ResumePoints:
    """Rastreia pontos de retomada para filmes/séries."""

    def __init__(self, addon=None):
        if addon is None:
            addon = xbmcaddon.Addon()
        profile = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
        if not os.path.exists(profile):
            os.makedirs(profile)
        self._path = os.path.join(profile, 'resume_points.json')
        self._data = self._load()

    def _load(self):
        try:
            with open(self._path, 'r', encoding='utf-8') as f:
                _raw = json.load(f)
            _result = {}
            for _k, _v in _raw.items():
                if isinstance(_v, dict):
                    _v = deobfuscate_dict(_v)
                _result[_k] = _v
            return _result
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return {}

    def _save(self):
        _to_save = {}
        for _k, _v in self._data.items():
            if isinstance(_v, dict):
                _to_save[_k] = obfuscate_dict(_v)
            else:
                _to_save[_k] = _v
        tmp_file = self._path + '.tmp'
        try:
            with open(tmp_file, 'w', encoding='utf-8') as f:
                json.dump(_to_save, f, ensure_ascii=False)
            os.replace(tmp_file, self._path)
        except Exception:
            pass

    def _key(self, name, url):
        return hash_key(name, url)

    def save_position(self, name, url, position, duration):
        """Salva posição de reprodução. Só salva se >60s e não perto do fim."""
        if position < 60 or duration < 120:
            return
        if position > duration * 0.93:
            # Perto do fim — marca como assistido, remove ponto de retomada
            self._data.pop(self._key(name, url), None)
            self._save()
            return
        self._data[self._key(name, url)] = {
            'name': name,
            'url': url,
            'position': position,
            'duration': duration,
            'timestamp': time.time(),
        }
        self._save()

    def get_position(self, name, url):
        """Retorna posição salva em segundos, ou 0 se não houver."""
        entry = self._data.get(self._key(name, url))
        if entry:
            return entry.get('position', 0)
        return 0

    def remove(self, name, url):
        """Remove ponto de retomada."""
        self._data.pop(self._key(name, url), None)
        self._save()

    def clear(self):
        """Limpa todos os pontos de retomada."""
        self._data = {}
        self._save()
