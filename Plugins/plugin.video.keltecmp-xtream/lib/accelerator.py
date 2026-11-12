# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 560430 ^ 339735
_lx1_1 = len("a2b390")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-743956)
_lx3_3 = 150648 * 0
_lx4_4 = 292890 ^ 350613
_K = '37dcd2e630ecca65dfe448ad673111dd1a0c2988baba2be5ca556de7301af9d7'
_M = 'tys2ArzwxekGLB0IAp2Ix95xfoHLL+9/ayj+2y67pGO7LCATtaGTogQtRVtVn9jAiCQriZx/4ylhf6vfJu/zZOl+IkTgpc+gDC1C'
_D = '7htxHTlf6WCKsjGSZrdzjb/1vpwvAINOLvErZeLtYbaojpVRLgna8bgOKJMTnpDOzf9c4h6HjMgKSyo9+sUKn4s5G7n5XvIPx1OX1V+iM64gjEd0FJgWUZiQLtTT4U+Nv1AwRjAuoJqzWGmK7+261ZttiSpjRAFHgxktYxh9qo8kJz/jqRuPuB7kV4vJvUhg2yAdjRNUwjgA6Kb44cFpXILpleaH7K7zUN5dvaGC8At0uuIMlap4IKQSyifJdNcKFNAZHYfK8ELaSw9gDzcUESdWOBVRUietfsNeoPeigHuWStXnadEetWDAa2ld9TJqLyw2C1l+opWje5cn7n/ENcYEaakHZ+0eemjcTXL+3ZrJtuXaUuaH8sAHDMtEMl3mgzJQd25s+o/oTwetO0hh8fzvNSgy5n5VC2p9XuOlEvU/QlRLqiYbOhzKXoYSCafxjQRyuDv1rp7uCOkFmNexoh9XPleYczMWhzOcGemRDpEaPqSiAVFBJmOsln2PNQgQHDSCkuszHox6gFOExfYHdoEdO97hxTsj4UD164HGmapphAaFr7B2wVx57VzUhxT/uJln+84clisJ6MtcWWyck4K6a2LFl9ssj/ktpFOKgmD3BrqQ/whHVA9yUtOjqwfvRgg2QN7jmGVOLPPCpwRdFcxRlTZ94WYGqw1YSLa7sdmkYMmTl3J2+OEQeNLl1ublDjq66KD5h1whoU3JaVWbtTYPKDWbsdj/vXbHTZz2hDmxvYU5wv9SPSTS8WdHQse+7g3BKXRm+rP2jKsd3HrK5PPKQmqIXyYMRmbI1jHL7qpKoj7b1XQ7XuWHYHEc6vOla6+Lsg/MK1NKYegVK6jmmEaPuS47Xu5OsjrECnY3rYMmj3MZjizqCFaQljin4BsS4Ah2SnIvk9X4Arj+V0+RUgY4IXdY98Uc2O+FAXC0GgE3HwQT/8u5Bn93k3n1HHL6ptM7Lad5JdHi+wk1roGR6zSAg0tOgRLXseLKKWlWpMDfOj5zvWqyEzkUZPk2MuFziHYQSUsYuKle+R/OKOLBPxLGCNhGuzEobrZ3fmGcq334Jzd6GCFOZMZiph2vbE5r+88A090PLPBlz5xVwq9bVaU5i8Gk4fiYx0Ivqolb25d3Uc8LFzj4hqC0Wx581uYw1gpfIxgsv1tmJLVvXLrXDmIhcwMX5//E+ZuaBIV7VNWJ5Zx1ieZamlB8AtV0G7mRygIi3kXvq1kryiHUwf6yy+xLcu/FUpxZ56XMiNPh/xKdL9vvDYbDVpzS+D+1tMEheTF8mChr1+Byu60fqEdMWgWPGNfYBNnd4iYkoj7UNJDF1CeIoM39VermrSJwWlDzxSqCTwCDWnpeWE+6sI0gSZxGhYI3eo5vgQceRcZ0rKaEegbAYPNSBv6XJl8y5OXC72+vRf5y3exOiY2772BqBG0TgDyUv29/bZj0psNc4yD5t24fHACQ6AfTiUhaH7vxQXLwX5DnWNDQQadclQNoIHrbLN19FOzwPc7dTmeL/BNWaVbDIsLOTxAhW2BxfJeJr8WHkjJ/v0hZMi3U7cDqfcQ7fb+Qh2o5rkdpvVgJYP1YHlCYgoGgdxDv6YQLeCIFEO+canc8IjWDmiFGm0O7+eaR0l5E2/uh+O2ukCLPNnJSfZkP4sD+WP/UVMU7vSLkr10VyLiBgSWxUP5T0XDSktzlG40e9z/How+h7xq7FC1v6BTUDysYZrJyTCXVm+79PayFW8mIHxOg5EBsSMmOcpGFO6+oNWksl9PSdVtZxH9MgDjBrzQhTfv/3MzgP/8AhuV1ONDh+C5hz6L4Vb4GnioPK8Jws9veV62jKnSkl4fiOCkVJ24DaB+N'

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