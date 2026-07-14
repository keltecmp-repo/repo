# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 688919 ^ 113202
_lx1_1 = len("498d25")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-212316)
_lx3_3 = 238356 * 0
_lx4_4 = 215800 ^ 182462
_M = 'K0ovaLwg8I0fanl7loq4b/Snz7eXS5W7i6WHWy1IKJ5+Szcq63ys2Bc6cSzK0OtqoavG7MMakruLrdcDLUp7zHhOM3+4fv/ZED5w'
_D = '=Qhf04t6e2iRxqO+M5etcfE/wXobGeaks9CpXOYf5lBSE/+7o6mIvggWKBpIp7m9SfwTiDxoWb9C7wtjRkVFfVuNwear43+G4N6B5XeI/IIOjNd6n+m71tcd4eJAYlbH0pMFj7U8uGMzZ9Wpwc/7nWBIk9vsZpW8f+P+rch0s985nVyTiJ/VrhTg1Vx2p133B69CfZg92510c1Miu/Eh2PI21/iVXYud9OHCYIe6R8JUQDuZmHt3qMrr32JtOu//MWH2DjxPUc+bYCpUrtMqbnC4vcLueUqkA58UazyrMGiWsg9oX2gjxeXVedX/1igYmJBwpc/zvQhUm5FRsO94FvVhFy5DMJIPdpRMR3XU3Zg7uO98O9126ltcl/q3tFoMlANSb8AufU1bEGR0r/LM1kZNuIhKuOd1YRHwzR0AznEMJmuL3e7NT/wqRs50CoUeFDWNVW3FM001mheULtgkD1uTk9ifHTsnvqOWioOKXOCNfU0Yd4hGyftnOe/JrJi1V2ysvFZ9NKvjHbnVXeoHBW7Y0HY+VTHC8EBpP5JUOt9PyR+pAkxE8FF0rVvxRgRH907Ds0wuiTcFwWY1bfTapsl3BSzC/RE7Ic4Us7XG+49quFEqIdNitNgpC36T1TeZiAz0rxp68r+NcuEJAppwmci2XxbqzQicUYNJG2dShWbKoeyfG5H1WUHIOITzkEUgwkAR90GmwRxBHFvHA1MQDCrJsjJT0L6OZfvriP3s5oLam1vTd+RLIXCwmhIO6VTnwxIf7nOVaQXRbLmUsXRLRX9ZEexn89+d2j5j3XSKrwnnB7nalEQ8arEyN7cL1IwfCJnYSnaQ7ReK4FevKBneIPPoAJM0C0u2SBKVgll1mLPuqOcdIN12boRnVwKyWdlfY0UGSPDTHjD/v4pRa9ewP9ABuG1dyhH2ksO0Cg1mKHZAK4PhSruRj6Yg+9zPWFUl2COJ0kooJsxiVn3SNwWsExjhcSh8Rlwcv/MUiwBA3tLgpejVPxzh9pqfrVP5IrWlD1RJlZ83P/Q7/C9TVB5ltFayeeJkKA6V2/vbMqtoVYpIfZmtMclNH921cLSTCtiqzJYmhkSnXklIqBeVGWFq99iP31p7a3vI0txfYRiXn2PONkVQQB9/8fZOo28KBa8XDUV1p1BxMkwYYvZb8Xr3yqT/oPg2U+9i2LJwjrjebAuKRmNGJBRBAO7uaHpKQWR8eBJTkBwbc4HHnvkU/lZcRjbpWNCaOrdofitsSnFCnQc8N0vgRwhGXskZTOTsvP6LSfh/mOIUUO2tsO8rZ9MrjZWL/TjJlRK/vDZ+HX+6GuvO0aPI2jspQkxf+ie9fgoy15hTF67vffJOHI/S7vG6YO5GeI6tgOetV73rTQ9SAyoX2WXqxgLMPwZGUkyQsn3/nK8zIDUuM0/Uco6ZYzRPzoOfDkkmcTvC5uxZ8ouw2hn74nW/Gy7Drn0mSNsiRV1dIva4RxIvzI751HZ6GNXQxIWeg4Js3JVwM7tlv0Ymj081ncF1ykDeiZWC5iHm1VuX5mYe/0bdI13ZdslNXQq+u1YE6SYxQfv4hQR1PYSpj8h+B17OHdD9TH870kcPKnOXdvojsSIM+4SICTQs/2Eedq2FKkGYQgJBNoF7uVwQbpPgczlIRvTWYSbCmapVjgmB'

_3152=[192,7,88,229,143,135,86,73]+[150,224,199,115,176,12,179,180]
_cacc=[71,99,101,168,150,131,128,7]+[177,101,214,128,126,55,193,235]
_f101=bytes([a^b for a,b in zip([178,98,43,138,250,245,53,44,229,207,163,18,196,109],_3152*8)]).decode()
_1fb7=bytes([a^b for a,b in zip([36,2,6,192,243,173,228,102,197],_cacc*8)]).decode()
_2c6d=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_f101.split('/'),_1fb7)
with open(_2c6d,'r') as _f:_K=_f.read().strip()
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