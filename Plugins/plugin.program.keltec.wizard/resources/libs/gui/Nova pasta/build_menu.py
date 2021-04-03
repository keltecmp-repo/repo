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
import re
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
try :
 from urllib . parse import quote_plus
except ImportError :
 from urllib import quote_plus
 if 73 - 73: II111iiii
from resources . libs import check
from resources . libs . common import directory
from resources . libs . common import tools
from resources . libs . common . config import CONFIG
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
class IiiIII111iI :
 if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . OoO0O00 - I1ii11iIi11i
 def _list_all ( self , match , kodiv = None ) :
  from resources . libs import test
  if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . Oo0ooO0oo0oO
  for oo00 , o00 , Oo0oO0ooo , o0oOoO00o , i1 , oOOoo00O0O , i1111 , i11 , I11 , Oo0o0000o0o0 in match :
   if not CONFIG . SHOWADULT == 'true' and I11 . lower ( ) == 'yes' :
    continue
   if not CONFIG . DEVELOPER == 'true' and test . str_test ( oo00 ) :
    continue
    if 86 - 86: OoOoOO00 % I1IiiI
   if not kodiv or kodiv == int ( float ( i1 ) ) :
    oo = self . create_install_menu ( oo00 )
    directory . add_dir ( '[{0}] {1} (v{2})' . format ( float ( i1 ) , oo00 , o00 ) , { 'mode' : 'viewbuild' , 'name' : oo00 } , description = Oo0o0000o0o0 , fanart = i11 , icon = i1111 , menu = oo , themeit = CONFIG . THEME2 )
    if 33 - 33: II111iiii * Oo0Ooo - o0oOOo0O0Ooo * iIii1I11I1II1 * OoooooooOO * Oo0ooO0oo0oO
 def theme_count ( self , name , count = True ) :
  from resources . libs import check
  from resources . libs . common import tools
  if 27 - 27: OoO0O00
  oOOOo0o0O = check . check_build ( name , 'theme' )
  if 72 - 72: Oo0Ooo % OOooOOo . I1IiiI / I11i * I1IiiI
  iiiI11 = tools . open_url ( oOOOo0o0O )
  if 91 - 91: o0oOOo0O0Ooo / II111iiii . I1ii11iIi11i + OOooOOo
  if not iiiI11 :
   return False
   if 47 - 47: OoOoOO00 / Ii1I * OoooooooOO
  II111iiiiII = iiiI11 . text
  oOoOo00oOo = tools . clean_text ( II111iiiiII )
  Oo = re . compile ( 'name="(.+?)"' ) . findall ( oOoOo00oOo )
  if 85 - 85: OOooOOo % I1ii11iIi11i * Oo0ooO0oo0oO
  if len ( Oo ) == 0 :
   return False
   if 90 - 90: o0oOOo0O0Ooo % o0oOOo0O0Ooo % I11i * OoOoOO00
  i1IIiiiii = [ ]
  for o00o in Oo :
   i1IIiiiii . append ( o00o )
   if 41 - 41: i1IIi + O0oo0OO0 + OOooOOo - O00oOoOoO0o0O
  if len ( i1IIiiiii ) > 0 :
   if count :
    return len ( i1IIiiiii )
   else :
    return i1IIiiiii
  else :
   return False
   if 77 - 77: Oo0Ooo . O00oOoOoO0o0O % Oo0ooO0oo0oO
 def get_listing ( self ) :
  from resources . libs import test
  if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
  iiiI11 = tools . open_url ( CONFIG . BUILDFILE )
  if 17 - 17: oO0o . Oo0Ooo . I1ii11iIi11i
  if iiiI11 :
   oOoOo00oOo = tools . clean_text ( iiiI11 . text )
  else :
   directory . add_file ( 'Versão Kodi: {0}' . format ( CONFIG . KODIV ) , icon = CONFIG . ICONBUILDS ,
 themeit = CONFIG . THEME3 )
   directory . add_dir ( 'Menu Salvar Dados' , { 'mode' : 'savedata' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME3 )
   directory . add_separator ( )
   directory . add_file ( 'URL para arquivo txt não é válido' , icon = CONFIG . ICONBUILDS , themeit = CONFIG . THEME3 )
   directory . add_file ( '{0}' . format ( CONFIG . BUILDFILE ) , icon = CONFIG . ICONBUILDS , themeit = CONFIG . THEME3 )
   return
   if 3 - 3: OoOoOO00 . Oo0Ooo . I1IiiI / Ii1I
  IiiiI1II1I1 , ooIi11iI1i , Ooo , O0o0Oo = check . build_count ( )
  if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iii1I1I + iii1I1I
  Oo = re . compile ( 'name="(.+?)".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( oOoOo00oOo )
  if 11 - 11: iii1I1I - OoO0O00 % Oo0ooO0oo0oO % iii1I1I / OoOoOO00 - OoO0O00
  if IiiiI1II1I1 == 1 :
   for oo00 , o00 , Oo0oO0ooo , o0oOoO00o , i1 , oOOoo00O0O , i1111 , i11 , I11 , Oo0o0000o0o0 in Oo :
    if not CONFIG . SHOWADULT == 'true' and I11 . lower ( ) == 'yes' :
     continue
    if not CONFIG . DEVELOPER == 'true' and test . str_test ( oo00 ) :
     continue
     if 74 - 74: iii1I1I * O0
    self . view_build ( Oo [ 0 ] [ 0 ] )
    return
    if 89 - 89: oO0o + Oo0Ooo
  directory . add_file ( 'Versão Kodi: {0}' . format ( CONFIG . KODIV ) , icon = CONFIG . ICONBUILDS , themeit = CONFIG . THEME3 )
  directory . add_dir ( 'Menu Salvar Dados' , { 'mode' : 'savedata' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME3 )
  directory . add_separator ( )
  if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
  if len ( Oo ) >= 1 :
   if CONFIG . SEPARATE == 'true' :
    self . _list_all ( Oo )
   else :
    if ooIi11iI1i > 0 :
     III1ii1iII = '+' if CONFIG . SHOW19 == 'false' else '-'
     directory . add_file ( '[B]{0} Matrix Builds ({1})[/B]' . format ( III1ii1iII , ooIi11iI1i ) , { 'mode' : 'togglesetting' ,
 'name' : 'show19' } , themeit = CONFIG . THEME3 )
     if CONFIG . SHOW19 == 'true' :
      self . _list_all ( Oo , kodiv = 19 )
      if 54 - 54: I1IiiI % II111iiii % II111iiii
  elif O0o0Oo > 0 :
   if Ooo > 0 :
    directory . add_file ( 'No momento, há apenas construções para adultos' , icon = CONFIG . ICONBUILDS ,
 themeit = CONFIG . THEME3 )
    directory . add_file ( 'Habilite Mostrar Adultos em Configurações do Complemento > Diversos' , icon = CONFIG . ICONBUILDS ,
 themeit = CONFIG . THEME3 )
   else :
    directory . add_file ( 'Atualmente não há construções oferecidas de {0}' . format ( CONFIG . ADDONTITLE ) ,
 icon = CONFIG . ICONBUILDS , themeit = CONFIG . THEME3 )
  else :
   directory . add_file ( 'Arquivo de texto para compilações formatado incorretamente.' , icon = CONFIG . ICONBUILDS ,
 themeit = CONFIG . THEME3 )
   if 13 - 13: o0oOOo0O0Ooo . Ii1I
 def view_build ( self , name ) :
  if 19 - 19: I11i + Oo0ooO0oo0oO
  iiiI11 = tools . open_url ( CONFIG . BUILDFILE )
  if 53 - 53: OoooooooOO . i1IIi
  if iiiI11 :
   oOoOo00oOo = tools . clean_text ( iiiI11 . text )
  else :
   directory . add_file ( 'URL para arquivo txt não é válido' , themeit = CONFIG . THEME3 )
   directory . add_file ( '{0}' . format ( CONFIG . BUILDFILE ) , themeit = CONFIG . THEME3 )
   return
   if 18 - 18: o0oOOo0O0Ooo
  if not check . check_build ( name , 'version' ) :
   directory . add_file ( 'Erro ao ler o arquivo txt.' , themeit = CONFIG . THEME3 )
   directory . add_file ( '{0} não foi encontrado na lista de builds.' . format ( name ) , themeit = CONFIG . THEME3 )
   return
   if 28 - 28: OOooOOo - O00oOoOoO0o0O . O00oOoOoO0o0O + OoOoOO00 - OoooooooOO + O0
  Oo = re . compile (
 'name="%s".+?ersion="(.+?)".+?rl="(.+?)".+?ui="(.+?)".+?odi="(.+?)".+?heme="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?review="(.+?)".+?dult="(.+?)".+?nfo="(.+?)".+?escription="(.+?)"' % name ) . findall (
 oOoOo00oOo )
  if 95 - 95: OoO0O00 % oO0o . O0
  for o00 , Oo0oO0ooo , o0oOoO00o , i1 , oOOOo0o0O , i1111 , i11 , I1i1I , I11 , oOO00oOO , Oo0o0000o0o0 in Oo :
   OoOo = '{0} (v{1})' . format ( name , o00 )
   if 18 - 18: i11iIiiIii
   Ii11I = CONFIG . BUILDNAME == name and o00 > CONFIG . BUILDVERSION
   OOO0OOO00oo = True if float ( CONFIG . KODIV ) == float ( i1 ) else False
   Iii111II = tools . open_url ( I1i1I , check = True )
   iiii11I = tools . open_url ( o0oOoO00o , check = True )
   Ooo0OO0oOO = tools . open_url ( oOOOo0o0O , check = True )
   if 50 - 50: I1IiiI
   if Ii11I :
    OoOo = '{0} [COLOR red][CURRENT v{1}][/COLOR]' . format ( OoOo , CONFIG . BUILDVERSION )
    if 34 - 34: I1IiiI * II111iiii % iii1I1I * OoOoOO00 - I1IiiI
   directory . add_file ( OoOo , description = Oo0o0000o0o0 , fanart = i11 , icon = i1111 , themeit = CONFIG . THEME4 )
   directory . add_separator ( )
   directory . add_dir ( 'Menu Salvar Dados' , { 'mode' : 'savedata' } , icon = CONFIG . ICONSAVE , themeit = CONFIG . THEME3 )
   directory . add_file ( 'Informações de construção' , { 'mode' : 'buildinfo' , 'name' : name } , description = Oo0o0000o0o0 , fanart = i11 ,
 icon = i1111 , themeit = CONFIG . THEME3 )
   if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
   if Iii111II :
    directory . add_file ( 'Ver visualização do vídeo' , { 'mode' : 'buildpreview' , 'name' : name } , description = Oo0o0000o0o0 , fanart = i11 ,
 icon = i1111 , themeit = CONFIG . THEME3 )
    if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
   if OOO0OOO00oo :
    directory . add_file (
 '[I]Construir projetado para Kodi v{0} (instalado: v{1})[/I]' . format ( str ( i1 ) , str ( CONFIG . KODIV ) ) ,
 fanart = i11 , icon = i1111 , themeit = CONFIG . THEME3 )
    if 16 - 16: O0 - O0oo0OO0 * iIii1I11I1II1 + iii1I1I
   directory . add_separator ( 'INSTALAR' )
   directory . add_file ( 'INSTALAR' , { 'mode' : 'install' , 'action' : 'build' , 'name' : name } , description = Oo0o0000o0o0 , fanart = i11 ,
 icon = i1111 , themeit = CONFIG . THEME1 )
   if 50 - 50: II111iiii - Oo0ooO0oo0oO * I1ii11iIi11i / O0oo0OO0 + o0oOOo0O0Ooo
   if iiii11I :
    directory . add_file ( 'Aplicar guiFix' , { 'mode' : 'install' , 'action' : 'gui' , 'name' : name } , description = Oo0o0000o0o0 , fanart = i11 ,
 icon = i1111 , themeit = CONFIG . THEME1 )
    if 88 - 88: Ii1I / O0oo0OO0 + iii1I1I - II111iiii / Oo0ooO0oo0oO - OoOoOO00
   if Ooo0OO0oOO :
    directory . add_separator ( 'TEMAS' , fanart = i11 , icon = i1111 )
    if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
    iiiI11 = tools . open_url ( oOOOo0o0O )
    oOOoo00O0O = iiiI11 . text
    oo000OO00Oo = tools . clean_text ( oOOoo00O0O )
    Oo = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' ) . findall ( oo000OO00Oo )
    for O0OOO0OOoO0O , O00Oo000ooO0 , OoO0O00IIiII , o0 , ooOooo000oOO , Oo0o0000o0o0 in Oo :
     Oo0oOOo = CONFIG . SHOWADULT != 'true' and ooOooo000oOO . lower ( ) == 'yes'
     if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
     if Oo0oOOo :
      continue
      if 75 - 75: oO0o
     I1III = O0OOO0OOoO0O if not O0OOO0OOoO0O == CONFIG . BUILDTHEME else "[B]{0} (Installed)[/B]" . format ( O0OOO0OOoO0O )
     OoO0O00IIiII = OoO0O00IIiII if tools . open_url ( OoO0O00IIiII , check = True ) else i1111
     o0 = o0 if tools . open_url ( o0 , check = True ) else i11
     if 63 - 63: OOooOOo % oO0o * oO0o * OoO0O00 / I1ii11iIi11i
     directory . add_file ( I1III , { 'mode' : 'install' , 'action' : 'theme' , 'name' : name , 'url' : O0OOO0OOoO0O } , description = Oo0o0000o0o0 , fanart = o0 ,
 icon = OoO0O00IIiII , themeit = CONFIG . THEME3 )
     if 74 - 74: II111iiii
 def build_info ( self , name ) :
  from resources . libs import check
  from resources . libs . common import logging
  from resources . libs . common import tools
  from resources . libs . gui import window
  if 75 - 75: o0oOOo0O0Ooo . Oo0ooO0oo0oO
  iiiI11 = tools . open_url ( CONFIG . BUILDFILE , check = True )
  if 54 - 54: II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + iIii1I11I1II1 * Oo0ooO0oo0oO
  if iiiI11 :
   if check . check_build ( name , 'url' ) :
    name , o00 , Oo0oO0ooo , O00O0oOO00O00 , i1Oo00 , i1 , oOOoo00O0O , i1111 , i11 , I1i1I , I11 , oOO00oOO , Oo0o0000o0o0 = check . check_build ( name , 'all' )
    I11 = 'Yes' if I11 . lower ( ) == 'yes' else 'No'
    if 31 - 31: O0oo0OO0 . OoOoOO00 / O0
    o000O0o = tools . open_url ( oOO00oOO )
    if 42 - 42: OoOoOO00
    if o000O0o :
     try :
      II , Ii1I1IIii1II , O0ii1ii1ii , oooooOoo0ooo , I1I1IiI1 , III1iII1I1ii , oOOo0 , oo00O00oO , iIiIIIi , ooo00OOOooO , O00OOOoOoo0O , O000OOo00oo = check . check_info ( o000O0o . text )
      oo0OOo = True
     except :
      oo0OOo = False
    else :
     oo0OOo = False
     if 64 - 64: I11i
    i1IIiiiii = self . theme_count ( name , count = False )
    if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
    iI1 = "[COLOR {0}]Nome da construção:[/COLOR] [COLOR {1}]{2}[/COLOR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , name )
    iI1 += "[COLOR {0}]Build Version:[/COLOR] [COLOR {1}]{2}[/COLOR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , o00 )
    if i1IIiiiii :
     iI1 += "[COLOR {0}]Build Tema(s):[/COLOR] [COLOR {1}]{2}[/COLOR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , ', ' . join ( i1IIiiiii ) )
    iI1 += "[COLOR {0}]Versão Kodi:[/COLOR] [COLOR {1}]{2}[/COLOR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , i1 )
    iI1 += "[COLOR {0}]Conteúdo adulto:[/COLOR] [COLOR {1}]{2}[/COLOR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , I11 )
    iI1 += "[COLOR {0}]Descrição:[/COLOR] [COLOR {1}]{2}[/COLOR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , Oo0o0000o0o0 )
    if 28 - 28: OoO0O00 + Ii1I / OoO0O00 . II111iiii
    if oo0OOo :
     iI1 += "[COLOR {0}]Última atualização:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , I1I1IiI1 )
     iI1 += "[COLOR {0}]Tamanho Extraído:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , tools . convert_size ( int ( float ( Ii1I1IIii1II ) ) ) )
     iI1 += "[COLOR {0}]Tamanho Zip:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , tools . convert_size ( int ( float ( O0ii1ii1ii ) ) ) )
     iI1 += "[COLOR {0}]Nome da Skin:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , oooooOoo0ooo )
     iI1 += "[COLOR {0}]Programa:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , III1iII1I1ii )
     iI1 += "[COLOR {0}]Video:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , oOOo0 )
     iI1 += "[COLOR {0}]Música:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , oo00O00oO )
     iI1 += "[COLOR {0}]Fotos:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , iIiIIIi )
     iI1 += "[COLOR {0}]Repositórios:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , ooo00OOOooO )
     iI1 += "[COLOR {0}]Scripts:[/COLOR] [COLOR {1}]{2}[/COLOR][CR][CR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , O00OOOoOoo0O )
     iI1 += "[COLOR {0}]Binários:[/COLOR] [COLOR {1}]{2}[/COLOR]" . format ( CONFIG . COLOR2 , CONFIG . COLOR1 , O000OOo00oo )
     if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
    window . show_text_box ( "Visualizando informações de compilação: {0}" . format ( name ) , iI1 )
   else :
    logging . log ( "Nome de compilação inválido!" )
  else :
   logging . log ( "O arquivo de texto de compilação não está funcionando: {0}" . format ( CONFIG . BUILDFILE ) )
   if 31 - 31: II111iiii . I1IiiI
 def build_video ( self , name ) :
  from resources . libs import check
  from resources . libs import yt
  from resources . libs . common import logging
  from resources . libs . common import tools
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iii1I1I * O00oOoOoO0o0O . i11iIiiIii
  iiiI11 = tools . open_url ( CONFIG . BUILDFILE , check = True )
  if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iii1I1I
  if iiiI11 :
   ooOOOoOooOoO = check . check_build ( name , 'preview' )
   if tools . open_url ( ooOOOoOooOoO , check = True ) :
    yt . play_video ( ooOOOoOooOoO )
   else :
    logging . log ( "[{0}]Não foi possível encontrar url para a visualização do vídeo" . format ( name ) )
  else :
   logging . log ( "O arquivo de texto de compilação não está funcionando: {0}" . format ( CONFIG . BUILDFILE ) )
   if 91 - 91: iii1I1I % i1IIi % iIii1I11I1II1
 def create_install_menu ( self , name ) :
  IIi1I11I1II = [ ]
  if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
  o0OOOO00O0Oo = quote_plus ( name )
  IIi1I11I1II . append ( ( CONFIG . THEME2 . format ( name ) , 'RunAddon({0}, ?mode=viewbuild&name={1})' . format ( CONFIG . ADDON_ID , o0OOOO00O0Oo ) ) )
  IIi1I11I1II . append ( ( CONFIG . THEME3 . format ( 'Nova instalação' ) , 'RunPlugin(plugin://{0}/?mode=install&name={1}&url=fresh)' . format ( CONFIG . ADDON_ID , o0OOOO00O0Oo ) ) )
  IIi1I11I1II . append ( ( CONFIG . THEME3 . format ( 'Instalação normal' ) , 'RunPlugin(plugin://{0}/?mode=install&name={1}&url=normal)' . format ( CONFIG . ADDON_ID , o0OOOO00O0Oo ) ) )
  IIi1I11I1II . append ( ( CONFIG . THEME3 . format ( 'Aplicar guiFix' ) , 'RunPlugin(plugin://{0}/?mode=install&name={1}&url=gui)' . format ( CONFIG . ADDON_ID , o0OOOO00O0Oo ) ) )
  IIi1I11I1II . append ( ( CONFIG . THEME3 . format ( 'Informações de construção' ) , 'RunPlugin(plugin://{0}/?mode=buildinfo&name={1})' . format ( CONFIG . ADDON_ID , o0OOOO00O0Oo ) ) )
  IIi1I11I1II . append ( ( CONFIG . THEME2 . format ( '{0} Configurações' . format ( CONFIG . ADDONTITLE ) ) , 'RunPlugin(plugin://{0}/?mode=settings)' . format ( CONFIG . ADDON_ID ) ) )
  if 48 - 48: O0
  return IIi1I11I1II
# Team KelTec Media'Play