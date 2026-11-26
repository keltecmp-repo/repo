# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 818941 ^ 863761
_lx1_1 = len("6b0545")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-563325)
_lx3_3 = 486097 * 0
_lx4_4 = 951859 ^ 735207
_K = 'bd30117abfa4ed7b1ea326ffee20961dd7c691850c338912e379c4949a283a7a'
_M = 'm5et1sqst2W1Rg=='
_D = '==gotnnE5+/VFXGuabyGgSBx4kVqzZrTGIhcW+hlEOP0ZfMMLP3zzDUKhEsd1+Wuf65Yie/bA16dsHQz862BaRmso/wBkkMLcjywn5JcJRt9XkxFkObpGbzXMjM+RHrMAn3oAx/cgnSOPwuGZHTFjkDPolyFT22R0pnDOZKSPNzWixxRJlYtTaDUB5lBW5IpneGdiFrCsk7ZI0v0ZvUtMcul3iW2T9xJbMzox2e6sWs+xYeNMeuJy/r/G2xNbpSrnUlkzLh/WeEBgiOxV7ZUaGBhI18R9gD6EGhWCsVu+Y73rcRhJVQI9B2sSrYGYeN0h98iZKA9iqNtoetmhbOvGjRV+d40yJ4qcBvRVsRVosQCxQjZMC7X3mRBrJA5wTSUi/Lwi3HKylO8oId1OB3sJr9EqOxKI+eFypBmRHwotXKaSDbwB0WVLwglgJlmx61revOIHXHXN6a2yfedFv8P7AWK9wO87u0bbBUPCx2xAXuWP6ZbkoVy03kvdP1z9+pF/+BQnPdBoE4PRpLL/kBkUhA+SiwCI5TbRu9sA1KhJraxeHgmLuZ3Y7laL6uaaV6/SbksNqVZGEXFuEIKRLzoEvTkX6E+dhi3nfhWs6YKTTihZ9jeLj8rinRVLCauW/Ta6F/NNMEVXA+CEE3aurxUbSAHoNuRtKjbLuatyaQCyupj5JJ/qZWG2k91AhX4G1YF5Jnm/x92zyuvLnQ6s58xufYAevJ/jc6Qp/xZw121HpcwYg63TT5UsV8r1dU4WxgpOfqbFxAtiIGzldj5/Yh9FpKzyfYnqQ/mIN1wxm42DKg72MNL9O8B8+acllZBDWUwXsFl6c+3byoJaxNpsbZLqe20Yt4wS8WcwmrGS0r8WArle7OB9UJiNfcidbn3dTnjyxZocYj5npK7MGK4f9NgGwSv9vR2xME9/OctaoY3GJxGiX21EsWdQVU8eIrWD44enagP1XqDQUJxRP4NlD7jmgPYKt7R4flhJazvJki0ax/rQLbNe6P2UmFzorpweJdf7ITztDBBESuEU4G7CKSZmMxn7Tl20aIjRm7Oj9HhFqX120ukhhQle0y36McVSkqvKquLsa5JTpcWx/C5lY+tjWOM/ppi7JiwDLphcUfvBs91JjDdwaTTNX86Xs8B9pqKNwTQ7wayat9+InJyUZ166yW8aQLkMlnBRXbNgmePpZ/J7bYQjMywyUqtaT7gOJdVJbjuOD4zahJKA0VODoK8iODDp5grJ7dfT2nFdD6neZP+kD7ON2eIZXJ1pHR4+9WDekcXsQZoYO6WsiUCKwtOe5IxrSqzNoXFW/zpGZmHVWeqO0GYIkaw7GBdzqG2az4xQOPTdH+HKA/6tHaNWd0hCziF2iQnqtdMNieiMoE8OTaZR5VZ/6J3ITKU/TipdfcOb+/OUxCK04as1yotxf2RWjT+L4vp/xNv14WZOzA9jsiIy43g+3USZVBM5axOUI0la8TOQqB8YMxdshLk91cR1tuxi75uwQhKmSoHcMS0BRKDK1vsrter1+sU32MM8RWd46dy7mQ0AVD4a3I7PmnMJPYKeosYwOcf97Fgf+8TLQ8GLhDg9QrigCnnF282pBHD7oLWqrn08p2YkFpNplp9BPeQEjAYqtyVqgJm/hRHpmojRL/aPaTmEgZGEn7zEKYLaXP5TBXi2YqwWrVtb9B1u1Rkubo19fI6s/6OLEW6I5BcXTZDV74RA39nzY1PhEcKiBSZBVukL7+NkAvP2CITxIwwH3WsBB4ayfbGuxq2NN89uxqRWPbCXJatplFqHe/WisGulWsK5MUgWL1bUg5IGU6S1YfQNV8MSXJQRFeQgzQP'

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
