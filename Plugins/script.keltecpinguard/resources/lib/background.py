# -*- coding: utf-8 -*-
import xbmcaddon
import xbmcgui

# Import the common settings
from resources.lib.settings import log
from resources.lib.settings import Settings

ADDON = xbmcaddon.Addon(id='script.keltecpinguard')
CWD = ADDON.getAddonInfo('path')


# Class to set the background while a pin is prompted for
class Background(xbmcgui.WindowXML):
    BACKGOUND_IMAGE_ID = 3004

    @staticmethod
    def createBackground():
        # Check to see if the background is enabled
        if not Settings.isDisplayBackground():
            return None
        return Background("keltecpinguard-background.xml", CWD)

    def onInit(self):
        xbmcgui.WindowXMLDialog.onInit(self)

        # Get the background image to be used
        bgImage = Settings.getBackgroundImage()

        if bgImage is not None:
            log("Background: Setting background image to %s" % bgImage)
            bgImageCtrl = self.getControl(Background.BACKGOUND_IMAGE_ID)
            bgImageCtrl.setImage(bgImage)
