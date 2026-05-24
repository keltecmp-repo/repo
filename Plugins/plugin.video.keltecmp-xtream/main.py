# -*- coding: utf-8 -*-
# KelTec MediaPlay — Fenix Format
# Gerado em: 2026-05-24
# Camadas: 5

_lx0_0 = 148485 ^ 615447
_lx1_1 = len("16ace2")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-883542)
_lx3_3 = 474014 * 0
_lx4_4 = 266587 ^ 875342
# _K: carregamento protegido
_M = 'a+5p1SSvUZiloGjDVv6kvskLfVYI9SklfWWGdYLo795noGOFdOlRzauiZJUE9qLsy197Cw/0KSciaYR/0bi82zbzMtR07gTJrqZi'
_D = '==wJZxI/n574leulwM9WsD5XwaDkwLeyAyZgesBBKJmUfCUah5c71B6mvc/MeSacmDKPwSOVMEonN8cl5nL59YaQO1ix2jgPetoUfbxdzCnpcd/nW70P62TlIrXc1ApZiepHFopbtPmg5NqCULSmOFIZExONTNnB3ZqS8wICbIG8nWaoRCSk9IfNOHF7IEOy4XUPzZo/QeuLZLXs96vYU/LCorcCK/q973zMu6/u89h3I5A4HOTdM23anScx7N3hJBjmp57WbQqhhE/P/5qaJImfQHK2T1wGXR8VwqHJTDhCtCLJmctvZ0Fop6ZHwPyYRSGYfjspmcTAAOHDekrZCPHLARKVUdl4aDmlIp7CmEOixXa5kQwndPaMkunzW69lusSqbjuLrpv0qQ1CVOhHSDXrSUgLlhbLDashyiMUNihpX9GwgPPnM14CyFvFnDy0IaA9xfKJ8kRScYbMw0PbrC6ETQ8tSLKlo3KaIydwbJKistYtfozbPfNxnS2nzQ6++5u72ZqTKIJ9zy4lmAAI+m9UFe3uxzn1KVyXtcyj1rc4fND75XcEJuHMVIi6WRFHfS48CT8qdsz5q0vBJ91uxAiYdZzueXBs26TBmSe5e5xBAd2qA5W26zFp5NM3a3Zqn86IbvqCTrs/61KL6Zl6d0Oblg1CsSZOPE/xWCqGiMj6SAwcL5lKitqWVBZ8b6x3Y62IQcmDtuLfcBVNzeD2YTSDHC0Hd89eYcoBTxIKam2sBnY1t0KJ+xKJm2a8yhbmuqwtMlJmFerpJyGwTdo2SQFG6mF5SEeD8VPmR0t6K7/CFLf1kmUGrYQ7yZI221Miy2BgkgarzHXJcw3xiXXkpJgSbkdvlGotcpEg3jjd7fRNNdjFpNKQdw/myRqljXq7yHoIeWKhKf3X9vvO8ZctFiy2ioX3+t+qTWDJ/twDQ52jpRoBLuWVN1R4T/w6uiZB6fYHMyxdfrLs+J3CJDtgmUzp91fvA90cMuSe7Z3ssKWR1ew5uRujR/y7X6L7nVWpk7kB1b8SXT0VBRUuGzODwZ4CI2Jd8cHbMEfH7dvi/J89x2peJDGFoSft0uJAUbhTxs4xmGj7fCUv8OqGMsI8u+B5IdUhDc33c82Wsn6QwYDbGQPyKjxzLBhy7mdUzo4Q9HMDzGUgi2bNxVR6E+VJUgmSAYH8nCAVHGBhRyNsQjyW3WWlO9LEKU1hn9pT8/STmhdYDN/nK7V8/Dqju5Xa1HFc4q34iTiJBwJ3iXRXgSE6+uGuXJdmF/7cj1h0XHrTpAcuv6YKnijVHHoOGrFG/hdxk+Be4Jr/D8nAcncgKXo6t/PMNJozvrQXKid4xB81+4jzVhXaJdj6dqvDjr4yGz4yGs3I+DWn5c0XF4//8TS9Ls/tPLFyS/U2rhWOtiwIb/qcqI6umWQzK4bZsFLHEuBuKxrlsTRPv5Ari2G42VioCrxlLr4XPISUgzaQ4QA2WXmcuj3vzXUrXZlhtb3PGLrGotUPCNtDWJs00eBzWj2KPyFwivLeZNBpt8ufcPm3V7GR5uZ7'

import re as _re
_7aed=[49,219,54,133,114,188,32,178]+[7,99,143,186,164,194,195,2]
_03ff=[236,251,148,5,71,61,168,89]+[158,11,118,122,180,231,254,188]
_93d2=bytes([a^b for a,b in zip([67,190,69,234,7,206,67,215,116,76,235,219,208,163],_7aed*8)]).decode()
_f93e=bytes([a^b for a,b in zip([136,154,224,100,105,69,197,53],_03ff*8)]).decode()
_0792=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_93d2.split('/'),_f93e)
with open(_0792,'r') as _f:_292c=_f.read()
_km=_re.search(bytes([0x3c,0x6b,0x3e]).decode()+r'([^<]+)'+bytes([0x3c,0x2f,0x6b,0x3e]).decode(),_292c)
_K=_km.group(1).strip() if _km else ''
def _xr(d,k):
    kl=len(k);return bytes(d[i]^k[i%kl] for i in range(len(d)))
def _dk(sd,c):
    return _h.sha256((_K+sd+str(c)).encode('utf-8')).digest()
def _dc(s,c,sd):
    r=_b.b64decode(s[::-1]);return _z.decompress(_xr(r,_dk(sd,c))).decode('utf-8')
def _run():
    mk=_h.sha256(_K.encode('utf-8')).digest()
    meta=_xr(_b.b64decode(_M),mk).decode('utf-8').split(':',2)
    sd=meta[0];nc=int(meta[1])
    d=_D
    for c in range(nc-1,-1,-1):d=_dc(d,c,sd)
    idx=d.find('||')
    src=d[idx+2:] if idx!=-1 else d
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()