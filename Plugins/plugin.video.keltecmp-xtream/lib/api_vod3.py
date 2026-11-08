# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 248760 ^ 913440
_lx1_1 = len("293c62")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-695050)
_lx3_3 = 692502 * 0
_lx4_4 = 323151 ^ 243405
_K = 'ad9b7eafe45c64a2907124da482f697988b96de8d17cae7883135e35f1d7db03'
_M = 'OV93hcuUxrfpWbMMHHFXJ9ojqhU6+DTpwOZJeoG3p09iCTLImp/K/+JUvwlNJARxiiCtQWz8Yb3O4hF917+qG28IYcrMlpz/51q/'
_D = '==AKWxJa+2OS8C3335SiscF9F9c7q0Nd+UWDWW2aTbZmzYnpv14xB0+gzl001MSPhROC70lFtXIguXw9GyRNIdiDvleWEEe7L5vwC5q7iKGo+zxXqEZRBEVmtT5aoONt8rMhSdl0y18QTcu9Twk1VkvOD10ito8RFAYmSmFZ0OSnTfnlsprfFYCxkH/f28qBjEGNBAWzObFhRsdgx1PXhrBG/dslmkbjOO4lxIeg5GGkdoH0mzB/GDuuNnuz8yQGjkXkRqbtZGyLod/26JTiR3im0O/s/AedQhC70HcST5d33v7raOLl8/XROTIfJSOhg6oQoF1QKhW/+SKW0CSBZSL6BZ27+OHwpz6vfAuFqhF4nOpiScY9mBnJRugE2ZCGA0Nw6Q0nlmvZRkZEulstSNfGYPtO20qHghiVODfH9eTpHij5fpawjRh4KHzLdtL1hxPBJXpYLg8dJSwbA3zJRZrofHpVu0Uni1gm3VQuGAHYLPgF97bA32sQYquW1agTHj2nutEyhIDSJ2/Yeq0h/wMShHAIGUoKDY9Gu1fC0ZYwyfeKP35ChrocwHOoKzi+cl2/c7P3nAaoBxeCBTXGRVg6PlKDiBgyksMcd4nRCHFVn5UQMF1iYeEi6QbGtu7hP6rOKgj6rEpZFCld6J/EXxzzEvdGdKprxVpt0LwbFaztNwqXH8T/byn90you86NgCwa4+0F+gh/v7qpAfEvixcfN6JBdqbuPT3m2S+mOGEzBuH1j0vXiVCivgjwMm1kSBVTZBKAaBtqXEwxGd3HxuGZ9LFs9yLo17QfO4pjj2yQV4FbWagx7AvFgUzbnWSItJKK+KZUffJ9y8e3n5A2j0LUsYfMpSq/54ti5cktN/eHoQGTdJo/3/q+qAGdqQAMyoqqDDQfXBZZ2jyM4dC3qBs7O0lnroiIgj2t3LtI7N6mvpZ0I4T+M37JVBL/Yokr+OmRNojX3iCiI29Wlo1MY9/H+VB38uf44uV71bH7SVBOHQa8GCwyxrfMl/v5Sn/jz5gVWnhr4sWVdvV54apZzhvNDhs7oD4ft9MtmzUIDczYzbvxOkmLyWtrj2gDLTv6JF/ul3rkTG31qDhMqUDlqRyuqVxM6UI1bmon3/pgnhIWCFvVlIvGOzdC8GTOk81j0GbP002o36COPATrnZmh00TSAeG7xzEgLX/eHnlGcmzZ64E6jQtR+D5pBIxnFTbCrV9Qfpc89qYwgGfaTusFXln4r8McTs00RDDo9Z0X7SULzmriQBH0Z4mdzwSp88msSys8R4pNw9v8LSvu01Hz6CDnq1zv36nDjltSfMS4FeJA56PmhjPphraAXtWUlCMzNwE0qKbQ+aR06BqYn2gAeOnDoiM/JjoU3bL3u6KPealEbDKC+JfE12cy2Zm/XXINjXDCwUS9YdYJTED9S73ZvWJga0aTabEgBtlRtR3yBhyA1909bsdsVRbSzByaddMlgNzf97XruPi3Wy2PP1PeHZewlsU0DqvEqDVD+KFjZHNH/vY+BShKCBdN7UDLsvpywYzZvYsXKkH40EyAr/uu/9nxCTJRqVFPJgShKSv+o2pzthw8nI4v2+BU+w0OXB8co6SOK7V/ye4k11AdD987Ldtrb+hzB+B9cp6XeY3DvpJxqDtqxgWnbAU+Y0LUQLembibLpRrYri/btgLWhHAQndtrBAfwVXfG4h6p7sWrxBOLt0nv+lI2jm6ffYrSGGAQEa6D2GWl7OtbLNsU7jd1aQNA1m+pQnacc2RMNFjgFP+aS8kwCuK4FoLsqKjb1jp/ybPm+CRFsH6/TFaM8A3JKYGtixQfu4tC4ZKZSDe0tKDOklcRCfZVQeZmydwZdiE95TJO3'

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