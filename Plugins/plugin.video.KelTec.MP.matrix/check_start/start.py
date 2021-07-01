# -*- coding: utf-8 -*-
#
import re
import json
import requests
from bs4 import BeautifulSoup
if 64 - 64: i11iIiiIii
class OO0o :
 def __init__ ( self ) :
  self . sockets = [ ]
  self . acquire_sockets ( )
  self . proxies = self . mount_proxies ( )
  if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
 def acquire_sockets ( self ) :
  ii11i = requests . get (
 'https://api.proxyscrape.com/?request=displayproxies&proxytype='
 'http&timeout=7000&country=BR&anonymity=elite&ssl=yes'
 ) . text
  self . sockets = ii11i . split ( '\n' )
  if 66 - 66: iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
 def mount_proxies ( self ) :
  I11i = self . sockets . pop ( 0 )
  O0O = {
 'http' : self . sockets ,
 }
  return O0O # Team KelTec
