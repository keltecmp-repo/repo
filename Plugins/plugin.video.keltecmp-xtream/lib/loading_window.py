import os, threading, time

import xbmc, xbmcaddon, xbmcgui


class _PlaybackMonitor(xbmc.Player):

    def __init__(self):
        super().__init__()
        self._av_ready = threading.Event()
        self._failed = threading.Event()
        self._cancelled = threading.Event()
        self._av_fired = False

    def onAVStarted(self):
        if not self._av_fired:
            self._av_fired = True
            self._av_ready.set()

    def onPlayBackError(self):
        if not self._av_fired:
            self._failed.set()

    def onPlayBackStopped(self):
        if not self._av_fired:
            self._failed.set()

    def onPlayBackFailed(self):
        if not self._av_fired:
            self._failed.set()

    def reset(self):
        self._av_ready.clear()
        self._failed.clear()
        self._cancelled.clear()
        self._av_fired = False

    def cancel(self):
        self._cancelled.set()

    def wait_until_playing(self, max_wait=45.0, confirm_secs=0.4):
        kodi_monitor = xbmc.Monitor()
        deadline = time.monotonic() + max_wait
        poll_interval = 0.1
        phase1_ok = False
        while time.monotonic() < deadline:
            if self._cancelled.is_set() or self._failed.is_set():
                return False
            if kodi_monitor.abortRequested():
                return False
            if self._av_ready.is_set():
                phase1_ok = True
                break
            try:
                if self.isPlaying() and self.getTime() > 0.0:
                    phase1_ok = True
                    break
            except Exception:
                pass
            kodi_monitor.waitForAbort(poll_interval)
        if not phase1_ok:
            return False
        check_interval = 0.1
        last_pos = -1.0
        confirm_deadline = min(time.monotonic() + confirm_secs, deadline)
        while time.monotonic() < confirm_deadline:
            if self._cancelled.is_set() or self._failed.is_set():
                return False
            if kodi_monitor.abortRequested():
                return False
            try:
                if not self.isPlaying():
                    return False
                pos = self.getTime()
            except Exception:
                kodi_monitor.waitForAbort(check_interval)
                continue
            if last_pos >= 0.0 and pos > last_pos:
                return True
            last_pos = pos
            kodi_monitor.waitForAbort(check_interval)
        try:
            return self._av_ready.is_set() and self.isPlaying() and self.getTime() >= 0.0
        except Exception:
            return self._av_ready.is_set()


class LoadingWindow(xbmcgui.WindowXMLDialog):

    PROGRESS_CONTROL = 100
    LABEL_CONTROL = 200

    def __new__(cls, xmlFile, scriptPath, defaultSkin, defaultSkinRes, **kwargs):
        instance = super(LoadingWindow, cls).__new__(cls, xmlFile, scriptPath, defaultSkin, defaultSkinRes)
        instance._search_func = kwargs.pop('search_func', None)
        instance._cancel_event = threading.Event()
        instance.result = None
        return instance

    def onInit(self):
        if self._search_func is None:
            xbmcgui.Window(10000).setProperty('loading.phase2', 'true')
            return
        self._update_ui(0, 'Iniciando busca...')
        t = threading.Thread(target=self._run_search, daemon=True)
        t.start()

    def _update_ui(self, pct, msg):
        try:
            ctrl = self.getControl(self.PROGRESS_CONTROL)
            ctrl.setPercent(min(100, max(0, pct)))
        except Exception:
            pass
        try:
            lbl = self.getControl(self.LABEL_CONTROL)
            lbl.setLabel(str(msg))
        except Exception:
            pass
        xbmcgui.Window(10000).setProperty('loading.progress', str(pct))

    def _progress_callback(self, pct, msg):
        if self._cancel_event.is_set():
            return
        self._update_ui(pct, msg)

    def _run_search(self):
        try:
            self.result = self._search_func(self._progress_callback, self._cancel_event)
        except Exception as e:
            import traceback
            xbmc.log(f'[LoadingWindow] search error: {e}', xbmc.LOGERROR)
            xbmc.log(traceback.format_exc(), xbmc.LOGERROR)
            self.result = []
        try:
            self.close()
        except Exception:
            pass

    def onAction(self, action):
        if action.getId() in (xbmcgui.ACTION_PREVIOUS_MENU, xbmcgui.ACTION_NAV_BACK):
            self._cancel_event.set()

    def is_cancelled(self):
        return self._cancel_event.is_set()

    def dismiss(self):
        self._cancel_event.set()
        try:
            self.close()
        except Exception:
            pass
        for prop in ('loading.phase', 'loading.phase2', 'loading.progress', 'loading.fanart'):
            try:
                xbmcgui.Window(10000).clearProperty(prop)
            except Exception:
                pass


class SourceSelectWindow(xbmcgui.WindowXMLDialog):

    LIST_CONTROL = 200

    def __new__(cls, xmlFile, scriptPath, defaultSkin, defaultSkinRes, **kwargs):
        instance = super(SourceSelectWindow, cls).__new__(cls, xmlFile, scriptPath, defaultSkin, defaultSkinRes)
        instance.labels = kwargs.pop('labels', [])
        instance.selected_index = -1
        return instance

    def onInit(self):
        try:
            ctrl = self.getControl(self.LIST_CONTROL)
            ctrl.reset()
            for label in self.labels:
                ctrl.addItem(xbmcgui.ListItem(label=label))
            self.setFocusId(self.LIST_CONTROL)
        except Exception:
            pass

    def onClick(self, control_id):
        if control_id == self.LIST_CONTROL:
            try:
                self.selected_index = self.getControl(self.LIST_CONTROL).getSelectedPosition()
            except Exception:
                self.selected_index = 0
            self.close()

    def onAction(self, action):
        if action.getId() in (
            xbmcgui.ACTION_PREVIOUS_MENU,
            xbmcgui.ACTION_NAV_BACK,
            xbmcgui.ACTION_STOP,
        ):
            self.selected_index = -1
            self.close()


class LoadingManager:

    def __init__(self):
        self._lock = threading.Lock()
        self._window = None
        self._generation = 0
        self._monitor = _PlaybackMonitor()
        self._busy_stop = threading.Event()

    def _run_busy_suppressor(self):
        while not self._busy_stop.wait(0.1):
            try:
                xbmc.executebuiltin('Dialog.Close(busydialog,true)')
                xbmc.executebuiltin('Dialog.Close(busydialognocancel,true)')
            except Exception:
                pass

    def _start_busy_suppressor(self):
        self._busy_stop.clear()
        threading.Thread(target=self._run_busy_suppressor, daemon=True).start()

    def _stop_busy_suppressor(self):
        self._busy_stop.set()

    def _addon_path(self):
        return xbmcaddon.Addon('plugin.video.keltecmp-xtream').getAddonInfo('path')

    def _default_fanart(self):
        return os.path.join(
            self._addon_path(), 'resources', 'skins', 'Default', 'media', 'fanart.jpg'
        )

    def _do_dismiss(self, window):
        self._stop_busy_suppressor()
        if window is not None:
            try:
                window.dismiss()
            except Exception:
                pass

    def show_search(self, title, all_servers, tmdb_browser, tmdb_type, fanart_path=None):
        addon_path = self._addon_path()
        fanart = fanart_path or self._default_fanart()
        xbmcgui.Window(10000).setProperty('loading.fanart', fanart)

        if not tmdb_browser:
            return []

        def search_func(progress_cb, cancel_ev):
            return tmdb_browser.find_in_all_servers(
                title=title,
                tmdb_type=tmdb_type,
                servers=all_servers,
                progress_cb=progress_cb,
                cancel_event=cancel_ev,
            )

        self._start_busy_suppressor()
        window = LoadingWindow(
            'DialogLoadingKelTec.xml', addon_path, 'Default', '1080i',
            search_func=search_func,
        )
        window.doModal()
        self._stop_busy_suppressor()

        for prop in ('loading.phase', 'loading.phase2', 'loading.progress', 'loading.fanart'):
            try:
                xbmcgui.Window(10000).clearProperty(prop)
            except Exception:
                pass

        return window.result if not window.is_cancelled() else None

    def show_search_start(self, fanart_path=None):
        addon_path = self._addon_path()
        fanart = fanart_path or self._default_fanart()
        xbmcgui.Window(10000).setProperty('loading.fanart', fanart)
        self._start_busy_suppressor()
        self._window = None

        def _run():
            window = LoadingWindow(
                'DialogLoadingKelTec.xml', addon_path, 'Default', '1080i',
            )
            with self._lock:
                self._window = window
                self._generation += 1
            window.doModal()

        threading.Thread(target=_run, daemon=True).start()

    def show_search_update(self, pct, msg):
        try:
            xbmcgui.Window(10000).setProperty('loading.progress', str(pct))
            with self._lock:
                if self._window is not None:
                    self._window._update_ui(pct, msg)
        except Exception:
            pass

    def show_search_end(self):
        for _ in range(20):
            with self._lock:
                if self._window is not None:
                    break
            time.sleep(0.1)
        self.force_close()

    def show_playback_start(self, fanart_path=None):
        addon_path = self._addon_path()
        fanart = fanart_path or self._default_fanart()
        xbmcgui.Window(10000).setProperty('loading.fanart', fanart)
        self._start_busy_suppressor()
        self._window = None

        def _run():
            window = LoadingWindow(
                'DialogLoadingKelTec.xml', addon_path, 'Default', '1080i',
            )
            with self._lock:
                self._window = window
                self._generation += 1
            window.doModal()

        threading.Thread(target=_run, daemon=True).start()

    def show_playback_end(self):
        for _ in range(20):
            with self._lock:
                if self._window is not None:
                    break
            time.sleep(0.1)
        self.force_close()

    def show_source_select(self, players, fanart_path=None):
        try:
            addon_path = self._addon_path()
            fanart = fanart_path or self._default_fanart()
            xbmcgui.Window(10000).setProperty('mdl.loading.fanart', fanart)
            xbmcgui.Window(10000).setProperty('loading.phase', '2')
            labels = [label for label, _ in players]
            dialog = SourceSelectWindow(
                'DialogSourceSelect.xml', addon_path, 'Default', '1080i',
                labels=labels
            )
            dialog.doModal()
            xbmcgui.Window(10000).clearProperty('mdl.loading.fanart')
            return dialog.selected_index
        except Exception:
            return -1

    def set_phase3(self):
        try:
            xbmcgui.Window(10000).setProperty('loading.phase', '3')
            xbmcgui.Window(10000).setProperty('loading.phase2', 'true')
        except Exception:
            pass

    set_phase2 = set_phase3

    def close(self, max_wait=20.0, confirm_secs=0.4):
        with self._lock:
            window = self._window
            self._window = None
            gen = self._generation
        if window is None:
            return
        self._monitor.wait_until_playing(max_wait=max_wait, confirm_secs=confirm_secs)
        with self._lock:
            if self._generation != gen:
                return
        self._do_dismiss(window)

    def force_close(self):
        with self._lock:
            window = self._window
            self._window = None
            self._generation += 1
        self._monitor.cancel()
        self._do_dismiss(window)


loading_manager = LoadingManager()
