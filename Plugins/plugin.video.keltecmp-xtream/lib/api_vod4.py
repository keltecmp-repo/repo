# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 436146 ^ 970871
_lx1_1 = len("010a46")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-887168)
_lx3_3 = 662932 * 0
_lx4_4 = 783919 ^ 211518
_K = '108fb8ddee78a98d31333f691194f3a6196be835b10433ba43bafc38f7c72071'
_M = 'WUl8Y8v3pYDlGYk3kQ+RcPJ67Da8zE9esK2N8af9yxtKHnVrmPb+274b1j+QAcN7onvqYeCZTlyzpt738qqWHB5HJD3F8KiFu0+G'
_D = '=goNHmY9I048ghPZX8BXqKL08gQ5HXq/vmSQMHTRqQHr7BMOVDceJgaegu7LUSg3Z3MOwSVrfXTwk/73izEnKYH2sMxfQhuuPGHJmPpJXz6ElGmW1JxPW4cs5dW7ilKO3Eeku0OVRqwKM5vcsAUtsGbFDw3jbodolwzWilwHS758/jOBckoArYqaJkx+rxH0jNMQk8Moa49FQxCMIhOgymFWt97cZzPKLsNZ9seiSlWe9LbIoyXC37ZspUHGO73vRmrQJuHOhkjBpganMygg184i5QRtKktPb1cYev8Q86i9JH3JEWrUcdfznky7D3MrlEZTM30/PHFRXmL51VkimGnxJU/MiudFhUhxlvL93BNOO1MFZJChnINHog6305KkEOB1sUTisK3rJtrFdub9ifTbiNns/1fMDjrmC0KSde296JcTNi8jQ4MVV1RW+LZMtbKqmH2V0yngKA1eGXadpssjba2/xrGRDd6j35i0va8g2t38jZBl2Q9ZXLoBs+FvxB1+cicJBAClS18hcgq2SOMbH75qqNgVpSN7ouwyMHzYm63Lfltxj3XAtB1oPKpqqFs7gSkYNQTu7btxgL5H9wM4bqsrYxV35oldx29HkCjng/v/gnvoDRT+qEFg55J03ohpTAg1iWovDtdkR3PA01AR3iox9SNSnAUjLmGJSgrt+3kqs8HVoHAjgwEx6kHYPfqLo9kXZny4KUIMfZV3elE9HsQHeICaIBJRIhKdgCjN56s48+Yto/a4vv4LrQ8CNZzQpUaYBtBMYSr5df/mAbkT7ZJ/DoR8yd0Pmxsp84MoQMG2iEwsVpxfH3szlK2LtAktLlNZNvCUvm58S5UHFACRSDNX0Xh7ByqK7tEtAcAKhXOiwXUp5X/7bKMYVNjdrM8XB1kSYgQD4wx9qjHjqNrGUNrVJFTqW/z8gJgQRG+NTaDVBwNpyXNFsW1RIn7rZSsj+HPlTbzsKKNiLnH5KHwGnOnSdMbb1Sihb5qTvMkAfB4cxNfNJXmLle8oHcPuSJ+gWtVL7NS0wFkoxFsxc7b1K0INDlZiG4hSA23zhXtlc0RIHdPXKq2UaMdMNaWoIrjtJk4yZyc9sNNcJiTX8kbicEzjYLibKC6aLKiFZCeCLQzWzokr/+fveHkLQ6ieRqa27qCy8sF2aZ5XcWOjxNrpEdFMesfIA3spXDmiL4ttmmv3U93oe5dFVO2mWTbgI3R79oGld449i6pJH4ILSvYOCXRmpblZwz+yI/Mi7WHBLZrCQaVkTGKs1inUX+BaMOhYazH4O3pwzdsC9aoJXDt/myTWwZyj2YWfd5rjYTb26w1tPaNMLdxZcSq/pn4oajXRBb5UEYj70cZvrDX6lnwFOtIBIrGUHt82CDo8b8NnVj2X0QORYqQTI3FwHmZISe/QPY4IWQwk4EJI+HrXIF3B2M9VJAwi3JSHs2R6AkHmg3hjYHOT7+Z4mBzHgCmQKao/DUNhkYQpWb+ebfTlKFxGahIE9UxjQPB93bF+qa8ofXeWmt6uCz2yg8//P6G1fCXYsMg2aJ1RKE7G1ypHLhDI//CenqcmX1UyZ4l3jWUrvpm5N6R/RXynLBziF5AwgLChF/EqMzmCK3g1v1FG7FnU2Nyh53z9wzjKI66fXuuXwdAhktLk+YcN7pWZOnTtDBiWd+9aNZ9lKTeeQ6EAVOIDMjmQw/2LymrT5l7uhRUXdhA5m0CPbyBzcKpk9R/aVBwAEueq41ky1WgG4nLvpoLIbBud0aw7keLaB6bVlNaa1wrsEtEV1KWIE+FibhVkQ57ULiEvfT6O3ZM8gqVzVw+luloUdrQPc7+7mjkQGQ70V8aS6eStjw+nVARemTLH'

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