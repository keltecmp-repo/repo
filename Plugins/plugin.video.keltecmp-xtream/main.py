# -*- coding: utf-8 -*-
# KelTec MediaPlay — Fenix Format
# Gerado em: 2026-06-24
# Camadas: 5

_lx0_0 = 264807 ^ 427347
_lx1_1 = len("8dde92")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-673192)
_lx3_3 = 647287 * 0
_lx4_4 = 396036 ^ 559288
# _K: carregamento protegido
_M = 'c55Xviek+B0szgp2joBWOsusgnmIGKZ/7RmbuA5dTHghlgq6ePC8EyDCBXOOhgM4kqWBK4weonG+TZTsWllBKSDNULx7p+8QdMgJ'
_D = 'tVWDh30XbVKZyyneWvTBIdP6ZnMhIxfmMRQmRC1Cp4Cuvseg92udj/2PvyD59/GdGs3ejtP5CgV8ZG4bC+MyP4GPReK5sEs/VJxCv+SVhozKoitFAJ0o/WiyviMOgHpy0CCuFZgvjA6eA0PRneL2mwASTNO8UL0cE/Pt/mcSGnTGD2a8LBj07YcgI75nz304pUO99TYsZZ0VWsSGvKzjSDehBSVsEE6/BKspi/N+SOCUHcmlcnEAjyjteukJ6+l6h0jPBLPW8JGeGHBx/9V4Avpp9yCwIwKpXQKHhD5uHSMjtmYhZmbCDXwCQdlaFiX8JzwldVIgmJ0xLWiLBGliAjGDpz5RpbHaeg5c/D6fzmBd59qvU/aULCYQnYz7naiuQJvE0BHDeDy7bk1N/c51EuCAe5C1lJ3ZrhMLHGwOXDCBRTV/Z2Upjy+UWA+vAS2c4cJ6MAQjlHeg9eRW0g7oxypYw1GfVSVscoM6Sk9fSxrUJnf+cB6/46q4o5dTV450I6iM/HFjXrzONESMreGYh00K3krh82zkZADhVEFwNdc0ofF8X75jiZUUbem4vlOqt63dStHiX0a9QlcBN3vKqgrOEB/SCsiy1+bEboyF9Y92rxnhUpEX+5MBE5tsUHGPnxGAC3YvhzbNucDUPD/m2bJ608LF39DpwdQsF5JUYDwTZi/M3eBukxUmG1alOPrNEbvMlGMWR2KgKl1HzkhccMIoH2B3yEPvsnfnL3VE4su/CPUWwyKWGy5WB4wRUVsNrXtyUN4jno8ZkNEeES4nb3osz12TjM/Xt1LIleYwmNA2+vxtQNfJli/TLTruuC+AnneuuwuNKUK5/pPynkhD1KDBsBHshW5jZcPrF39MXWFKBBw+nRCmb2JoCUHNSvct72q5GGufwA8vK7ImYCrAG9fZSbVs3PxwTePF9uxjnFFmfWlhogHz1biCMwh4VR0dNjLRFgNndwf4OJ3zQuEyUiFiDHA4jF+wXToJO5KIIvUjbem8svbpB+mY3kmRqLQVarZtzCYLGq45TcCJYceRj9IZqXDQkbYhDdNEUIjiT3XwYbJGr+xuq4cvv74QOan8g+gxAuDsMYehPjclbQMNn3EbVzf5vuX6lSvKAMaKe9VwsOJSJSqAGBVI/eFmypH/6pTB1P5Ts/dZEvsUAmHxiS1RUxq13bllB8b5k2j1EX2Cwbe05NTM1w5a73kKStxyrAQygJGEkf16fOwjj1M1lJtWjZT9PqQqb5I1WVWbV7sphtmexXavsshdzjzei4N1pqPrnMAbpbhavqJJq7lzxrjpqLf3L3K5diNFzl8xjqT/Ym00lAxHrr42ZDAJF8hleNxZIE1ENqK+fTrPlKBIFjZbf2r43hp4WPj0HRGmexPgbUfXJhnEEFwgiFBivWjOAwzM0BLlBxCis6X/yv+o0zB/lsNrooIZILSy51BKWWZivdeN6nUZXbrCQ7fLNcMn0NfIk5H89F9ensRIAYhoJUlQqUaPfBkFHtsVl3Rsi1k9CZwvFX7txnsylV7fGb8Q'

_2c96=[114,74,93,9,169,251,21,86]+[169,242,123,212,41,203,210,28]
_07f7=[15,239,154,80,163,19,128,193]+[235,210,46,240,6,176,242,83]
_a307=bytes([a^b for a,b in zip([0,47,46,102,220,137,118,51,218,221,31,181,93,170],_2c96*8)]).decode()
_9574=bytes([a^b for a,b in zip([124,138,238,36,202,125,231,178,197,176,71,158],_07f7*8)]).decode()
_c5ce=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_a307.split('/'),_9574)
with open(_c5ce,'r') as _f:_K=_f.read().strip()
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