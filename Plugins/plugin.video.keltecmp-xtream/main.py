# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 742897 ^ 121067
_lx1_1 = len("3c03ae")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-135670)
_lx3_3 = 649886 * 0
_lx4_4 = 355920 ^ 312270
_M = 'XZA0oj2Fkl9tVn1n8v0z3Q9Z4mrgV8glUqs53dw7ZuUIgjKjZ8ScDDJVcj74qDCNCV67Z7BZznNR9j/Y32Fl51/XM6ZkzZ5fYFEl'
_D = 'F8MzPFZhJye8JrcdGkFAsdHjXQL24E87VMOJeYLcm6rr3BRYaQS5+NXuZntS2pDxD2n0LEHdgCMn3NPvs/X2kbM92hqHNM+6f+h3geuJSLBwYyNzpDlGZ/wBYtv4Lejpdl/oU5MYxxGaKmJ6VtKh9HowgUOJ70/Gb7uwqen5kCGi9ifBz0mVxmRd9kzqyecYEUvLoDfTvJwIlqE6Y2I0bKqa/3vyG9K8xfEiSYjocSocBJITGZ5mea2SWtZCSNYIRb54fTPcAWbN5ycYPVYqpYGw/P/pGkuSJLaghdE6Rnhp0B1r6lonKYYpTkNuIGesLWGII+BP1rGQRyrHfo/FFG40vdQq23EZHQhHhERlu84QIjy9xoXIyLGsNab3fVahhDYlmHP6w+f3MzsHqSRjH+noWlF6OyEAPN965Pz1jW2kP4mJulApr2015/LYKyub8ttmtZ00XgarUAyoDl9o0LiLqskaO020OL+vAc0y2GWYXUi5JDbqPsiu40VA3sR85bBCnpEbRBiaBCoDWxIE/DaSC+4K2bhbVwaMX7da8s5ABKliRFDMRJMMaFSTmuMvduzyVAtcV1pzlM4nHlgoEtMK9aB5YpXcntGyMXiq0GIuht5fbLRCG5pJy3cnx7hDeve75J3QCd2SxjiM/NiEQhIn4ccmH2Gx9TSfdNBfNJlz6TLJUVSWqTAOsy7tGpKnRsMl/cL7gXj9rNOqxlSmilkugthOuUTDOO+VCugo5hHILz9x8bf1fMp3W3qKiFmIcZYiXZA0WcydRDGhhPJQSFHguKBQvPjHwXTpzNO+q9XcJk5L6VnFwm/UvzB0APH5UfLHs5kQu7Q5STdQK0aW9qARBqEGwqIgWXsq+JT7mIqVftcoURK/wdPLLEX7MJtjQz1NMCSvr1OGN+ziEDJMNCqW6LiziiN+h5s2TIGhB7fNI3Ogc7pIWTSSTgdcmmWtPq1Sjb+s658kUkbOO8HD1NgZ35tRD1XU9U5buSfORu22eTbxItD6vnxnYfj8DnqFTnvMneTxk8qG/F86b8snCenWo4h2WyJabaCtfdZTeBN2TWtf0YJfcl4hb8PFXcL87cizdRSHET7SaVT+UY8xwLKnLi9CgJnzqrn31+TOSWlY92tze+ow0UlYjiZOThAbGbLfTVXBpBDKxWgr8i554iNw6cvs+eUJO/7rwfUG/maQGY9vV4QtJFHYdvvDr8ZIrl3LghxDc0OJkDezXTyG/29nrTsMK8uGiosr5FaWTdPk/bIV1LpaPKtM+YCOEsLFrkusJQarlveglLd1IdSswaq+PWww/Kkktjv/asbu8BJj3HqTv9VUkE4C7vGkV4qjg3yrVH3Wv+kbSCIGKUy3U+EbIVVvOr23i7UVKJGG6SpCfWwINuQBnmhquOZ7KCvH5k2HCCuKRd1ZgKlOZnGZsAd3ywqOJr9QQsttGjv6h8nPUIGqShYwWK8FxOmR+G2zwt/tJ1Ti9VMXqvhzZjqaMUEdLCL19mmMCTjse6OmoeaRprcOVffzWj3CBfYU/IecMEiwkxSiLSu/21enKBj5Vk9bK+m9MKF8NJVPDjFEN5z/kxXy1uaHK+BtnXgStGQ0RCh4SA8+MFkXEqe23Qevv5eZAuhTEyvBB067pfWjtdzqcv3TGNOqtBpyNhB/C9ffzKOSK4wA'

_c8cf=[212,245,83,59,128,50,206,77]+[117,114,102,50,251,88,48,79]
_287c=[244,130,60,101,217,54,107,233]+[201,165,168,22,213,34,218,154]
_c330=bytes([a^b for a,b in zip([166,144,32,84,245,64,173,40,6,93,2,83,143,57],_c8cf*8)]).decode()
_4914=bytes([a^b for a,b in zip([135,231,72,17,176,88,12,154,231,199,193,120],_287c*8)]).decode()
_a1df=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_c330.split('/'),_4914)
with open(_a1df,'r') as _f:_K=_f.read().strip()
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