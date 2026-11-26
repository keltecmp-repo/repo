# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 728322 ^ 290539
_lx1_1 = len("4e1b4b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-990099)
_lx3_3 = 385914 * 0
_lx4_4 = 145839 ^ 953150
_K = 'fadd8e37ba8e4f6986efe144c7b141132ab3b7948f9391513c2e04e722f1c608'
_M = 'BpGMuvsYLDrMdA=='
_D = '=ojSVjQr6/U4IGRAjdctWfP0jViundlIqXFdAfQQuHducgliG96tQKcSHcrQWetT7DNhOD86IWH06BbyIl3hQDsFpuY0YaJgjMm6PE+C+e3p4ovRtvXOfqeOHKzHhwjuuvPhyc3Uawk2izZOVMfBNLvhR7a240ChEEStaCKga5xOShkbwFcGapSWLqSac3HTsRYKQYTqnaNVzQPwTabG7Qz5lS8MlwOrDv1ftO8B4XY2bj5N1lExVFv7PQ94BWAuP2XNg4fk29T4afTvTfXR+mC4g2mVFPX5jtDFbeqAHa+DJSV0anprQbBo7uL3qu/YIrQVZEkXT2L8VWEtMs7SQkga5cr7Xpo47XeR/b6fO7R1ECtXB6pDgYnB5AwnqF07aFb/7KWlXMx6rZsrRofKnx8knyx1x5+3mmM3zDEoKdDgkBx7jaSxcEq0HuCKRFmK12fN4x0GVI7qUt0g/Ce4jmBfsgisdOphTXVbmbH9GnkmBmRG388rZN7uOpClHn3PelwtDaDYXHNmaE4IVgGIBTsE6v03IQHUY9JBcVspGND/uviflIjxynlpq0JF30LAXbRy6c0RQQoTbHXXr4AdO0TWi2u5yGI3ozBh1j5wV3J1OT6xQWAlfCigZadK17CnYXxBf+oJtq7pttDy6KMx3zUoARrF7xK8gbavcGu5bjMFL5ScdIdPTvgEAVsU06HSWVGjk9Uoh0MumQiJ+wKO6qDAFmd9nlls+aRDwtBsHW/N5v6JT9EheWppEk594BA8Yu6J0kU3cy/W3arYU5x+1X76eToohP7GfwsqZGr4lPSGWJAHKwTXctj/ZzJv+SqcFA3K3CONkziCG3GtYFOD84469D0/PLeDakxZsXGxnbjFepOw86YeX4zoA47Of0LozoJJ44DqyhocouZhO9y2l2/JmQIhoDX1AVp01SVVc/N9KTnyalgOF6PvvR4cyGYaR32ukF3Hxq70XWr7Mu8aMYBU+E8l9+ZbD4V9yYN9VNXlXoytyhVpE5Y00w8ZOplPqAbJtUjAaP3S6zqv3IvFx2GQt58gl9gXW6vrQ7JWm3l8swhxZNw73jPHhaVdfnUyjQ/wLRF2C/ji/op2UzJK1rOEcPILUNRzARLn9xff5ohMxxDbZykjswzxeMGLzMmDcnr2ld+lw/8DLhsWvK58kEHbajTPLBUvSZpzHV7ssBqJ9biXEDj1vwkapQjAODGJmNJspadkvAlFDGHvKwTrD36aRluuViw26Nb4c1wmYC6YhgJjUBS2CAMdwrmPIto+LnPq8RSMzi8FPTPNXlIT6UN9ThsHQF6LERKywAizEeTzsyy/R6Is2Qz3AOZef26C3wb1tHlLBw9r81Rj9hLJG1QGPb4CIvOfPJy+nQ6xD6TObt5M/fw3n5e336wkigJXcFm8hxtLm1i8WV4kJjTJcUirpvhLAiF3GFHZ5NPdUdlkCyuRK1csmqs6yo2tv4+NSlGngBZOLRsbcMDclj9DDMoeQXV+VR7B9MN4xbrOlFhnDje6UiKETje4kfDqaHNmur7Pjc3qjur+kkiEaWP0MkAmmoFmOjXOTEFizWApmZOVx6l+hglZE2/MepDoVQa6cT0s+dhxZDNlOAqBIPlnCKG+MMFOxReeefpIQUpqjLRzgXFCXvEmBagOtRnxWmXlLmDctfKRctdlzcThMjZct5qBxCAvvi4wMBlffQiVb0zt26qFW8tCx8Y9cS8SiDjdTGreTeUQZ33Kdjsqud859EBkjLlIwGb0cpuE5EGKTcwa06rToWzIOu0xYmxf3hOVpPUlo6aBv7kh1K76J61sWBUvqugZa8j/EHOvn5KU2u8G'

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
