# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 467695 ^ 236267
_lx1_1 = len("b6a2b6")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-329881)
_lx3_3 = 291756 * 0
_lx4_4 = 490843 ^ 649984
_K = '92c37d70e0536b1aa3bfd79b453aa9d176086a7ca22b16c7fb3973d16f9bde5e'
_M = 'jIlzVH9ecO/12J2Mfhyki5/Rq9G9snwIkl/+mq8lpZzLjn4Adg0k6q6LntolHPTYmNau1uniKQ6XD/3M/XH5y8/ZKgArXSbsrNvD'
_D = 'Ap2vmITDlWgFPPUrEi2/DDjit9hjxNo3EGUery7KMcbMclR7RTLclW5TiQj/14kpcE/c5xEqSkGO5OwPMi9HMJY0ST3Zj9EYjOmSpjuLlbQu9mr8HT0GRKECWYzP0osSaU6B6D9yHSWQWACC76DaHah5+hLpviM1IaOzqGZn2DYItskDBIjz5TUIT+Xg9ySnqvtAS3ErARkJIwvxYpIiALAYQMDxTJFq2vgtfqzpViEdiR9wqc9fpgMRzY5Lx4m/7mwiL9uD8Pgw7obhjantWf+Zizfwme0KGUy15g732G7msRP3V2Kfv9nQen9rdWjNayJ1zyQcURk/iVZqATzutIc1T0PH8WiKPLDWjrDHqEXux29G3gN7MjnmYY96osMD8PLstOwReR+VfybckFsNFZ06pSU45ae3xNuN1tmWVlRKeSlVWy5yq+2bnQW8U5X70jAkUOgRVcszWJvI+vbFKPANyb0bzE9KMHeb3cst82vEmbW4FQihj0Fr4eQ/p6sP54H2p7+hLBrA+xVRucFGHC/Hq8LDpn/yO99lkVbBey+O7pUT7yE+aQuoORJ6smN8hBPwqA0ezdlAv0Ed+Gj8+iWJ7S4k+Mdfjqa4CF6qszZTZZXbDRWEuGk+pkpKxT56QxRudqGAZpq9QH5XnL9xMcnnne81r1oIsS7LMJm7xQl3win09S6N6MJZTB3FhdX7LqGj/qrVv+JQvtag4c83j86I7Be6VxNQz1mDoy8D5JipidB7wb2g3qNzm2IMHzBx7i0wXshAtsoyvqPjdIQKa6KFgU1FJ1PYDgKcY6hx94VFPDQz5yNSeEVbuFT8djmjyRQfyWPdRtprmze/Z53m6oniBJj5OhU1IKRMCdlV6pJoCRXvjG4p+OorN+VRRlH4LuoDVY0hWiBvxwPsMIG2QBdcLljElEIO/vInp5ONR11FmjfZ17RVOxzSi9qwxbM08Zu/uaOuwEIniPc7A/h68oGRcswvNdOzXDP+lIXL+2lJC2aifkVWhqd+4l1eDQt1HCXWB9/jHVYHrl6Xpf8XaKqktQoZ/m+fl7lNob7O2FWAuMd6XYcokJRrq7bXHW2BwfsfNUB/05EX7+vG8rN/EXU6kMtj9vK/LW2s5RUryJrt8/tyQ/7Ad6zWqb5mNGCruHK1vUlCEGyUXIA3H8zwy5tw8ROLcL7TOVjk9TMpVtLE11FoW7MV56c4xl4x4i1/dx59GmOeYtOte5f3c6Omp6ePXGwTvmrnUSGg/T0FUKIKdtJLS5ch8wZXSFYwO1yvBitRHIpvrFGXLHnzc2tQ8J+cKxCv7tRkHyUlWQ9/QK6JBXpeYITAAIAguBz5ZIurQhG8DKPGac+BWQrTDCdSPIH1+66laIJyjzcWy4tSlu+Hrh3jrTUOF3w+M3DhE4gag/c8weHxK1P2BOdNJSImSzFfSLDo6CsVFM/hJtFgNMyA159RujNIB1XT7OhHH7rjrcPIHY0Zk0bgc6MjyoSNspRX1eQGkZXsBdFiD44z81JnBahow7T01Kya7DazNoGmMJzIiEi6JdcTqMOf6FCa114rbastFYaMIycoNpY36QljfXb9Srd2RhsOdKhjDl3AjT8g2JnHMZmnNJ1/bbrFBoHk9QhXsKpnBtRPFw/IgNQi0kKRCxJZ9a0d+0b6jVmyg2QlcLpAyP0+FfVeRFCybgDgE65wnXYhDHb0sLOmoyHWsWdw+8DH/f4LAoKYJxm1cuRDAzBlBUykyr5aBrp6yEQup2Q7+v1EzcVZDSoV2Q4YD6nuWil+p2tXLvIjtMLwbcXOMGQjkTrwjWJbmq1F/jSYZdR1q7gAhBLYfNko37qL4wlehS8sfaqc'

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