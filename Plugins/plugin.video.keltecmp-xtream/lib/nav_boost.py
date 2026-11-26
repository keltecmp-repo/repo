# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 980880 ^ 156522
_lx1_1 = len("6c3add")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-293352)
_lx3_3 = 351347 * 0
_lx4_4 = 818304 ^ 833946
_K = '12462f85fe6812980c948c2de3a38fa064f6eeb408999e14f772c4e968f795b8'
_M = '2uKmQNooegU0RQ=='
_D = '7NSKegPJlobsb4yS1uTUXdgHzf7+KcBoHXRbhzwWLJXEf0u08hGtQh6TM1swvAcXZJfRmzmww4E8mNjNqWVW9zN/jT1uqN57IYyxfBYGono6WU/2uz2DPZjlYRMbsaUdcyxY6c+YR71NZ67c6ijZtd9nTlS5PtWcdGyPu5M8+9lIS3jR61SYPtIfjgYIXuH0PoPAQ6IEHC6ePSaS62uKbU1fWhd2xqn/Yj/p85uIC4GICFn/xZ4g1b27vvvkw4TZNj7Fu5Zq32JI+KWzgl31FuhqEVLAkaBsNWOi7NFMHlM5Nvulo6YOsVaq6X7O+chDffZkgO8tskyMN87/48leC01dGTKVesNvyQ3xG8qUG+aLBaHGEzU+r4GII2iFJDSUbJT6pSh3lRuxlfZZsweCgsirOsQwBJFO6wJAt9xYhEeJ0iFWpEQANOzZiIo+jksDBk8HgK3fqmjbSBnFFa2xozhedXX25ZaBFP4BWCGBvHQ8lV3PuU8iNw4WraEcGvDt/cxnrkM0eBpC2kJRiePoG36IJLmkXkGBTHta6FT48QRpsEAlgneJk9TfYY3Uxuu7bBFd80O5R2IV76zAq0c23WZizY7W6cduVXKXLPArlw/n+LwWJLU5k+qp1zj3Cxkt3zwV1/Ngxof56w+nAHcLpwlc2RHtuxvwYwT9BW5cUkb37b2rcAXnlataktHf6tlsKIY+r6FqdNGZvAKKwfcyzzjpDPUZWom6QuoAydeaw6stm0HBSLWd7KbtTp7IF08vYh8j1p1EgUn76X4+sd4KTu2Vyv17AJ1PFsZ2ptG0YPohT7IPWtOpH03DcC6o5oH+iSUYPqRHdozwHbx/91usXbYsgGhCgHpb41PvbBVXlfl7uyH/NGR05O2/CTn+AbwF85vKaTybU2b/96wrhYUbT4VDqZV59IX+zBFiGXnOk7TNLEdaIuDWSYRmTkelsirs/FKhykRYGwtfDumEP6o+m+kbpMO7mP7yPv3DyToheEAPH+rqYKtXT4E3f3MkYs1EX43NSNVzkCZlDYFnKZZ5F6HaZa25ImLDE7ZEB9ntZc7yv6tm1p+T4m6C3pBv/p7BQcRgmRXMpAVE2FXSFlPomApyd2HTqdWyghQSzEpjjF0g3M0zEXj8jbG+Z7QR/4pEfHB9UE21bIJQCNlGfXEycQ7q+1F0fgsUP0G4v9y6ZyXJxoJ2QGctrB9+MOtR70F4W68c1kWOse78FHTMVahZQsZy2oFaQ2ujnrTf5OioA/7pOaGFYF274FfOg2vCCVjmcR6oRDC7wa/t2MTXQoQ7iR2HX2K/2eC7yVH62CmWMfIe3xIl1M57A9c3j5h6jKyK7gVTniD6YEXm85U7BtbEM9O/6SpEkp5+elYmPhN7wGq/0AcQqY4WDASBs3VdxtmMiSigKr8brHtItPRlPb75KghsBiUkNFnogyqZtZA5qdr5dBONV6O7Pjg4IJPRpqBCmhse3hUKp4plZH1yD94rCGxZY9d4HucspdylfW6T0YqGnH/ycXX32Wj9XYdG3GXfjXWyQsTQyrzujSI+zlEGba+WkDVD9ucsyfkr88IR0oqRZi2AKL+Hwzh9KS1knIt1L0frAKGugON19/2tQSVEt9F/V20MKtfOC0hsmAJST2r614quk4+A/bVhwZVCKHfDYshis7kcjgXrQbxIYSZt9o2gC4PdhobU6DpmIsE5l2M4GVcAbAbqJn84P2SqpGj1SluS2MgnZcpz1OchLjS1mWzg2eqLru7gzAEIvfYKLHDK7z7eCeFlRUvZWqkY3AoIsB9AYd/x9ihm/69jWqcVG56bOrjOJHMrOYdP'

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
