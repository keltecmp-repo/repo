# -*- coding: utf-8 -*-
import traceback
import xbmc
import xbmcaddon

# Import the common settings
from resources.lib.settings import log
# Load the database interface
from resources.lib.database import KeltecPinGuardDB

ADDON = xbmcaddon.Addon(id='script.keltecpinguard')


#########################
# Main
#########################
if __name__ == '__main__':
    log("KeltecPinGuardCleanup: Cleanup called (version %s)" % ADDON.getAddonInfo('version'))

    try:
        # Start by removing the database
        extrasDb = KeltecPinGuardDB()
        extrasDb.cleanDatabase()
        del extrasDb
    except:
        log("KeltecPinGuardCleanup: %s" % traceback.format_exc(), xbmc.LOGERROR)
