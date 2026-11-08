# -*- coding: utf-8 -*-
# KelTec MediaPlay — Fenix Format
# Gerado em: 2026-11-08
# Camadas: 5

_lx0_0 = 799012 ^ 224871
_lx1_1 = len("216a99")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-941295)
_lx3_3 = 796999 * 0
_lx4_4 = 255536 ^ 608773
# _K: carregamento protegido
_M = 'xWPSvOpRwRS6G0yjAqHznPK2Y+iGBJcDCF1jhgcm5A6QMojorgLUEbgfEqQHpqef+bZm54ZfklBfUTqMVHHmBcJmieOvA45H4hZA'
_D = 'qDhj76oK/ZNi4nTN2Ckm6WSbuqZ74/o3pgn++7XD7q7uTZJrz/9EJ9yjbUHh6r9HDSobX0jcGjs2THHFBMprUIbsHjJ58Clqjg42I/iEkIqXQfkUG3WmJ6nNmeiPCu7D2nzfiAukft04rUwqmiQW0Qk7XOiePQ6yXffDsRidh9emmGxxmmiyHU7z1ZcfDjR3pLit0lxUDrDYI+UafH5b6zxbzmOzNQyGdzE1Zgyms+ot8HUsW3tP5TC34pjrpVX6fClvMt1kdlFPD4ERdeaJCeKsuwtl2nESL15ts4IWF96SjiDppKUmlBbfKqXoE6jK/8qwGsMuPfWE/CoqzI7X8UWxtetNCq0n2BQf8DC9wL7P85LC6BpaPs6fahJhPgWuDeBoulIQZ00ro/PJZUHeh6fZai8G5PuHKhfmkstBV8SNis5Xa4xdzeU4IE1aItYWlyKWVB7JU0xYDA3wNuk0lgL4TvgmLq1nbIVSo6xWCM6mz7dk98bK4+AuzNWCxHnl/eF5JE7C8bk0Q7lLKyXMOdO4BMbss0U+0Lbb8L4sd0z/7qURh2XNxC264c+MmgWFo5UZPxEvdwib7/RVdYw8KsIywagwo9B0fl8YKFFSVvq4atpckiu2KNw/ixFoWTvfV48mPX/7KGFPoWBfV1xqqxQ/waJhoaAUSVvD1ZQUizb4K8ZO2QNvPLnvDOg3+2l1RIru/z9B6vtGwnaXD+oaqvactrp/TGBiYunMT/25wvb2U7xr3AkMQWrCqayswoMtthsnKFxIbKSqdR+Jn0N3ROiZrlP2llQxIP8aC3xO7FXUGGnGq5PDXjZPYDvvNOYwYV8l6W8sYgsYEscMbsfMxK10XP9Ba7sDEicvgjn4KKK4ZGzGxIJ5B/r7oGJGDcsGwYAFOaWpTvMxr2XhfBmtQTrO2Wxdt2RXbe6rSHPWc//akB1yHe2PlIK3VIEEfQQlCJ+lN93fbQMIGaZ85jIpExwQVVSrQ4scymqxDLfDKDw+2Ffn+968sGjky7E3R/py9hJ4am7AOmd5J5DFnwpUrfe+PfjtHDqcBqjtj7uR6oh7l4f82lOISYybdPQJlzXDn5ihhl7mhQjmftsn3wgSxT02y5CGKWvEG8mEqEvvo8Gl17ReUoG0rMyvlNgpuHjWvWoLH23U7dqZjz1t/ITmeNVn3oIuoYu5sAk4z9k5wuk41aeNtt5to6fcgKnvf8/USNzl8Bggp8CW4Lb8qYbI7mBfCBAjigRkWDC85/Fzaj8y8iXqFAf6YL7TstYo1Xgs5IUCA2xWBYGgSDqZIFg0I84Rlu39OWnmjm7rDsFPKitX2a9g71K3MgfWrpFWl3GVMKlr24CS6gGhSIXUqdQbCGJZZ5O6U/2e9R8qyT0KN2PYxZp/qhoayGCYSavlj86GW+pXVFXEC7nrVHfaRoo+6UOqVu6hSLT5ersqPADEIzPT5bzfm7bDrFuAmoYC0qemdrA9LbFmWtLNuSURTczrzhYSuF07NN3Tcta/q59TqXbm8aE5OdL15VVSjGEX7V01pG8nlDkE295LVEz2JnoTDMHMdlKarfqogPFjn6yqSshjPP0riyCx18ewT3NaJ0d01MoOjecteqbBZuiDw7Y6rCeSKyl7kix8sXew4jvBSTn+fapSgSSn6uzH2dz2'

_5021=[66,8,189,85,237,75,115,69]+[180,51,171,112,226,40,18,175]
_59b0=[49,181,58,167,85,234,46,238]+[124,142,135,57,227,225,49,157]
_1121=bytes([a^b for a,b in zip([48,109,206,58,152,57,16,32,199,28,207,17,150,73],_5021*8)]).decode()
_641e=bytes([a^b for a,b in zip([82,212,89,207,48,196,74,143,8],_59b0*8)]).decode()
_7adc=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_1121.split('/'),_641e)
with open(_7adc,'r') as _f:_K=_f.read().strip()
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
    _e={'__name__':'__main__','__file__':__file__}
    exec(compile(src,'<mediaplay>','exec'),_e)
    return _e
_e=_run()
globals().update({_k:_v for _k,_v in _e.items() if not _k.startswith('_')})