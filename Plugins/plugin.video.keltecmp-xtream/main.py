# -*- coding: utf-8 -*-
# KelTec MediaPlay 
_lx0_0 = 568865 ^ 943564
_lx1_1 = len("0f1f78")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-561676)
_lx3_3 = 546360 * 0
_lx4_4 = 101627 ^ 102451
_M = '22PV1V9wVRkzigcmV7iK5UxSrlES91Nk7f5MDim8fybTYJKCRy0VS2iLBHNQuorgQlaqUhPzAWfs+BgNK+old9Rln9MeJBRIPIkK'
_D = '=Ahxkk4NHfBzwarX/0nwdhUovjNk8CDQ7/e9Tfe8Nh1UlptTczGCTp+vsDeldZ6CANcbh+wrl+roHkKeuGAxhiwT2IDMqzyIzm2+5gFl7zTOHrJktKki5wlGkhkTgQ0dUTFrN8yDezAQH2amG4xSbEtF5jZEW0RlgliN+bP31YCMWxoZxwakh76+MCT1HTOIohYFOaJmhQICM3kJvXCnN9VDScyLxHYac0V+PkoLlFG37sgTrmgUX1UaVsBcqPBhkz2zW0jADHEBHoGUarYqVMYW2sLGmnfle2VQG/8gmrDklRMdYsyE8k9a1Hsyj8pDzzpQeP0hnqw3R6LHm3ikdEMGD6c63v5CpS76rgEph7kVbBI/mUNnTOLINOjiyESqbLrrkyR1RMQd4I5ev1lathNztOxRY/uCx0+BAMEstUKI/SvMZQ36KzxRmbGMJsKWb0QRwqPf5MltBdRQQp8g57auTzojbuuxf+ifk69KMlv7KtS2FdbYXlJYvxnD3B8U8nukpK9i5swGMxJcwHXqanWpETRUntQnaLl72M5cwI/lqm3CQMmdANgrKx40SDl0/r80azARJ+X+x9S6inQ/3gnCKf6F+qPu5ZNZRKCehe9EzmIZ/A0SRY95d3mdfQwe5gnr1L5hnIq8wAHP7Z1RnEY5IfYvNvQxnr28DVsIE6Xzm+VWDWAujvxK8/N/EL1SkegO3D6shfNMxGww5KJA50ejvzdD4WL14TpWb4WaoR1ouepAPNeZd0NPKrtDP8+9YKufD8Vh5f1s1j5/3VQlQaSlMsKQCkDnP2lXBS0xqyw+QLTpoKgWh8WOOv5oSfdB7fiMXb8sVsDJ2EAojKdc9UtYxMcn/qUfDNuYWmeYGQcSZAo4YQauN0BTSbLAPs95yVHO0qmtoytlyynsoqfRL2wJt+DFOtks36xJIXDCUL/sdQTcTk9OV6oXS8rAL2tsS5VsZilvpA1x1KrXsWHol6pOARjVjd7e3Riib58qsgfutQ85U92P2280sSTUbmxnSYa+N2cJ0OcDlbdgUCGZ2RyFFTjilFTM1jxnePmiJZYhnuQRYXSbiH135+6M8mJpyqWcMs1QmN1h5VvcfLCxOCXosmcN/eAGGmM525E+PF0DIuA1moRGqYONLEO+dWTTl1cujKwyl/pVnCUOcmTNZBGc6iHY6NjjhNqlz5lExHizupKL4rpYqTIkSB+Vuhz18Rgxd2kB7nQ5jr28mKePU+FypgWo8L4yQoKSLRPd/Mhk6nn0pfPr1KoQY/BIzFGdd0V0Xtd9k6crHN7duV6TWZcOhzCA8RGjRoJNBTHX4z5nojh+VSJ7/Ei7G90zgy2zjboE0z8hPxytYR6yszjPSUHxLpkIGBf8CIq395zyeKHByhjXCQ2y6X5iEj9tspnSOTghEbIwpVqtHscPsq3d1B20ZOQAjH+Ug1KXvrqM89qRJdotqt42cPEhD4TOTn6AwQV9aS4T6LetywxG8lHFwWENyPM5PAOuZxXGPNRyTpW0EVcHsokiy2D85CCxA05siUZTzJgNkplpid759Y+LCSMXWhhWuCHCUvdo4qamsJP6buSs+AqpzUpWNeVU5fj0z/Ako+9kzaM4Q+jYPXTdNTSWriWCUlUPyNqfe3vGIpMMl6U1OdczGYAxkxGCbMxNIZNkD8sSH97izZla9DVbDXuBk/top1hpqFhrXn6PkB2S/YLwFFQrNYMq'

_1e88=[91,9,80,120,66,167,131,144]+[174,101,173,100,103,123,195,124]
_b27d=[154,76,100,2,243,157,123,26]+[225,154,150,98,116,164,142,192]
_c966=bytes([a^b for a,b in zip([41,108,35,23,55,213,224,245,221,74,201,5,19,26],_1e88*8)]).decode()
_16cf=bytes([a^b for a,b in zip([233,41,16,118,154,243,28,105,207,248,255,12],_b27d*8)]).decode()
_9f38=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_c966.split('/'),_16cf)
with open(_9f38,'r') as _f:_K=_f.read().strip()
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