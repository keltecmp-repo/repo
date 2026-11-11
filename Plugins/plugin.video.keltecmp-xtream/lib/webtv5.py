# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 425148 ^ 623580
_lx1_1 = len("0373c8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-716314)
_lx3_3 = 314989 * 0
_lx4_4 = 338630 ^ 930962
_K = '1e8a13675d7b94b60de5f73e2649d865e1153f83d1f42c75885b33f1520ae816'
_M = 'VNONNueGQ/YMpDjwD6yUtXZ95eMW/OF4akWS7JaybbkP19Jk5oMa/AXwY/RZoZ7tI3fm6UH7sihqSpPhxuhvvwvXgTbl0B/9A6cz'
_D = '=sRmEl4CyTNXvw7CAwu0rl+W7azL2Nk7uQylHhP6Y4CRr+iBFOcsR7EsIHUnv/Ob3qEyQDmjFeKZU14esp/9qjKzzQlV3hooI+Ilcs5+QENdb3S0DlMFnfHq82vPx2veUpO32RbKJIBn1QOCebjb3l/jCqJS6bFqA4Ud0W45uWeJb18Ku8AmrssrksciqShxCOTp85dnefDIPOoZnY3pUf4yTsb1gdAUyyAnv0cTPjxBR9V6tq0lPCtaQpJDG+lsJEezApxIdpKnNjLpW1dKysKFuBss4lKIqH8lM5fx2/ZtrMNjonnDimgZBF3qFmn22ZPRhI+xruEDFmEb9G+E7jgww4+uyNsfXpeVFhZ/NeBaPW21bm5c8v5H8BvGx6C65GsEJ/HjljzRW2PCzGzIgLwodQuaVMcmREDS5yIBxLgqvIwsccXfp4Hf7FT/6VZ9XOPN2Mbpeve9UkzB+iZ8HZJjrCnk9jTFpufll0ujdovLRL3oafIKn7brT9ZmGTMPCfcWYtu6m0u5J6325MLtn8HMcaSNQdmm6sBTXt7cyga0aF8BM7szXeLBBLi4ump3deZ3P5PzlTs8mb1/RDdP/WvQkhpJ+VugBgBWsEhiDjG+i1Ds96XGVrpxik4UrzTgOOLroy2WOXRTdTxC1ycvciw9lCVdwHURUQvFWs6YAMmdXlRwZAk6oYzgDB1AJdDf+n5aLz4AlBpXPxbb2bzXmkBVWZgJJHCFfQFbSMLfbK4B03nnpSO6ASJOwRuUG49zuAaXex61tQnYIpoxS7lqs+qdoSIQEFdRdTchV5yDHezjAITiAwk2FvPx67GkvQo8EnI5HGapeoyo8eriebHkOTam7mmauGqGb21LOVGIdYL2l2+aJFE+SzI4IwDHsnXSL5ZHJY92Yl+RIvlt237oVkw2TXGj6PQZ6tSvkdsu+Kdz2yB9a49rAwpzQxXeg9V1mootCPYh6Hgy01d5s/IJ5QoxV8NwP/2FAk8bXHp2gT2vIvWxZKXPZcB/Zdf+Z1AHbPciBsV5oxr/Az+Wp/mKY5SGMK5i9HAW6mrZ5kZhJlrs8XtSH6/ueRe3W9W/lvLnLSIY3ZT9q9g80xv31mxOxFcDFIWsBs+DERk5ChvnrUzxHCN4ufTxpj4XJu/ADjoy1uzJqSQ54dp61T0lJH3phvl3cRtXnYRbtrQmTgJlvCcp4LN9MoI366/hMLT9vjRWjTSFibNZgytPhPO/y3OCIHAZBG8gnaefMe9KkeINAv8sAnXeole2h3NBE04CoT+FRgyptgfLgGxzp2UPc2rkLnBpsb54fP2LWIGhtxMKLY8QRwjnZ+EQg/qW4+IferTuZUk36jZ3KlGlWaaos6bamSA3NVCNpdlsg7bXw8xH/hBjqat3TZgSDnWus0Mmci+ultqTbmrV70eJyJhQ6WYl1TDUygp+Hg4sehvYqjrcMcI7kdTc1emkFGZ7bR3bcOLsqA/CyiyDgYKz7bcJio5OHx4F/fT+JlmYFzv5qo/rlyhDFLI1Sq/tHrbg961ngnfAjwD0bjaIx1XW9uu6Ja7fLsCQD3KzToeQxT7ZFMu0f/9mWLCkdo1stqyQOYuvD2wGRm6mnJ1u2vZ6scy+Ej80EmbBkhVRrZ7XOw8lZyOsGJh+Y/U0Rb+Rf7iiuktd/1/T7cgCzW4G0tyurAe3Nz3uqgLvy5RGkvpVyuy8XgmyR3hW4vlTyKxuOMY+ns5GxE64CTrQMVGAhF+gKYbFCwyAcArXe2fzIzqxImZEI6mAXVhLEt3P2pKSXmcBETzWcQBJb7g7jPbXRJxDPtDq4DvsMgZoatnHPslW7xTIV+TkwNkaFZfgYyFqjp7AyXmF'

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