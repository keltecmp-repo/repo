# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 585582 ^ 311836
_lx1_1 = len("032c2c")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-276928)
_lx3_3 = 903057 * 0
_lx4_4 = 299543 ^ 742902
_M = '7GFWjBSStrKpzNunRWfbHMTOhdBkJ5u1ZfKz67uzp5PvIgiMApWgtqTJ1/dCb4obkcqE0zN2zuZgqLHq5u+vxuwtV4FWkfe995zQ'
_D = '==g2C/dmZJYA3I8+bvCAAvFO+cpHrJi2rxSEvFTsQ9nb1fra7EaYgOVpvO4MsfqJlqQL4mU/VMt+e+lWd+i/2OXSj5mIsjT+DDI71bYlCkn0O9AEgy7Ae/oannAh64bpSlD/PiBatNosboLApRzMG/fXNLH6Kjxs5cU7Zgd/4B5CQxaM9qH1wN/bjiegTJxvNyN4hAMe/l/Rp5ByyFLEIyjZ0PwxMJAZX7ppoGik898GFQZQxwli5ZlBLxV9VQTjKZFub17yysrT1k0Wqa2WbthnIrkWgnIwRe5tEfMq950qmTJz7V5IWjXfBFGtqLzdzXMcekS3wA0832MsHrARYvGCCmgK6Te/PRuADAwDlBRGU1xp9sBU33AsGMtQ/LG04mxTWbfpD3jC733rSChcConnWdK8MKbOynukiMDCsCF/x5aj4haPqjPhHxxumKTJmXROUfbyiWx6/+vwHGTJHB0S0QQ0YRP0LHZr/KBVbprJGTSBWFQPAP6q2D76BMK6rPr8qX5WAbhvTMOmVMK2e15am4dw83vvUhNgWI24MXuEg6sZDXtO1HQIvXTMzUsSUYKPDO+Fgg5GRQG9SkN418W2uASZzoL7Y4P3KI2n7K8G76P9DxOxp9sVfNl2/JMx5VhAJ/s6iriHOnTccRlMzUBIgs2sTHfQGGlXJQT0UQ6fEvwJFBd5ZDpp0GV3Ztr0sp8ibqwYImx21ucLsHQx40cLA8k7Frtwf5NVgqzJzlfzBJ3l3AG27dJTJZY454pgsn14wjyji//SY8bPr7t3bE3vZlUT3yk3w7p64kF3Zed+st8FwTVQnxkaHXpFlaU9hhYGz7hfj+Jy6e4dFZCSh81UMmAAkmkcSq7EUDQnpGOsyqJrsTZKecnq0EksUEe908cBNa/iDEs9tlVlNhgSmwn1c7t/SpT/sC4LVk2wZiILwSBLnfgsbbeelxkyMBL4eCef3fYTKYdhCujnvAwolVxMPTbfuLrtovHZezS34K5YG0jcDuy8KUibQCy8e9vFBR3dUhsxOny3IkbZ7AeIiAbrjtWtO4OarVK2AgU9+wGRFbxDku1LhNv3vhMOgm+AdqV+gGERdhRBRXTa2h0455MyrnUJ0Xupt2TzX/oTvY9qHAxE7Jhl4EbqInvHIQswOJzGtZOX1QJMqAyQeFS0m4rwLnhbzPO3slFfhbBFzPowO8foyfIISbqNrgrGnJhGuraSsG4NveGgyEC6ZTml/a1a5m1RtaQ5NMQVwVOu5JHIbBzEdIddeBK7U9mf4A9jC++g56H3Ipq14n9oWRrJmRlfbRkmMQPBPlPtQvmF/MXsN39vE6SxEZyKXy8yISyJz6NIZFCqYNgyg3tKkMAiGh5wqLb97Im/rdxQ27FwhZzsVNjwuMjIeHFj28Q3/wZ10MndaqsTYvivuLy7gzKdMpQKkFxH7nfHUVtWwt6uwCrwCC9GbuG8GojKYX0aIGtPfoOqtpuEOdYzjcSe4L9SdBvrsA4Ne5GT4+fWPHJNkz6P0Oj4jX+VvJncMw+6k6tCg7/YGHLiNR7XeoC3yVR3qrHup1Vq4xUZh72ghnwBr2CwjJEBO0HKGNiCARRLyDO2RH+b4x1Wv5FIVWRXi0VP+Z1GDZnUtFd7wuYoi83kBzjrFMoLdB/y6IVwqva5pH5QOgNWrdGlnuyzk9cSoMlJNa3eyeKPuPNoCALF31162VVkmYZn'

_ed71=[5,147,112,166,252,215,84,196]+[14,253,210,112,103,62,176,56]
_d80f=[164,113,97,81,107,232,174,32]+[195,1,169,37,91,114,56,140]
_d75a=bytes([a^b for a,b in zip([119,246,3,201,137,165,55,161,125,210,182,17,19,95],_ed71*8)]).decode()
_4267=bytes([a^b for a,b in zip([199,16,2,57,14,198,202,65,183],_d80f*8)]).decode()
_fab8=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_d75a.split('/'),_4267)
with open(_fab8,'r') as _f:_K=_f.read().strip()
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