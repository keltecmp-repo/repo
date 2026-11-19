# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 108221 ^ 951570
_lx1_1 = len("8e020e")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-123236)
_lx3_3 = 618754 * 0
_lx4_4 = 824349 ^ 805969
_K = '2911680bcb7932acdad4e9dbbec9ea6b4396408061128ce49886c58646e43016'
_M = 'rfZUUnZTRrdKDTQt1bswan82COaQDRS9Up2cv2Uzii6r9l0cMFtWtxVeOX3QumVmKTcI5p1bR7QIl865ZmTZf6ihWkw2Xwy2SAw5'
_D = '==wMfIYnXGSUmifUWCFvk3UDfdjI8PYCqosyW6IcPHLIB36ysY/mniPQINN4x3MusqASkkaCt9P5u4r7umHREy1lEM+V+b4PYqqIFfpUNn0ydczx7f+InaYIKqnu6+CVVbisn2q6EHwO9s1hrVovY5qTWGkLmblNDK9r9+bulVXQ4cOv8p5eZlnkbKngF057i+s3sj9sx4hZttNJo0yIVi9TSebzip1yQrM6qXuybr52djcPlxWKLXCChqpycKtfa3sFq/kAawEdsmaHgnt0vBtMOlVXg/HsXMFJ2g2s+OstDIlonnmCVBGVyUGtqUklNxbaTXZ79aWxpy63l+xo0mdu1+8E5/inVsf6sTFV54gVrJVUUaAKMAisblwhA7vWTutBe9kb12tvasVH65gNdo6I2xzcK+n/o/7FkBd8EQRGcuRZEHk+rIl6JNc8ohvYb4pLXdHDDR0PVdkaIvYVQfnOM077Z7U3D+q+8M3IKx/FU4u3Mjv3ZVXTaK8SYrnz2pZG6ooRcGUmh2p+g74u7vFlKXtUM0cHG7Oacj9sR614c1qmbMAUNLCyYEQs28n7mvZTUmonpOX9B7cdirHqJVRYw2cdnL1T58+o/ZEFahecjlRs2uqkbv5QkS70J4O4R1+MetIRr1YCt9ro2lr7iG2mecdRYVt0/9aLN2mbslfArTt94jOSIBQiQVORglwIKrIbswi0TqM5xlyZRhmm7HfvaygaklB3rP6S5PdligS2MsN66+jTXBRzF2xelZY2o+eR4JBVl2wDo/MmK6/HYESO7buQk8WXMh0O8xVVg6xpgf722Gs/pdwE3DQXiIoBiLJZQECm3ykm7C6N+Pp4AnefFVP4fzAUJR23l7uqJNpWwVsuUPtfeEl/228NP21qGow+0BeiqR2WaZgygFvagmTauFcaJ/hfZ73SsrHC2Ei9BiWpFxSyBPeq4yM7flQ/x8eBlIzMeFHO3NLOwh+HtNZU7GyRjz7wNpTh0Lgfrl3h4tI0YC7jsXwiiZjuCtZ9usLXOAFIZ4Cr5gjWmGnaBxr+7bSGxWJoobZqb/IzT+6ewPkxgYlA0UTlDaG2xZLcCgJuTE046lus2GzNThogKM//GTMji5ka/klfuoSFOvRHLK7D7/G8BKbmevxbOCRPGgS/V/dvnZaNOjJjJs96kV61jti+TufP5G1OrmIt9y5xaw5vcSziD2T9zGZYvHfh+TN9QXWKSzAPYAM0h5VfuKJHKRR4zXGdLdw3EtB/Kia8PXu+C7LBWqDl58ylJ1o7nNiYjefiUpKQ/plJkTQwA4EpMF6UPD+gYpGcRjgN3fpnYvKqqQlHjq7R1VIndqVUFl1W8jM0FXqQLEJOVGgzOJaxYB/jdGCV1i3+PeC8ioX6fITAyFD2fu5aoAOlSEVP915E3h7dn8ODSwZnqx2Z37Yss9o+DoVFbpcaOhE4SNc7jkBwDlDjfGBU7RpCeAv+yWDAz+YGS7IgHTIBqAJuNegkcic1Lnmo8/7oPLNUh6LMw5+RWktqIoglf0GIJT123R5l1H9Av4iH3PFY3oyxPaEBWfpQVylXicDTVWiL3RZ2R2yKK4/2/j+ztHPByDOiAfNQKA6cbq5Uv2Dtr7DAYJB8eK0/GZU4eNXH6Eu9MgTj7wfWqCI0/GJ6fHC3k+6X9gpby8WPBNYxlZO6EEKxeGxPCKjWcanPMutFtr29FjT5XSLL20kBhNkEzyRWdmwuGQox5KRv0YSSP1CqOdQI9+4KUjKcRyjFUbH06yczAHmK+eEG/Mmn48A81VgHNOLJDDV0+ibp1pD5dQuZxfYBQCchjd6KIB8+SKdIOcWGfbH1pi9xOsS7SLDSfhGjzD+y'

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