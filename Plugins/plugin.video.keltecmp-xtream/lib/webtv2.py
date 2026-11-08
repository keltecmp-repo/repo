# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 353550 ^ 648224
_lx1_1 = len("a2202d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-717588)
_lx3_3 = 348752 * 0
_lx4_4 = 445192 ^ 712439
_K = 'b7bc7dd95f38c3b3cde8558217204fb6d7f9d20adc7dfbd28f8b41453667069a'
_M = '8YrD5s3pZmDMAcEa2JS6/khcYptaoZZU1j4nL6aU1HL305SlzbozJ84MnRLdxub6TQ4+mQz3x1yFbSp6opLRefDexfGdsmhwlAed'
_D = 'l0AL93B/ijsCdv/g1c9NGmN4yDFYOGfxg7eSEfNGsFkqBjmrFJFwig6rBEOiVmBXM8jZAucxG6HHEbvbygBuhrtbHlO7xmxMteZeT+8tASnTX7UqJp3JfL0JIsDeNHe+52rncs1l42a4ChaxwH1TTz3psy+caFhKzfk3U7e0NSje0AxpB2sde65VIAzSsPaFMyORwI93l7q9L1GNd/SDhlZTDkqwwG/444VcRVedzlgDwG4KMCTTXYjTUKti6rIexa5Vk46UzVsMmOEA1/xxGdRrYMGzNYtrGYjWYO+nFg7XG0T+EycVUsTDojzA0qoUNsVoDrP3MfmR6THjLFT5sP8YjoOqAbeeXfPt3fpeFa2FZ+8o1Kg7HzZH/E6TfWSAz3wtA03e86+/gnn3Hii8I1xio2QoyAUQKqvKpy6G+jOQ+Q3HPZMXnwImNF6xbanvRwwwws+SAqgkZuWh0Rah/WGmtZhz549rmbWLP1wz+Sym2B1c2/zAg5XIqmEagKOfNhWIvoBzP5W4f3ZAMc8YRAs3851qde5yt94ktLWdKnRjyMtWGrsfKMzctUt9GeLZl1ftYeWOonDqDLdOYG8pEDwW73rWRI5BsYubkbhWb1IyoCWGhlBbnX8dyfaKkGrEsSE8ypQNJYf4Pq3qBtzsb6bD2ut17fentV/r1AYq96542L4duajJaym0WGN1E5KURYWjYO17wHzE/+2Rmj/gvZOQU9xqUxXGQ4snJSMhevaovJSuNEeAy/oSB4G425/cVJjpvAENK0UIJz8IGWxcjuVWPylA6/+QkcI7D8APNfSm8wBo8IeU0syTYPEuMCk9+W5PMWdxHSFv/IUXVE5m7vOiIilDqkGu4pwd4bgZu0M198CV+IeVhPlI3RQ1oe0mWH9jx/SVrVwB12OWQNrNWsoyLiPTkS8omEjXsbae2yxItM1LhLVsnr2iQBKU0LgXGrntjs0cKR58qO2dNBMjLMMOdX8By/KplZ1qKI5s6ulGyiGXaNoTokYK1kvUXng/W2zKuSBxuYy+HcsAd/hRB78wuhC1erNXloz6JxidefqwgfYjlJoWGSMD+KVgsICZJIX92ZUNFQ7jgIlV+74YBxkyQWpuh1NUCY/xzNd4DwTdycoYSY2YqoTCr4nN7OH322IGxllnIV4kxUXzQ+bKvClT+2OgX0pGtkwcVWl9tn7Mm0aSR7zzIZYzdh/pzWLyIAxoWWwTPHouvQIbdEyE6U/yiyy+z2fMtsB9QAWJvQ+EaV7mOc0cLISZH7rlD75z5BTxj1BYtRBxyr8yRAQjMABUXC7CHkGBUIVFYaY4ZYS3EthP7X2QcXco4/VgY7ZScsXGGMo/qRfe07qJo28DMVFQlrERQK83n7o2RLM5AyjNj59+hgP6t0vMk3AUVF/9WSSJyP4Fq5RQ4h0+smolAjSpphhV3/FUR/Y0JoVe1J2r8IEeaWtpgvYDT7gEdLFR0jIXBz3St90S5J1uADuT6pPvTR4q1lxwyvsEGZJv+oiSuiO+nrGZa8hV7g94fGxAzkSgvHW1QbhiUK/bO8qcZHHsyooOQ2Km0m2Qf1Fvr89ekdV/NfheBXj3SSHd/n/d0YY1BXqU95GFA4ai7nHThL8N5t4cNh21rqt46NmocXCN'

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