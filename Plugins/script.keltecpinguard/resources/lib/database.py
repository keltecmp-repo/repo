# -*- coding: utf-8 -*-
# KeltecPinGuard - Database module
# Updated for Python 3 / Kodi 19+ (Matrix, Nexus, Omega)

import xbmc
import xbmcaddon
import xbmcvfs
import sqlite3
import xbmcgui

from resources.lib.settings import log
from resources.lib.settings import os_path_join

ADDON = xbmcaddon.Addon(id='script.keltecpinguard')


class KeltecPinGuardDB():
    def __init__(self):
        # xbmcvfs.translatePath replaces the deprecated xbmc.translatePath
        self.configPath = xbmcvfs.translatePath(ADDON.getAddonInfo('profile'))
        self.databasefile = os_path_join(self.configPath, "keltecpinguard_database.db")
        log("KeltecPinGuardDB: Database file location = %s" % self.databasefile)
        self._createDatabase()

    def cleanDatabase(self):
        msg = "%s?" % ADDON.getLocalizedString(32113)
        isYes = xbmcgui.Dialog().yesno(ADDON.getLocalizedString(32001), msg)
        if isYes:
            if xbmcvfs.exists(self.databasefile):
                xbmcvfs.delete(self.databasefile)
                log("KeltecPinGuardDB: Removed database: %s" % self.databasefile)
            else:
                log("KeltecPinGuardDB: No database exists: %s" % self.databasefile)

    def _createDatabase(self):
        if not xbmcvfs.exists(self.databasefile):
            conn = sqlite3.connect(self.databasefile)
            c = conn.cursor()
            c.execute('CREATE TABLE version (version text primary key)')
            c.execute("INSERT INTO version VALUES (?)", ("5",))
            c.execute('CREATE TABLE TvShows (id integer primary key, name text unique, dbid integer unique, level integer)')
            c.execute('CREATE TABLE Movies (id integer primary key, name text unique, dbid integer unique, level integer)')
            c.execute('CREATE TABLE MovieSets (id integer primary key, name text unique, dbid integer unique, level integer)')
            c.execute('CREATE TABLE Plugins (id integer primary key, name text unique, dbid text unique, level integer)')
            c.execute('CREATE TABLE Repositories (id integer primary key, name text unique, dbid text unique, level integer)')
            c.execute('CREATE TABLE MusicVideos (id integer primary key, name text unique, dbid integer unique, level integer)')
            c.execute('CREATE TABLE FileSources (id integer primary key, name text unique, dbid text unique, level integer)')
            c.execute('CREATE TABLE ClassificationsMovies (id integer primary key, name text unique, dbid text, level integer)')
            c.execute('CREATE TABLE ClassificationsTV (id integer primary key, name text unique, dbid text, level integer)')
            conn.commit()
            conn.close()

    def createOrUpdateDB(self):
        if not xbmcvfs.exists(self.databasefile):
            self._createDatabase()
            return

        conn = sqlite3.connect(self.databasefile)
        c = conn.cursor()
        c.execute('SELECT * FROM version')
        currentVersion = int(c.fetchone()[0])
        log("KeltecPinGuardDB: Current version number in DB is: %d" % currentVersion)

        if currentVersion < 2:
            log("KeltecPinGuardDB: Updating to version 2")
            c.execute('CREATE TABLE MusicVideos (id integer primary key, name text unique, dbid integer unique, level integer)')
            currentVersion = 2
            c.execute('DELETE FROM version')
            c.execute("INSERT INTO version VALUES (?)", (currentVersion,))
            conn.commit()

        if currentVersion < 3:
            log("KeltecPinGuardDB: Updating to version 3")
            c.execute('CREATE TABLE FileSources (id integer primary key, name text unique, dbid text unique, level integer)')
            currentVersion = 3
            c.execute('DELETE FROM version')
            c.execute("INSERT INTO version VALUES (?)", (currentVersion,))
            conn.commit()

        if currentVersion < 4:
            log("KeltecPinGuardDB: Updating to version 4")
            c.execute('CREATE TABLE ClassificationsMovies (id integer primary key, name text unique, dbid text, level integer)')
            c.execute('CREATE TABLE ClassificationsTV (id integer primary key, name text unique, dbid text, level integer)')
            currentVersion = 4
            c.execute('DELETE FROM version')
            c.execute("INSERT INTO version VALUES (?)", (currentVersion,))
            conn.commit()

        if currentVersion < 5:
            log("KeltecPinGuardDB: Updating to version 5")
            c.execute('CREATE TABLE Repositories (id integer primary key, name text unique, dbid text unique, level integer)')
            currentVersion = 5
            c.execute('DELETE FROM version')
            c.execute("INSERT INTO version VALUES (?)", (currentVersion,))
            conn.commit()

        conn.close()

    def getConnection(self):
        return sqlite3.connect(self.databasefile)

    def setTvShowSecurityLevel(self, showName, dbid, level=1):
        if level != 0:
            return self._insertOrUpdate("TvShows", showName, dbid, level)
        self._deleteSecurityDetails("TvShows", showName)
        return -1

    def setMovieSecurityLevel(self, movieName, dbid, level=1):
        if level != 0:
            return self._insertOrUpdate("Movies", movieName, dbid, level)
        self._deleteSecurityDetails("Movies", movieName)
        return -1

    def setMovieSetSecurityLevel(self, movieSetName, dbid, level=1):
        if level != 0:
            return self._insertOrUpdate("MovieSets", movieSetName, dbid, level)
        self._deleteSecurityDetails("MovieSets", movieSetName)
        return -1

    def setPluginSecurityLevel(self, pluginName, dbid, level=1):
        if level != 0:
            return self._insertOrUpdate("Plugins", pluginName, dbid, level)
        self._deleteSecurityDetails("Plugins", pluginName)
        return -1

    def setRepositorySecurityLevel(self, repoName, dbid, level=1):
        if level != 0:
            return self._insertOrUpdate("Repositories", repoName, dbid, level)
        self._deleteSecurityDetails("Repositories", repoName)
        return -1

    def setMusicVideoSecurityLevel(self, musicVideoName, dbid, level=1):
        if level != 0:
            return self._insertOrUpdate("MusicVideos", musicVideoName, dbid, level)
        self._deleteSecurityDetails("MusicVideos", musicVideoName)
        return -1

    def setFileSourceSecurityLevel(self, sourceName, sourcePath, level=1):
        if level != 0:
            return self._insertOrUpdate("FileSources", sourceName, sourcePath, level)
        self._deleteSecurityDetails("FileSources", sourceName)
        return -1

    def setMovieClassificationSecurityLevel(self, id, match, level=1):
        if level != 0:
            return self._insertOrUpdate("ClassificationsMovies", id, match, level)
        self._deleteSecurityDetails("ClassificationsMovies", id)
        return -1

    def setTvClassificationSecurityLevel(self, id, match, level=1):
        if level != 0:
            return self._insertOrUpdate("ClassificationsTV", id, match, level)
        self._deleteSecurityDetails("ClassificationsTV", id)
        return -1

    def _insertOrUpdate(self, tableName, name, dbid, level=1):
        log("KeltecPinGuardDB: Adding %s %s (id:%s) at level %d" % (tableName, name, str(dbid), level))
        conn = self.getConnection()
        c = conn.cursor()
        cmd = 'INSERT OR REPLACE INTO %s (name, dbid, level) VALUES (?,?,?)' % tableName
        c.execute(cmd, (name, dbid, level))
        rowId = c.lastrowid
        conn.commit()
        conn.close()
        return rowId

    def _deleteSecurityDetails(self, tableName, name):
        log("KeltecPinGuardDB: delete %s for %s" % (tableName, name))
        conn = self.getConnection()
        c = conn.cursor()
        cmd = 'DELETE FROM %s where name = ?' % tableName
        c.execute(cmd, (name,))
        conn.commit()
        log("KeltecPinGuardDB: delete for %s removed %d rows" % (name, conn.total_changes))
        conn.close()

    def getTvShowSecurityLevel(self, showName):
        return self._getSecurityLevel("TvShows", showName)

    def getMovieSecurityLevel(self, movieName):
        return self._getSecurityLevel("Movies", movieName)

    def getMovieSetSecurityLevel(self, movieSetName):
        return self._getSecurityLevel("MovieSets", movieSetName)

    def getPluginSecurityLevel(self, pluginName):
        return self._getSecurityLevel("Plugins", pluginName)

    def getRepositorySecurityLevel(self, pluginName):
        return self._getSecurityLevel("Repositories", pluginName)

    def getMusicVideoSecurityLevel(self, musicVideoName):
        return self._getSecurityLevel("MusicVideos", musicVideoName)

    def getFileSourceSecurityLevel(self, sourceName):
        return self._getSecurityLevel("FileSources", sourceName)

    def getFileSourceSecurityLevelForPath(self, path):
        return self._getSecurityLevel("FileSources", path, 'dbid')

    def getMovieClassificationSecurityLevel(self, className):
        return self._getSecurityLevel("ClassificationsMovies", className, 'dbid')

    def getTvClassificationSecurityLevel(self, className):
        return self._getSecurityLevel("ClassificationsTV", className, 'dbid')

    def _getSecurityLevel(self, tableName, name, dbField='name'):
        log("KeltecPinGuardDB: select %s for %s (dbField=%s)" % (tableName, name, dbField))
        conn = self.getConnection()
        c = conn.cursor()
        cmd = 'SELECT * FROM %s where %s = ?' % (tableName, dbField)
        c.execute(cmd, (name,))
        row = c.fetchone()
        securityLevel = 0
        if row is None:
            log("KeltecPinGuardDB: No entry found in the database for %s" % name)
        else:
            log("KeltecPinGuardDB: Database info: %s" % str(row))
            securityLevel = row[3]
        conn.close()
        return securityLevel

    def getAllTvShowsSecurity(self):
        return self._getAllSecurityDetails("TvShows")

    def getAllMoviesSecurity(self):
        return self._getAllSecurityDetails("Movies")

    def getAllMovieSetsSecurity(self):
        return self._getAllSecurityDetails("MovieSets")

    def getAllPluginsSecurity(self):
        return self._getAllSecurityDetails("Plugins")

    def getAllRepositoriesSecurity(self):
        return self._getAllSecurityDetails("Repositories")

    def getAllMusicVideosSecurity(self):
        return self._getAllSecurityDetails("MusicVideos")

    def getAllFileSourcesSecurity(self):
        return self._getAllSecurityDetails("FileSources")

    def getAllFileSourcesPathsSecurity(self):
        return self._getAllSecurityDetails("FileSources", keyCol=2)

    def getAllMovieClassificationSecurity(self, useCertKey=False):
        return self._getAllSecurityDetails("ClassificationsMovies", 2 if useCertKey else 1)

    def getAllTvClassificationSecurity(self, useCertKey=False):
        return self._getAllSecurityDetails("ClassificationsTV", 2 if useCertKey else 1)

    def _getAllSecurityDetails(self, tableName, keyCol=1):
        log("KeltecPinGuardDB: select all %s" % tableName)
        conn = self.getConnection()
        c = conn.cursor()
        c.execute('SELECT * FROM %s' % tableName)
        rows = c.fetchall()
        resultDict = {}
        if rows:
            for row in rows:
                resultDict[row[keyCol]] = row[3]
        conn.close()
        return resultDict
