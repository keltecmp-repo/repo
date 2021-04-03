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
import xbmcgui
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import os
if 73 - 73: II111iiii
from resources . libs . common . config import CONFIG
from resources . libs . common import directory
from resources . libs . common import logging
from resources . libs . common import tools
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
def IiiIII111iI ( addon ) :
 IiII = os . path . join ( CONFIG . ADDONS , addon , 'addon.xml' )
 if os . path . exists ( IiII ) :
  try :
   iI1Ii11111iIi = tools . parse_dom ( tools . read_from_file ( IiII ) , 'addon' , ret = 'name' , attrs = { 'id' : addon } )
   i1i1II = os . path . join ( CONFIG . ADDONS , addon , 'icon.png' )
   logging . log_notify ( '[COLOR {0}]{1}[/COLOR]' . format ( CONFIG . COLOR1 , iI1Ii11111iIi [ 0 ] ) ,
 '[COLOR {0}]Add-on ativado[/COLOR]' . format ( CONFIG . COLOR2 ) , '2000' , i1i1II )
  except :
   pass
   if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / Oo0ooO0oo0oO * Oo0Ooo
   if 16 - 16: oO0o % OOooOOo * o0OO0 . OOooOOo / iIii1I11I1II1 * iIii1I11I1II1
def II1iI ( plugin ) :
 import time
 if 27 - 27: o0OO0 * OoO0O00 . II111iiii
 Ii1IIii11 = 'System.HasAddon({0})' . format ( plugin )
 Oooo0000 = 'Window.IsTopMost(yesnodialog)'
 if 22 - 22: Ii1I . Oo0ooO0oo0oO
 if xbmc . getCondVisibility ( Ii1IIii11 ) :
  logging . log ( 'Já instalado ' + plugin , level = xbmc . LOGDEBUG )
  return True
  if 41 - 41: I1i1iI1i . o00ooo0 * Oo0ooO0oo0oO % i11iIiiIii
 logging . log ( 'Baixando ' + plugin , level = xbmc . LOGDEBUG )
 xbmc . executebuiltin ( 'InstallAddon({0})' . format ( plugin ) )
 if 74 - 74: o0OO0 * Oo0ooO0oo0oO
 oo00o0Oo0oo = False
 i1iII1I1i1i1 = time . time ( )
 i1iIIII = 20
 while not xbmc . getCondVisibility ( Ii1IIii11 ) :
  if time . time ( ) >= i1iII1I1i1i1 + i1iIIII :
   logging . log ( 'Instalação expirada' , level = xbmc . LOGDEBUG )
   return False
   if 26 - 26: I1i1iI1i . I11i - OOooOOo % O0 + OOooOOo
  xbmc . sleep ( 500 )
  if 34 - 34: I11i * I1IiiI
  if 31 - 31: II111iiii + OoO0O00 . I1i1iI1i
  if xbmc . getCondVisibility ( Oooo0000 ) and not oo00o0Oo0oo :
   logging . log ( 'Caixa de diálogo para clicar em abrir' , level = xbmc . LOGDEBUG )
   xbmc . executebuiltin ( 'SendClick(yesnodialog, 11)' )
   oo00o0Oo0oo = True
  else :
   logging . log ( '...espera' , level = xbmc . LOGDEBUG )
   if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
 logging . log ( 'Instalado {0}!' . format ( plugin ) , level = xbmc . LOGDEBUG )
 return True
 if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
 if 3 - 3: o0OO0 + O0
class I1Ii :
 def __init__ ( self ) :
  self . dialog = xbmcgui . Dialog ( )
  self . progress_dialog = xbmcgui . DialogProgress ( )
  if 66 - 66: Ii1I
 def show_menu ( self , url = None ) :
  oo0Ooo0 = tools . open_url ( CONFIG . ADDONFILE )
  I1I11I1I1I = tools . open_url ( url )
  OooO0OO = os . path . join ( CONFIG . ADDON_PATH , 'resources' , 'text' , 'addons.json' )
  if 28 - 28: II111iiii
  if I1I11I1I1I :
   iii11iII = I1I11I1I1I . text
  elif oo0Ooo0 :
   iii11iII = oo0Ooo0 . text
  elif os . path . exists ( OooO0OO ) :
   iii11iII = tools . read_from_file ( OooO0OO )
  else :
   iii11iII = None
   logging . log ( "[Menu Addon] Nenhuma lista Addon adicionada." )
   if 42 - 42: I1i1iI1i + I1ii11iIi11i
  if iii11iII :
   import json
   if 70 - 70: Oo0Ooo % Oo0Ooo . Oo0ooO0oo0oO % OoO0O00 * o0oOOo0O0Ooo % oO0o
   try :
    iiI1IiI = json . loads ( iii11iII )
   except :
    iiI1IiI = None
    logging . log ( "[Configurações avançadas] ERRO: Formato inválido para {0}." . format ( iii11iII ) )
    if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
   if iiI1IiI :
    ii1I = iiI1IiI [ 'addons' ]
    if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
    if ii1I and len ( ii1I ) > 0 :
     for Oooo in ii1I :
      O00o = Oooo . get ( 'name' , '' )
      type = Oooo . get ( 'type' , 'addon' )
      O00 = Oooo . get ( 'section' , False )
      i11I1 = Oooo . get ( 'plugin' , '' )
      Ii11Ii11I = Oooo . get ( 'url' , '' )
      iI11i1I1 = Oooo . get ( 'repository' , '' )
      o0o0OOO0o0 = Oooo . get ( 'repositoryxml' , '' )
      ooOOOo0oo0O0 = Oooo . get ( 'repositoryurl' , '' )
      i1i1II = Oooo . get ( 'icon' , CONFIG . ADDON_ICON )
      o0 = Oooo . get ( 'fanart' , CONFIG . ADDON_FANART )
      I11II1i = Oooo . get ( 'adult' , False )
      IIIII = Oooo . get ( 'description' , '' )
      if 75 - 75: II111iiii % II111iiii
      if not O00o :
       logging . log ( '[Configurações avançadas] Tag ausente \'name\'' , level = xbmc . LOGDEBUG )
       continue
       if 13 - 13: o0oOOo0O0Ooo . Ii1I
      if not Ii11Ii11I :
       logging . log ( '[Configurações avançadas] Tag ausente \'url\'' , level = xbmc . LOGDEBUG )
       continue
      else :
       if '.zip' in Ii11Ii11I :
        pass
       elif not O00 :
        i11Iiii = False
        if not iI11i1I1 :
         logging . log ( '[Configurações avançadas] Tag ausente \'repository\'' , level = xbmc . LOGDEBUG )
         i11Iiii = True
        if not o0o0OOO0o0 :
         logging . log ( '[Configurações avançadas] Tag ausente \'repositoryxml\'' ,
 level = xbmc . LOGDEBUG )
         i11Iiii = True
        if not ooOOOo0oo0O0 :
         logging . log ( '[Configurações avançadas] Tag ausente \'repositoryurl\'' ,
 level = xbmc . LOGDEBUG )
         i11Iiii = True
        if i11Iiii :
         continue
         if 23 - 23: o0oOOo0O0Ooo . II111iiii
      if O00 :
       directory . add_dir ( O00o , { 'mode' : 'addons' , 'url' : Ii11Ii11I } , description = IIIII ,
 icon = i1i1II , fanart = o0 , themeit = CONFIG . THEME3 )
      else :
       if not CONFIG . SHOWADULT == 'true' and I11II1i :
        continue
        if 98 - 98: iIii1I11I1II1 % OoOoOO00 * I1ii11iIi11i * OoOoOO00
       if type . lower ( ) == 'skin' :
        directory . add_file ( O00o ,
 { 'mode' : 'addons' , 'action' : 'skin' , 'name' : O00o ,
 'url' : Ii11Ii11I } , description = IIIII , icon = i1i1II , fanart = o0 ,
 themeit = CONFIG . THEME2 )
       elif type . lower ( ) == 'addonpack' :
        directory . add_file ( O00o , { 'mode' : 'addons' , 'action' : 'addonpack' ,
 'name' : O00o , 'url' : Ii11Ii11I } ,
 description = IIIII , icon = i1i1II , fanart = o0 ,
 themeit = CONFIG . THEME2 )
       else :
        try :
         i1 = tools . get_addon_info ( i11I1 , 'path' )
         if os . path . exists ( i1 ) :
          O00o = "[COLOR springgreen][Instalado][/COLOR] {0}" . format ( O00o )
        except :
         pass
         if 48 - 48: O0 + O0 - I1ii11iIi11i . o00ooo0 / iIii1I11I1II1
        directory . add_file ( O00o , { 'mode' : 'addons' , 'action' : 'addon' , 'name' : i11I1 ,
 'addonurl' : Ii11Ii11I , 'repository' : iI11i1I1 , 'repositoryxml' : o0o0OOO0o0 ,
 'repositoryurl' : ooOOOo0oo0O0 } , description = IIIII ,
 icon = i1i1II , fanart = o0 , themeit = CONFIG . THEME2 )
    else :
     if not ii1I :
      directory . add_file ( 'Arquivo de texto não formatado corretamente!' , themeit = CONFIG . THEME3 )
      logging . log ( "[Menu Addon] ERRO: Formato inválido." )
     elif len ( ii1I ) == 0 :
      directory . add_file ( "Nenhum complemento adicionado a este menu ainda!" , themeit = CONFIG . THEME2 )
  else :
   logging . log ( "[Menu Addon] ERRO: URL para a lista Addon não funciona." )
   directory . add_file ( 'O URL do arquivo txt não é válido' , themeit = CONFIG . THEME3 )
   directory . add_file ( '{0}' . format ( CONFIG . ADDONFILE ) , themeit = CONFIG . THEME3 )
   if 77 - 77: i1IIi % OoOoOO00 - Oo0ooO0oo0oO + o00ooo0
 def install_dependency ( self , plugin ) :
  from resources . libs import db
  if 31 - 31: I11i - i1IIi * OOooOOo / OoooooooOO
  iI = os . path . join ( CONFIG . ADDONS , plugin , 'addon.xml' )
  if os . path . exists ( iI ) :
   o00O = tools . parse_dom ( tools . read_from_file ( iI ) , 'import' , ret = 'addon' )
   for OOO0OOO00oo in o00O :
    if 'xbmc.python' not in OOO0OOO00oo :
     self . progress_dialog . update ( 0 , '\n' + '[COLOR {0}]{1}[/COLOR]' . format ( CONFIG . COLOR1 , OOO0OOO00oo ) )
     if 31 - 31: II111iiii - OOooOOo . I1i1iI1i % OoOoOO00 - O0
     try :
      i1 = tools . get_addon_by_id ( id = OOO0OOO00oo )
      iii11 = tools . get_addon_info ( i1 , 'name' )
     except :
      db . create_temp ( OOO0OOO00oo )
      db . addon_database ( OOO0OOO00oo , 1 )
      if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1i1iI1i - I1ii11iIi11i / oO0o
 def install_addon_from_url ( self , plugin , url ) :
  from resources . libs . downloader import Downloader
  from resources . libs import db
  from resources . libs import extract
  from resources . libs import skin
  if 50 - 50: I1IiiI
  oo0Ooo0 = tools . open_url ( url , check = True )
  if 34 - 34: I1IiiI * II111iiii % o0OO0 * OoOoOO00 - I1IiiI
  if not oo0Ooo0 :
   logging . log_notify ( "[COLOR {0}]Addon Installer[/COLOR]" . format ( CONFIG . COLOR1 ) ,
 '[COLOR {0}]{1}:[/COLOR] [COLOR {2}]Invalid Zip Url![/COLOR]' . format ( CONFIG . COLOR1 ,
 plugin ,
 CONFIG . COLOR2 ) )
   return
   if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
  tools . ensure_folders ( CONFIG . PACKAGES )
  if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
  self . progress_dialog . create ( CONFIG . ADDONTITLE ,
 '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR2 ,
 CONFIG . COLOR1 ,
 plugin )
 + '\n' + ''
 + '\n' + '[COLOR {0}]Por favor, aguarde[/COLOR]' . format ( CONFIG . COLOR2 ) )
  Ii11Ii1I = url . split ( '/' )
  O00oO = os . path . join ( CONFIG . PACKAGES , Ii11Ii1I [ - 1 ] )
  if 39 - 39: Oo0ooO0oo0oO - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  try :
   os . remove ( O00oO )
  except :
   pass
   if 59 - 59: iIii1I11I1II1 + I1IiiI - o0oOOo0O0Ooo - I1IiiI + OOooOOo / I1ii11iIi11i
  Downloader ( ) . download ( url , O00oO )
  I1 = '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR2 , CONFIG . COLOR1 ,
 plugin )
  self . progress_dialog . update ( 0 , I1
 + '\n' + ''
 + '\n' + '[COLOR {0}]Por favor, aguarde[/COLOR]' . format ( CONFIG . COLOR2 ) )
  OO00Oo , O0OOO0OOoO0O , O00Oo000ooO0 = extract . all ( O00oO , CONFIG . ADDONS , title = I1 )
  self . progress_dialog . update ( 0 , I1
 + '\n' + ''
 + '\n' + '[COLOR {0}]Baixando Dependencies[/COLOR]' . format ( CONFIG . COLOR2 ) )
  IiiIII111iI ( plugin )
  OoO0O00IIiII = db . grab_addons ( O00oO )
  logging . log ( str ( OoO0O00IIiII ) )
  db . addon_database ( OoO0O00IIiII , 1 , True )
  self . install_dependency ( plugin )
  self . progress_dialog . close ( )
  if 80 - 80: Oo0ooO0oo0oO . oO0o
  xbmc . executebuiltin ( 'UpdateAddonRepos()' )
  xbmc . executebuiltin ( 'UpdateLocalAddons()' )
  xbmc . executebuiltin ( 'Container.Refresh()' )
  if 25 - 25: OoOoOO00 . II111iiii / o0OO0 . OOooOOo * OoO0O00 . I1IiiI
  for Oo0oOOo in OoO0O00IIiII :
   if Oo0oOOo . startswith ( 'skin.' ) and not Oo0oOOo == 'skin.shortcuts' :
    if not CONFIG . BUILDNAME == '' and CONFIG . DEFAULTIGNORE == 'true' :
     CONFIG . set_setting ( 'defaultskinignore' , 'true' )
    skin . switch_to_skin ( Oo0oOOo , 'Skin Installer' )
    if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
 def install_addon ( self , plugin , urls , over = False ) :
  from resources . libs import db
  if 75 - 75: oO0o
  I1III = None
  if 63 - 63: OOooOOo % oO0o * oO0o * OoO0O00 / I1ii11iIi11i
  if not over :
   if xbmc . getCondVisibility ( 'System.HasAddon({0})' . format ( plugin ) ) :
    I1III = self . dialog . yesno ( CONFIG . ADDONTITLE , '[COLOR {0}]{1}[/COLOR] já instalado. Você gostaria de reinstalá-lo?' . format ( CONFIG . COLOR1 , plugin ) )
   else :
    I1III = self . dialog . yesno ( CONFIG . ADDONTITLE , 'Você gostaria de instalar [COLOR {0}]{1}[/COLOR]?' . format ( CONFIG . COLOR1 , plugin ) )
  else :
   I1III = True
   if 74 - 74: II111iiii
  if not I1III :
   return
   if 75 - 75: o0oOOo0O0Ooo . o00ooo0
  I1I11I1I1I = tools . open_url ( urls [ 0 ] , check = True )
  Oo0O00Oo0o0 = tools . open_url ( urls [ 2 ] , check = True )
  O00O0oOO00O00 = tools . open_url ( urls [ 3 ] )
  if 11 - 11: Oo0ooO0oo0oO . I1ii11iIi11i
  if False not in [ O00O0oOO00O00 , Oo0O00Oo0o0 ] :
   if 92 - 92: o0OO0 . I1i1iI1i
   i1i = urls [ 1 ]
   if 50 - 50: Oo0ooO0oo0oO
   if not xbmc . getCondVisibility ( 'System.HasAddon({0})' . format ( i1i ) ) :
    logging . log ( "Repositório não instalado, instalando-o" )
    if 14 - 14: I11i % OoO0O00 * I11i
    from xml . etree import ElementTree
    iII = ElementTree . fromstring ( O00O0oOO00O00 . text . encode ( 'ascii' , 'backslashreplace' ) )
    oO00o0 = iII . findall ( 'addon' )
    OOoo0O = None
    if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
    for o0oo in oO00o0 :
     if o0oo . attrib [ 'id' ] == i1i :
      OOoo0O = o0oo . attrib [ 'version' ]
      if 91 - 91: Oo0ooO0oo0oO
    if OOoo0O :
     iiIii = '{0}{1}-{2}.zip' . format ( urls [ 2 ] , i1i , OOoo0O )
     logging . log ( iiIii )
     db . addon_database ( i1i , 1 )
     self . install_addon ( i1i , iiIii , over = True )
     xbmc . executebuiltin ( 'UpdateAddonRepos()' )
     I1III = II1iI ( plugin )
     if I1III :
      xbmc . executebuiltin ( 'Container.Refresh()' )
      return True
    else :
     logging . log (
 "[Addon Installer] Repositório não instalado: Incapaz de obter url! ({0})" . format ( urls [ 1 ] ) )
   else :
    logging . log ( "Repositório instalado, instalando addon" )
    I1III = II1iI ( plugin )
    if I1III :
     xbmc . executebuiltin ( 'Container.Refresh()' )
     return True
  elif I1I11I1I1I :
   logging . log ( "Sem repositório, instalando addon" )
   self . install_addon_from_url ( plugin , urls [ 0 ] )
   if 79 - 79: OoooooooOO / O0
   if os . path . exists ( os . path . join ( CONFIG . ADDONS , plugin ) ) :
    return True
    if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1i1iI1i
   from xml . etree import ElementTree
   iII = ElementTree . parse ( O00O0oOO00O00 . text )
   oO00o0 = iII . findall ( 'addon' )
   OOoo0O = None
   if 5 - 5: o0oOOo0O0Ooo * o00ooo0 + OoOoOO00 . OOooOOo + OoOoOO00
   for o0oo in oO00o0 :
    if o0oo . attrib [ 'id' ] == i1i :
     OOoo0O = o0oo . attrib [ 'version' ]
     if 91 - 91: O0
   if OOoo0O > 0 :
    IiII = "{0}{1}-{2}.zip" . format ( urls [ 0 ] , plugin , OOoo0O )
    logging . log ( str ( IiII ) )
    db . addon_database ( plugin , 1 )
    self . install_addon_from_url ( plugin , IiII )
    xbmc . executebuiltin ( 'Container.Refresh()' )
   else :
    logging . log ( "no match" )
    return False
    if 61 - 61: II111iiii
 def install_addon_pack ( self , name , url ) :
  from resources . libs . downloader import Downloader
  from resources . libs import db
  from resources . libs import extract
  from resources . libs . common import logging
  from resources . libs . common import tools
  if 64 - 64: o00ooo0 / OoOoOO00 - O0 - I11i
  O0oOoOOOoOO = xbmcgui . DialogProgress ( )
  if 38 - 38: I1i1iI1i
  oo0Ooo0 = tools . open_url ( url , check = True )
  if 7 - 7: O0 . o0OO0 % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
  if not oo0Ooo0 :
   logging . log_notify ( "[COLOR {0}]Addon Installer[/COLOR]" . format ( CONFIG . COLOR1 ) ,
 '[COLOR {0}]{1}:[/COLOR] [COLOR {2}]Invalid Zip Url![/COLOR]' . format ( CONFIG . COLOR1 , name , CONFIG . COLOR2 ) )
   return
   if 36 - 36: Oo0ooO0oo0oO % o00ooo0 % Oo0Ooo - I1ii11iIi11i
  if not os . path . exists ( CONFIG . PACKAGES ) :
   os . makedirs ( CONFIG . PACKAGES )
   if 22 - 22: iIii1I11I1II1 / Oo0Ooo * I1ii11iIi11i % o0OO0
  O0oOoOOOoOO . create ( CONFIG . ADDONTITLE ,
 '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , name )
 + '\n' + ''
 + '\n' + '[COLOR {0}]Por favor, aguarde[/COLOR]' . format ( CONFIG . COLOR2 ) )
  Ii11Ii1I = url . split ( '/' )
  O00oO = xbmc . makeLegalFilename ( os . path . join ( CONFIG . PACKAGES , Ii11Ii1I [ - 1 ] ) )
  try :
   os . remove ( O00oO )
  except :
   pass
  Downloader ( ) . download ( url , O00oO )
  I1 = '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , name )
  O0oOoOOOoOO . update ( 0 , I1
 + '\n' + ''
 + '\n' + '[COLOR {0}]Por favor, aguarde[/COLOR]' . format ( CONFIG . COLOR2 ) )
  OO00Oo , O0OOO0OOoO0O , O00Oo000ooO0 = extract . all ( O00oO , CONFIG . ADDONS , title = I1 )
  IiiIII111iI = db . grab_addons ( O00oO )
  db . addon_database ( IiiIII111iI , 1 , True )
  O0oOoOOOoOO . close ( )
  logging . log_notify ( "[COLOR {0}]Addon Installer[/COLOR]" . format ( CONFIG . COLOR1 ) ,
 '[COLOR {0}]{1}: Instalado![/COLOR]' . format ( CONFIG . COLOR2 , name ) )
  xbmc . executebuiltin ( 'UpdateAddonRepos()' )
  xbmc . executebuiltin ( 'UpdateLocalAddons()' )
  xbmc . executebuiltin ( 'Container.Refresh()' )
  if 85 - 85: oO0o % i11iIiiIii - o0OO0 * OoooooooOO / I1IiiI % I1IiiI
  if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
 def install_skin ( self , name , url ) :
  from resources . libs . downloader import Downloader
  from resources . libs import db
  from resources . libs import extract
  from resources . libs . common import logging
  from resources . libs import skin
  from resources . libs . common import tools
  if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
  O0oOoOOOoOO = xbmcgui . DialogProgress ( )
  if 49 - 49: Ii1I / OoO0O00 . II111iiii
  oo0Ooo0 = tools . open_url ( url , check = False )
  if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
  if not oo0Ooo0 :
   logging . log_notify ( "[COLOR {0}]Addon Installer[/COLOR]" . format ( CONFIG . COLOR1 ) ,
 '[COLOR {0}]{1}:[/COLOR] [COLOR {2}]Invalid Zip Url![/COLOR]' . format ( CONFIG . COLOR1 , name , CONFIG . COLOR2 ) )
   return
   if 31 - 31: II111iiii . I1IiiI
  if not os . path . exists ( CONFIG . PACKAGES ) :
   os . makedirs ( CONFIG . PACKAGES )
   if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % o0OO0 * Oo0ooO0oo0oO . i11iIiiIii
  O0oOoOOOoOO . create ( CONFIG . ADDONTITLE ,
 '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , name )
 + '\n' + ''
 + '\n' + '[COLOR {0}]Por favor, aguarde[/COLOR]' . format ( CONFIG . COLOR2 ) )
  if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % o0OO0
  Ii11Ii1I = url . split ( '/' )
  O00oO = xbmc . makeLegalFilename ( os . path . join ( CONFIG . PACKAGES , Ii11Ii1I [ - 1 ] ) )
  try :
   os . remove ( O00oO )
  except :
   pass
  Downloader ( ) . download ( url , O00oO )
  I1 = '[COLOR {0}][B]Baixando:[/B][/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , name )
  O0oOoOOOoOO . update ( 0 , I1
 + '\n' + ''
 + '\n' + '[COLOR {0}]Por favor, aguarde[/COLOR]' . format ( CONFIG . COLOR2 ) )
  OO00Oo , O0OOO0OOoO0O , O00Oo000ooO0 = extract . all ( O00oO , CONFIG . HOME , title = I1 )
  IiiIII111iI = db . grab_addons ( O00oO )
  db . addon_database ( IiiIII111iI , 1 , True )
  O0oOoOOOoOO . close ( )
  logging . log_notify ( "[COLOR {0}]Addon Installer[/COLOR]" . format ( CONFIG . COLOR1 ) ,
 '[COLOR {0}]{1}: Installed![/COLOR]' . format ( CONFIG . COLOR2 , name ) )
  xbmc . executebuiltin ( 'UpdateAddonRepos()' )
  xbmc . executebuiltin ( 'UpdateLocalAddons()' )
  for Oo0oOOo in IiiIII111iI :
   if Oo0oOOo . startswith ( 'skin.' ) and not Oo0oOOo == 'skin.shortcuts' :
    if not CONFIG . BUILDNAME == '' and CONFIG . DEFAULTIGNORE == 'true' :
     CONFIG . set_setting ( 'defaultskinignore' , 'true' )
    skin . switch_to_skin ( Oo0oOOo , 'Skin Installer' )
  xbmc . executebuiltin ( 'Container.Refresh()' )
# Team KelTec Media'Play