# -*- coding: utf-8 -*-
# KeltecPinGuard - Settings module
# Updated for Python 3 / Kodi 19+ (Matrix, Nexus, Omega)

import os
import hashlib
import time
from datetime import date
import xbmc
import xbmcaddon
import xbmcvfs

ADDON = xbmcaddon.Addon(id='script.keltecpinguard')
ADDON_ID = ADDON.getAddonInfo('id')  # script.keltecpinguard


# Common logging module
def log(txt, loglevel=xbmc.LOGDEBUG):
    if (ADDON.getSetting("logEnabled") == "true") or (loglevel != xbmc.LOGDEBUG):
        if not isinstance(txt, str):
            txt = str(txt)
        message = '%s: %s' % (ADDON_ID, txt)
        xbmc.log(msg=message, level=loglevel)


# Path join helper (Python 3 strings are always unicode)
def os_path_join(dir_path, file_name):
    return os.path.join(dir_path, file_name)


##############################
# Stores Various Settings
##############################
class Settings():
    INVALID_PIN_NOTIFICATION_POPUP = 0
    INVALID_PIN_NOTIFICATION_DIALOG = 1
    INVALID_PIN_NOTIFICATION_NONE = 2

    flags = [{'lang': 32301, 'icon': 'UK/UK-flag.png'},
             {'lang': 32302, 'icon': 'USA/USA-flag.png'},
             {'lang': 32303, 'icon': 'Germany/Germany-flag.png'},
             {'lang': 32304, 'icon': 'Ireland/Ireland-flag.png'},
             {'lang': 32305, 'icon': 'Netherlands/Netherlands-flag.png'},
             {'lang': 32306, 'icon': 'Australia/Australia-flag.png'},
             {'lang': 32307, 'icon': 'Brazil/Brazil-flag.png'},
             {'lang': 32308, 'icon': 'Hungary/Hungary-flag.png'},
             {'lang': 32309, 'icon': 'Denmark/Denmark-flag.png'},
             {'lang': 32310, 'icon': 'Norway/Norway-flag.png'},
             {'lang': 32311, 'icon': 'Sweden/Sweden-flag.png'},
             {'lang': 32312, 'icon': 'Finland/Finland-flag.png'},
             {'lang': 32313, 'icon': 'Canada/Canada-flag.png'},
             {'lang': 32315, 'icon': 'France/France-flag.png'},
             {'lang': 32316, 'icon': 'Italy/Italy-flag.png'},
             {'lang': 32317, 'icon': 'Spain/Spain-flag.png'},
             {'lang': 32318, 'icon': 'SouthKorea/SouthKorea-flag.png'},
             {'lang': 32319, 'icon': 'India/India-flag.png'},
             {'lang': 32320, 'icon': 'Portugal/Portugal-flag.png'}]

    movieCassificationsNames = [
        {'id': 1,  'name': '%s - U',    'lang': 32301, 'match': 'U',    'icon': 'UK/UK-U.png'},
        {'id': 2,  'name': '%s - PG',   'lang': 32301, 'match': 'PG',   'icon': 'UK/UK-PG.png'},
        {'id': 3,  'name': '%s - 12A',  'lang': 32301, 'match': '12A',  'icon': 'UK/UK-12A.png'},
        {'id': 4,  'name': '%s - 12',   'lang': 32301, 'match': '12',   'icon': 'UK/UK-12.png'},
        {'id': 5,  'name': '%s - 15',   'lang': 32301, 'match': '15',   'icon': 'UK/UK-15.png'},
        {'id': 6,  'name': '%s - 18',   'lang': 32301, 'match': '18',   'icon': 'UK/UK-18.png'},
        {'id': 7,  'name': '%s - R18',  'lang': 32301, 'match': 'R18',  'icon': 'UK/UK-R18.png'},
        {'id': 8,  'name': '%s - G',    'lang': 32302, 'match': 'G',    'icon': 'USA/USA-G.png'},
        {'id': 9,  'name': '%s - PG',   'lang': 32302, 'match': 'PG',   'icon': 'USA/USA-PG.png'},
        {'id': 10, 'name': '%s - PG-13','lang': 32302, 'match': 'PG-13','icon': 'USA/USA-PG-13.png'},
        {'id': 11, 'name': '%s - R',    'lang': 32302, 'match': 'R',    'icon': 'USA/USA-R.png'},
        {'id': 12, 'name': '%s - NC-17','lang': 32302, 'match': 'NC-17','icon': 'USA/USA-NC-17.png'},
        {'id': 13, 'name': '%s - FSK 0','lang': 32303, 'match': '0',    'icon': 'Germany/Germany-FSK-0.png'},
        {'id': 14, 'name': '%s - FSK 6','lang': 32303, 'match': '6',    'icon': 'Germany/Germany-FSK-6.png'},
        {'id': 15, 'name': '%s - FSK 12','lang': 32303,'match': '12',   'icon': 'Germany/Germany-FSK-12.png'},
        {'id': 16, 'name': '%s - FSK 16','lang': 32303,'match': '16',   'icon': 'Germany/Germany-FSK-16.png'},
        {'id': 17, 'name': '%s - FSK 18','lang': 32303,'match': '18',   'icon': 'Germany/Germany-FSK-18.png'},
        {'id': 36, 'name': '%s - L',    'lang': 32307, 'match': 'L',    'icon': 'Brazil/Brazil-L.png'},
        {'id': 37, 'name': '%s - 10',   'lang': 32307, 'match': '10',   'icon': 'Brazil/Brazil-10.png'},
        {'id': 38, 'name': '%s - 12',   'lang': 32307, 'match': '12',   'icon': 'Brazil/Brazil-12.png'},
        {'id': 39, 'name': '%s - 14',   'lang': 32307, 'match': '14',   'icon': 'Brazil/Brazil-14.png'},
        {'id': 40, 'name': '%s - 16',   'lang': 32307, 'match': '16',   'icon': 'Brazil/Brazil-16.png'},
        {'id': 41, 'name': '%s - 18',   'lang': 32307, 'match': '18',   'icon': 'Brazil/Brazil-18.png'},
    ]

    tvCassificationsNames = [
        {'id': 1,  'name': '%s - TV-Y',  'lang': 32302, 'match': 'TV-Y',  'icon': 'USA/USA-TV-Y.png'},
        {'id': 2,  'name': '%s - TV-Y7', 'lang': 32302, 'match': 'TV-Y7', 'icon': 'USA/USA-TV-Y7.png'},
        {'id': 3,  'name': '%s - TV-G',  'lang': 32302, 'match': 'TV-G',  'icon': 'USA/USA-TV-G.png'},
        {'id': 4,  'name': '%s - TV-PG', 'lang': 32302, 'match': 'TV-PG', 'icon': 'USA/USA-TV-PG.png'},
        {'id': 5,  'name': '%s - TV-14', 'lang': 32302, 'match': 'TV-14', 'icon': 'USA/USA-TV-14.png'},
        {'id': 6,  'name': '%s - TV-MA', 'lang': 32302, 'match': 'TV-MA', 'icon': 'USA/USA-TV-MA.png'},
        {'id': 20, 'name': '%s - L',     'lang': 32307, 'match': 'L',     'icon': 'Brazil/Brazil-L.png'},
        {'id': 21, 'name': '%s - 10',    'lang': 32307, 'match': '10',    'icon': 'Brazil/Brazil-10.png'},
        {'id': 22, 'name': '%s - 12',    'lang': 32307, 'match': '12',    'icon': 'Brazil/Brazil-12.png'},
        {'id': 23, 'name': '%s - 14',    'lang': 32307, 'match': '14',    'icon': 'Brazil/Brazil-14.png'},
        {'id': 24, 'name': '%s - 16',    'lang': 32307, 'match': '16',    'icon': 'Brazil/Brazil-16.png'},
        {'id': 25, 'name': '%s - 18',    'lang': 32307, 'match': '18',    'icon': 'Brazil/Brazil-18.png'},
    ]

    @staticmethod
    def reloadSettings():
        global ADDON
        pinLength = Settings.getPinLength()
        pinValue = ADDON.getSetting("pinValue")
        ADDON = xbmcaddon.Addon(id='script.keltecpinguard')
        if Settings.isPinSet():
            if pinLength != Settings.getPinLength():
                if pinValue == ADDON.getSetting("pinValue"):
                    for i in range(1, 6):
                        Settings.setPinValue("", i)
                        userId = "user%dPin" % i
                        Settings.setUserPinValue("", userId)
                    ADDON.setSetting("pinValueSet", "false")

    @staticmethod
    def setPinValue(newPin, pinLevel=1):
        encryptedPin = ""
        if len(newPin) > 0:
            encryptedPin = Settings.encryptPin(newPin)
        pinSettingsValue = "pinValue"
        if pinLevel > 1:
            pinSettingsValue = "%s%d" % (pinSettingsValue, pinLevel)
        ADDON.setSetting(pinSettingsValue, encryptedPin)

    @staticmethod
    def setUserPinValue(newPin, pinId):
        encryptedPin = ""
        pinSet = 'false'
        if len(newPin) > 0:
            encryptedPin = Settings.encryptPin(newPin)
            pinSet = 'true'
        ADDON.setSetting(pinId, encryptedPin)
        ADDON.setSetting("%sSet" % pinId, pinSet)

    @staticmethod
    def checkPinSettings():
        numLevels = Settings.getNumberOfLevels()
        clearPinNum = 5
        while numLevels < clearPinNum:
            log("SetPin: Clearing pin %d" % clearPinNum)
            Settings.setPinValue("", clearPinNum)
            clearPinNum -= 1
        allPinsSet = True
        pinCheck = 1
        while pinCheck <= numLevels:
            if not Settings.isPinSet(pinCheck):
                allPinsSet = False
                break
            pinCheck += 1
        ADDON.setSetting("pinValueSet", "true" if allPinsSet else "false")
        numUsers = Settings.getNumberOfLimitedUsers()
        clearUserPinNum = 5
        while numUsers < clearUserPinNum:
            log("SetPin: Clearing user pin %d" % clearUserPinNum)
            userId = "user%dPin" % clearUserPinNum
            userNameId = "%sName" % userId
            Settings.setUserPinValue("", userId)
            userName = "%s %d" % (ADDON.getLocalizedString(32036), clearUserPinNum)
            ADDON.setSetting(userNameId, userName)
            clearUserPinNum -= 1
        if numUsers < 1:
            Settings.setUserPinValue("", "unrestrictedUserPin")

    @staticmethod
    def encryptPin(rawValue):
        # Python 3: encode string to bytes before hashing
        if isinstance(rawValue, str):
            rawValue = rawValue.encode('utf-8')
        return hashlib.sha256(rawValue).hexdigest()

    @staticmethod
    def isPinSet(pinLevel=1):
        pinSettingsValue = "pinValue"
        if pinLevel > 1:
            pinSettingsValue = "%s%d" % (pinSettingsValue, pinLevel)
        pinValue = ADDON.getSetting(pinSettingsValue)
        return pinValue not in [None, ""]

    @staticmethod
    def getPinLength():
        return int(float(ADDON.getSetting('pinLength')))

    @staticmethod
    def isPinCorrect(inputPin, pinLevel=1):
        pinSettingsValue = "pinValue"
        if pinLevel > 1:
            pinSettingsValue = "%s%d" % (pinSettingsValue, pinLevel)
        inputPinEncrypt = Settings.encryptPin(inputPin)
        return inputPinEncrypt == ADDON.getSetting(pinSettingsValue)

    @staticmethod
    def isUserPinCorrect(inputPin, pinId, blankIsCorrect=True):
        storedPin = ADDON.getSetting(pinId)
        if storedPin in [None, ""]:
            return blankIsCorrect
        inputPinEncrypt = Settings.encryptPin(inputPin)
        return inputPinEncrypt == storedPin

    @staticmethod
    def checkPinClash(newPin, pinLevel=1):
        pinCheck = Settings.getNumberOfLevels()
        while pinCheck > 0:
            if pinCheck != pinLevel:
                if Settings.isPinSet(pinCheck):
                    if Settings.isPinCorrect(newPin, pinCheck):
                        return True
            pinCheck -= 1
        return False

    @staticmethod
    def checkUserPinClash(newPin, pinId):
        numUsers = Settings.getNumberOfLimitedUsers()
        checks = ['unrestrictedUserPin', 'user1Pin', 'user2Pin', 'user3Pin', 'user4Pin', 'user5Pin']
        limits = [1, 1, 2, 3, 4, 5]
        for i, uid in enumerate(checks):
            if uid == pinId:
                continue
            if numUsers >= limits[i]:
                if Settings.isUserPinCorrect(newPin, uid, False):
                    return True
        return False

    @staticmethod
    def getSecurityLevelForPin(inputPin):
        pinCheck = Settings.getNumberOfLevels()
        aPinSet = False
        while pinCheck > 0:
            if Settings.isPinSet(pinCheck):
                aPinSet = True
                if Settings.isPinCorrect(inputPin, pinCheck):
                    return pinCheck
            pinCheck -= 1
        return -1 if aPinSet else 5

    @staticmethod
    def getUserForPin(inputPin):
        numUsers = Settings.getNumberOfLimitedUsers()
        if numUsers > 0:
            if Settings.isUserPinCorrect(inputPin, 'unrestrictedUserPin'):
                return 'unrestrictedUserPin'
            if Settings.isUserPinCorrect(inputPin, 'user1Pin'):
                return 'user1Pin'
        if numUsers > 1 and Settings.isUserPinCorrect(inputPin, 'user2Pin'):
            return 'user2Pin'
        if numUsers > 2 and Settings.isUserPinCorrect(inputPin, 'user3Pin'):
            return 'user3Pin'
        if numUsers > 3 and Settings.isUserPinCorrect(inputPin, 'user4Pin'):
            return 'user4Pin'
        if numUsers > 4 and Settings.isUserPinCorrect(inputPin, 'user5Pin'):
            return 'user5Pin'
        return None

    @staticmethod
    def getInvalidPinNotificationType():
        return int(float(ADDON.getSetting('invalidPinNotificationType')))

    @staticmethod
    def isPinActive():
        if ADDON.getSetting("timeRestrictionEnabled") != 'true':
            return True
        localTime = time.localtime()
        currentTime = (localTime.tm_hour * 60) + localTime.tm_min
        startTimeStr = ADDON.getSetting("startTime")
        startTimeSplit = startTimeStr.split(':')
        startTime = (int(startTimeSplit[0]) * 60) + int(startTimeSplit[1])
        if startTime > currentTime:
            return False
        endTimeStr = ADDON.getSetting("endTime")
        endTimeSplit = endTimeStr.split(':')
        endTime = (int(endTimeSplit[0]) * 60) + int(endTimeSplit[1])
        return endTime >= currentTime

    @staticmethod
    def getPinCachingEnabledDuration():
        cacheSelection = int(ADDON.getSetting("pinCachingStatus"))
        if cacheSelection == 0:
            return 0
        elif cacheSelection == 1:
            return -1
        else:
            return int(float(ADDON.getSetting("pinCachingDuration")))

    @staticmethod
    def isDirectionKeysAsPin():
        return ADDON.getSetting("directionKeysAsPin") == 'true'

    @staticmethod
    def isDisplayBackground():
        return ADDON.getSetting("background") != "0"

    @staticmethod
    def getBackgroundImage():
        selectIdx = ADDON.getSetting("background")
        if selectIdx == "2":
            return ADDON.getAddonInfo('fanart')
        elif selectIdx == "3":
            return ADDON.getSetting("backgroundImage")
        return None

    @staticmethod
    def isActiveVideoPlaying():
        return ADDON.getSetting("activityVideoPlaying") == 'true'

    @staticmethod
    def isActiveNavigation():
        return ADDON.getSetting("activityNavigation") == 'true'

    @staticmethod
    def isActivePlugins():
        return ADDON.getSetting("activityPlugins") == 'true'

    @staticmethod
    def isActiveSystemSettings():
        return ADDON.getSetting("activitySystemSettings") == 'true'

    @staticmethod
    def isActiveRepositories():
        return ADDON.getSetting("activityRepositories") == 'true'

    @staticmethod
    def isActiveFileSource():
        return ADDON.getSetting("activityFileSource") == 'true'

    @staticmethod
    def isActiveFileSourcePlaying():
        return ADDON.getSetting("activityFileSourceNavigationOnly") != 'true'

    @staticmethod
    def showSecurityLevelInPlugin():
        if Settings.getNumberOfLevels() < 2:
            return False
        return ADDON.getSetting("showSecurityInfo") == 'true'

    @staticmethod
    def isSupportedMovieClassification(classification):
        return any(c['match'] == classification for c in Settings.movieCassificationsNames)

    @staticmethod
    def isSupportedTvShowClassification(classification):
        return any(c['match'] == classification for c in Settings.tvCassificationsNames)

    @staticmethod
    def getDefaultMoviesWithoutClassification():
        return 0 if ADDON.getSetting("defaultMoviesWithoutClassification") == '0' else 1

    @staticmethod
    def getDefaultTvShowsWithoutClassification():
        return 0 if ADDON.getSetting("defaultTvShowsWithoutClassification") == '0' else 1

    @staticmethod
    def isHighlightClassificationUnprotectedVideos():
        return ADDON.getSetting("highlightClassificationUnprotectedVideos") == 'true'

    @staticmethod
    def isPromptForPinOnStartup():
        return ADDON.getSetting("promptForPinOnStartup") == 'true'

    @staticmethod
    def getNumberOfLevels():
        return int(ADDON.getSetting("numberOfLevels")) + 1

    @staticmethod
    def getSettingsSecurityLevel():
        pinCheck = Settings.getNumberOfLevels()
        while pinCheck > 0:
            if Settings.isPinSet(pinCheck):
                return pinCheck
            pinCheck -= 1
        return -1

    @staticmethod
    def getNumberOfLimitedUsers():
        return int(ADDON.getSetting("numberOfLimitedUsers"))

    @staticmethod
    def getUserStartTime(userId):
        startTimeTag = "%sStartTime" % userId
        startTimeStr = ADDON.getSetting(startTimeTag)
        startTimeSplit = startTimeStr.split(':')
        startTime = (int(startTimeSplit[0]) * 60) + int(startTimeSplit[1])
        return (startTime, startTimeStr)

    @staticmethod
    def getUserEndTime(userId):
        endTimeTag = "%sEndTime" % userId
        endTimeStr = ADDON.getSetting(endTimeTag)
        endTimeSplit = endTimeStr.split(':')
        endTime = (int(endTimeSplit[0]) * 60) + int(endTimeSplit[1])
        return (endTime, endTimeStr)

    @staticmethod
    def getUserViewingLimit(userId):
        viewingLimitTag = "%sViewingLimit" % userId
        return int(ADDON.getSetting(viewingLimitTag))

    @staticmethod
    def getUserViewingUsedTime(userId):
        lastLimitDataTag = "%sLastLimitData" % userId
        lastLimitData = ADDON.getSetting(lastLimitDataTag)
        todaysDate = date.today().strftime("%d/%m/%y")
        if todaysDate != lastLimitData:
            return 0
        limitUsedTag = "%sLimitUsed" % userId
        limitUsed = ADDON.getSetting(limitUsedTag)
        if limitUsed in [None, ""]:
            return 0
        return int(limitUsed)

    @staticmethod
    def setUserViewingUsedTime(userId, usedViewingTime):
        todaysDate = date.today().strftime("%d/%m/%y")
        lastLimitDataTag = "%sLastLimitData" % userId
        ADDON.setSetting(lastLimitDataTag, todaysDate)
        limitUsedTag = "%sLimitUsed" % userId
        ADDON.setSetting(limitUsedTag, str(usedViewingTime))

    @staticmethod
    def getWarnExpiringTime():
        return int(float(ADDON.getSetting('warnExpiringTime')))

    @staticmethod
    def getUserName(userId):
        userNameTag = "%sName" % userId
        return ADDON.getSetting(userNameTag)
