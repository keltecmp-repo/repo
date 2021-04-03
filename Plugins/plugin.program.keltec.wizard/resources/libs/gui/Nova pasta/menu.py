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
import xbmcaddon
import xbmcgui
import xbmcvfs
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import glob
import os
import re
if 73 - 73: II111iiii
try :
 from urllib . parse import quote_plus
 from urllib . request import urlretrieve
except ImportError :
 from urllib import quote_plus
 from urllib import urlretrieve
 if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
from resources . libs . common import directory
from resources . libs . common . config import CONFIG
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
def o0oO0 ( ) :
 if not xbmc . getCondVisibility ( 'System.HasAddon(script.kodi.android.update)' ) :
  from resources . libs . gui import addon_menu
  addon_menu . install_from_kodi ( 'script.kodi.android.update' )
  if 100 - 100: i1IIi
 try :
  I1Ii11I1Ii1i = xbmcaddon . Addon ( 'script.kodi.android.update' )
 except RuntimeError as Ooo :
  return False
  if 56 - 56: I11i - i1IIi
 o00oOoo = int ( I1Ii11I1Ii1i . getSetting ( 'File_Manager' ) )
 O0OOo = xbmcvfs . listdir ( 'androidapp://sources/apps/' ) [ 1 ]
 if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
 if o00oOoo == 0 and 'com.android.documentsui' not in O0OOo :
  i11 = xbmcgui . Dialog ( )
  I11 = i11 . yesno ( CONFIG . ADDONTITLE , 'Parece que seu dispositivo não tem gerenciador de arquivos padrão. Você gostaria de definir um agora?' )
  if not I11 :
   i11 . ok ( CONFIG . ADDONTITLE , 'Se um APK for baixado, mas não abrir para instalação, tente alterar o gerenciador de arquivos em {}\'s "Configurações de instalação".' . format ( CONFIG . ADDONTITLE ) )
  else :
   from resources . libs import install
   install . choose_file_manager ( )
   if 98 - 98: i11iIiiIii * I1IiiI % iII111i * iII111i * II111iiii
 return True
 if 79 - 79: IiII
 if 86 - 86: OoOoOO00 % I1IiiI
def oo ( url = None ) :
 from resources . libs . common import logging
 from resources . libs . common import tools
 if 33 - 33: II111iiii * Oo0Ooo - o0oOOo0O0Ooo * iIii1I11I1II1 * OoooooooOO * ooOoO0o
 if o0oO0 ( ) :
  directory . add_dir ( 'Official Kodi APK\'s' , { 'mode' : 'kodiapk' } , icon = CONFIG . ICONAPK , themeit = CONFIG . THEME1 )
  directory . add_separator ( )
  if 27 - 27: OoO0O00
 oOOOo0o0O = tools . open_url ( CONFIG . APKFILE )
 OOoOoo00oo = tools . open_url ( url )
 if 41 - 41: iIii1I11I1II1 / I1Ii111 + OOooOOo
 if oOOOo0o0O :
  OOooO = tools . clean_text ( OOoOoo00oo . text if url else oOOOo0o0O . text )
  if 58 - 58: OoO0O00 + OoOoOO00 / Ii1I * OoooooooOO
  if OOooO :
   II111iiiiII = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( OOooO )
   if len ( II111iiiiII ) > 0 :
    oOoOo00oOo = 0
    for Oo , o00O00O0O0O , url , OooO0OO , iiiIi , IiIIIiI1I1 , OoO000 in II111iiiiII :
     if not CONFIG . SHOWADULT == 'true' and IiIIIiI1I1 . lower ( ) == 'yes' :
      continue
     if o00O00O0O0O . lower ( ) == 'yes' :
      oOoOo00oOo += 1
      directory . add_dir ( "[B]{0}[/B]" . format ( Oo ) , { 'mode' : 'apk' , 'name' : Oo , 'url' : url } , description = OoO000 , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME3 )
     else :
      oOoOo00oOo += 1
      directory . add_file ( Oo , { 'mode' : 'apkinstall' , 'name' : Oo , 'url' : url } , description = OoO000 , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME2 )
     if oOoOo00oOo == 0 :
      directory . add_file ( "No addons added to this menu yet!" , themeit = CONFIG . THEME2 )
   else :
    logging . log ( "[Menu APK] ERRO: Formato inválido." , level = xbmc . LOGERROR )
  else :
   logging . log ( "[Menu APK] ERROR: URL para a lista apk não funciona." , level = xbmc . LOGERROR )
   directory . add_file ( 'O URL do arquivo txt não é válido' , themeit = CONFIG . THEME3 )
   directory . add_file ( '{0}' . format ( CONFIG . APKFILE ) , themeit = CONFIG . THEME3 )
 else :
  logging . log ( "[Menu APK] Nenhuma lista de APK adicionada." )
  if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
  if 17 - 17: oO0o . Oo0Ooo . I1ii11iIi11i
def IIi ( url = None ) :
 from resources . libs . common import logging
 from resources . libs . common import tools
 if 38 - 38: Ii1I / Oo0Ooo
 oOOOo0o0O = tools . open_url ( CONFIG . YOUTUBEFILE )
 OOoOoo00oo = tools . open_url ( url )
 if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
 if oOOOo0o0O :
  Oooo = OOoOoo00oo . text if url else oOOOo0o0O . text
  if 67 - 67: OOooOOo / OoooooooOO % I11i - iIii1I11I1II1
  if Oooo :
   OooO0o0Oo = Oooo . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
   II111iiiiII = re . compile ( 'name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( OooO0o0Oo )
   if len ( II111iiiiII ) > 0 :
    for Oo00OOOOO , o00O00O0O0O , url , OooO0OO , iiiIi , OoO000 in II111iiiiII :
     if o00O00O0O0O . lower ( ) == "yes" :
      directory . add_dir ( "[B]{0}[/B]" . format ( Oo00OOOOO ) , { 'mode' : 'youtube' , 'name' : Oo00OOOOO , 'url' : url } , description = OoO000 , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME3 )
     else :
      directory . add_file ( Oo00OOOOO , { 'mode' : 'viewVideo' , 'url' : url } , description = OoO000 , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME2 )
   else :
    logging . log ( "[Menu YouTube] ERRO: Formato inválido." )
  else :
   logging . log ( "[Menu do YouTube] ERRO: URL da lista do YouTube não funciona." )
   directory . add_file ( 'O URL do arquivo txt não é válido' , themeit = CONFIG . THEME3 )
   directory . add_file ( '{0}' . format ( CONFIG . YOUTUBEFILE ) , themeit = CONFIG . THEME3 )
 else :
  logging . log ( "[Menu do YouTube] Nenhuma lista do YouTube adicionada." )
  if 85 - 85: ooOoO0o . iII111i - OoO0O00 % ooOoO0o % II111iiii
  if 81 - 81: OoO0O00 + II111iiii % iII111i * O0
  if 89 - 89: oO0o + Oo0Ooo
  if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
def III1ii1iII ( ) :
 directory . add_dir ( 'Teste rápido' , { 'mode' : 'speedtest' } , icon = CONFIG . ICONSPEED , themeit = CONFIG . THEME1 )
 if CONFIG . HIDESPACERS == 'No' :
  directory . add_separator ( )
 directory . add_dir ( 'Exibir endereço IP e endereço MAC' , { 'mode' : 'viewIP' } , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME1 )
 if 54 - 54: I1IiiI % II111iiii % II111iiii
 if 13 - 13: o0oOOo0O0Ooo . Ii1I
def i11Iiii ( ) :
 from resources . libs import speedtest
 if 23 - 23: o0oOOo0O0Ooo . II111iiii
 Oo0O0OOOoo , oOoOooOo0o0 , OOOO , OOO00 , iiiiiIIii , O000OO0 , I11iii1Ii = speedtest . net_info ( )
 directory . add_file ( '[COLOR {0}]MAC:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , Oo0O0OOOoo ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]IP interno: [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oOoOooOo0o0 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]IP externo:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , OOOO ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Cidade:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , OOO00 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Estado:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , iiiiiIIii ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]País:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , O000OO0 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]ISP:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , I11iii1Ii ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 if 13 - 13: I1Ii111 % OoOoOO00 - i11iIiiIii . I1IiiI + II111iiii
 if 10 - 10: I1ii11iIi11i * ooOoO0o * II111iiii % Ii1I . OOooOOo + I1Ii111
def IIiIi11i1 ( ) :
 from datetime import date
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 directory . add_file ( 'Executar teste de velocidade' , { 'mode' : 'speedtest' } , icon = CONFIG . ICONSPEED , themeit = CONFIG . THEME3 )
 if os . path . exists ( CONFIG . SPEEDTEST ) :
  i1I1iI = glob . glob ( os . path . join ( CONFIG . SPEEDTEST , '*.png' ) )
  i1I1iI . sort ( key = lambda oo0OooOOo0 : os . path . getmtime ( oo0OooOOo0 ) , reverse = True )
  if len ( i1I1iI ) > 0 :
   directory . add_file ( 'Resultados claros' , { 'mode' : 'clearspeedtest' } , icon = CONFIG . ICONSPEED , themeit = CONFIG . THEME3 )
   directory . add_separator ( 'Execuções anteriores' , icon = CONFIG . ICONSPEED , themeit = CONFIG . THEME3 )
   for o0O in i1I1iI :
    O00oO = date . fromtimestamp ( os . path . getmtime ( o0O ) ) . strftime ( '%m/%d/%Y %H:%M:%S' )
    I11i1I1I = o0O . replace ( os . path . join ( CONFIG . SPEEDTEST , '' ) , '' )
    directory . add_file ( '[B]{0}[/B]: [I]Ran {1}[/I]' . format ( I11i1I1I , O00oO ) , { 'mode' : 'viewspeedtest' , 'name' : I11i1I1I } , icon = CONFIG . ICONSPEED , themeit = CONFIG . THEME3 )
    if 83 - 83: I1ii11iIi11i / ooOoO0o
    if 49 - 49: o0oOOo0O0Ooo
def IIii1Ii1 ( ) :
 from resources . libs . common import tools
 if 5 - 5: iII111i % OOooOOo + ooOoO0o % i11iIiiIii + o0oOOo0O0Ooo
 i1I1iI = glob . glob ( os . path . join ( CONFIG . SPEEDTEST , '*.png' ) )
 for file in i1I1iI :
  tools . remove_file ( file )
  if 60 - 60: OoO0O00 * OoOoOO00 - OoO0O00 % OoooooooOO - ooOoO0o + I1IiiI
  if 70 - 70: IiII * Oo0Ooo * I11i / Ii1I
def oO ( img = None ) :
 from resources . libs . gui import window
 if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
 img = os . path . join ( CONFIG . SPEEDTEST , img )
 window . show_speed_test ( img )
 if 38 - 38: o0oOOo0O0Ooo
 if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
def i11iIIIIIi1 ( ) :
 from resources . libs . common import logging
 from resources . libs import speedtest
 if 20 - 20: i1IIi + I1ii11iIi11i - ooOoO0o
 try :
  IiI11iII1 = speedtest . speedtest ( )
  if not os . path . exists ( CONFIG . SPEEDTEST ) :
   os . makedirs ( CONFIG . SPEEDTEST )
  IIII11I1I = IiI11iII1 [ 0 ] . split ( '/' )
  OOO0o = os . path . join ( CONFIG . SPEEDTEST , IIII11I1I [ - 1 ] )
  urlretrieve ( IiI11iII1 [ 0 ] , OOO0o )
  oO ( IIII11I1I [ - 1 ] )
 except Exception as Ooo :
  logging . log ( "[Teste de velocidade] Erro ao executar o teste de velocidade: {0}" . format ( Ooo ) , level = xbmc . LOGDEBUG )
  pass
  if 30 - 30: iIii1I11I1II1 / ooOoO0o - I1Ii111 - II111iiii % iII111i
  if 49 - 49: I1IiiI % ooOoO0o . ooOoO0o . I11i * ooOoO0o
def O0oOO0 ( ) :
 from resources . libs . common import logging
 from resources . libs . common import tools
 from resources . libs import speedtest
 if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
 o0 = [ 'System.FriendlyName' , 'System.BuildVersion' , 'System.CpuUsage' , 'System.ScreenMode' ,
 'Network.IPAddress' , 'Network.MacAddress' , 'System.Uptime' , 'System.TotalUptime' , 'System.FreeSpace' ,
 'System.UsedSpace' , 'System.TotalSpace' , 'System.Memory(free)' , 'System.Memory(used)' ,
 'System.Memory(total)' ]
 oo0oOo = [ ]
 oOoOo00oOo = 0
 for o000O0o in o0 :
  iI1iII1 = tools . get_info_label ( o000O0o )
  oO0OOoo0OO = 0
  while iI1iII1 == "Busy" and oO0OOoo0OO < 10 :
   iI1iII1 = tools . get_info_label ( o000O0o )
   oO0OOoo0OO += 1
   logging . log ( "{0} sleep {1}" . format ( o000O0o , str ( oO0OOoo0OO ) ) )
   xbmc . sleep ( 200 )
  oo0oOo . append ( iI1iII1 )
  oOoOo00oOo += 1
 O0ii1ii1ii = oo0oOo [ 8 ] if 'Una' in oo0oOo [ 8 ] else tools . convert_size ( int ( float ( oo0oOo [ 8 ] [ : - 8 ] ) ) * 1024 * 1024 )
 oooooOoo0ooo = oo0oOo [ 9 ] if 'Una' in oo0oOo [ 9 ] else tools . convert_size ( int ( float ( oo0oOo [ 9 ] [ : - 8 ] ) ) * 1024 * 1024 )
 I1I1IiI1 = oo0oOo [ 10 ] if 'Una' in oo0oOo [ 10 ] else tools . convert_size ( int ( float ( oo0oOo [ 10 ] [ : - 8 ] ) ) * 1024 * 1024 )
 III1iII1I1ii = tools . convert_size ( int ( float ( oo0oOo [ 11 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oOOo0 = tools . convert_size ( int ( float ( oo0oOo [ 12 ] [ : - 2 ] ) ) * 1024 * 1024 )
 oo00O00oO = tools . convert_size ( int ( float ( oo0oOo [ 13 ] [ : - 2 ] ) ) * 1024 * 1024 )
 if 23 - 23: OoO0O00 + OoO0O00 . OOooOOo
 ii1ii11IIIiiI = [ ]
 O00OOOoOoo0O = [ ]
 O000OOo00oo = [ ]
 oo0OOo = [ ]
 ooOOO00Ooo = [ ]
 IiIIIi1iIi = [ ]
 ooOOoooooo = [ ]
 if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
 III1Iiii1I11 = glob . glob ( os . path . join ( CONFIG . ADDONS , '*/' ) )
 for IIII in sorted ( III1Iiii1I11 , key = lambda oOoOo00oOo : oOoOo00oOo ) :
  iiIiI = os . path . split ( IIII [ : - 1 ] ) [ 1 ]
  if iiIiI == 'packages' : continue
  o00oooO0Oo = os . path . join ( IIII , 'addon.xml' )
  if os . path . exists ( o00oooO0Oo ) :
   o0O0OOO0Ooo = re . compile ( "<provides>(.+?)</provides>" ) . findall ( tools . read_from_file ( o00oooO0Oo ) )
   if len ( o0O0OOO0Ooo ) == 0 :
    if iiIiI . startswith ( 'skin' ) :
     ooOOoooooo . append ( iiIiI )
    elif iiIiI . startswith ( 'repo' ) :
     ooOOO00Ooo . append ( iiIiI )
    else :
     IiIIIi1iIi . append ( iiIiI )
   elif not ( o0O0OOO0Ooo [ 0 ] ) . find ( 'executable' ) == - 1 :
    oo0OOo . append ( iiIiI )
   elif not ( o0O0OOO0Ooo [ 0 ] ) . find ( 'video' ) == - 1 :
    O000OOo00oo . append ( iiIiI )
   elif not ( o0O0OOO0Ooo [ 0 ] ) . find ( 'audio' ) == - 1 :
    O00OOOoOoo0O . append ( iiIiI )
   elif not ( o0O0OOO0Ooo [ 0 ] ) . find ( 'image' ) == - 1 :
    ii1ii11IIIiiI . append ( iiIiI )
    if 45 - 45: O0 / o0oOOo0O0Ooo
 directory . add_file ( '[B]Media Center Info:[/B]' , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Nome:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo0oOo [ 0 ] ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME3 )
 directory . add_file ( '[COLOR {0}]Versão:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo0oOo [ 1 ] ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME3 )
 directory . add_file ( '[COLOR {0}]Plataforma:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , tools . platform ( ) . title ( ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME3 )
 directory . add_file ( '[COLOR {0}]CPU Usage:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo0oOo [ 2 ] ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME3 )
 directory . add_file ( '[COLOR {0}]Screen Mode:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo0oOo [ 3 ] ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME3 )
 if 32 - 32: iII111i . IiII . IiII
 directory . add_file ( '[B]Uptime:[/B]' , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Tempo de atividade atual:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo0oOo [ 6 ] ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Tempo de atividade total:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo0oOo [ 7 ] ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 if 62 - 62: I1ii11iIi11i + IiII % iII111i + OOooOOo
 directory . add_file ( '[B]Armazenamento Local:[/B]' , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Armazenamento Usado:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oooooOoo0ooo ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Armazenamento grátis:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , O0ii1ii1ii ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Armazenamento Total:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , I1I1IiI1 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 if 33 - 33: O0 . IiII . I1IiiI
 directory . add_file ( '[B]Ram Usage:[/B]' , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Used Memory:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , III1iII1I1ii ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Free Memory:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oOOo0 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Total Memory:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oo00O00oO ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
 Oo0O0OOOoo , oOoOooOo0o0 , OOOO , OOO00 , iiiiiIIii , O000OO0 , I11iii1Ii = speedtest . net_info ( )
 directory . add_file ( '[B]Network:[/B]' , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Mac:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , Oo0O0OOOoo ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Internal IP: [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , oOoOooOo0o0 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]External IP:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , OOOO ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]City:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , OOO00 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]State:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , iiiiiIIii ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Country:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , O000OO0 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]ISP:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , I11iii1Ii ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 if 29 - 29: I1ii11iIi11i + oO0o % O0
 I1I11 = len ( ii1ii11IIIiiI ) + len ( O00OOOoOoo0O ) + len ( O000OOo00oo ) + len ( oo0OOo ) + len ( IiIIIi1iIi ) + len ( ooOOoooooo ) + len ( ooOOO00Ooo )
 directory . add_file ( '[B]Addons([COLOR {0}]{1}[/COLOR]):[/B]' . format ( CONFIG . COLOR1 , I1I11 ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Video Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( O000OOo00oo ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Program Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( oo0OOo ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Music Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( O00OOOoOoo0O ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Picture Addons:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( ii1ii11IIIiiI ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Repositories:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( ooOOO00Ooo ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Skins:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( ooOOoooooo ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 directory . add_file ( '[COLOR {0}]Scripts/Modules:[/COLOR] [COLOR {1}]{2}[/COLOR]' . format ( CONFIG . COLOR1 , CONFIG . COLOR2 , str ( len ( IiIIIi1iIi ) ) ) , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME2 )
 if 34 - 34: I1IiiI . OOooOOo * I1ii11iIi11i + I1Ii111
 if 31 - 31: iII111i % iII111i % I11i
def OOOOoo0Oo ( ) :
 ii111iI1iIi1 = '[COLOR springgreen]Ligado[/COLOR]'
 OOO = '[COLOR red]Desligado[/COLOR]'
 if 68 - 68: II111iiii + I11i
 I1I1I = 'true' if CONFIG . KEEPTRAKT == 'true' else 'false'
 OoOO000 = 'true' if CONFIG . KEEPDEBRID == 'true' else 'false'
 i1Ii11i1i = 'true' if CONFIG . KEEPLOGIN == 'true' else 'false'
 o0oOOoo = 'true' if CONFIG . KEEPSOURCES == 'true' else 'false'
 oOo00O0oo00o0 = 'true' if CONFIG . KEEPADVANCED == 'true' else 'false'
 ii = 'true' if CONFIG . KEEPPROFILES == 'true' else 'false'
 OOooooO0Oo = 'true' if CONFIG . KEEPPLAYERCORE == 'true' else 'false'
 OO = 'true' if CONFIG . KEEPGUISETTINGS == 'true' else 'false'
 iIiIIi1 = 'true' if CONFIG . KEEPFAVS == 'true' else 'false'
 ooOOO00Ooo = 'true' if CONFIG . KEEPREPOS == 'true' else 'false'
 super = 'true' if CONFIG . KEEPSUPER == 'true' else 'false'
 I1IIII1i = 'true' if CONFIG . KEEPWHITELIST == 'true' else 'false'
 if 2 - 2: I11i + Ii1I - I1IiiI % o0oOOo0O0Ooo . iII111i
 directory . add_dir ( 'Keep Trakt Data' , { 'mode' : 'trakt' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME1 )
 directory . add_dir ( 'Keep Debrid' , { 'mode' : 'realdebrid' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME1 )
 directory . add_dir ( 'Keep Login Info' , { 'mode' : 'login' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Import Save Data' , { 'mode' : 'managedata' , 'name' : 'import' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Export Save Data' , { 'mode' : 'managedata' , 'name' : 'export' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( '- Click to toggle settings -' , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Save Trakt: {0}' . format ( I1I1I . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keeptrakt' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Save Debrid: {0}' . format ( OoOO000 . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepdebrid' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Save Login Info: {0}' . format ( i1Ii11i1i . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keeplogin' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep \'Sources.xml\': {0}' . format ( o0oOOoo . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepsources' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep \'Profiles.xml\': {0}' . format ( ii . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepprofiles' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep \'playercorefactory.xml\': {0}' . format ( OOooooO0Oo . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepplayercore' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep \'guisettings.xml\': {0}' . format ( OO . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepguiseettings' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep \'Advancedsettings.xml\': {0}' . format ( oOo00O0oo00o0 . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepadvanced' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep \'Favourites.xml\': {0}' . format ( iIiIIi1 . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepfavourites' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep Super Favourites: {0}' . format ( super . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepsuper' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep Installed Repo\'s: {0}' . format ( ooOOO00Ooo . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keeprepos' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Keep My \'WhiteList\': {0}' . format ( I1IIII1i . replace ( 'true' , ii111iI1iIi1 ) . replace ( 'false' , OOO ) ) , { 'mode' : 'togglesetting' , 'name' : 'keepwhitelist' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
 if I1IIII1i == 'true' :
  directory . add_file ( 'Edit My Whitelist' , { 'mode' : 'whitelist' , 'name' : 'edit' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
  directory . add_file ( 'View My Whitelist' , { 'mode' : 'whitelist' , 'name' : 'view' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
  directory . add_file ( 'Clear My Whitelist' , { 'mode' : 'whitelist' , 'name' : 'clear' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
  directory . add_file ( 'Import My Whitelist' , { 'mode' : 'whitelist' , 'name' : 'import' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
  directory . add_file ( 'Export My Whitelist' , { 'mode' : 'whitelist' , 'name' : 'export' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
  if 18 - 18: OOooOOo + iII111i - Ii1I . II111iiii + i11iIiiIii
  if 20 - 20: I1Ii111
def Oo0oO00o ( ) :
 from resources . libs import traktit
 if 13 - 13: I11i * Oo0Ooo * ooOoO0o
 iI11iI1IiiIiI = '[COLOR springgreen]ON[/COLOR]' if CONFIG . KEEPTRAKT == 'true' else '[COLOR red]OFF[/COLOR]'
 Ii1I1i = str ( CONFIG . TRAKTSAVE ) if not CONFIG . TRAKTSAVE == '' else 'Trakt hasn\'t been saved yet.'
 directory . add_file ( '[I]Register FREE Account at https://www.trakt.tv/[/I]' , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Save Trakt Data: {0}' . format ( iI11iI1IiiIiI ) , { 'mode' : 'togglesetting' , 'name' : 'keeptrakt' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 if CONFIG . KEEPTRAKT == 'true' :
  directory . add_file ( 'Last Save: {0}' . format ( str ( Ii1I1i ) ) , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 directory . add_separator ( icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 if 99 - 99: oO0o . iII111i + ooOoO0o % oO0o . i11iIiiIii % O0
 for I1I1I in traktit . ORDER :
  if xbmc . getCondVisibility ( 'System.HasAddon({0})' . format ( traktit . TRAKTID [ I1I1I ] [ 'plugin' ] ) ) :
   Oo00OOOOO = traktit . TRAKTID [ I1I1I ] [ 'name' ]
   oOO00O = traktit . TRAKTID [ I1I1I ] [ 'path' ]
   OOOoo0OO = traktit . TRAKTID [ I1I1I ] [ 'saved' ]
   file = traktit . TRAKTID [ I1I1I ] [ 'file' ]
   oO0o0 = CONFIG . get_setting ( OOOoo0OO )
   iI1Ii11iIiI1 = traktit . trakt_user ( I1I1I )
   OooO0OO = traktit . TRAKTID [ I1I1I ] [ 'icon' ] if os . path . exists ( oOO00O ) else CONFIG . ICONTRAKT
   iiiIi = traktit . TRAKTID [ I1I1I ] [ 'fanart' ] if os . path . exists ( oOO00O ) else CONFIG . ADDON_FANART
   OO0Oooo0oOO0O = o00O0 ( 'Trakt' , I1I1I )
   oOO0O00Oo0O0o = ii1 ( 'Trakt' , I1I1I )
   OO0Oooo0oOO0O . append ( ( CONFIG . THEME2 . format ( '{0} Settings' . format ( Oo00OOOOO ) ) , 'RunPlugin(plugin://{0}/?mode=opensettings&name={1}&url=trakt)' . format ( CONFIG . ADDON_ID , I1I1I ) ) )
   if 35 - 35: iII111i * oO0o / iIii1I11I1II1 - o0oOOo0O0Ooo / OoooooooOO - I1Ii111
   directory . add_file ( '[+]-> {0}' . format ( Oo00OOOOO ) , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME3 )
   if not os . path . exists ( oOO00O ) :
    directory . add_file ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   elif not iI1Ii11iIiI1 :
    directory . add_file ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , { 'mode' : 'authtrakt' , 'name' : I1I1I } , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   else :
    directory . add_file ( '[COLOR springgreen]Addon Data: {0}[/COLOR]' . format ( iI1Ii11iIiI1 ) , { 'mode' : 'authtrakt' , 'name' : I1I1I } , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   if oO0o0 == "" :
    if os . path . exists ( file ) :
     directory . add_file ( '[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]' , { 'mode' : 'importtrakt' , 'name' : I1I1I } , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
    else :
     directory . add_file ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , { 'mode' : 'savetrakt' , 'name' : I1I1I } , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
   else :
    directory . add_file ( '[COLOR springgreen]Saved Data: {0}[/COLOR]' . format ( oO0o0 ) , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
    if 16 - 16: oO0o % I1ii11iIi11i * i11iIiiIii % i11iIiiIii
 directory . add_separator ( )
 directory . add_file ( 'Save All Trakt Data' , { 'mode' : 'savetrakt' , 'name' : 'all' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Recover All Saved Trakt Data' , { 'mode' : 'restoretrakt' , 'name' : 'all' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Import Trakt Data' , { 'mode' : 'importtrakt' , 'name' : 'all' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Clear All Addon Trakt Data' , { 'mode' : 'addontrakt' , 'name' : 'all' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Clear All Saved Trakt Data' , { 'mode' : 'cleartrakt' , 'name' : 'all' } , icon = CONFIG . ICONTRAKT , themeit = CONFIG . THEME3 )
 if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
 if 96 - 96: OOooOOo % O0 / O0
def iIi1 ( ) :
 from resources . libs import debridit
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 oooOo0OOOoo0 = '[COLOR springgreen]ON[/COLOR]' if CONFIG . KEEPDEBRID == 'true' else '[COLOR red]OFF[/COLOR]'
 Ii1I1i = str ( CONFIG . DEBRIDSAVE ) if not CONFIG . DEBRIDSAVE == '' else 'Debrid authorizations haven\'t been saved yet.'
 directory . add_file ( '[I]https://www.real-debrid.com/ is a PAID service.[/I]' , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_file ( '[I]https://www.premiumize.me/ is a PAID service.[/I]' , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Save Debrid Data: {0}' . format ( oooOo0OOOoo0 ) , { 'mode' : 'togglesetting' , 'name' : 'keepdebrid' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 if CONFIG . KEEPDEBRID == 'true' :
  directory . add_file ( 'Last Save: {0}' . format ( str ( Ii1I1i ) ) , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_separator ( icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
 for OoOO000 in debridit . ORDER :
  if xbmc . getCondVisibility ( 'System.HasAddon({0})' . format ( debridit . DEBRIDID [ OoOO000 ] [ 'plugin' ] ) ) :
   Oo00OOOOO = debridit . DEBRIDID [ OoOO000 ] [ 'name' ]
   oOO00O = debridit . DEBRIDID [ OoOO000 ] [ 'path' ]
   OOOoo0OO = debridit . DEBRIDID [ OoOO000 ] [ 'saved' ]
   file = debridit . DEBRIDID [ OoOO000 ] [ 'file' ]
   oO0o0 = CONFIG . get_setting ( OOOoo0OO )
   iI1Ii11iIiI1 = debridit . debrid_user ( OoOO000 )
   OooO0OO = debridit . DEBRIDID [ OoOO000 ] [ 'icon' ] if os . path . exists ( oOO00O ) else CONFIG . ICONDEBRID
   iiiIi = debridit . DEBRIDID [ OoOO000 ] [ 'fanart' ] if os . path . exists ( oOO00O ) else CONFIG . ADDON_FANART
   OO0Oooo0oOO0O = o00O0 ( 'Debrid' , OoOO000 )
   oOO0O00Oo0O0o = ii1 ( 'Debrid' , OoOO000 )
   OO0Oooo0oOO0O . append ( ( CONFIG . THEME2 . format ( '{0} Settings' . format ( Oo00OOOOO ) ) , 'RunPlugin(plugin://{0}/?mode=opensettings&name={1}&url=debrid)' . format ( CONFIG . ADDON_ID , OoOO000 ) ) )
   if 73 - 73: OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
   directory . add_file ( '[+]-> {0}' . format ( Oo00OOOOO ) , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME3 )
   if not os . path . exists ( oOO00O ) :
    directory . add_file ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   elif not iI1Ii11iIiI1 :
    directory . add_file ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , { 'mode' : 'authdebrid' , 'name' : OoOO000 } , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   else :
    directory . add_file ( '[COLOR springgreen]Addon Data: {0}[/COLOR]' . format ( iI1Ii11iIiI1 ) , { 'mode' : 'authdebrid' , 'name' : OoOO000 } , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   if oO0o0 == "" :
    if os . path . exists ( file ) :
     directory . add_file ( '[COLOR red]Saved Data: Save File Found (Import Data)[/COLOR]' , { 'mode' : 'importdebrid' , 'name' : OoOO000 } , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
    else :
     directory . add_file ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , { 'mode' : 'savedebrid' , 'name' : OoOO000 } , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
   else :
    directory . add_file ( '[COLOR springgreen]Saved Data: {0}[/COLOR]' . format ( oO0o0 ) , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
    if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
 directory . add_separator ( themeit = CONFIG . THEME3 )
 directory . add_file ( 'Save All Debrid Data' , { 'mode' : 'savedebrid' , 'name' : 'all' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Recover All Saved Debrid Data' , { 'mode' : 'restoredebrid' , 'name' : 'all' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Import Debrid Data' , { 'mode' : 'importdebrid' , 'name' : 'all' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Clear All Addon Debrid Data' , { 'mode' : 'addondebrid' , 'name' : 'all' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Clear All Saved Debrid Data' , { 'mode' : 'cleardebrid' , 'name' : 'all' } , icon = CONFIG . ICONDEBRID , themeit = CONFIG . THEME3 )
 if 51 - 51: iIii1I11I1II1
 if 34 - 34: oO0o + I1IiiI - oO0o
def IiI1I1i1I1 ( ) :
 from resources . libs import loginit
 if 98 - 98: I11i % i11iIiiIii % ooOoO0o + Ii1I
 OOoOO0o0o0 = '[COLOR springgreen]ON[/COLOR]' if CONFIG . KEEPLOGIN == 'true' else '[COLOR red]OFF[/COLOR]'
 Ii1I1i = str ( CONFIG . LOGINSAVE ) if not CONFIG . LOGINSAVE == '' else 'Login data hasn\'t been saved yet.'
 directory . add_file ( '[I]Several of these addons are PAID services.[/I]' , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Save API Keys: {0}' . format ( OOoOO0o0o0 ) , { 'mode' : 'togglesetting' , 'name' : 'keeplogin' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 if CONFIG . KEEPLOGIN == 'true' :
  directory . add_file ( 'Last Save: {0}' . format ( str ( Ii1I1i ) ) , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 directory . add_separator ( icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 if 11 - 11: I1IiiI
 for i1Ii11i1i in loginit . ORDER :
  if xbmc . getCondVisibility ( 'System.HasAddon({0})' . format ( loginit . LOGINID [ i1Ii11i1i ] [ 'plugin' ] ) ) :
   Oo00OOOOO = loginit . LOGINID [ i1Ii11i1i ] [ 'name' ]
   oOO00O = loginit . LOGINID [ i1Ii11i1i ] [ 'path' ]
   OOOoo0OO = loginit . LOGINID [ i1Ii11i1i ] [ 'saved' ]
   file = loginit . LOGINID [ i1Ii11i1i ] [ 'file' ]
   oO0o0 = CONFIG . get_setting ( OOOoo0OO )
   iI1Ii11iIiI1 = loginit . login_user ( i1Ii11i1i )
   OooO0OO = loginit . LOGINID [ i1Ii11i1i ] [ 'icon' ] if os . path . exists ( oOO00O ) else CONFIG . ICONLOGIN
   iiiIi = loginit . LOGINID [ i1Ii11i1i ] [ 'fanart' ] if os . path . exists ( oOO00O ) else CONFIG . ADDON_FANART
   OO0Oooo0oOO0O = o00O0 ( 'Login' , i1Ii11i1i )
   oOO0O00Oo0O0o = ii1 ( 'Login' , i1Ii11i1i )
   OO0Oooo0oOO0O . append ( ( CONFIG . THEME2 . format ( '{0} Settings' . format ( Oo00OOOOO ) ) , 'RunPlugin(plugin://{0}/?mode=opensettings&name={1}&url=login)' . format ( CONFIG . ADDON_ID , i1Ii11i1i ) ) )
   if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
   directory . add_file ( '[+]-> {0}' . format ( Oo00OOOOO ) , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME3 )
   if not os . path . exists ( oOO00O ) :
    directory . add_file ( '[COLOR red]Addon Data: Not Installed[/COLOR]' , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   elif not iI1Ii11iIiI1 :
    directory . add_file ( '[COLOR red]Addon Data: Not Registered[/COLOR]' , { 'mode' : 'authlogin' , 'name' : i1Ii11i1i } , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   else :
    directory . add_file ( '[COLOR springgreen]Addon Data: {0}[/COLOR]' . format ( iI1Ii11iIiI1 ) , { 'mode' : 'authlogin' , 'name' : i1Ii11i1i } , icon = OooO0OO , fanart = iiiIi , menu = OO0Oooo0oOO0O )
   if oO0o0 == "" :
    if os . path . exists ( file ) :
     directory . add_file ( '[COLOR red]Saved Data: Save File Found (Import Data)[/COLOR]' , { 'mode' : 'importlogin' , 'name' : i1Ii11i1i } , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
    else :
     directory . add_file ( '[COLOR red]Saved Data: Not Saved[/COLOR]' , { 'mode' : 'savelogin' , 'name' : i1Ii11i1i } , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
   else :
    directory . add_file ( '[COLOR springgreen]Saved Data: {0}[/COLOR]' . format ( oO0o0 ) , icon = OooO0OO , fanart = iiiIi , menu = oOO0O00Oo0O0o )
    if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
 directory . add_separator ( themeit = CONFIG . THEME3 )
 directory . add_file ( 'Save All Login Info' , { 'mode' : 'savelogin' , 'name' : 'all' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Recover All Saved Login Info' , { 'mode' : 'restorelogin' , 'name' : 'all' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Import Login Info' , { 'mode' : 'importlogin' , 'name' : 'all' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Clear All Addon Login Info' , { 'mode' : 'addonlogin' , 'name' : 'all' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 directory . add_file ( 'Clear All Saved Login Info' , { 'mode' : 'clearlogin' , 'name' : 'all' } , icon = CONFIG . ICONLOGIN , themeit = CONFIG . THEME3 )
 if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
 if 71 - 71: I1Ii111 + Ii1I
def iI1111ii1I ( ) :
 from resources . libs . common import tools
 if 45 - 45: i1IIi + o0oOOo0O0Ooo
 from xml . etree import ElementTree
 if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
 directory . add_file ( "[I][B][COR vermelho] !! Aviso: Desabilitar alguns complementos pode causar problemas !![/COLOR][/B][/I]" , icon = CONFIG . ICONMAINT )
 III1Iiii1I11 = glob . glob ( os . path . join ( CONFIG . ADDONS , '*/' ) )
 ooO0O00Oo0o = [ ]
 OOOOo0o00OO0000 = [ ]
 for IIII in sorted ( III1Iiii1I11 , key = lambda oOoOo00oOo : oOoOo00oOo ) :
  iiIiI = os . path . split ( IIII [ : - 1 ] ) [ 1 ]
  if iiIiI in CONFIG . EXCLUDES :
   continue
  elif iiIiI in CONFIG . DEFAULTPLUGINS :
   continue
  elif iiIiI == 'packages' :
   continue
  o00oooO0Oo = os . path . join ( IIII , 'addon.xml' )
  if os . path . exists ( o00oooO0Oo ) :
   I1i = ElementTree . parse ( o00oooO0Oo ) . getroot ( )
   O00Oooo = I1i . get ( 'id' )
   i11I = I1i . get ( 'name' )
   if 76 - 76: IiII * iII111i
   try :
    ooO0O00Oo0o . append ( tools . get_addon_info ( O00Oooo , 'name' ) )
    OOOOo0o00OO0000 . append ( O00Oooo )
   except :
    pass
    if 52 - 52: OOooOOo
   if xbmc . getCondVisibility ( 'System.HasAddon({0})' . format ( O00Oooo ) ) :
    iiiiiIIii = "[COLOR springgreen][Habilitado][/COLOR]"
    iiii1 = "false"
   else :
    iiiiiIIii = "[COLOR red][Desabilitado][/COLOR]"
    iiii1 = "true"
    if 96 - 96: i11iIiiIii % OOooOOo
   OooO0OO = os . path . join ( IIII , 'icon.png' ) if os . path . exists ( os . path . join ( IIII , 'icon.png' ) ) else CONFIG . ADDON_ICON
   iiiIi = os . path . join ( IIII , 'fanart.jpg' ) if os . path . exists ( os . path . join ( IIII , 'fanart.jpg' ) ) else CONFIG . ADDON_FANART
   directory . add_file ( "{0} {1}" . format ( iiiiiIIii , i11I ) , { 'mode' : 'toggleaddon' , 'name' : O00Oooo , 'url' : iiii1 } , icon = OooO0OO , fanart = iiiIi )
 if len ( ooO0O00Oo0o ) == 0 :
  directory . add_file ( "No Addons Found to Enable or Disable." , icon = CONFIG . ICONMAINT )
  if 70 - 70: iIii1I11I1II1
  if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
def oooo0OOOO ( ) :
 if os . path . exists ( CONFIG . ADDON_DATA ) :
  directory . add_file ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data' , { 'mode' : 'removedata' , 'name' : 'all' } , themeit = CONFIG . THEME2 )
  directory . add_file ( '[COLOR red][B][REMOVE][/B][/COLOR] All Addon_Data for Uninstalled Addons' , { 'mode' : 'removedata' , 'name' : 'uninstalled' } , themeit = CONFIG . THEME2 )
  directory . add_file ( '[COLOR red][B][REMOVE][/B][/COLOR] All Empty Folders in Addon_Data' , { 'mode' : 'removedata' , 'name' : 'empty' } , themeit = CONFIG . THEME2 )
  directory . add_file ( '[COLOR red][B][REMOVE][/B][/COLOR] {0} Addon_Data' . format ( CONFIG . ADDONTITLE ) , { 'mode' : 'resetaddon' } , themeit = CONFIG . THEME2 )
  directory . add_separator ( themeit = CONFIG . THEME3 )
  III1Iiii1I11 = glob . glob ( os . path . join ( CONFIG . ADDON_DATA , '*/' ) )
  for IIII in sorted ( III1Iiii1I11 , key = lambda oOoOo00oOo : oOoOo00oOo ) :
   iiIiI = IIII . replace ( CONFIG . ADDON_DATA , '' ) . replace ( '\\' , '' ) . replace ( '/' , '' )
   OooO0OO = os . path . join ( IIII . replace ( CONFIG . ADDON_DATA , CONFIG . ADDONS ) , 'icon.png' )
   iiiIi = os . path . join ( IIII . replace ( CONFIG . ADDON_DATA , CONFIG . ADDONS ) , 'fanart.png' )
   Oo00 = iiIiI
   iiIiIIIiiI = { 'audio.' : '[COLOR orange][AUDIO] [/COLOR]' , 'metadata.' : '[COLOR cyan][METADATA] [/COLOR]' ,
 'module.' : '[COLOR orange][MODULE] [/COLOR]' , 'plugin.' : '[COLOR blue][PLUGIN] [/COLOR]' ,
 'program.' : '[COLOR orange][PROGRAM] [/COLOR]' , 'repository.' : '[COLOR gold][REPO] [/COLOR]' ,
 'script.' : '[COLOR springgreen][SCRIPT] [/COLOR]' ,
 'service.' : '[COLOR springgreen][SERVICE] [/COLOR]' , 'skin.' : '[COLOR dodgerblue][SKIN] [/COLOR]' ,
 'video.' : '[COLOR orange][VIDEO] [/COLOR]' , 'weather.' : '[COLOR yellow][WEATHER] [/COLOR]' }
   for iiI1IIIi in iiIiIIIiiI :
    Oo00 = Oo00 . replace ( iiI1IIIi , iiIiIIIiiI [ iiI1IIIi ] )
   if iiIiI in CONFIG . EXCLUDES :
    Oo00 = '[COLOR springgreen][B][PROTECTED][/B][/COLOR] {0}' . format ( Oo00 )
   else :
    Oo00 = '[COLOR red][B][REMOVE][/B][/COLOR] {0}' . format ( Oo00 )
   directory . add_file ( ' {0}' . format ( Oo00 ) , { 'mode' : 'removedata' , 'name' : iiIiI } , icon = OooO0OO , fanart = iiiIi , themeit = CONFIG . THEME2 )
 else :
  directory . add_file ( 'No Addon data folder found.' , themeit = CONFIG . THEME3 )
  if 47 - 47: Oo0Ooo % I11i % i11iIiiIii - O0 + ooOoO0o
  if 94 - 94: I1Ii111
def i11II1I11I1 ( ) :
 from resources . libs . common import logging
 if 67 - 67: I1IiiI - o0oOOo0O0Ooo / I11i - i1IIi
 i11 = xbmcgui . Dialog ( )
 if 1 - 1: II111iiii
 O0oOo00o = i11 . select ( "[COLOR {0}]Com que frequência você listaria Limpeza automática na inicialização?[/COLOR]" . format ( CONFIG . COLOR2 ) , CONFIG . CLEANFREQ )
 if not O0oOo00o == - 1 :
  CONFIG . set_setting ( 'autocleanfreq' , str ( O0oOo00o ) )
  logging . log_notify ( '[COLOR {0}]Limpeza Automática[/COLOR]' . format ( CONFIG . COLOR1 ) ,
 '[COLOR {0}]Frequência Agora {1}[/COLOR]' . format ( CONFIG . COLOR2 , CONFIG . CLEANFREQ [ O0oOo00o ] ) )
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
def I11iI ( ) :
 directory . add_file ( 'Create QR Code' , { 'mode' : 'createqr' } , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Notificações de teste' , { 'mode' : 'testnotify' } , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Atualização de teste' , { 'mode' : 'testupdate' } , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Test Build Prompt' , { 'mode' : 'testbuildprompt' } , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Testar configurações de salvamento de dados' , { 'mode' : 'testsavedata' } , themeit = CONFIG . THEME1 )
 directory . add_file ( 'Testar configurações de salvamento de dados' , { 'mode' : 'binarycheck' } , themeit = CONFIG . THEME1 )
 if 68 - 68: iIii1I11I1II1 / OOooOOo
 if 23 - 23: I1Ii111 . IiII
 if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 if 42 - 42: Oo0Ooo
 if 76 - 76: I1IiiI * iII111i % I1Ii111
 if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
 if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
def o00O0 ( add = '' , name = '' ) :
 I1 = [ ]
 if 97 - 97: ooOoO0o
 ii1I1IIIi = quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
 o0OOOOooo = add . replace ( 'Debrid' , 'Real Debrid' )
 OooO0OOo0OOo0o0O0O = quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
 name = name . replace ( 'url' , 'URL Resolver' )
 I1 . append ( ( CONFIG . THEME2 . format ( name . title ( ) ) , ' ' ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Save {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=save{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Restore {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=restore{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Clear {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=clear{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 if 65 - 65: i11iIiiIii
 I1 . append ( ( CONFIG . THEME2 . format ( '{0} Settings' . format ( CONFIG . ADDONTITLE ) ) , 'RunPlugin(plugin://{0}/?mode=settings)' . format ( CONFIG . ADDON_ID ) ) )
 if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
 return I1
 if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
 if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
def ii1 ( add = '' , name = '' ) :
 I1 = [ ]
 if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
 ii1I1IIIi = quote_plus ( add . lower ( ) . replace ( ' ' , '' ) )
 o0OOOOooo = add . replace ( 'Debrid' , 'Real Debrid' )
 OooO0OOo0OOo0o0O0O = quote_plus ( name . lower ( ) . replace ( ' ' , '' ) )
 name = name . replace ( 'url' , 'URL Resolver' )
 I1 . append ( ( CONFIG . THEME2 . format ( name . title ( ) ) , ' ' ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Register {0}' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=auth{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Save {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=save{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Restore {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=restore{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Import {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=import{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 I1 . append ( ( CONFIG . THEME3 . format ( 'Clear Addon {0} Data' . format ( o0OOOOooo ) ) , 'RunPlugin(plugin://{0}/?mode=addon{1}&name={2})' . format ( CONFIG . ADDON_ID , ii1I1IIIi , OooO0OOo0OOo0o0O0O ) ) )
 if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
 I1 . append ( ( CONFIG . THEME2 . format ( '{0} Settings' . format ( CONFIG . ADDONTITLE ) ) , 'RunPlugin(plugin://{0}/?mode=settings)' . format ( CONFIG . ADDON_ID ) ) )
 if 79 - 79: O0 * i11iIiiIii - IiII / IiII
 return I1
# Team KelTec Media'Play