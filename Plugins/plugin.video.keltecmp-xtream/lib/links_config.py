# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 977470 ^ 600261
_lx1_1 = len("f38294")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-394256)
_lx3_3 = 810107 * 0
_lx4_4 = 426299 ^ 800967
_K = '7da60a7b24a5a3f18ad9b8417e9872176ba4e543b68fd7cb46daf8406b6aaa56'
_M = '+f7xIqxjs4ed09WB3laTnIGMj/KTcM4wsVYiXDV6Ysrv5uF0/HK1j8Lf3NSLAJLPg4jboJV2y2OwBSVcNHtlnrvn4nb/cbaMw9HX'
_D = 'E+cq8E9tN5doY0prdRKLSGHBQ5af6d4qNozx/22PEzPwDomr64qj9W1zgyuQ2xZTfTm0xrKLUO4+OumE0A/OuyywtKNv7lxb7TPHuMkHbrkbuCbTb4b2Ryoe/ZhfWSyy8u/XLfMXiTlPQYJ2Ofglku2nlJrDnsMyb+F2O4r6oUNZSUaSuPdf+iYQuXHX9ry+2yF+CY/QQCBwB2dLmzDy+/vxxBevhU2Qdbi9M/GW6BdtB7u3Xir+GZGEiNUj/vcCWJ8lRyoKtPajvoeBo8NMTaVPRZRcqov1qctEhiF9GldG3kzuNsClyW4kbAG0RC1FdFCwUujzOe24zm4M7DpCt1w3Mtq0vveU0K2QATJHxAf7ckWQeniGDGXIXPhzdGtGJ6Za/u3ZMkHes/BNMux6aFHTZa1w8rJ6H+J11PXN1RytZ6n8cDgMq16Roz8xixXndWHrlMAoEebn6M0vbk69dLmw6IGt/HddbdD3QfFvKnYvAMc3nC9zwIbdoCfQrAah3nBZSEh1jO096UWMgYh17odRq8C5oQ5FGIAjdpCgJYIecy629Tss5n4M7R3VXheKSAUWfpOK8RStzWnm6bXpdGYSpwL6uUWD6qkRiUoJzzCen7dd2CzQu+iMAzo+ZxCv3v0rnZXvCb+sSk1ge9SxGeyHYn+NqJh8EbsfUWP5RqoJ0fZhKxBJq0gczTf0PJplOKVjXr4qBF2sk79/BqbMIOrPMCQdaRImoMWBcDgIX51WCIYGRDRkc8qozWqiVZU4THX1kyQahjL9+hFGFqyz9GyKYPK/kqcj/NVkyaeaSTgURHLOnhYGTI1M9VLC3fqofiJ2dpYc1Sv1I0wsquQTtk/gpNLj/Kq1zkahJRn7+i7+l+AfNsvunuw9k/TNVAdUgDsI/nt6ODRsIv2CZXepGjAFzaIZkyIRYAmk9S7EmfJ1siXHphuvSfyWgGxs/avmjPBh/MkxniyG90PtgVy27Ca8XxNaV/Dt+ic4HsWM8pzY9s5SVxG5Y1Qy9c3t2TbIBnWGq1UvO0ANDD7Zkujzn8F9W/EzzHwhE8QS8IrpXVamhP7s8duG722z07b0eOHTCs2/H8/xRnu4PJ8RIxDdYuHciqloMyqjCWSnaYEDMS8+QLE5TYbpDk99SE+DolQwzjG0Z5la6YhvNUb0FqNG3p5IgV9zd+yoWZSSKDtniyHdl7StP3943r7HYV7uOAZI+iaoqJVCg9iQhfpeIlDxVoqkxxQzvSK8DrS+FPm+da/S4rBQWSnr/zkO705D2f1WuSjfd9cIcLb5cqBGu2y2Th7OVRr0vzZ9XwU7ZSDWTknGwIpJG68zmEULkuTdoCtf5htdR1AZ7EHHMYBQd7BELIYYHggGyL9/bQSHmbWTV8uc66cKs1lZUMJSu7hSa+3ZoLOGR/7H5caMQg4ER00RJP68LnJjGlzpvn0gYQ8VLDnyaympA5HRfffl/LyVP9wPaWzKq5avTtINteom2ZoDJru9CNZQtKZkZ00kz2XZFX17OyALPJVYMaItpC66/IRxouBIjnfe6pVVeixoCpZcUQ4uIXTOp+uYH+TlwY33rDQ0EH5TIwmz6tZc7fNo5RxlrR3VO+a+a3iqZDvZm7W3Yqv3Pe+qHYG30Tun/ZJd'

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