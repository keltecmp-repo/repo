# -*- coding: utf-8 -*-
# KelTec MediaPlay 
_lx0_0 = 517720 ^ 350397
_lx1_1 = len("60d5b6")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-292046)
_lx3_3 = 280978 * 0
_lx4_4 = 761547 ^ 140541
_K = '28582a85e128cb7c0d848115d5ff144d50fc74c6bafa122df0d7564f8dc11865'
_M = '9EIrXj/Pr8a90tbFlj/IbGHEUpytulWKKq660gJ5RaGnEiIDZs+qkebe25GWb88/YZhQxvm6VI0rr7uPBSpDofRGJAtrnv+Ss9Tb'
_D = '==wzf9O/wdoFcKVUgYzz4NHDg7jnEacMXwy5EKB7GDOkK4YZ95fMEPzckSm1IGBkdxJAr9RkJByRtfiKJexyvKSjC662LyDB9smUUP6jRHDpnBtAeHbhAyUbmj81auMRSH4Epnoentz5zyLQMMQTpQF7yhItfa4SRfi6Aro02xxKGXXWXWL32Ns8Chz6T1AcUus7rOFs4IY1kgm/MAFvr7Lx02utB+85Q+8bqYaffiBRAkxAbtNLNEoRa4vZGzELEXbCqK4l/S8XGnNXkgdpIcB3QILD+3map2B326Czt2hZyLGjxtwIXZAzWeF0Y3T5e5KOy49GH0Z+gsU7ZXDn4bI6QZY+9UjLtbcw5OFWhsZAmfS1fPZqG/DBjRicU9RLTXGZAfrz/7KFgU+q+JE5KbPURTEZVftviPUQyT2ZYQK/++2e39HNyLuLQHToK0nYvAYh7Sok9qOu+YkNp/VWu2koSYKF26R01VGlaBkVfr3rcAHccI6S9Ne4x7tGSmw3NnEL7oEUXoGMC6My7m5vkkusltUgpIUO60pT+WHu34aRhnt7Ulk+WxzbE5Vt6ZRlvYXj4oaRUx7o3Q/wuEu1QbLFhMBT0Im5mOyiSYUGKf47vKHv6uK0qUmNYIyWmmnUjcxvSEIfJRP+sUMPIHou42j6JRecnmh/tUUAcI8un6LX7chbnpjBADWuE/3pdg7JeMnAqO8ZXAGg4Zylpp9SFhnVtFZkj5xm7avVmErPb8h8rKUI4z27UL3A4uVnAcigpGfA56buWVvWX7Y1Fq44knyiMviAsiBtFlg/T17waPxwOS4LBcH1aEZDXmbIJXqjs2h0O0DWeIp5TaQ4iRedLRx89BPrTaJuHmfVEbHnIJrmOgNiMzmvumPfBGyrkdNo5oi+L4xdK/fEngFAkgQQnuKdkItf2+tonalUuAceSiwyFOxXY9Wp/exLAeS08Bv90m+OHLa/RVLbS1R6EuwxeSYPcaNweQclQc0M73ZCtwr5Ys/st9zwGTzwIVa0XDGY37e18rN4eOGe5+AOcPV8GwMqWyQiwX+A5/8/dFH4hbRkAvNhflKeDLh/10VAGmEykRLlpHwegJbAIZmSZMxMENKhVSfRw8vVEmSQ7px7Sjiq2ZZQ1FFOBbPXkO13Rtf10ri0jzMeNUCl8mxhLYVssgedzDs0teLb08reRraE4CZKz/WglSc7LwL8GvdnyXLgCWSKUvKGaEqthd25xbgZaXW39slGZZQulu668POvXGaaGdKxWKnFaLZDNddQtGwagUG/wFGdgssjAPGFyCG2nPK23CAKM417TVGE1QBQSBZhtK2spom/dlvp6Ms46VFUJFvOGCx3tXVMBz2xwvBXf5DVHUsM4OUvH47K64BzK6YJy03XVdiATQRVwdELj3PKkO+0NmK/S6CdfQUl2pLVkhrT2qbIShj3SyOWC7pX5JdzTp81c2jxutOCdKe1wFDcTln8ECSzyzI3dsUdILZfPY7xDo4wkK3WLKO/Bvqhwwo6inIJ6xbJOcb7hOCMac2eP8wuG2tt68iQhI7Gsts97v7srUJf0ConPdPxsHw3sjUshGn2+8onmWIvE+BwNwk3paIQDyvX+gsdBykRLjhvL69hq+2LJLC6VSLj2OKdmLYCLXGNSBiRRolXl6ilB8iTPVBkIgWtInD9FfSFvfdT9omMSJXNohcs4yD7uqMD4YHoRqQKrt9AdnYHLSiRKi+8MF7DgAjeuuPw6fI0d1sqt7wD+Kw1XJNtON8Kn6pCII+jX/xacHDuYVC0daiwN3RzxhiV8bJDnKoF6Aac2+kLLZCyXaJCTeI8PBmQrCCno9f6FpwQ7262IvicSJ5U'

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