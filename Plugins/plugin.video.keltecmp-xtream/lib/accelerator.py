# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 628953 ^ 563223
_lx1_1 = len("4eeb55")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-255995)
_lx3_3 = 865842 * 0
_lx4_4 = 548858 ^ 435496
_K = '272f5c272f8ca3792ed27584e09ddb4b27ab9c31f3ed45b000a5dfdf84e008f4'
_M = '2A6/makSZPB5YhyB9elMS16puO+q8n2e9g2RM4aDzRvXGOrBqhUupno0RYeg5BZHUq7ls6f3fJD3W5A/04HNS9dE6sL9FH7zIWQU'
_D = '3PrMGFMmw6N5O+G7hrcxPi/4Zp5l+LillNneBIQrx2HiXxv4PPjVK34Tdo2s7M9SvEut23Pg5jvjMz3N2P0dw0BNYbTc5Lr4ZZ8d3UbQiz/0QjxaGsmimgljEpZFKKqpffQUAWT7IfRi0KzL57gmDGy98hgSi9xyiiGCn2AXTp9M8edrVOXEfYcCCQhiabP/FwKEFMKINk1PQM2DN6RSZsRwEcRub30FiXOYf1gvvNKjJrgStY1Hw3L2M1p1x4HdtRFodk5coGoo1RQhigEKkKxUCbghgr62zX6k/oZ4Y3FtkSn9KJzeu/D1SOlIBcNXLel4boWi9AjJeAn/sY73gsX9XgcRYAnGlClFLRmjCgs6wruxfOe1DVgqFheVJ3H90RHPC4P4IU9wW7h2INP6kGQgDPoTyiql7VPZu7c6LjhwB/nocqk8Y3vxtzizoH73Zcc7KvQ382eyeDVGJVD696Zr7fxAypKTps+kFIMp5Pk77KJj4CeKVo23VdSSDOCzQfmPQhbiqx+LZPY6BqH1W6UxgK0+pDQrPoB8LSxNjnlGE+JCpfSiSrlAxiqG5HUvXQtA1G9ljaeEf5n0m56LHmxjfytOA1/4Ah+00HOZiMJi0iypn9aPLYosfHpD1CrWwsk9thCmq7I4E0o9Wm9k2WEQSoiW0R4q7DMtmWcML4aSvTzTtog5tRynWdKe7y4dqLaOQc1MTF3NgXvbrBSZggQYsl6AVHynZIJrPEbXksMa5xTL+5qJu2UN0xUQDesYKKmHbmWUzbNyJ2vvxzhPs8BDZPd0s2OnGM3Qmo+mgI5I+ybh9u9GAYNAaU2Cspr1XqMv0WJPnV4VXSLYr2fJRR+v/9NW7aiyMP++JMUhbL6aq34bGGuFASni9juCl3RgY1ktRPNc7Es9dG3QZ0ow9RyZps8jZF2luk2yQJV2B5DF7RSavUO1uDXj0zPf7g9Wx4li4ev0sKgGLwS405RVxzCVksBeKDS7eTII64X4LQJlddkk1dgI/ipAfhPS6e6psUwR21lVNcXdhT7bs7GV2RpS46+pLDa5rLxn/LlYwEHoR3QFmRbSoBb5rCUCKdfKeJ2kIG7SovhkXi8ewlWsyQrJQ+np7vmHdg6y7BiYB/WmphGvRiiGDXCY89oLL8lHsMYc2StSI14YSXiBXL2jOVWJmbw5WQ/NEXBYol1MQtCz5ho5GlYs5FAv6CNWXzf5HXrWg0CDmbZBBrxyDUiy0hB6eUvOVV4uvL7u+7kaSHRelbIsjdUmXEm5xp6IRJDdDJifk6P9orlV2FUrYWfnDY6LYM7uyzdMq2R3Nl/yJx7h1gc4VNOI7H/WqvJKKBGDdAWVg4RrtPVO5tLj+F5jitniXoxCjBs1qpamm3rA5vKvF5DYNPo1O7JkCquCf1aXFvFOzQAhgSoJwYoAbiTr+7AEXqJ3gLo45rcbXlo2wQXr55XMhFl/c5Wpxiep/nV8tmtfI5XFjyokaVg51hbzEEAdguH1DhnBFTZ5SLc+wMm2kTr8thl63tILqRbcgQ/CflR/bfGtJ0tjm1xR3dEjLMiCoG2k8GV4lWuMVXvnEO1rsKnJYFSojw0xZyhZqE5dpoo42/5GvdLdFuvi+sdAqU4o0B9/QZIfmBAhORrpHubw'

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