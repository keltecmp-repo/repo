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
import os
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from resources . libs . common import directory
from resources . libs . common . config import CONFIG
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
class I1IiI :
 if 73 - 73: OOooOOo / ii11ii1ii
 def get_listing ( self ) :
  from resources . libs import check
  from resources . libs . common import logging
  from resources . libs . common import tools
  if 94 - 94: OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo
  O0oOO0o0 = int ( logging . error_checking ( count = True ) )
  i1ii1iIII = str ( O0oOO0o0 ) + ' Error(s) Found' if O0oOO0o0 > 0 else 'None Found'
  if 59 - 59: II1i * o00ooo0 / o00O0oo * Oo0Ooo
  if CONFIG . AUTOUPDATE == 'Yes' :
   II1Ii1iI1i = tools . open_url ( CONFIG . BUILDFILE , check = True )
   if 12 - 12: I1ii11iIi11i
   if II1Ii1iI1i :
    IiIiI11iIi = check . check_wizard ( 'version' )
    if IiIiI11iIi :
     if IiIiI11iIi > CONFIG . ADDON_VERSION :
      directory . add_file (
 '{0} [v{1}] [COLOR red][B][UPDATE v{2}][/B][/COLOR]' . format ( CONFIG . ADDONTITLE ,
 CONFIG . ADDON_VERSION , IiIiI11iIi ) ,
 { 'mode' : 'wizardupdate' } , themeit = CONFIG . THEME2 )
     else :
      directory . add_file ( '{0} [v{1}]' . format ( CONFIG . ADDONTITLE , CONFIG . ADDON_VERSION ) ,
 themeit = CONFIG . THEME2 )
   else :
    directory . add_file ( '{0} [v{1}]' . format ( CONFIG . ADDONTITLE , CONFIG . ADDON_VERSION ) ,
 themeit = CONFIG . THEME2 )
  else :
   directory . add_file ( '{0} [v{1}]' . format ( CONFIG . ADDONTITLE , CONFIG . ADDON_VERSION ) , themeit = CONFIG . THEME2 )
  if len ( CONFIG . BUILDNAME ) > 0 :
   Ii1IIii11 = check . check_build ( CONFIG . BUILDNAME , 'version' )
   Oooo0000 = '{0} (v{1})' . format ( CONFIG . BUILDNAME , CONFIG . BUILDVERSION )
   if Ii1IIii11 > CONFIG . BUILDVERSION :
    Oooo0000 = '{0} [COLOR red][B][UPDATE v{1}][/B][/COLOR]' . format ( Oooo0000 , Ii1IIii11 )
   directory . add_dir ( Oooo0000 , { 'mode' : 'viewbuild' , 'name' : CONFIG . BUILDNAME } , themeit = CONFIG . THEME4 )
   if 22 - 22: OoOO0ooOOoo0O . o00O0oo
   from resources . libs . gui . build_menu import BuildMenu
   I11 = BuildMenu ( ) . theme_count ( CONFIG . BUILDNAME )
   if I11 :
    directory . add_file ( 'Nenhum' if CONFIG . BUILDTHEME == "" else CONFIG . BUILDTHEME , { 'mode' : 'theme' , 'name' : CONFIG . BUILDNAME } ,
 themeit = CONFIG . THEME5 )
  else :
   directory . add_dir ( 'Nenhum' , { 'mode' : 'builds' } , themeit = CONFIG . THEME4 )
  directory . add_separator ( )
  directory . add_dir ( 'Builds' , { 'mode' : 'builds' } , icon = CONFIG . ICONBUILDS , themeit = CONFIG . THEME1 )
  directory . add_dir ( 'Manutenção & Ferramentas' , { 'mode' : 'maint' } , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME1 )
  if ( tools . platform ( ) == 'android' or CONFIG . DEVELOPER == 'true' ) :
   directory . add_dir ( 'Instalador de APK' , { 'mode' : 'apk' } , icon = CONFIG . ICONAPK , themeit = CONFIG . THEME1 )
  if tools . open_url ( CONFIG . ADDONFILE , check = True ) or os . path . exists ( os . path . join ( CONFIG . ADDON_PATH , 'resources' , 'text' , 'addons.json' ) ) :
   directory . add_dir ( 'Instalador de Addon' , { 'mode' : 'addons' } , icon = CONFIG . ICONADDONS , themeit = CONFIG . THEME1 )
  if tools . open_url ( CONFIG . YOUTUBEFILE , check = True ) and not CONFIG . YOUTUBETITLE == '' :
   directory . add_dir ( CONFIG . YOUTUBETITLE , { 'mode' : 'youtube' } , icon = CONFIG . ICONYOUTUBE , themeit = CONFIG . THEME1 )
  directory . add_dir ( 'Guardar dados' , { 'mode' : 'savedata' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME1 )
  if CONFIG . HIDECONTACT == 'No' :
   directory . add_file ( 'Contato' , { 'mode' : 'contact' } , icon = CONFIG . ICONCONTACT , themeit = CONFIG . THEME1 )
  directory . add_separator ( )
  directory . add_file ( 'Carregar arquivo de log' , { 'mode' : 'uploadlog' } , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME1 )
  directory . add_file ( 'Ver Erros no Log: {0}' . format ( i1ii1iIII ) , { 'mode' : 'viewerrorlog' } , icon = CONFIG . ICONMAINT ,
 themeit = CONFIG . THEME1 )
  if O0oOO0o0 > 0 :
   directory . add_file ( 'Ver o último erro no log' , { 'mode' : 'viewerrorlast' } , icon = CONFIG . ICONMAINT , themeit = CONFIG . THEME1 )
  directory . add_separator ( )
  directory . add_file ( 'Configurações' , { 'mode' : 'settings' , 'name' : CONFIG . ADDON_ID } , icon = CONFIG . ICONSETTINGS , themeit = CONFIG . THEME1 )
  if CONFIG . DEVELOPER == 'true' :
   directory . add_dir ( 'Menu do desenvolvedor' , { 'mode' : 'developer' } , icon = CONFIG . ADDON_ICON , themeit = CONFIG . THEME1 )
# Team KelTec Media'Play