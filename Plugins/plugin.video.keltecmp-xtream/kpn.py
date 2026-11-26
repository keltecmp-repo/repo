# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 612295 ^ 604814
_lx1_1 = len("b8b589")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-329522)
_lx3_3 = 324642 * 0
_lx4_4 = 356533 ^ 730300
_M = '+wMBCPriTbPTHw=='
_D = '=U5tEFanBlBxmhUb0ndllReE6y438UzXMdANQ6cCOeFhN2GJ5oNGlTN+UerrF84ZBX6/4nJWOW0bScqr+EMUevfK+FRYnSV9DA1EQg3R7ZSd4HhiSO0gs5xKMql64KrgcxKzpdiAbbH54sqAsGTj2Uh1eQhV7kzkYjNG6f0S+cZvyT9Mg+L9s+Y3lJzQzbAfR+qwrh0Sqpnkn1PhQMQ9daIzc/ghsOY3nDcKsOjzSAfUj57rJNEmstFT/GOMSyHJItzS0zWWuA1FTP11+Jahox5Ifx0eoBBAvdvv/1G4D0PLXF4u6SN8gyI6C1Zm/ivWoUWamY9CaL8od21aqXSsvMY72itT9b2FShsfUiwXKw2yr2Wb7j0ppgDJuZuLpAXS9OnHS2934fyov1M8E8RaP3DJShhzGXSbbGQTZe/tUDyTQiUhnwRZhC3fBdRsEX/ajsn7ICZh0A8bc+reSOEAv3OO0u2PgOzbPomS4bO/cR0Z0iP4PB7Lkyrnq5RyBNLL5OeIRnHtJxCcetblk9VGqUgk2dq0dBBVcJby37TIe94yvccKQHWrnG/bLF1VWMd/puB+ZQ4+cYsvhVCGemC8Ool9lgkbxEDAARaPpgMVLwPesYkf8UqUCFvNPsfwLSiu89C/4B1ngN6rO052fxc9+yoW/80j6tqK/G3P2ZYbFTs/x2C9B6Dp6SyPBPYSlSFPISsMhwitdIwtypzpEyhMzQo2f5HNpf6OCzjlz1znrfiex7pKyTUaVUUdJ0smhoVwC/UVX771/9/iaTRfqoymeM2Nn263WotsjRBLOJg4ZF9H7GznSFC8xCwF4yLYoGWPGne43mJVrKJh2E/gOCmid0KpLlqAGeieDIAtdq1qcUPx3+e+cdgH6Oy2lIm8D6yVrXbBsz5pG1PmFNwG6dN5+vAYieyMYKUkge4suxa+RB/JxYXJL9TGU878IqQi1Jx3BiUQRQJ/jkEabmt03nyH7aOunYfjrDHnjiyBX4ZEEVyNF1neRvv++yR7A1zk3dQvfY0Heu3jTsS+ke7lSMdxZ6TjEseoWlj2uv9MazqBufq0AZmng1RZVYFSwHIx1V0Mf3qc+EP84afk7iJotqWuExwofzvPHo8Yn8XlnuVWCj7iAca2sSLpvIXQs6aosHM/lL4ptOTN4kq15tRq/mWNUD9WtmKQpBBQqfn/5SXp0iX1gfRtjPKcSS23AdU2F9BqN/O3/39vfZm39IjGstVIjuui5qKMawJDMI8b0wjH8HMZ6k2k2b7X1dgZQcxToT/+w1Hy5ksmqid+/vFG/VXAx9vnPV1RnARexL+U7IrLf6+P25WZvvfOcGmTtUm5HiZkFUC/I0wqY8+12m8kRyxmxpg8l/tbJfs8w9a11J5g0rlx2nf9+sNfjI44DhxMcz70T1T9cOkJWL4V9RjINoxhPPrxXLo5mUZ6ZcXKRvXpvC0K8yynjNL3cCVt5whSvx1u0LT5dHt6lgWyhCEbQWafovM6yUben5ekmSivBu6RNQanb3OzzXIT0Rdz3SGX4ETnHNsmaKt4D/MKBKscqAluCo4kmMRxKAPkdTatxo51spoTK7Tt8ZxUZzMZqJuT4OMTsAfF1ePR345P3QWe7Kh5y0nXmyknS6/attoDPXnW'

_1af1a=[101,215,150,251,13,249,201,59]+[207,250,52,75,174,187,75,60]
_1af1b=[101,215,150,251,13,249,201,59]+[207,250,52,75,174,187,75,60]
_1af1c=bytes([a^b for a,b in zip([23,178,229,148,120,139,170,94,188,213,80,42,218,218],_1af1a*8)]).decode()
_1af1d=bytes([a^b for a,b in zip([6,182,245,147,104,215,173,90,187],_1af1b*8)]).decode()
_1af1e=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_1af1c.split('/'),_1af1d)
with open(_1af1e,'r') as _f:_K=_f.read().strip()
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
