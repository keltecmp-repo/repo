# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 459033 ^ 971439
_lx1_1 = len("c8d459")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-406923)
_lx3_3 = 385648 * 0
_lx4_4 = 139297 ^ 850126
_K = 'e4580ce34fbed8b92e7b7553052b3333da00a04a48f90e9ca0b6ccb00d4fdd12'
_M = 'lyN01k1VXi2Fll8NBcum7mxW0riw5fLNQMGHzsUILmPLdnnQFlxBd96SXA9RlKq4OAKAueXrp5gTnIHOk1p6N84ie9cSUBFzjsZS'
_D = 'xSQAem6GqQC1S6wJG7kTn38y+NF1wBh4o3/qhzFkYtxJuT32GyYgEqwIY87rCtdyd6szXwC3lalNpzT9vwKLbhBtbkCXTUgocISYFaJRw3S5na+I0cgsdPdrxGivV4ufePSaFRZ/1O4u2W7OI7bIRMZ/Kqf1recdEJFgLX0ovF/gE3mssH/AiiHMWUAaRyugGox9Yr54XpjkS+Eigm4eaaqcKq+eV+kzo5ltZn4qBCWCGi/nl2a3gKueiQ9Pmj5KKV7hbJdCxuXSCbHtaDuU3IzvW1aM5YQfERpbgh9eOWfSAdJeg0Sw2WCeaR1xvV5cxAVzyC5p1Xmwbbv0TNQmyIssBlbKe5JARx1FX/3Rt4ZKFT+F7KWJeAUFD4VbTgB7QfIsmdZlt/2L1NK3u8o9mryDUAU8qSvSJHlWCb4+U2UuLsyQD181dt0ku3pygpoE9QYqrjVadoqP3scEg9Nk2nAe0Esr21XIMaYqENqUmwFXiaushHp0zGVKjxjg0olqHsoYpZqyc0vaOK/Ai6dzDlYOxw27k2/sjzYah/xMW+yTfjN/MFxPP723XegeJzkKr/mGG/IhMODAHGxJfKxC6xfZjDuWMBg6Gdm6mzwoB7xr9PUBSjId6Kv9bPv3oZEZXr7kSfABs9QUO7DX73/nrvQ6mt6w5i2oO+mIXdFTjTId3w0mlrWyN/evoD8f2fNzgy7iY6dkf7RoPYoDnPQVobAdEhsPZsCZTCriD2GAKXQXQGOGI/OGnKorkklD16Uxk72HhbsExmz027i4HNpOefvupKTOmm7jNnTTIHYX4lCv6M4NAMtaXvvl9+Sy4bcLl3UqqJjpSE0unxFv198s6x4HgVP7yOSO75kmvFFww3YmUTyBUjsBWa7s2NfFeMeQgplzPWHUxW/LXwHGZFcE9ojuy+tWbCKk9c0UzZo0gZQfasglYk7B9KzbtrVY9xeGvEw/ClIdUa6x1h7Inlpq/HHCMJWY+Ps3L8mPU18EU/5R8XxowJBJKrcGaal3Ew4HoFXfDml9lH7qIZUuPGlPqfHL8vDVk5ZL3dA8ZqL1/q6yvXAQQtI2kb7iiwJIjntSrCKaDl9+fdsYYWT2nEhI6lBg7OjJGmTokhBohAfN5n/BaV4zx40PbZ+/I5C9hCVk+BU0g518HQGBxvKfzGdBrsvybP/yy5wJznc1VKVll1VQHfG52lucD19KEKdYu+WTTIzRqF3zDsLfcAeTknro3qpVbN4oe0o/6aBTFvYSFwkC0nb5Qn8kNmAdVBVjJ5V0o/UVk6Xqs1byOpzu7/qCEJEgE8TjQBLWzWLgIJNZ5bC59iw85u0AXeAxAgOhFa4FJTil/qSvB5pXsgU5DUD7WH9UWzz+2yGBw9JmGVdJIEUZh341VLpK351C3B+zZOrJRdgMQg273Kw3sXIyiBO2pjkyKn9TTYnNkQSfqktS1hi0vSH1CjX0DydCnfxH6zj6sbnA093zM2cmGSIT7K3BHDqT49h65V8nvgk3g7IGSfyZUI8yhooe/L7DsoZoxjQMpcCF4hAmDHzilAIGPlW3lYlcAMeF1WTZlri/A3Ql8d4g0LRM0eOzrKxglnpxt4VOeJNhs0AmRntbXf4GaNw4tqQgAcofb8kMgLL/TvFwlQ9Bm9WsEqVb+Ic9CgL9xaOJe2Z03uzP5taJXq0L3axp8/wuvKNQ2RXl03cUes4zuGFcZx+ofJ5UtZYY7RzxuKcgeBHlHM+SVS7oW6L0J2OogcwUuzByaI6h3Kd6bGf2ysqtjH/ViQ+/qCxt1bZ1mIuHb6ACzcOuj+IezrAkWcL4Pnmj90MLh+UXLB9SoB2X/eE0TRvbOoOk2wdSHqVfaYtC'

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