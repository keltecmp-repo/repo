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
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return []

    def _save(self):
        tmp_file = self._path + '.tmp'
        try:
            with open(tmp_file, 'w', encoding='utf-8') as f:
                json.dump(self._items, f, ensure_ascii=False)
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
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return {}

    def _save(self):
        tmp_file = self._path + '.tmp'
        try:
            with open(tmp_file, 'w', encoding='utf-8') as f:
                json.dump(self._data, f, ensure_ascii=False)
            os.replace(tmp_file, self._path)
        except Exception:
            pass

    def _key(self, name, url):
        return f'{name}||{url}'

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
