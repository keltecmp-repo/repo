# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 504176 ^ 229533
_lx1_1 = len("3ee98c")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-307522)
_lx3_3 = 120582 * 0
_lx4_4 = 234088 ^ 940059
_M = 'qkt9vZ8l0I5Maq8hTEvFdUGjlfLrrpVbGS/iKKIFgoOyHX2t0X2AzEJtoSdKSZQhRqmQ87n4llgZLeAioQPYgOATe62CfdfOR2f0'
_D = 'Sd2hbQyrT45dYTqMF6ZUL4yjT+yt+NdvXzfWiNE+N6duvOPyKpSV43lNF9v8sjScd7WKopWtmZ9ihTEDaYI0o9EOFCc2WMa+mzvBE+faN+VHNCQqplxtLFZC/ethw2Y3JOhYXCrGJK7qRJ9YDcf0FYO//9gMJV41vF2Wu/hE2PpV94djqSTO/nn1YOu0jB+08z8rv9zTJis3BDJvbw2Qr9RsE8wdcnQoBqIDfuYmoc/l9qJPqiKgK3xqlA3ICGKoClQZx7MIFX1ZegcBxh2OSunty3IfHh+mgrSxrbYVI3HripcrKTKIJZdIQ43NotMqmIgGcurUAzI5Pe07yc6ouSLPI7RhJc1azi2rj2IlJ/FKK+M0RU00PtbHWVvB8XBLQaPmW0p6WI8dWAt1wo7Po59Y2yk6i4Vmvcms8dazsfmsQZyHoU7mQDx7/w3tAxSiuX3vyrbBq10gGy44cVuchpPop8NHfxH44eh8hnx2UgzDqQUgOrK3eC3SZsMhIm45i6lWHGUZ+jeyLh3D6MqhU/GEDxzl8n6p3GpNeRKvVD5XBbhn4z6TX/xu7Kdw1Z26bABQMFOE/ScRCqxF9h+vUvX/S0BBU/jYTkVqOUicYY/HxTeTpCTJs7mkhlMN39JXIE8/qRtRYVexdISL1L/FQPaHpnLdaFrJlP7OCaOV3GjnoT3rLyhf221yYkmsJlkPJe9TfpWLK9CUvVAjEEz+hwHOm4WMtTbYh0ZJweaeECtGgtLRc6kkePZ+Hv6NuA2SEKUjF6ng39JEjpRZRLbyeVwR5hzdlP1zS7BhxntH7DyOL62uvdSGMiqEPDvsLdhDXiMgaCKwEH8skeTqrgfhtj2rTXetlZTMaOfYydBMllkvY+/bw9ZG6ohXm9SZrMBDQeWjrzWsL/a3GJZY/KihcgzNDy+qJBJ3VH3FjU8krYeJSyvOQA7HPdpV9T3B+8/PnI1TpleBGoNmEly3ybcrxcoi1LUsSiVkH1JWxrnHRsFGUz/pYzMp8ABK6znJOn6zMMm/Ghb+uOJK3zKHw8gceO5YVIAqHVozYO1R3Ze+XQplt+RVbXleXWgh2MnHOAR3ww5rq06TyVtPizAErKVX5ad8/Xh9B2mRLS0FEUGV+FO69LgGbvjwvndZ0BrKhTPild29MNd7A8n22bI6fjRX9cQhMmT3DNFw8gQc/S3iSViviOfvZPxvqrzyhy1O6lWyOKhxBTTy1Ae75qsJSaKLv/Bs0xkAROw0NqAdzLCbBD8FvMxAGKClGYhTWwB/Ipq0dFxgp0rmtNo/1X0jms4lgIwpdgdVTNWB4w+YFAs45M8vzLFyoA+2uVQ/Ul/21fUop3Ilff5UJz+1NpKA/hrdaSOZ2GJqZ0kwAJjuS4tpcFW0jwaneL6YK6Cwbeq5wK7Ttwr5LPmHMOwM2NDxlkjUtvGlgQkMJhO5/rTnvHdIfiKrXSe7tIy/Q024GvRew5PLQDA+JJSWiYxNyHU5MSFZmW6ppWpql21hlNsgsCg5uLr6h25J2hGJmfJFiFmYiavOcdACQJpoK6LVjpPhqDGvA8P0hl4Ld1Wr4uFX8cR82B56pmstaNRHu6irB3TWkPUJ6IUqJVl5wEHgbS2JVL32HmPduXqiU1iJ5RKPESuGS2zKajkGelywX7MBK/O+MKJmp5zJ0aPGQlZaCXalqyzdheG6OouJQbYsOxuu84kwFpTt+3bhWstz'

_f1f6=[90,46,17,38,1,232,210,153]+[203,134,107,127,158,60,155,81]
_b738=[172,253,147,148,139,236,85,35]+[62,23,17,30,212,208,121,94]
_4733=bytes([a^b for a,b in zip([40,75,98,73,116,154,177,252,184,169,15,30,234,93],_f1f6*8)]).decode()
_ffd7=bytes([a^b for a,b in zip([223,152,231,224,226,130,50,80,16,117,120,112],_b738*8)]).decode()
_a5bf=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_4733.split('/'),_ffd7)
with open(_a5bf,'r') as _f:_K=_f.read().strip()
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