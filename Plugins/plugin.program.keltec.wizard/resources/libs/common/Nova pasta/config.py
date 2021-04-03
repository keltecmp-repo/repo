################################################################################
#      Copyright (C) 2019 drinfernoo                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################
if 64 - 64: i11iIiiIii
import xbmc
import xbmcaddon
import xbmcvfs
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import os
if 73 - 73: II111iiii
import uservar
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
class IiiIII111iI :
 def __init__ ( self ) :
  self . init_meta ( )
  self . init_uservars ( )
  self . init_paths ( )
  self . init_settings ( )
  if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
 def init_meta ( self ) :
  self . ADDON_ID = xbmcaddon . Addon ( ) . getAddonInfo ( 'id' )
  self . ADDON = xbmcaddon . Addon ( self . ADDON_ID )
  self . ADDON_NAME = self . ADDON . getAddonInfo ( 'name' )
  self . ADDON_VERSION = self . ADDON . getAddonInfo ( 'version' )
  self . ADDON_PATH = self . ADDON . getAddonInfo ( 'path' )
  self . ADDON_ICON = self . ADDON . getAddonInfo ( 'icon' )
  self . ADDON_FANART = self . ADDON . getAddonInfo ( 'fanart' )
  self . KODIV = float ( xbmc . getInfoLabel ( "System.BuildVersion" ) [ : 4 ] )
  self . RAM = int ( xbmc . getInfoLabel ( "System.Memory(total)" ) [ : - 2 ] )
  if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . Oo0ooO0oo0oO
 def init_uservars ( self ) :
  if 100 - 100: i1IIi
  self . ADDONTITLE = uservar . ADDONTITLE
  self . BUILDERNAME = uservar . BUILDERNAME
  self . EXCLUDES = uservar . EXCLUDES
  self . BUILDFILE = uservar . BUILDFILE
  self . UPDATECHECK = uservar . UPDATECHECK
  self . APKFILE = uservar . APKFILE
  self . YOUTUBETITLE = uservar . YOUTUBETITLE
  self . YOUTUBEFILE = uservar . YOUTUBEFILE
  self . ADDONFILE = uservar . ADDONFILE
  self . ADVANCEDFILE = uservar . ADVANCEDFILE
  if 27 - 27: O00oOoOoO0o0O * OoooooooOO + I11i * Oo0ooO0oo0oO - i11iIiiIii - iii1I1I
  if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
  self . ICONBUILDS = uservar . ICONBUILDS if not uservar . ICONBUILDS . endswith ( '://' ) else self . ADDON_ICON
  self . ICONMAINT = uservar . ICONMAINT if not uservar . ICONMAINT . endswith ( '://' ) else self . ADDON_ICON
  self . ICONSPEED = uservar . ICONSPEED if not uservar . ICONSPEED . endswith ( '://' ) else self . ADDON_ICON
  self . ICONAPK = uservar . ICONAPK if not uservar . ICONAPK . endswith ( '://' ) else self . ADDON_ICON
  self . ICONADDONS = uservar . ICONADDONS if not uservar . ICONADDONS . endswith ( '://' ) else self . ADDON_ICON
  self . ICONYOUTUBE = uservar . ICONYOUTUBE if not uservar . ICONYOUTUBE . endswith ( '://' ) else self . ADDON_ICON
  self . ICONSAVE = uservar . ICONSAVE if not uservar . ICONSAVE . endswith ( '://' ) else self . ADDON_ICON
  self . ICONTRAKT = uservar . ICONTRAKT if not uservar . ICONTRAKT . endswith ( '://' ) else self . ADDON_ICON
  self . ICONDEBRID = uservar . ICONREAL if not uservar . ICONREAL . endswith ( '://' ) else self . ADDON_ICON
  self . ICONLOGIN = uservar . ICONLOGIN if not uservar . ICONLOGIN . endswith ( '://' ) else self . ADDON_ICON
  self . ICONCONTACT = uservar . ICONCONTACT if not uservar . ICONCONTACT . endswith ( '://' ) else self . ADDON_ICON
  self . ICONSETTINGS = uservar . ICONSETTINGS if not uservar . ICONSETTINGS . endswith ( '://' ) else self . ADDON_ICON
  self . HIDESPACERS = uservar . HIDESPACERS
  self . SPACER = uservar . SPACER
  self . COLOR1 = uservar . COLOR1
  self . COLOR2 = uservar . COLOR2
  self . THEME1 = uservar . THEME1
  self . THEME2 = uservar . THEME2
  self . THEME3 = uservar . THEME3
  self . THEME4 = uservar . THEME4
  self . THEME5 = uservar . THEME5
  self . HIDECONTACT = uservar . HIDECONTACT
  self . CONTACT = uservar . CONTACT
  self . CONTACTICON = uservar . CONTACTICON if not uservar . CONTACTICON . endswith ( '://' ) else self . ADDON_ICON
  self . CONTACTFANART = uservar . CONTACTFANART if not uservar . CONTACTFANART . endswith ( '://' ) else self . ADDON_FANART
  if 72 - 72: II111iiii - OoOoOO00
  if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
  self . AUTOUPDATE = uservar . AUTOUPDATE
  if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . O00oOoOoO0o0O / O00oOoOoO0o0O % O00oOoOoO0o0O
  if 22 - 22: Ii1I . O00oOoOoO0o0O
  self . AUTOINSTALL = uservar . AUTOINSTALL
  self . REPOID = uservar . REPOID
  self . REPOADDONXML = uservar . REPOADDONXML
  self . REPOZIPURL = uservar . REPOZIPURL
  if 41 - 41: O0oo0OO0 . Oo0ooO0oo0oO * O00oOoOoO0o0O % i11iIiiIii
  if 74 - 74: iii1I1I * O00oOoOoO0o0O
  self . ENABLE_NOTIFICATION = uservar . ENABLE
  self . NOTIFICATION = uservar . NOTIFICATION
  self . HEADERTYPE = uservar . HEADERTYPE
  self . FONTHEADER = uservar . FONTHEADER
  self . HEADERMESSAGE = uservar . HEADERMESSAGE
  self . HEADERIMAGE = uservar . HEADERIMAGE
  self . FONTSETTINGS = uservar . FONTSETTINGS
  self . BACKGROUND = uservar . BACKGROUND
  self . BACKGROUND = self . BACKGROUND if not self . BACKGROUND == '' else self . ADDON_FANART
  if 82 - 82: iIii1I11I1II1 % O00oOoOoO0o0O
 def init_paths ( self ) :
  if 86 - 86: OoOoOO00 % I1IiiI
  self . CLEANFREQ = [ 'Every Startup' , 'Every Day' , 'Every Three Days' ,
 'Weekly' , 'Monthly' ]
  self . LOGFILES = [ 'log' , 'xbmc.old.log' , 'kodi.log' ]
  self . DEFAULTPLUGINS = [ 'metadata.album.universal' ,
 'metadata.artists.universal' ,
 'metadata.common.fanart.tv' ,
 'metadata.common.imdb.com' ,
 'metadata.common.musicbrainz.org' ,
 'metadata.themoviedb.org' ,
 'metadata.tvdb.com' ,
 'service.xbmc.versioncheck' ]
  self . USER_AGENT = ( 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36'
 ' (KHTML, like Gecko) Chrome/35.0.1916.153 Safari'
 '/537.36 SE 2.X MetaSr 1.0' )
  self . DB_FILES = [ 'Addons' , 'ADSP' , 'Epg' , 'MyMusic' , 'MyVideos' ,
 'Textures' , 'TV' , 'ViewModes' ]
  self . EXCLUDE_FILES = [ 'onechannelcache.db' , 'saltscache.db' ,
 'saltscache.db-shm' , 'saltscache.db-wal' ,
 'saltshd.lite.db' , 'saltshd.lite.db-shm' ,
 'saltshd.lite.db-wal' , 'queue.db' ,
 'commoncache.db' , 'access.log' , 'trakt.db' ,
 'video_cache.db' , '.gitignore' , '.DS_Store' ,
 'Textures13.db' , 'Thumbs.db' ]
  self . XMLS = [ 'advancedsettings.xml' , 'sources.xml' , 'favourites.xml' ,
 'profiles.xml' , 'playercorefactory.xml' , 'guisettings.xml' ]
  self . MODURL = 'http://mirrors.kodi.tv/addons/matrix/'
  self . MODURL2 = 'http://mirrors.kodi.tv/addons/jarvis/'
  self . DEPENDENCIES = [ 'script.module.bottle' , 'script.module.certifi' ,
 'script.module.chardet' , 'script.module.idna' ,
 'script.module.requests' , 'script.module.six' ,
 'script.module.urllib3' , 'script.module.web-pdb' ]
  if 80 - 80: OoooooooOO . I1IiiI
  if 87 - 87: oO0o / Oo0ooO0oo0oO + O0oo0OO0 - Oo0ooO0oo0oO . Oo0ooO0oo0oO / II111iiii
  self . XBMC = xbmcvfs . translatePath ( 'special://xbmc/' )
  self . HOME = xbmcvfs . translatePath ( 'special://home/' )
  self . TEMP = xbmcvfs . translatePath ( 'special://temp/' )
  self . MASTERPROFILE = xbmcvfs . translatePath ( 'special://masterprofile/' )
  self . PROFILE = xbmcvfs . translatePath ( 'special://profile/' )
  self . SUBTITLES = xbmcvfs . translatePath ( 'special://subtitles/' )
  self . USERDATA = xbmcvfs . translatePath ( 'special://userdata/' )
  self . DATABASE = xbmcvfs . translatePath ( 'special://database/' )
  self . THUMBNAILS = xbmcvfs . translatePath ( 'special://thumbnails/' )
  self . RECORDINGS = xbmcvfs . translatePath ( 'special://recordings/' )
  self . SCREENSHOTS = xbmcvfs . translatePath ( 'special://screenshots/' )
  self . MUSICPLAYLISTS = xbmcvfs . translatePath ( 'special://musicplaylists/' )
  self . VIDEOPLAYLISTS = xbmcvfs . translatePath ( 'special://videoplaylists/' )
  self . CDRIPS = xbmcvfs . translatePath ( 'special://cdrips/' )
  self . SKIN = xbmcvfs . translatePath ( 'special://skin/' )
  self . LOGPATH = xbmcvfs . translatePath ( 'special://logpath/' )
  if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
  if 58 - 58: i11iIiiIii % O0oo0OO0
  self . ADDONS = os . path . join ( self . HOME , 'addons' )
  self . KODIADDONS = os . path . join ( self . XBMC , 'addons' )
  self . PLUGIN = os . path . join ( self . ADDONS , self . ADDON_ID )
  self . PACKAGES = os . path . join ( self . ADDONS , 'packages' )
  self . ADDON_DATA = os . path . join ( self . USERDATA , 'addon_data' )
  self . PLUGIN_DATA = os . path . join ( self . ADDON_DATA , self . ADDON_ID )
  self . QRCODES = os . path . join ( self . PLUGIN_DATA , 'QRCodes' )
  self . SPEEDTEST = os . path . join ( self . PLUGIN_DATA , 'SpeedTest' )
  self . ARCHIVE_CACHE = os . path . join ( self . TEMP , 'archive_cache' )
  self . ART = os . path . join ( self . PLUGIN , 'resources' , 'art' )
  self . DEBRIDFOLD = os . path . join ( self . PLUGIN_DATA , 'debrid' )
  self . TRAKTFOLD = os . path . join ( self . PLUGIN_DATA , 'trakt' )
  self . LOGINFOLD = os . path . join ( self . PLUGIN_DATA , 'login' )
  if 54 - 54: OOooOOo % O0 + I1IiiI - iii1I1I / I11i
  if 31 - 31: OoO0O00 + II111iiii
  self . ADVANCED = os . path . join ( self . USERDATA , 'advancedsettings.xml' )
  self . SOURCES = os . path . join ( self . USERDATA , 'sources.xml' )
  self . GUISETTINGS = os . path . join ( self . USERDATA , 'guisettings.xml' )
  self . FAVOURITES = os . path . join ( self . USERDATA , 'favourites.xml' )
  self . PROFILES = os . path . join ( self . USERDATA , 'profiles.xml' )
  self . WIZLOG = os . path . join ( self . PLUGIN_DATA , 'wizard.log' )
  self . WHITELIST = os . path . join ( self . PLUGIN_DATA , 'whitelist.txt' )
  if 13 - 13: OOooOOo * oO0o * I1IiiI
  self . EXCLUDE_DIRS = [ self . ADDON_PATH ,
 os . path . join ( self . HOME , 'cache' ) ,
 os . path . join ( self . HOME , 'system' ) ,
 os . path . join ( self . HOME , 'temp' ) ,
 os . path . join ( self . HOME , 'My_Builds' ) ,
 os . path . join ( self . HOME , 'cdm' ) ,
 os . path . join ( self . ADDONS , 'temp' ) ,
 os . path . join ( self . ADDONS , 'packages' ) ,
 os . path . join ( self . ADDONS , 'archive_cache' ) ,
 os . path . join ( self . USERDATA , 'Thumbnails' ) ,
 os . path . join ( self . USERDATA , 'peripheral_data' ) ,
 os . path . join ( self . USERDATA , 'library' ) ]
  if 55 - 55: II111iiii
 def init_settings ( self ) :
  self . FIRSTRUN = self . get_setting ( 'first_install' )
  if 43 - 43: OoOoOO00 - i1IIi + O0oo0OO0 + Ii1I
  if 17 - 17: o0oOOo0O0Ooo
  self . BUILDNAME = self . get_setting ( 'buildname' )
  self . BUILDCHECK = self . get_setting ( 'nextbuildcheck' )
  self . DEFAULTSKIN = self . get_setting ( 'defaultskin' )
  self . DEFAULTNAME = self . get_setting ( 'defaultskinname' )
  self . DEFAULTIGNORE = self . get_setting ( 'defaultskinignore' )
  self . BUILDVERSION = self . get_setting ( 'buildversion' )
  self . BUILDTHEME = self . get_setting ( 'buildtheme' )
  self . BUILDLATEST = self . get_setting ( 'latestversion' )
  self . DISABLEUPDATE = self . get_setting ( 'disableupdate' )
  self . INSTALLED = self . get_setting ( 'installed' )
  self . EXTRACT = self . get_setting ( 'extract' )
  self . EXTERROR = self . get_setting ( 'errors' )
  if 64 - 64: Ii1I % i1IIi % OoooooooOO
  if 3 - 3: iii1I1I + O0
  self . SHOW19 = self . get_setting ( 'show19' )
  self . SHOWADULT = self . get_setting ( 'adult' )
  self . SEPARATE = self . get_setting ( 'separate' )
  self . DEVELOPER = self . get_setting ( 'developer' )
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
  self . AUTOCLEANUP = self . get_setting ( 'autoclean' )
  self . AUTOCACHE = self . get_setting ( 'clearcache' )
  self . AUTOPACKAGES = self . get_setting ( 'clearpackages' )
  self . AUTOTHUMBS = self . get_setting ( 'clearthumbs' )
  self . AUTOFREQ = self . get_setting ( 'autocleanfreq' )
  self . AUTOFREQ = int ( float ( self . AUTOFREQ ) ) if self . AUTOFREQ . isdigit ( ) else 0
  self . AUTONEXTRUN = self . get_setting ( 'nextautocleanup' )
  if 18 - 18: O0 - iii1I1I / iii1I1I + Oo0ooO0oo0oO % Oo0ooO0oo0oO - O00oOoOoO0o0O
  if 62 - 62: iii1I1I - O00oOoOoO0o0O - OoOoOO00 % i1IIi / oO0o
  self . INCLUDEVIDEO = self . get_setting ( 'includevideo' )
  self . INCLUDEALL = self . get_setting ( 'includeall' )
  self . INCLUDEEXODUSREDUX = self . get_setting ( 'includeexodusredux' )
  self . INCLUDEGAIA = self . get_setting ( 'includegaia' )
  self . INCLUDESEREN = self . get_setting ( 'includeseren' )
  self . INCLUDETHECREW = self . get_setting ( 'includethecrew' )
  self . INCLUDEYODA = self . get_setting ( 'includeyoda' )
  self . INCLUDEVENOM = self . get_setting ( 'includevenom' )
  self . INCLUDENUMBERS = self . get_setting ( 'includenumbers' )
  self . INCLUDESCRUBS = self . get_setting ( 'includescrubs' )
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
  if 14 - 14: I11i % O0
  self . NOTIFY = self . get_setting ( 'notify' )
  self . NOTEID = self . get_setting ( 'noteid' )
  self . NOTEDISMISS = self . get_setting ( 'notedismiss' )
  if 41 - 41: i1IIi + O0oo0OO0 + OOooOOo - O00oOoOoO0o0O
  if 77 - 77: Oo0Ooo . O00oOoOoO0o0O % Oo0ooO0oo0oO
  self . TRAKTSAVE = self . get_setting ( 'traktnextsave' )
  self . DEBRIDSAVE = self . get_setting ( 'debridnextsave' )
  self . LOGINSAVE = self . get_setting ( 'loginnextsave' )
  self . KEEPFAVS = self . get_setting ( 'keepfavourites' )
  self . KEEPSOURCES = self . get_setting ( 'keepsources' )
  self . KEEPPROFILES = self . get_setting ( 'keepprofiles' )
  self . KEEPPLAYERCORE = self . get_setting ( 'keepplayercore' )
  self . KEEPADVANCED = self . get_setting ( 'keepadvanced' )
  self . KEEPGUISETTINGS = self . get_setting ( 'keepguisettings' )
  self . KEEPREPOS = self . get_setting ( 'keeprepos' )
  self . KEEPSUPER = self . get_setting ( 'keepsuper' )
  self . KEEPWHITELIST = self . get_setting ( 'keepwhitelist' )
  self . KEEPTRAKT = self . get_setting ( 'keeptrakt' )
  self . KEEPDEBRID = self . get_setting ( 'keepdebrid' )
  self . KEEPLOGIN = self . get_setting ( 'keeplogin' )
  if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
  if 17 - 17: oO0o . Oo0Ooo . I1ii11iIi11i
  self . BACKUPLOCATION = xbmcvfs . translatePath ( self . get_setting ( 'path' ) if not self . get_setting ( 'path' ) == '' else self . HOME )
  self . MYBUILDS = os . path . join ( self . BACKUPLOCATION , 'My_Builds' )
  if 3 - 3: OoOoOO00 . Oo0Ooo . I1IiiI / Ii1I
  if 38 - 38: II111iiii % i11iIiiIii . Oo0ooO0oo0oO - OOooOOo + Ii1I
  self . DEBUGLEVEL = self . get_setting ( 'debuglevel' )
  self . ENABLEWIZLOG = self . get_setting ( 'wizardlog' )
  self . CLEANWIZLOG = self . get_setting ( 'autocleanwiz' )
  self . CLEANWIZLOGBY = self . get_setting ( 'wizlogcleanby' )
  self . CLEANDAYS = self . get_setting ( 'wizlogcleandays' )
  self . CLEANSIZE = self . get_setting ( 'wizlogcleansize' )
  self . CLEANLINES = self . get_setting ( 'wizlogcleanlines' )
  self . MAXWIZSIZE = [ 100 , 200 , 300 , 400 , 500 , 1000 ]
  self . MAXWIZLINES = [ 100 , 200 , 300 , 400 , 500 ]
  self . MAXWIZDATES = [ 1 , 2 , 3 , 7 ]
  self . KEEPOLDLOG = self . get_setting ( 'oldlog' ) == 'true'
  self . KEEPWIZLOG = self . get_setting ( 'wizlog' ) == 'true'
  self . KEEPCRASHLOG = self . get_setting ( 'crashlog' ) == 'true'
  self . LOGEMAIL = self . get_setting ( 'email' )
  self . NEXTCLEANDATE = self . get_setting ( 'nextwizcleandate' )
  if 66 - 66: OoooooooOO * OoooooooOO . OOooOOo . i1IIi - OOooOOo
 def get_setting ( self , key , id = xbmcaddon . Addon ( ) . getAddonInfo ( 'id' ) ) :
  try :
   return xbmcaddon . Addon ( id ) . getSetting ( key )
  except :
   return False
   if 77 - 77: I11i - iIii1I11I1II1
 def set_setting ( self , key , value , id = xbmcaddon . Addon ( ) . getAddonInfo ( 'id' ) ) :
  try :
   return xbmcaddon . Addon ( id ) . setSetting ( key , value )
  except :
   return False
   if 82 - 82: i11iIiiIii . OOooOOo / Oo0Ooo * O0 % oO0o % iIii1I11I1II1
 def open_settings ( self , id = None , cat = None , set = None , activate = False ) :
  Oo00OOOOO = [ ( 100 , 200 ) , ( - 100 , - 80 ) ]
  if not id :
   id = self . ADDON_ID
   if 85 - 85: Oo0ooO0oo0oO . iii1I1I - OoO0O00 % Oo0ooO0oo0oO % II111iiii
  try :
   xbmcaddon . Addon ( id ) . openSettings ( )
  except :
   import logging
   logging . log ( 'Não é possível abrir as configurações para {}' . format ( id ) , level = xbmc . LOGERROR )
   if 81 - 81: OoO0O00 + II111iiii % iii1I1I * O0
  if int ( self . KODIV ) < 18 :
   oOOo0oo = 0
  else :
   oOOo0oo = 1
   if 80 - 80: I11i * i11iIiiIii / O0oo0OO0
  if cat is not None :
   I11II1i = cat + Oo00OOOOO [ oOOo0oo ] [ 0 ]
   xbmc . executebuiltin ( 'SetFocus({})' . format ( I11II1i ) )
   if set is not None :
    IIIII = set + Oo00OOOOO [ oOOo0oo ] [ 1 ]
    xbmc . executebuiltin ( 'SetFocus({})' . format ( IIIII ) )
    if 75 - 75: II111iiii % II111iiii
    if activate :
     xbmc . executebuiltin ( 'SendClick({})' . format ( IIIII ) )
     if 13 - 13: o0oOOo0O0Ooo . Ii1I
     if 19 - 19: I11i + Oo0ooO0oo0oO
 def clear_setting ( self , type ) :
  ooo = { 'buildname' : '' , 'buildversion' : '' , 'buildtheme' : '' ,
 'latestversion' : '' , 'nextbuildcheck' : '2019-01-01 00:00:00' }
  ii1I1i1I = { 'extract' : '' , 'errors' : '' , 'installed' : '' }
  OOoo0O0 = { 'defaultskinignore' : 'false' , 'defaultskin' : '' ,
 'defaultskinname' : '' }
  iiiIi1i1I = [ 'default.enablerssfeeds' , 'default.font' , 'default.rssedit' ,
 'default.skincolors' , 'default.skintheme' ,
 'default.skinzoom' , 'default.soundskin' ,
 'default.startupwindow' , 'default.stereostrength' ]
  if type == 'build' :
   for oOO00oOO in ooo :
    self . set_setting ( oOO00oOO , ooo [ oOO00oOO ] )
   for oOO00oOO in ii1I1i1I :
    self . set_setting ( oOO00oOO , ii1I1i1I [ oOO00oOO ] )
   for oOO00oOO in OOoo0O0 :
    self . set_setting ( oOO00oOO , OOoo0O0 [ oOO00oOO ] )
   for oOO00oOO in iiiIi1i1I :
    self . set_setting ( oOO00oOO , '' )
  elif type == 'default' :
   for oOO00oOO in OOoo0O0 :
    self . set_setting ( oOO00oOO , OOoo0O0 [ oOO00oOO ] )
   for oOO00oOO in iiiIi1i1I :
    self . set_setting ( oOO00oOO , '' )
  elif type == 'install' :
   for oOO00oOO in ii1I1i1I :
    self . set_setting ( oOO00oOO , ii1I1i1I [ oOO00oOO ] )
  elif type == 'lookfeel' :
   for oOO00oOO in iiiIi1i1I :
    self . set_setting ( oOO00oOO , '' )
  else :
   self . set_setting ( type , '' )
   if 75 - 75: i1IIi / OoooooooOO - O0 / OoOoOO00 . II111iiii - i1IIi
   if 71 - 71: OOooOOo + Ii1I * OOooOOo - OoO0O00 * o0oOOo0O0Ooo
Oooo0Ooo000 = IiiIII111iI ( )
if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
# Team KelTec Media'Play