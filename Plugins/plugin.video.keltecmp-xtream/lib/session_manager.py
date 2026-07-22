# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 401562 ^ 312927
_lx1_1 = len("387924")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-900167)
_lx3_3 = 483694 * 0
_lx4_4 = 811038 ^ 550755
_K = '3f710e98da1dfa399f87444410caa99d8490ede40bb626a27b8b62142f18e0d9'
_M = 'MhQWkZrOgXTtc9OfAHnJZ3a/dMWI/L5MdLPCD4JenEFiTBzRgt7ILuMi38ZVe81keON3ldj8vkIltMEI1V6RFzJDQ9OG2sYi53KI'
_D = '==wh2puxJLm+l90X0W3is9NX87dOR6L1QcYQi6WFubcvNPFyk+Ymr895GzZHlFDvgQdCLwsYWoxRNeoAlZYXXr0CHMtO1NCNvHshGUv0tvxyV7N0QQTJ/T/84+GQF97dWA8h9+WQ1A1FPbkBEGZpMC9ZKHut36V//rYyWpkRxx9Gv5X0k3RSTJZkY5AlW3ZVMSLZK5LiVuMiHwtKiYBnpTgTtF68eyJwzP02R5uChahO7oin15FEYE8mnq0tdXZ6ZggJ/NVw+8511UR0Jius20dQQfvXGKjisvDu1ifq5PDjAmqzpTTg98egKIxxvLR7OI4ZePXeT8tzP91eV9ywXev/nOGe6TKlz7hy6MU2DJYrrfA06veEduvJzkNFmm1ka7y3IDuctpRI1qthCXHp9vRTdJ6wCsqR4iw1sjAbG4iwOY2IX4zQ5b/+mMnmKm98pKOGy/ck+gjCrbyTV1FpOc42//U/V0yOzquCg+GLP1sgFrxAnCHgjR7NJQZDSDGEJ0aGWc5zPlepLkOvTpLY/24RwbkyOEOVt4XWGTshOrnwRIl2YCjZBWAaHRPtNaORnbmWQPkRKR+dAIeBY9r9GtPIXeY+i5EjCZwsIMiy0F2Q6gW1dTGAbkCxDjSsSUx7pOMr3lToL+ta8wXIJkDleEAuvGWEGcId4XRZkL+7nQ5YoUjiv/sBkG+hAhW7ub1AcBtTXGKoJcHGaWLZUAiqEE4YSHZEzXSd39zsk5ajOkmE26qhA9b9qh8m6/w/P+cPZBm6bOJuMorIcuH2AKnE4yn5qfe1yvFhzlAEJEX6FsMtETU6dkXnFVnaJaIcXZDXeQ0j1TbK2Qf0MzmpXZ63wMJ2uIEA9eqGmF76wv1FNX0FOEI+D3uD654FJ572Z+5SQu0zfI4poBgprnaUBdRE0xPZRkh75hDpaFQnq3y0gK+WQniDa6phoAAsLqe6UoqGTbdVlmTzys7CRGy0VfVtnkfXRmlyS1HglfBomitWd7BrpClsbrJiqjuQiBD5eKf3FiPvsnHoxXlOKgH3j/aAiQg/zH2ULKt5IUI0HCoNTVPHTRgTPobgmsZ5iiyiGe4oDb26im7rdOgCbexVhikR+D+JGEMm9chyJ3iW6aR8zdFGfBl63ZyUxVCmFH7VYpjHWxeGkx1tjVFckNQUiiUvLBGMVDROpQ9ih3pMkSODMWsR2PiyaC5UMnOg9suDQq5p+smEecB+Gfh5Lsq1W4V8w/AMW6zh/4JFb5k6vs7na+oa9x0va/0piKrqtctpjU5I/P3zPSsVk6iq20PmyVBkhTNtutOVvFG8bHHrVzckoKgjhxeINc21+UYKGAmerMHjWppfxYiGoQ28n8LWTE6ntoKsTAv7zUkWl5n+JTepbyESR7Ow6UvSayjDQgB/1q/Z1sryjX4TJ7h7gBL3ZI3k3dmDhrQo28GDjKeUxRM81N/aCpINdpJj+P/P5k6oJR6l7nDHMuYsv47fX/HKZMFPp24i99nYgtg9W5sENYKRJqIDjbp12pRWlLoiKFrSVJjSUxfU2gNOTvECpqaE1zqaPA22hDIeoVRmyI8RVfFCkoC7FxGpr2+Ig0V3K5rPHPYCDN3nR1r9uq0dFCXY119FE4aBL2y5ZOAHEIoSwMdzlMtYRShklAOdJ5Ese64/XAHg'

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