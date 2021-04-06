# -*- coding: UTF-8 -*-if 64 - 64: i11iIiiIii
import sys
try :
 import cookielib
except ImportError :
 import http . cookiejar as cookielib
from urllib import request as urllib2 , parse as urllib
import datetime
from datetime import datetime
import re
import os
import base64
import codecs
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import time
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
try :
 import json
except :
 import simplejson as json
 if 73 - 73: II111iiii
IiII1IiiIiI1 = xbmcaddon . Addon ( ) . getAddonInfo ( 'name' )
if 40 - 40: oo * OoO0O00
IIiIiII11i = int ( sys . argv [ 1 ] )
__addon__ = xbmcaddon . Addon ( )
o0oOOo0O0Ooo = __addon__
__addonname__ = __addon__ . getAddonInfo ( 'name' )
__icon__ = __addon__ . getAddonInfo ( 'icon' )
I1ii11iIi11i = __addon__ . getAddonInfo ( 'version' )
try :
 I1IiI = xbmcvfs . translatePath ( __addon__ . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
except :
 I1IiI = xbmcvfs . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
try :
 o0OOO = xbmcvfs . translatePath ( __addon__ . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
except :
 o0OOO = xbmcvfs . translatePath ( __addon__ . getAddonInfo ( 'path' ) )
iIiiiI = os . path . join ( I1IiI , 'favorites.dat' )
Iii1ii1II11i = xbmcaddon . Addon ( ) . getSetting ( "favoritos" )
if 10 - 10: I1iII1iiII + I1Ii111 / OOo
if 41 - 41: I1II1
if os . path . exists ( iIiiiI ) == True :
 Ooo0OO0oOO = open ( iIiiiI ) . read ( )
else :
 Ooo0OO0oOO = [ ]
 if 86 - 86: oO0o
 if 12 - 12: OOO0o0o / o0oO0 + i111I * O0Oo0oO0o . II1iI . i1iIii1Ii1II
def i1I1Iiii1111 ( message , timeShown = 5000 ) :
 xbmc . executebuiltin ( 'Notification(%s, %s, %d, %s)' % ( __addonname__ , message , timeShown , __icon__ ) )
 if 22 - 22: OOo000 . O0Oo0oO0o
def oo0000o0o0 ( text , encoding = 'utf-8' , errors = 'strict' ) :
 if isinstance ( text , bytes ) :
  if 86 - 86: I1Ii111 % oo
  return text . decode ( encoding , errors = errors )
 return text
 if 80 - 80: OoooooooOO . oo
def OOO0O ( heading = '' , message = '' ) :
 oo0ooO0oOOOOo = None
 if 71 - 71: i1iIii1Ii1II
 O0OoOoo00o = xbmc . Keyboard ( message , heading )
 O0OoOoo00o . doModal ( )
 if O0OoOoo00o . isConfirmed ( ) :
  oo0ooO0oOOOOo = oo0000o0o0 ( O0OoOoo00o . getText ( ) )
 return oo0ooO0oOOOOo
 if 31 - 31: II111iiii + I1iII1iiII . i1iIii1Ii1II
def OoOooOOOO ( url , ref , userargent = False ) :
 try :
  if ref > '' :
   i11iiII = ref
  else :
   i11iiII = url
  if userargent :
   I1iiiiI1iII = userargent
  else :
   I1iiiiI1iII = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
  IiIi11i = cookielib . CookieJar ( )
  iIii1I111I11I = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( IiIi11i ) )
  iIii1I111I11I . addheaders = [ ( 'Accept-Language' , 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' ) , ( 'User-Agent' , I1iiiiI1iII ) , ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ) , ( 'Referer' , i11iiII ) ]
  OO00OooO0OO = iIii1I111I11I . open ( url ) . read ( )
  iiiIi = OO00OooO0OO . decode ( 'utf-8' )
  return iiiIi
 except :
  pass
  if 24 - 24: O0 % OOo + i1IIi + i1iIii1Ii1II + I1II1
  if 70 - 70: OoO0O00 % OoO0O00 . II1iI % I1iII1iiII * OOo % oO0o
def iiI1IiI ( data , re_patten ) :
 II = ''
 ooOoOoo0O = re . search ( re_patten , data )
 if ooOoOoo0O != None :
  II = ooOoOoo0O . group ( 1 )
 else :
  II = ''
 return II
 if 76 - 76: O0 / OOo . oo * i111I - OOO0o0o
def Oooo ( ) :
 try :
  O00o = xbmc . translatePath ( o0OOO + '/check.txt' )
  O00 = os . path . isfile ( O00o )
  Oooo = o0oOOo0O0Ooo . getSetting ( 'check_addon' )
  if 11 - 11: oo
  if O00 == True :
   if 68 - 68: o0oO0 + OOO0o0o . iIii1I11I1II1 - II1iI % iIii1I11I1II1 - OOo000
   oOOO00o = open ( O00o , 'r+' )
   O0O00o0OOO0 = o0oOOo0O0Ooo . getSetting ( 'elementum' )
   Ii1iIIIi1ii = o0oOOo0O0Ooo . getSetting ( 'youtube' )
   if oOOO00o and oOOO00o . read ( ) == '1' and Oooo == 'true' :
    if 80 - 80: o0oO0 * i11iIiiIii / i1iIii1Ii1II
    oOOO00o . close ( )
    I11II1i = OoOooOOOO ( 'https://keltecmp-iptv.directorioforuns.com/h153-elementum' , '' ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    II = re . compile ( 'addon_name="(.+?)".+?ddon_id="(.+?)".+?ir="(.+?)".+?rl_zip="(.+?)".+?escription="(.+?)"' ) . findall ( I11II1i )
    for IiII1IiiIiI1 , IIIII , ooooooO0oo , IIiiiiiiIi1I1 , I1IIIii in II :
     if IIIII == 'plugin.video.elementum' and O0O00o0OOO0 == 'false' :
      pass
     elif IIIII == 'script.module.six' and Ii1iIIIi1ii == 'false' :
      pass
     elif IIIII == 'plugin.video.youtube' and Ii1iIIIi1ii == 'false' :
      pass
     else :
      oOoOooOo0o0 = xbmc . translatePath ( ooooooO0oo )
      if 61 - 61: OOo / I1iII1iiII + OOo000 * oO0o / oO0o
      if os . path . exists ( oOoOooOo0o0 ) == False :
       OoOo ( IiII1IiiIiI1 , IIIII , IIiiiiiiIi1I1 , ooooooO0oo , I1IIIii )
       if IIIII == 'plugin.video.elementum' :
        xbmcgui . Dialog ( ) . ok ( )
      else :
       pass
  elif Oooo == 'true' :
   if 18 - 18: i11iIiiIii
   oOOO00o = open ( O00o , 'w' )
   oOOO00o . write ( '1' )
   oOOO00o . close ( )
   xbmcgui . Dialog ( ) . ok ( )
 except :
  pass
  if 46 - 46: i1IIi / o0oO0 % OOO0o0o + i1iIii1Ii1II
  if 79 - 79: i1iIii1Ii1II - OOo + i1iIii1Ii1II - O0Oo0oO0o
def OoOo ( name , addon_id , url , directory , description ) :
 try :
  import downloader
  import extract
  import ntpath
  i1Iii = xbmc . translatePath ( os . path . join ( 'special://' , 'home/' , 'addons' , 'packages' ) )
  OOOooOooo00O0 = ntpath . basename ( url )
  Oo0OO = xbmcgui . DialogProgress ( )
  Oo0OO . create ( "Instalador de Complementos" , "Baixando & Instalando " + name + ",\nPor favor aguarde...." )
  oOOoOo00o = os . path . join ( i1Iii , OOOooOooo00O0 )
  try :
   os . remove ( oOOoOo00o )
  except :
   pass
  downloader . download ( url , oOOoOo00o , Oo0OO )
  o0OOoo0OO0OOO = xbmc . translatePath ( os . path . join ( 'special://' , 'home/' , 'addons' ) )
  xbmc . sleep ( 100 )
  Oo0OO . update ( 0 , "Instalando " + name + ", Por Favor Espere" )
  try :
   xbmc . executebuiltin ( "Extract(" + oOOoOo00o + "," + o0OOoo0OO0OOO + ")" )
  except :
   extract . all ( oOOoOo00o , o0OOoo0OO0OOO , Oo0OO )
   if 19 - 19: oO0o % i1IIi % OOo
   if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
  xbmc . sleep ( 100 )
  xbmc . executebuiltin ( "XBMC.UpdateLocalAddons()" )
  i1I1Iiii1111 ( name + ' Instalado com Sucesso!' )
  import database
  database . enable_addon ( addon_id )
  if addon_id == 'plugin.video.elementum' :
   database . enable_addon ( 'repository.elementum' )
   if 16 - 16: O0 - i1iIii1Ii1II * iIii1I11I1II1 + O0Oo0oO0o
  xbmc . executebuiltin ( "XBMC.Container.Update()" )
  xbmcgui . Dialog ( ) . ok ( '[B][COLOR white]AVISO[/COLOR][/B]' , '' + name + ' instalado com sucesso!\nObservação;\nÉ necessário Forçar Fechar o KODI para iniciar o Elementum no menu a seguir.\nFeche e abra o Kodi novamente!' )
  Ii11iII1 ( )
 except :
  i1I1Iiii1111 ( 'Erro ao baixar o complemento' )
  if 51 - 51: II111iiii * I1iII1iiII % OOo * II111iiii % I1II1 / OOo000
  if 49 - 49: OOo
  if 35 - 35: I1Ii111 - OoooooooOO / I1II1 % i1IIi
def Ii11iII1 ( ) :
 o00OO00OoO = xbmcgui . Dialog ( )
 I11II1i = o00OO00OoO . select ( '[B][COLOR white]FINALIZANDO INSTALAÇÃO DO ELEMENTUM[/COLOR][/B]' , [ '[COLOR white]SIM POR FAVOR! [/COLOR][COLOR orange]|[/COLOR] [COLOR lime]FORÇAR FECHAR[/COLOR]' , '[COLOR white]NÃO POR FAVOR! [/COLOR][COLOR orange]|[/COLOR] [COLOR red]NÃO CANCELAR[/COLOR]' ] )
 if 60 - 60: I1iII1iiII * I1Ii111 - I1iII1iiII % OoooooooOO - OOo000 + oo
 if I11II1i == 0 :
  xbmcplugin . endOfDirectory ( int ( os . _exit ( 1 ) ) )
  if 70 - 70: II1iI * OoO0O00 * o0oO0 / i111I
 if I11II1i == 1 :
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 88 - 88: O0
  if 64 - 64: o0oO0 * O0 + II1iI - OOO0o0o + i11iIiiIii * i111I
def iII ( ) :
 o0 = [ ]
 ooOooo000oOO = sys . argv [ 2 ]
 if len ( ooOooo000oOO ) >= 2 :
  Oo0oOOo = sys . argv [ 2 ]
  Oo0OoO00oOO0o = Oo0oOOo . replace ( '?' , '' )
  if ( Oo0oOOo [ len ( Oo0oOOo ) - 1 ] == '/' ) :
   Oo0oOOo = Oo0oOOo [ 0 : len ( Oo0oOOo ) - 2 ]
  OOO00O = Oo0OoO00oOO0o . split ( '&' )
  o0 = { }
  for OOoOO0oo0ooO in range ( len ( OOO00O ) ) :
   O0o0O00Oo0o0 = { }
   O0o0O00Oo0o0 = OOO00O [ OOoOO0oo0ooO ] . split ( '=' )
   if ( len ( O0o0O00Oo0o0 ) ) == 2 :
    o0 [ O0o0O00Oo0o0 [ 0 ] ] = O0o0O00Oo0o0 [ 1 ]
    if 87 - 87: OOo000 * OoO0O00 % i11iIiiIii % I1Ii111 - OOO0o0o
 return o0
 if 68 - 68: i1iIii1Ii1II % i1IIi . II1iI . I1II1
Oo0oOOo = iII ( )
o0oo0oOo = None
o000O0o = None
iI1iII1 = None
oO0OOoo0OO = None
O0ii1ii1ii = None
I1IIIii = None
if 91 - 91: II1iI
try :
 o0oo0oOo = urllib . unquote ( Oo0oOOo [ "url" ] )
 if 15 - 15: II111iiii
except :
 pass
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
try :
 if 75 - 75: I1Ii111 % OOo % OOo . i1iIii1Ii1II
 o000O0o = urllib . unquote_plus ( Oo0oOOo [ "name" ] )
except :
 pass
 if 5 - 5: OOo * OOo000 + I1Ii111 . OOO0o0o + I1Ii111
try :
 if 91 - 91: O0
 oO0OOoo0OO = urllib . unquote_plus ( Oo0oOOo [ "iconimage" ] )
except :
 pass
 if 61 - 61: II111iiii
try :
 iI1iII1 = int ( Oo0oOOo [ "mode" ] )
except :
 pass
 if 64 - 64: OOo000 / I1Ii111 - O0 - o0oO0
try :
 if 86 - 86: o0oO0 % I1Ii111 / oo / I1Ii111
 O0ii1ii1ii = urllib . unquote_plus ( Oo0oOOo [ "fanart" ] )
except :
 pass
 if 42 - 42: I1iII1iiII
try :
 if 67 - 67: i1iIii1Ii1II . O0Oo0oO0o . O0
 I1IIIii = urllib . unquote_plus ( Oo0oOOo [ "description" ] )
except :
 pass
 if 10 - 10: I1II1 % I1II1 - iIii1I11I1II1 / OOO0o0o + i111I
if iI1iII1 == None :
 xbmcplugin . setContent ( IIiIiII11i , 'movies' )
 Oooo ( ) # Team KelTec Media'Play
