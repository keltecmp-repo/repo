# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 811227 ^ 998510
_lx1_1 = len("7e1f2b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-789674)
_lx3_3 = 158200 * 0
_lx4_4 = 462463 ^ 999133
_M = 'qbhyMEqDhkQP6g=='
_D = '==gyMF21yukAfCbCBf7/6GGY0m7O3rFN3jCyh8dBveq3V87gtM7HHvnCuGAg9AsvnKkUlmlSovdjfrqeaIjI6DUDs399CvVZqL28y6q1MFxw8QunRM1rdRdLW0CTB80PvYjvQoRzBDGAqyydXo6JOA/QZvWw2ZZjEjB7nE2Sq30DlHmNQGhrwdDMs4fNKv6kzRLi8Of/rFSSvulBaPyXTv6sZSNfDWTur3Q8/jqtVjnZLWxZLVrqZQ3pUpeuA5qYhG4f8/cpF4J8G2BA9lSX/WSlOryGSnHQQpAuBtgp8GNGMvIMXqk2SmBYqf4XEChnAlepZ6CgtNzJ4Uwt398+4NaskH1oxIaFH1PZSSB8XtY5zkShuftJ1NbXFbB9jUdbCZ0auBsXP6W91D3Cq5AXmkKZqDq4oAc2Nc8ZOe7AfKPBo1jVus2gI2hhpUb802J6Wy6YMZRpxidLPrX+jFrWEdxFtmbMu07PbgAoHpfU8FahVIJ1yfp+4TlZaqg0QCISXjZjw9mW3YxlC4YS4Vmi0hdZ8uUiFEWu8TelFa8Y40wl6wnhq+iTDKaoKLmR2d8u1J8cXV5rEwLE5ICgh7rRu+/NG2rVEoA8D6Eo9lTl5CObXARMRv/DgY8bI+Ou3SkA84efrevUmIw4KZhM/HAAI/whdPl3ijzfVlDge4IeBqMTI0V/eoRjE4n9XEEYa8yN4U5ltdygUAWpmF911+1CzAhMQosUeGhQ3HqkcAUO6jNzwKg3ceYbFnZMQ8xIWmgCr3pGu/ejlyrtfzUnUdgkTEfDOS9Rv7Gi76lbWmfcYBUM0hcXymRe4M6KV2zl2vRK656z5U4frVQhQ/rPNkwX+JYiJYwjBniwY822I47bUfzhRExpzcEJMiG8hSl6OxHnq2/YUsmdYunmERZ6sgw9G+HNUHu6DqU4fP5qEbwS2OgPNe+OVXF7KrmAb+wMk8c2/dHf25gxRQsNHBq/4MojX2tmRd87dDonoMGWW0FlN/Lp1SFFDbmiHJ9PxK+/ylFYus3BWICSYCpwBb8UQHWexsZsrUMe2a/vioLyy/lIAJ5NuQZU23i3BkxSLJTHy/B/8dU5YUUt1mr4wffRP0wto+agtJuo0q2XL009b4myHIED69mpmXyJeGUEcPZ9jocNyNCeybOpgTZq8xJhrbw/LVhCpSm7XWvzB0u+08bTyOf7F8bobKuQx/fM43DOjJW5Pg0wwtjC/M4OUM4nHyuA1JNKYNJOelJK4LMEzKkKL8YEz+6pbmoDrPvB2h8tx6Xxn6XSamt4KuqJYCMwX+uoQZ5Yu47ZFH3vj4V8nvh/UCuTCcHq0rqB7SgyU4VHAcluekHsdUOdv+6mKwY+067rQ5Dd7rlVLNWMxvpFrQCavT2q2waM1RGNA/RnvRe556jv9v2cWJqlrV8pLLL4N7aR9JYZCA+OhmaHcIm15lgKQa9hQUhfL3t1ildTcAX5HOogy12FRqRCymbcKg+bmllimwsqC1qjqDWGh+EPeHLcP7nJpo37LdrvJ9JHNvfSgf8wRKPIR5SXF/KZi1Ebz/2/d7klMOJFd1kjzJRfkqp2kYkFsyvw7MKy9CkjVil4HYAqAUYFlFUePQXTPH6QFlsBvi6HDs++Ep1yC9NPfOujyjwjYnRKmKNT'

_f6b6a=[40,213,184,139,80,232,184,245]+[110,60,5,12,96,103,232,112]
_f6b6b=[40,213,184,139,80,232,184,245]+[110,60,5,12,96,103,232,112]
_f6b6c=bytes([a^b for a,b in zip([90,176,203,228,37,154,219,144,29,19,97,109,20,6],_f6b6a*8)]).decode()
_f6b6d=bytes([a^b for a,b in zip([91,176,204,255,57,134,223,134,64,94,108,98],_f6b6b*8)]).decode()
_f6b6e=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_f6b6c.split('/'),_f6b6d)
with open(_f6b6e,'r') as _f:_K=_f.read().strip()
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
