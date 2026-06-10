# -*- coding: utf-8 -*-
# KeltecPinGuard - NumberPad module
# Developed for Keltec Media Play
# Based on KeltecPinGuard by Keltec Media Play, updated for Kodi 19+ / Python 3

import xbmcaddon
import xbmcgui

from resources.lib.settings import log
from resources.lib.settings import Settings

ADDON = xbmcaddon.Addon(id='script.keltecpinguard')
CWD = ADDON.getAddonInfo('path')


class NumberPad(xbmcgui.WindowXMLDialog):
    BUTTON_BACKSPACE = 23
    BUTTON_DONE = 21
    BUTTON_PREVIOUS = 20
    BUTTON_NEXT = 22

    def __init__(self, strXMLname, strFallbackPath, titleLangId=32103):
        self.code = ""
        self.stars = ""
        self.titleLangId = titleLangId
        self.cancelled = False  # Track if user pressed Back/Cancel

    @staticmethod
    def createNumberPad(titleLangId=32103):
        return NumberPad("DialogNumeric.xml", CWD, titleLangId=titleLangId)

    def wasCancelled(self):
        """Returns True if user dismissed the dialog without entering a PIN"""
        return self.cancelled

    def getPin(self):
        if Settings.getPinLength() < len(self.code):
            return ""
        return self.code

    def onInit(self):
        try:
            self.getControl(NumberPad.BUTTON_PREVIOUS).setEnabled(False)
            self.getControl(NumberPad.BUTTON_NEXT).setEnabled(False)
        except Exception:
            log("NumberPad: Failed to disable next and previous buttons")

        for i in range(0, 10):
            try:
                self.getControl(i + 10).setLabel(str(i))
            except Exception:
                log("NumberPad: Failed to update text on numeric button %d" % i)

        try:
            self.getControl(1).setLabel(ADDON.getLocalizedString(self.titleLangId))
        except Exception:
            log("NumberPad: Failed to set title")

        if Settings.isDirectionKeysAsPin():
            try:
                for i in range(0, 10):
                    self.getControl(i + 10).setEnabled(False)
                self.getControl(NumberPad.BUTTON_BACKSPACE).setEnabled(False)
            except Exception:
                log("NumberPad: Failed to disable keys on keypad")

        xbmcgui.WindowXMLDialog.onInit(self)

    def onAction(self, action):
        action_id = action.getId()
        ACTION_PREVIOUS_MENU = 10
        ACTION_NAV_BACK = 92
        ACTION_BACKSPACE = 110

        if action_id in (ACTION_PREVIOUS_MENU, ACTION_NAV_BACK):
            log("NumberPad: User cancelled (Back key)")
            self.cancelled = True
            self.close()
        elif action_id == ACTION_BACKSPACE:
            self._removeLastCharacter()
        elif 57 < action_id < 68:
            self._numberEntered(action_id - 58)
        elif 139 < action_id < 150:
            self._numberEntered(action_id - 140)
        elif Settings.isDirectionKeysAsPin() and 0 < action_id < 5:
            mapping = {1: 4, 2: 6, 3: 2, 4: 8}
            self._numberEntered(mapping[action_id])
        else:
            log("NumberPad: Unknown key pressed %s" % str(action_id))

    def _numberEntered(self, numValue):
        log("NumberPad: Entered number %d" % numValue)
        self.code += str(numValue)
        self.stars += "*"
        self.getControl(4).setLabel(self.stars)
        if len(self.code) == Settings.getPinLength():
            self.close()

    def _removeLastCharacter(self):
        log("NumberPad: Delete last character request")
        if len(self.code) > 0:
            self.code = self.code[:-1]
            self.stars = self.stars[:-1]
            self.getControl(4).setLabel(self.stars)

    def onClick(self, controlID):
        if 9 < controlID < 20:
            self._numberEntered(controlID - 10)
        elif controlID == NumberPad.BUTTON_DONE:
            self.close()
        elif controlID == NumberPad.BUTTON_BACKSPACE:
            self._removeLastCharacter()
