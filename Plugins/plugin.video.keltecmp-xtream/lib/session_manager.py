# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 597792 ^ 941106
_lx1_1 = len("3946a8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-735653)
_lx3_3 = 738792 * 0
_lx4_4 = 629125 ^ 968108
_K = 'cb963aa8a7fff46bbcf71cf532643113404b957f2f380c3bf54a9d9be65eec75'
_M = 'GYSOQggfZPLkvOuGe2t9fnD4J2tpsi7UiNVvl7jJ7SdbyNQGX0s/9uy/5owoZysqcagvajrjLIfY1TqS68+7eVvN0AgARmmj5rrl'
_D = 'cux/jtxCkKRFzmUULq3LUvEKMIjKnsybzGc+l7u1r/HwxMKRRWUoVCT0ZYiCKFFq+t7527WZT/hvLmYvqSwJJ6uCgS6BKisni5i2XHZB4bQz6IiugGJORyg/pSlaWxJo9rtn0tEfoF8L+VrY7hev6bMWmBqDAGZfAGSlKtbl0wL+EhrXe+4E5/dZMXS0/S7HAPD7lt+aevnc4UEGgwCq+rCkpKyN7lCsLAEwh+ZUonFwWjljVu1F3kUX2qO9ko4fT8CmiiMBiqbwAu9+yT9n99iye7WuANuyJT7ih1GbFnGqhAPYoIZvzDw72Mmp9MEYkYgVwKZ+SiTgSoaoYUAVbvc/xCGaP0tGXONQmkWHWWvhHZ1wY8CIvpUwSByg9RGb+Wj2v5NrYhYITcCwgM1FCUExW4f0l2K3EJVAB6dfgo3Ph/QAaAWXGunkbraDIV8EnO0yhI5L0g4tDEFi8wLYXnHnCIAhWCd/Ly57mgmUyBT5r85lIJRKj+8/ipea6c3lPSPpMCsciMye6aJKggLcCvOBkJjqhQr9IGSMeXA9gUiXg2f2HRayYCxHCYPi8b/STW4bZVUD14l5wM9cv19qAySKUoQY13sbGFpH4fi2v4DSMZB4PMEmhfI5ZEaqWMZRbBO3zE+UHF/h05qz582lB6+XZPfiTH4pICCR+GDmSlFii3ZYv1X2IDdMdIJy9T+7UjkoektZTyLRf6aZI7W3SURqQjMr+G1EfZEzwMK3KQVPO6KgkpiiYWnqyInA7LVCEUryHwmh+tO+MJOoXbiwn7vow1WVXHI3Hb/nB+WOE6lFVV3Uqd39OCpDbiecZZktzt8FBCKnQQY1EvbmbTMnyp39KscsiI77VwcwqXmTGX0j6/+xghZAxSweMoyXDhVuDoeNoy3ZA5GztMJf8KlvV3u45u0qkHWS8gnBh8vyqCgIHBFpOvuKdy4Cge46ZFkpukDnXyc6aVrPrOgAM3Wy9olsC+T1Er51G6gW6viHW/OmWC8LjfR/euPXFkhg6NhXWbZK7KDhI5KQQKnh/0xnKGpMVmH+EQknRlHda1927pY0WHUtBAmQ6QulmaR0Jl6Crofha0KadIzmoWwGEgCwVW+3PwnPAaEk/MAvgsTirSc/EWBJ5UGsoVK7u5jy0m80UzVac6YB3bc9Z/TpdxEHbQl2u5U5x82mcIAxaGwlMkxtU/+VrnkU+iORPeJALTqgEbPUW/PZ/04amRBKnveCLaUspQDIr3fu7FTGYYm9sf0hUols4keOxJHm7pGijoJoKF5ZsWENQAh5UtWVhNSuMeuu6Ovn/gQrxBX1l9exMJnV0KkJ6ZIDLm8usN9xDiJrb5QNbToyzX63BCg8U9fnnVAOolGstv5Xo19gRMaSYsLOYGQKMlKu6lHcLnTl4tPBfj68c/H6QfRxnrXLO6npBgX0MbX9+eTlUM4z0jBlHQWa/30QG7WHZt5nuY1lr1mew8vQt37161DhCHePGsmT/2wp1UUSO0+gSEMsRWmPKPus04G/GUn1okSAbWSebCd9HWAsvUzYC/jJeP5pa6W8HPFXoxtYty18x0EcKW9Fw6jcWVH0Hnz8X5qxGyfhA5RyZLkoamx3K5LlNzAsx01xE9pN5tHGn5PMmqL8nSC//SytpwbWGJSm3y3o6O4M'

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