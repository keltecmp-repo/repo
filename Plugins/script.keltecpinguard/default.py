# -*- coding: utf-8 -*-
import xbmcaddon
import xbmc
import xbmcgui

# Import the common settings
from resources.lib.settings import log

ADDON = xbmcaddon.Addon(id='script.keltecpinguard')


#########################
# Main
#########################
if __name__ == '__main__':
    log('script version %s started' % ADDON.getAddonInfo('version'))

    # Close any open dialogs
    xbmc.executebuiltin("Dialog.Close(all, true)", True)

    # Check if KeltecPinGuard is running for a restricted user, if that is the case
    # when the addon is run as a script we actually just display that users status
    if xbmcgui.Window(10000).getProperty("KeltecPinGuard_RestrictedUser") not in ["", None]:
        xbmcgui.Window(10000).setProperty("KeltecPinGuard_DisplayStatus", "true")
    else:
        # This provides a cut-through so that the KeltecPinGuard appears in the program
        # area, we could have make the "xbmc.python.pluginsource" extension point
        # also provide "executable", but that section does not allow for us to
        # put flags in the right hand of the display
        log("KeltecPinGuard: Running as Addon/Plugin")
        xbmc.executebuiltin("RunAddon(script.keltecpinguard)")
