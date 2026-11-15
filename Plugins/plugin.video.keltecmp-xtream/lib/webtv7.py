# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 351727 ^ 282447
_lx1_1 = len("34277b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-147622)
_lx3_3 = 154557 * 0
_lx4_4 = 855533 ^ 985622
_K = 'd8f83d797829a95ead77268bfef73eeea62f0a8ce4eb337cfee41fea577059fc'
_M = 'i4IGHeXu7BFPDo25UV91TwLYraMaKtEebPBBxihTA3XG31sR6qOvRxNdhesOAykYAo2s9Ewohhc480vILAYDcpnSXhi9ovxOE1mE'
_D = '+cTFcSah67vTY6WNVCgt+jONcv8DPP8uM75mKPiypbOVRThf3mhCgvkVGCZscJM8aznatkZuOgX2a5HsyKjMOt1KmAx+0kuATTIT/Ig9YmTDWMLxmH2oVbzEBD4KkHPzXrUBrhnLYAQlk5rwxexT3MXTacuqJWyLVDimE5WFCLfCxyzeiXe2u1Hg5WgXa3+/sEJF7xj2qBOwWniOmoS4wrAC/772oChIM9nqubyAwQEdTwPXX9eWijMa7B2oJ4rlIHfnkekki5U8Oz7EbmSw48uoTqnQAjwvBnMH9n0m3vkhMBbiIYuo94TSwgxcTIEU7nDQQJBszIFzOUUwmYfla7mK8UH6ChVywCI+TBf1wxt9TFwJXEbUEAvpMnHIXnSXs8MuIM4h6/y8xZ5utGMlTAW+ByWFhLRGZInhznTCfrYuob6TYTbJKmj209EnCBZwJJQGZkYaVyutXMIxKCs5GaaSclh6KdXqBTodGdmihIxCS9/gHXX+coubydXAOoxv7BpsulY9bc+DeFooDY9cvgq+fR++n4pps4AVNBLh8bbz1wYQ/UWefEfvd3q4sb6+l0FvBrnTcD4NYiaFP+y342GQIiME27fxN2kEVxstN2sAx7qWYBo/9SWHYqP8WDgrrXfIv/VyK+etknFJz5GW+DrkIw44TmotEyfTa2AxkPElQlfofecliuHa+8r6Tuquv8xIsZ4/A+IQhs4ss5VFXjpAeAInuQbftzlhxkpaH0rZ505jLkNIZEDsRF4AtZXHWeDMNf9H9OLd6Tcuy4qFNsA9TMGc8IvckQnlDHPQNHNqw/B052wzM0FtwF2J92GRIcVN6rWQV4Hmx5O1t82hJ0QwSrMLhXpZx4ZoH/kh7sFSpy7+hHuni1HjMHKrOh48CjmPBkyJAgiZsJ1PhgG/s7uiwQ1tcS36PkNBQBdtHMWCbGsK1C3Ubf5lqKES8HuKAkV/iZQhhCXiJqGX+q4XKaRC/8NuVNuo6Pn4qnNumhtEfpJAALJdXVEQ38D7laAEf6NjjaW8wv8YDZA2nz9hQLPKleoyvoW/GGMfd6TZfSBNl6dIQ1WRrGjIdC4H+TlcydlRQWLELdZL5LkqJElYI97V9Fa242j9GxNjGP+GgC/68GWjIxsrE2uyQhY0r/pfBMRoxZoNf2B3TmYsibep8TASojDluKnIOP6jNhG4oizTa/ACjJw+R7/yB3qyKshla4Ua3n6wXTuggnA/ksuhNUQf/czLe2wan6RGbON5JY9UTfrBh/vqdcforp9Xq3tGH3bkIXNENpniQGLH4C5cy+BRzpmbj2jjbRyQalEsJSG9yNyQ1dPX/KLAx0BR+HpuNnAJB32P7URTQ2lzmuVhvnosDfWU+W+uVrHQqOHEdN1iTpMJjuWxadUAsmw0+UQyWzoQ3E/dOlckth1w7HpFJrTbA0HnQsAL4U1EcsfIIiJFVj8O11re3epY/gpkcZ9EnPz4F+0Xzf0Te0/aIwUGiODEeO2enVehvYqC/aTIVJvc+tpJHo04akZXaXfxsmQ84kAzVV9WOOfQNaHhWAxknwolKiX1bYspnb82Ugolp4FcMltEGAhdO+HNgwiFzDfr1d57hPyXLgsiTl6zi9vLb5Sp9tn7xvczBsR9yb+HMm7XSbNNNe2tvTPd4hf16AZZG7yXU55fHnotcQrqAt7nuiA9DBo1p14RtS4AyTh+B/iB4gWH+yurapGNAFg9EZU7H/XKII04dTILQ3IBIrlvZ3RkslrnwLbjR+u1n7mvAERjybyH/L38TTydpSVaE8vVvVoSkrSEyLUQbP/Terdt+dNvDow63qRRW3KSC5dawms1eNUGfQBio40pv+GgvKJ+'

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