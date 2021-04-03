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
# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import xbmc
import xbmcgui
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import os
import re
if 73 - 73: II111iiii
try :
 from urllib . parse import quote_plus
except ImportError :
 from urllib import quote_plus
 if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
from resources . libs . common import logging
from resources . libs . common import tools
from resources . libs . common . config import CONFIG
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
i1I1ii1II1iII = 10
oooO0oo0oOOOO = 92
O0oO = 1
o0oO0 = 2
oo00 = 3
o00 = 4
Oo0oO0ooo = 104
o0oOoO00o = 105
i1 = 107
oOOoo00O0O = 7
i1111 = 110
i11 = 100
I11 = 108
if 98 - 98: i11iIiiIii * I1IiiI % iII111i * iII111i * II111iiii
o0o0Oo0oooo0 = [ i1I1ii1II1iII , oooO0oo0oOOOO , i1111 ]
if 97 - 97: Oo0Ooo - ooOoO0o
if 54 - 54: ooOoO0o . ooOoO0o / iIii1I11I1II1 / I11i + oO0o / o0oOOo0O0Ooo
def I1i1I ( msg ) :
 msg = msg . replace ( '\n' , '[NL]' )
 OOoOoo00oo = re . compile ( "-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--" ) . findall ( msg )
 for iiI11 in OOoOoo00oo :
  OOooO = '-->Python callback/script returned the following error<--{0}-->End of Python script error report<--' . format ( iiI11 )
  msg = msg . replace ( OOooO , '[COLOR red]{0}[/COLOR]' . format ( OOooO ) )
 msg = msg . replace ( 'WARNING' , '[COLOR yellow]WARNING[/COLOR]' ) . replace ( 'ERROR' , '[COLOR red]ERROR[/COLOR]' ) . replace ( '[NL]' , '\n' ) . replace ( ': EXCEPTION Thrown (PythonToCppException) :' , '[COLOR red]: EXCEPTION Thrown (PythonToCppException) :[/COLOR]' )
 msg = msg . replace ( '\\\\' , '\\' ) . replace ( CONFIG . HOME , '' )
 return msg
 if 58 - 58: OoO0O00 + OoOoOO00 / Ii1I * OoooooooOO
 if 9 - 9: I1IiiI - Ii1I % i1IIi % OoooooooOO
def i1iIIi1 ( file ) :
 if file == 'button' :
  return os . path . join ( CONFIG . SKIN , 'Button' , 'button-focus_lightblue.png' ) , os . path . join ( CONFIG . SKIN , 'Button' , 'button-focus_grey.png' )
  if 50 - 50: i11iIiiIii - Ii1I
 elif file == 'radio' :
  return os . path . join ( CONFIG . SKIN , 'RadioButton' , 'MenuItemFO.png' ) , os . path . join ( CONFIG . SKIN , 'RadioButton' , 'MenuItemNF.png' ) , os . path . join ( CONFIG . SKIN , 'RadioButton' , 'radiobutton-focus.png' ) , os . path . join ( CONFIG . SKIN , 'RadioButton' , 'radiobutton-nofocus.png' )
  if 78 - 78: OoO0O00
  if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
  if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
 elif file == 'slider' :
  return os . path . join ( CONFIG . SKIN , 'Slider' , 'osd_slider_nib.png' ) , os . path . join ( CONFIG . SKIN , 'Slider' , 'osd_slider_nibNF.png' ) , os . path . join ( CONFIG . SKIN , 'Slider' , 'slider1.png' ) , os . path . join ( CONFIG . SKIN , 'Slider' , 'slider1.png' )
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
  if 14 - 14: I11i % O0
  if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
  if 77 - 77: Oo0Ooo . IiII % ooOoO0o
  if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
def iIi ( window , active = False , count = 0 , counter = 15 ) :
 II = xbmc . getCondVisibility ( 'Window.IsActive({0})' . format ( window ) )
 logging . log ( "{0} is {1}" . format ( window , II ) )
 while not II and count < counter :
  logging . log ( "{0} is {1}({2})" . format ( window , II , count ) )
  II = xbmc . getCondVisibility ( 'Window.IsActive({0})' . format ( window ) )
  count += 1
  xbmc . sleep ( 500 )
  if 14 - 14: Oo0Ooo . I1IiiI / Ii1I
 while II :
  active = True
  logging . log ( "{0} is {1}" . format ( window , II ) )
  II = xbmc . getCondVisibility ( 'Window.IsActive({0})' . format ( window ) )
  xbmc . sleep ( 250 )
  if 38 - 38: II111iiii % i11iIiiIii . ooOoO0o - OOooOOo + Ii1I
 return active
 if 66 - 66: OoooooooOO * OoooooooOO . OOooOOo . i1IIi - OOooOOo
 if 77 - 77: I11i - iIii1I11I1II1
def Ooo ( title , msg ) :
 class O0o0Oo ( xbmcgui . WindowXMLDialog ) :
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . closebutton = 201
   if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
   self . setProperty ( 'texture.color1' , CONFIG . COLOR1 )
   self . setProperty ( 'texture.color2' , CONFIG . COLOR2 )
   self . setProperty ( 'message.title' , title )
   self . setProperty ( 'message.msg' , msg )
   if 11 - 11: iII111i - OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
  def onClick ( self , controlid ) :
   if controlid == self . closebutton :
    self . close ( )
    if 74 - 74: iII111i * O0
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close ( )
    if 89 - 89: oO0o + Oo0Ooo
 Ii1IOo0o0 = O0o0Oo ( "text_box.xml" , CONFIG . ADDON_PATH , 'Default' , title = title , msg = msg )
 Ii1IOo0o0 . doModal ( )
 del Ii1IOo0o0
 if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
 if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
def i1iiI11I ( msg = "" ) :
 class iiii ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . title = CONFIG . THEME3 . format ( kwargs [ "title" ] )
   self . image = kwargs [ "image" ]
   self . fanart = kwargs [ "fanart" ]
   self . msg = CONFIG . THEME2 . format ( kwargs [ "msg" ] )
   if 54 - 54: I1ii11iIi11i * OOooOOo
  def onInit ( self ) :
   self . fanartimage = 101
   self . titlebox = 102
   self . imagecontrol = 103
   self . textbox = 104
   self . scrollcontrol = 105
   self . show_dialog ( )
   if 13 - 13: IiII + OoOoOO00 - OoooooooOO + I1Ii111 . iII111i + OoO0O00
  def show_dialog ( self ) :
   self . getControl ( self . imagecontrol ) . setImage ( self . image )
   self . getControl ( self . fanartimage ) . setImage ( self . fanart )
   self . getControl ( self . fanartimage ) . setColorDiffuse ( '9FFFFFFF' )
   self . getControl ( self . textbox ) . setText ( self . msg )
   self . getControl ( self . titlebox ) . setLabel ( self . title )
   self . setFocusId ( self . scrollcontrol )
   if 8 - 8: iIii1I11I1II1 . I1IiiI - iIii1I11I1II1 * Ii1I
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close ( )
    if 61 - 61: o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * oO0o / oO0o
 OoOo = iiii ( "Contact.xml" , CONFIG . ADDON_PATH , 'Default' , title = CONFIG . ADDONTITLE , fanart = CONFIG . CONTACTFANART ,
 image = CONFIG . CONTACTICON , msg = msg )
 OoOo . doModal ( )
 del OoOo
 if 18 - 18: i11iIiiIii
 if 46 - 46: i1IIi / I11i % OOooOOo + I1Ii111
def O0OOO00oo ( layout , imagefile , message ) :
 class Iii111II ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . image = kwargs [ "image" ]
   self . text = kwargs [ "text" ]
   if 9 - 9: OoO0O00
  def onInit ( self ) :
   self . imagecontrol = 501
   self . textbox = 502
   self . okbutton = 503
   self . title = 504
   self . show_dialog ( )
   if 33 - 33: ooOoO0o . iII111i
  def show_dialog ( self ) :
   self . getControl ( self . imagecontrol ) . setImage ( self . image )
   self . getControl ( self . textbox ) . setText ( self . text )
   self . getControl ( self . title ) . setLabel ( CONFIG . ADDONTITLE )
   self . setFocus ( self . getControl ( self . okbutton ) )
   if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  def onClick ( self , controlid ) :
   if controlid == self . okbutton :
    self . close ( )
    if 50 - 50: I1IiiI
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close ( )
    if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
 II1III = Iii111II ( layout , CONFIG . ADDON_PATH , 'Default' , image = imagefile , text = message )
 II1III . doModal ( )
 del II1III
 if 19 - 19: oO0o % i1IIi % o0oOOo0O0Ooo
 if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
def Ii11Ii1I ( apk ) :
 class O00oO ( xbmcgui . WindowXMLDialog ) :
  if 39 - 39: IiII - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  def __init__ ( self , * args , ** kwargs ) :
   self . shut = kwargs [ 'close_time' ]
   xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
   xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
   if 59 - 59: iIii1I11I1II1 + I1IiiI - o0oOOo0O0Ooo - I1IiiI + OOooOOo / I1ii11iIi11i
  def onClick ( self , controlid ) :
   self . close_window ( )
   if 24 - 24: I11i . iII111i % OOooOOo + ooOoO0o % OoOoOO00
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close_window ( )
    if 4 - 4: IiII - OoO0O00 * OoOoOO00 - I11i
  def close_window ( self ) :
   xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
   xbmc . sleep ( 400 )
   self . close ( )
   if 41 - 41: OoOoOO00 . I1IiiI * oO0o % IiII
 xbmc . executebuiltin ( 'Skin.SetString(apkinstaller, Now that {0} has been downloaded[CR]Click install on the next window!)' . format ( apk ) )
 Oo000o = O00oO ( 'APK.xml' , CONFIG . ADDON_PATH , 'Default' , close_time = 34 )
 Oo000o . doModal ( )
 del Oo000o
 if 7 - 7: ooOoO0o * OoO0O00 % oO0o . IiII
 if 45 - 45: i11iIiiIii * II111iiii % iIii1I11I1II1 + I1ii11iIi11i - Ii1I
def iIi1iIiii111 ( img ) :
 class iIIIi1 ( xbmcgui . WindowXMLDialog ) :
  if 20 - 20: i1IIi + I1ii11iIi11i - ooOoO0o
  def __init__ ( self , * args , ** kwargs ) :
   self . imgfile = kwargs [ 'img' ]
   if 30 - 30: II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - II111iiii * Ii1I
  def onInit ( self ) :
   self . imagespeed = 101
   self . button = 201
   self . show_dialog ( )
   if 61 - 61: oO0o - I11i % OOooOOo
  def show_dialog ( self ) :
   self . setFocus ( self . getControl ( self . button ) )
   self . getControl ( self . imagespeed ) . setImage ( self . imgfile )
   if 84 - 84: oO0o * OoO0O00 / I11i - O0
  def onClick ( self , controlid ) :
   self . close ( )
   if 30 - 30: iIii1I11I1II1 / ooOoO0o - I1Ii111 - II111iiii % iII111i
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close ( )
    if 49 - 49: I1IiiI % ooOoO0o . ooOoO0o . I11i * ooOoO0o
 Oo000o = iIIIi1 ( 'SpeedTest.xml' , CONFIG . ADDON_PATH , 'Default' , img = img )
 Oo000o . doModal ( )
 del Oo000o
 if 97 - 97: Ii1I + o0oOOo0O0Ooo . OOooOOo + I1ii11iIi11i % iII111i
 if 95 - 95: i1IIi
def I1ii11iI ( ) :
 class IIi1i ( xbmcgui . WindowXMLDialog ) :
  if 46 - 46: I1Ii111 % I11i + OoO0O00 . OoOoOO00 . OoO0O00
  def __init__ ( self , * args , ** kwargs ) :
   self . whitelistcurrent = kwargs [ 'current' ]
   if 96 - 96: Oo0Ooo
  def onInit ( self ) :
   self . title = 101
   self . okbutton = 201
   self . trakt = 301
   self . debrid = 302
   self . login = 303
   self . sources = 304
   self . profiles = 305
   self . playercore = 314
   self . guisettings = 315
   self . advanced = 306
   self . favourites = 307
   self . superfav = 308
   self . repo = 309
   self . whitelist = 310
   self . cache = 311
   self . packages = 312
   self . thumbs = 313
   self . show_dialog ( )
   self . controllist = [ self . trakt , self . debrid , self . login ,
 self . sources , self . profiles , self . playercore , self . guisettings , self . advanced ,
 self . favourites , self . superfav , self . repo ,
 self . whitelist , self . cache , self . packages ,
 self . thumbs ]
   self . controlsettings = [ 'keeptrakt' , 'keepdebrid' , 'keeplogin' ,
 'keepsources' , 'keepprofiles' , 'keepplayercore' , 'keepguisettings' , 'keepadvanced' ,
 'keepfavourites' , 'keeprepos' , 'keepsuper' ,
 'keepwhitelist' , 'clearcache' , 'clearpackages' ,
 'clearthumbs' ]
   for iiI11 in self . controllist :
    if CONFIG . get_setting ( self . controlsettings [ self . controllist . index ( iiI11 ) ] ) == 'true' :
     self . getControl ( iiI11 ) . setSelected ( True )
     if 45 - 45: O0 * o0oOOo0O0Ooo % Oo0Ooo * OoooooooOO + iII111i . OoOoOO00
  def show_dialog ( self ) :
   self . getControl ( self . title ) . setLabel ( CONFIG . ADDONTITLE )
   self . setFocus ( self . getControl ( self . okbutton ) )
   if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
  def onClick ( self , controlid ) :
   if controlid == self . okbutton :
    if 77 - 77: IiII / I1IiiI
    for iiI11 in self . controllist :
     I1 = self . controllist . index ( iiI11 )
     if self . getControl ( iiI11 ) . isSelected ( ) :
      CONFIG . set_setting ( self . controlsettings [ I1 ] , 'true' )
     else :
      CONFIG . set_setting ( self . controlsettings [ I1 ] , 'false' )
      if 15 - 15: II111iiii
    if self . getControl ( self . whitelist ) . isSelected ( ) and not self . whitelistcurrent == 'true' :
     from resources . libs import whitelist
     whitelist . whitelist ( 'edit' )
     if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
    self . close ( )
    if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close ( )
    if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
 oO = IIi1i ( "FirstRunSaveData.xml" , CONFIG . ADDON_PATH , 'Default' , current = CONFIG . KEEPWHITELIST )
 oO . doModal ( )
 CONFIG . set_setting ( 'first_install' , 'false' )
 del oO
 if 7 - 7: o0oOOo0O0Ooo - I1IiiI
 if 100 - 100: oO0o + I11i . OOooOOo * Ii1I
def ooOOOoO ( ) :
 class o0o ( xbmcgui . WindowXMLDialog ) :
  if 84 - 84: O0
  def __init__ ( self , * args , ** kwargs ) :
   self . title = CONFIG . THEME3 . format ( CONFIG . ADDONTITLE )
   self . msg = "Atualmente nenhuma compilação instalada de {0}.\n\nSelecione 'Menu Build' para instalar um Community Build nosso ou 'Ignorar' para nunca mais ver esta mensagem.\n\nObrigado por escolher {1}." . format ( CONFIG . ADDONTITLE , CONFIG . ADDONTITLE )
   self . msg = CONFIG . THEME2 . format ( self . msg )
   if 74 - 74: I1ii11iIi11i - I1IiiI - Oo0Ooo . Ii1I - IiII
  def onInit ( self ) :
   self . image = 101
   self . titlebox = 102
   self . textbox = 103
   self . buildmenu = 201
   self . ignore = 202
   self . show_dialog ( )
   if 73 - 73: Oo0Ooo - i1IIi - i1IIi - iII111i . Ii1I + I1ii11iIi11i
  def show_dialog ( self ) :
   self . getControl ( self . image ) . setImage ( CONFIG . ADDON_FANART )
   self . getControl ( self . image ) . setColorDiffuse ( '9FFFFFFF' )
   self . getControl ( self . textbox ) . setText ( self . msg )
   self . getControl ( self . titlebox ) . setLabel ( self . title )
   self . setFocusId ( self . buildmenu )
   if 81 - 81: iII111i * oO0o - I1Ii111 . II111iiii % I11i / I1IiiI
  def do_build_menu ( self ) :
   logging . log ( "[Verificação de compilação atual] [Selecionado pelo usuário: Abrir menu de compilação] [Próxima verificação: {0}]" . format ( CONFIG . BUILDCHECK ) ,
 level = xbmc . LOGINFO )
   CONFIG . set_setting ( 'nextbuildcheck' , tools . get_date ( days = CONFIG . UPDATECHECK , formatted = True ) )
   CONFIG . set_setting ( 'installed' , 'ignored' )
   if 34 - 34: IiII
   oOo = 'plugin://{0}/?mode=builds' . format ( CONFIG . ADDON_ID )
   if 75 - 75: I1IiiI + Oo0Ooo
   self . close ( )
   if 73 - 73: O0 - OoooooooOO . OOooOOo - OOooOOo / OoOoOO00
   xbmc . executebuiltin ( 'ActivateWindow(Programs, {0}, return)' . format ( oOo ) )
   if 45 - 45: iIii1I11I1II1 % OoO0O00
  def do_ignore ( self ) :
   logging . log ( "[Verificação da compilação atual] [Selecionado pelo usuário: Menu Ignorar compilação] [Verificação seguinte: {0}]" . format ( CONFIG . BUILDCHECK ) ,
 level = xbmc . LOGINFO )
   CONFIG . set_setting ( 'nextbuildcheck' , tools . get_date ( days = CONFIG . UPDATECHECK , formatted = True ) )
   CONFIG . set_setting ( 'installed' , 'ignored' )
   if 29 - 29: OOooOOo + Oo0Ooo . i11iIiiIii - i1IIi / iIii1I11I1II1
   self . close ( )
   if 26 - 26: I11i . OoooooooOO
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . do_ignore ( )
    if 39 - 39: iII111i - O0 % i11iIiiIii * I1Ii111 . IiII
  def onClick ( self , controlid ) :
   if controlid == self . buildmenu :
    self . do_build_menu ( )
   elif controlid == self . ignore :
    self . do_ignore ( )
    if 58 - 58: OoO0O00 % i11iIiiIii . iII111i / oO0o
 oO = o0o ( "FirstRunBuild.xml" , CONFIG . ADDON_PATH , 'Default' )
 oO . doModal ( )
 del oO
 if 84 - 84: iII111i . I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
 if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
def IIi1I11I1II ( name = 'Testing Window' , current = '1.0' , new = '1.1' , icon = CONFIG . ADDON_ICON , fanart = CONFIG . ADDON_FANART ) :
 class OooOoooOo ( xbmcgui . WindowXMLDialog ) :
  if 46 - 46: iII111i
  def __init__ ( self , * args , ** kwargs ) :
   self . name = CONFIG . THEME3 . format ( kwargs [ 'name' ] )
   self . current = kwargs [ 'current' ]
   self . new = kwargs [ 'new' ]
   self . icon = kwargs [ 'icon' ]
   self . fanart = kwargs [ 'fanart' ]
   self . msgupdate = "Atualização disponível para compilação instalada:\n[COLOR {0}]{1}[/COLOR]\n\nVersão Atual: v[COLOR {2}]{3}[/COLOR]\nÚltima versão: v[COLOR {4}]{5}[/COLOR]\n\n[COLOR {6}]*Recomendado: nova instalação[/COLOR]" . format ( CONFIG . COLOR1 , self . name , CONFIG . COLOR1 , self . current , CONFIG . COLOR1 , self . new , CONFIG . COLOR1 )
   self . msgcurrent = "Executando a versão mais recente da compilação instalada:\n[COLOR {0}]{1}[/COLOR]\n\nVersão Atual: v[COLOR {2}]{3}[/COLOR]\nÚltima versão: v[COLOR {4}]{5}[/COLOR]\n\n[COLOR {6}]*Recomendado: nova instalação[/COLOR]" . format ( CONFIG . COLOR1 , self . name , CONFIG . COLOR1 , self . current , CONFIG . COLOR1 , self . new , CONFIG . COLOR1 )
   if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
  def onInit ( self ) :
   self . imagefanart = 101
   self . header = 102
   self . textbox = 103
   self . imageicon = 104
   self . fresh = 201
   self . normal = 202
   self . ignore = 203
   if 48 - 48: O0
   self . setProperty ( 'dialog.header' , self . name )
   self . setProperty ( 'dialog.textbox' , CONFIG . THEME2 . format ( self . msgupdate if current < new else self . msgcurrent ) )
   self . setProperty ( 'dialog.imagefanart' , self . fanart )
   self . setProperty ( 'dialog.imagediffuse' , '2FFFFFFF' )
   self . setProperty ( 'dialog.imageicon' , self . icon )
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
  def do_fresh_install ( self ) :
   logging . log ( "[Verificar atualizações] [Versão Instalada: {0}] [Versão Atual: {1}] [User Selected: Fresh Install build]" . format ( CONFIG . BUILDVERSION , CONFIG . BUILDLATEST ) )
   logging . log ( "[Verificar atualizações] [Next Check: {0}]" . format ( tools . get_date ( days = CONFIG . UPDATECHECK , formatted = True ) ) )
   oOo = 'plugin://{0}/?mode=install&name={1}&action=fresh' . format ( CONFIG . ADDON_ID , quote_plus ( CONFIG . BUILDNAME ) )
   xbmc . executebuiltin ( 'RunPlugin({0})' . format ( oOo ) )
   self . close ( )
   if 41 - 41: Ii1I - O0 - O0
  def do_normal_install ( self ) :
   logging . log ( "[Verificar atualizações] [Versão Instalada: {0}] [Versão Atual: {1}] [User Selected: Normal Install build]" . format ( CONFIG . BUILDVERSION , CONFIG . BUILDLATEST ) )
   logging . log ( "[Verificar atualizações] [Next Check: {0}]" . format ( tools . get_date ( days = CONFIG . UPDATECHECK , formatted = True ) ) )
   oOo = 'plugin://{0}/?mode=install&name={1}&action=normal' . format ( CONFIG . ADDON_ID , quote_plus ( CONFIG . BUILDNAME ) )
   xbmc . executebuiltin ( 'RunPlugin({0})' . format ( oOo ) )
   self . close ( )
   if 68 - 68: OOooOOo % I1Ii111
  def do_ignore ( self ) :
   logging . log ( "[Verificar atualizações] [Versão Instalada: {0}] [Versão Atual: {1}] [Selecionado pelo usuário: Ignore {2} Dias]" . format ( CONFIG . BUILDVERSION , CONFIG . BUILDLATEST , CONFIG . UPDATECHECK ) )
   logging . log ( "[Verificar atualizações] [Next Check: {0}]" . format ( tools . get_date ( days = CONFIG . UPDATECHECK , formatted = True ) ) )
   self . close ( )
   if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
  def onAction ( self , action ) :
   id = action . getId ( )
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . do_ignore ( )
    if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
  def onClick ( self , controlid ) :
   if controlid == self . fresh :
    self . do_fresh_install ( )
   elif controlid == self . normal :
    self . do_normal_install ( )
   elif controlid == self . ignore :
    self . do_ignore ( )
    if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
    if 23 - 23: O0
    if 85 - 85: Ii1I
    if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
 IIi1 = 'Executando a versão mais recente da compilação instalada: '
 I1I1I = 'Update available for installed build: '
 OoOO000 = '[COLOR {0}]{1}[/COLOR]' . format ( CONFIG . COLOR1 , name )
 i1Ii11i1i = 'Versão Atual: v[COLOR {0}]{1}[/COLOR]' . format ( CONFIG . COLOR1 , current )
 o0oOOoo = 'Última versão: v[COLOR {0}]{1}[/COLOR]' . format ( CONFIG . COLOR1 , new )
 if 51 - 51: Oo0Ooo * i11iIiiIii
 O0oo00o0O = '{0}{1}\n{2}\n{3}\n' . format ( IIi1 if current >= new else I1I1I ,
 OoOO000 , i1Ii11i1i , o0oOOoo )
 if 1 - 1: II111iiii
 OOooooO0Oo = xbmcgui . Dialog ( ) . yesno ( CONFIG . ADDONTITLE , O0oo00o0O ,
 yeslabel = 'Install' , nolabel = 'Ignore' )
 if OOooooO0Oo :
  from resources . libs . wizard import Wizard
  Wizard ( ) . build ( CONFIG . BUILDNAME )
  if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / oO0o + i1IIi
  if 42 - 42: ooOoO0o . o0oOOo0O0Ooo . ooOoO0o - I1ii11iIi11i
def i1ii1I1I1 ( notify ) :
 oOoO0O0o0Oooo = tools . open_url ( notify )
 if 5 - 5: ooOoO0o - II111iiii - OoooooooOO % Ii1I + I1IiiI * iIii1I11I1II1
 if oOoO0O0o0Oooo :
  I1I1II1I11 = oOoO0O0o0Oooo . text
  if 8 - 8: o0oOOo0O0Ooo % O0 / I1IiiI - oO0o
  try :
   I1I1II1I11 = oOoO0O0o0Oooo . text . decode ( 'utf-8' )
  except :
   pass
   if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
  I1I1II1I11 = I1I1II1I11 . replace ( '\r' , '' ) . replace ( '\t' , '    ' ) . replace ( '\n' , '[CR]' )
  if I1I1II1I11 . find ( '|||' ) == - 1 :
   return False , False
   if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  o0 , iI11I1II = I1I1II1I11 . split ( '|||' )
  o0 = o0 . replace ( '[CR]' , '' )
  if iI11I1II . startswith ( '[CR]' ) :
   iI11I1II = iI11I1II [ 4 : ]
   if 40 - 40: iIii1I11I1II1 / OoOoOO00 % I1ii11iIi11i + II111iiii
  return o0 , iI11I1II
 else :
  return False , False
  if 27 - 27: II111iiii * OoOoOO00 * iIii1I11I1II1
  if 86 - 86: OoO0O00 * OOooOOo . iII111i
def iI ( msg , test = False ) :
 class O0O0Oooo0o ( xbmcgui . WindowXMLDialog ) :
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  def __init__ ( self , * args , ** kwargs ) :
   self . test = kwargs [ 'test' ]
   self . msg = kwargs [ 'msg' ]
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  def onInit ( self ) :
   self . image = 101
   self . titlebox = 102
   self . titleimage = 103
   self . textbox = 104
   self . scroller = 105
   self . dismiss = 201
   self . remindme = 202
   self . show_dialog ( )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  def show_dialog ( self ) :
   self . testimage = os . path . join ( CONFIG . ART , 'text.png' )
   self . getControl ( self . image ) . setImage ( CONFIG . BACKGROUND )
   self . getControl ( self . image ) . setColorDiffuse ( '9FFFFFFF' )
   I111iI = CONFIG . THEME2 . format ( self . msg )
   self . getControl ( self . textbox ) . setText ( I111iI )
   self . setFocusId ( self . remindme )
   if CONFIG . HEADERTYPE == 'Text' :
    self . getControl ( self . titlebox ) . setLabel ( CONFIG . THEME3 . format ( CONFIG . HEADERMESSAGE ) )
   else :
    self . getControl ( self . titleimage ) . setImage ( CONFIG . HEADERIMAGE )
    if 56 - 56: I1IiiI
  def do_remind ( self ) :
   if not test :
    CONFIG . set_setting ( 'notedismiss' , 'false' )
   logging . log ( '[Notifications] Notification {0} Remind Me Later' . format ( CONFIG . get_setting ( 'noteid' ) ) )
   self . close ( )
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  def do_dismiss ( self ) :
   if not test :
    CONFIG . set_setting ( 'notedismiss' , 'true' )
   logging . log ( '[Notifications] Notification {0} Dismissed' . format ( CONFIG . get_setting ( 'noteid' ) ) )
   self . close ( )
   if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . do_remind ( )
    if 63 - 63: OoOoOO00 * iII111i
  def onClick ( self , controlid ) :
   if controlid == self . dismiss :
    self . do_dismiss ( )
   elif controlid == self . remindme :
    self . do_remind ( )
    if 69 - 69: O0 . OoO0O00
 xbmc . executebuiltin ( 'Skin.SetString(headertexttype, {0})' . format ( 'true' if CONFIG . HEADERTYPE == 'Text' else 'false' ) )
 xbmc . executebuiltin ( 'Skin.SetString(headerimagetype, {0})' . format ( 'true' if CONFIG . HEADERTYPE == 'Image' else 'false' ) )
 ii1111iII = O0O0Oooo0o ( "Notifications.xml" , CONFIG . ADDON_PATH , 'Default' , msg = msg , test = test )
 ii1111iII . doModal ( )
 del ii1111iII
 if 32 - 32: i1IIi / II111iiii . Oo0Ooo
 if 62 - 62: OoooooooOO * I1IiiI
def oOOOoo0O0oO ( window_title = "Viewing Log File" , window_msg = None , log_file = None , ext_buttons = False ) :
 class iIII1I111III ( xbmcgui . WindowXMLDialog ) :
  def __init__ ( self , * args , ** kwargs ) :
   self . log_file = kwargs [ 'log_file' ]
   if 20 - 20: o0oOOo0O0Ooo . II111iiii % OOooOOo * iIii1I11I1II1
  def onInit ( self ) :
   self . title = 101
   self . msg = 102
   self . scrollbar = 103
   self . upload = 201
   self . kodilog = 202
   self . oldlog = 203
   self . wizardlog = 204
   self . closebutton = 205
   if 98 - 98: I1IiiI % Ii1I * OoooooooOO
   if window_msg is None :
    self . logmsg = tools . read_from_file ( self . log_file )
   else :
    self . logmsg = window_msg
   self . logfile = os . path . basename ( self . log_file )
   if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
   self . buttons = 'true' if ext_buttons else 'false'
   if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
   self . setProperty ( 'texture.color1' , CONFIG . COLOR1 )
   self . setProperty ( 'texture.color2' , CONFIG . COLOR2 )
   self . setProperty ( 'message.title' , window_title )
   self . setProperty ( 'message.logmsg' , I1i1I ( self . logmsg ) )
   self . setProperty ( 'message.logfile' , self . logfile )
   self . setProperty ( 'message.buttons' , self . buttons )
   if 71 - 71: Oo0Ooo % OOooOOo
  def onClick ( self , controlId ) :
   if controlId == self . closebutton :
    self . close ( )
   elif controlId == self . upload :
    self . close ( )
    logging . upload_log ( )
   elif controlId in [ self . kodilog , self . oldlog , self . wizardlog ] :
    if controlId == self . kodilog :
     O00oO000O0O = logging . grab_log ( )
     I1i1i1iii = logging . grab_log ( file = True )
    elif controlId == self . oldlog :
     O00oO000O0O = logging . grab_log ( old = True )
     I1i1i1iii = logging . grab_log ( file = True , old = True )
    elif controlId == self . wizardlog :
     O00oO000O0O = logging . grab_log ( wizard = True )
     I1i1i1iii = logging . grab_log ( file = True , wizard = True )
     if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
    if not O00oO000O0O :
     self . setProperty ( 'message.title' , "Error Viewing Log File" )
     self . setProperty ( 'message.logmsg' , "File does not exist or could not be read." )
    else :
     self . logmsg = O00oO000O0O
     self . logfile = os . path . basename ( I1i1i1iii )
     if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
     self . setProperty ( 'message.logmsg' , I1i1I ( self . logmsg ) )
     self . setProperty ( 'message.logfile' , self . logfile )
     if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
  def onAction ( self , action ) :
   if action . getId ( ) in o0o0Oo0oooo0 :
    self . close ( )
    if 71 - 71: I1Ii111 + Ii1I
 if log_file is None :
  log_file = logging . grab_log ( file = True )
  if 28 - 28: OOooOOo
 I11ii1IIiIi = iIII1I111III ( "log_viewer.xml" , CONFIG . ADDON_PATH , 'Default' , log_file = log_file )
 I11ii1IIiIi . doModal ( )
 del I11ii1IIiIi
# Team KelTec Media'Play