# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 903587 ^ 972281
_lx1_1 = len("e88e63")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-240389)
_lx3_3 = 752708 * 0
_lx4_4 = 695776 ^ 409486
_K = 'dc10f2f6359667e0e2dc0da8808c4a215e3bd9b5ae1c476d04f242182a21446e'
_M = '6yZ9T1KUR/sQE9ePWvgua/XcFMJ4gNG4TUe7EBz/ZgTvYi8fEsxG+0lE3o1V/yUwr9pGwH7U2epJQrwfG/ozBew1eBpBzEj2HR7Y'
_D = '=cNoRc8i433TEDGE1HT2tfdOqiWxClRzakHd4qnh377/zm/rNNJEbrNo6me368ysB9OIzgxvVtpdEmTNN7OKHY/rdyry0GIDh/MpUeS9gJoUA6ZXv23wEDF7o+KK2HP5tgPE98/N0lLXUQ800UmfWsUXKdiqZSsuNmjjvNvAqzb40BiZ3SbF7l4M94PPw8NooIUQ0iPDrqRX9XL/ItamCcjymGeUz5aWC7azyhw8c9aYUQZba/drztj5F9cDYoHHklPFrQADgBeFSlxc+I6vN0gEGiV+R0nyuuHNGKhrZp1he91Y0X1sdDWy79wnh6DjWvuE1FzZHMtLS4CFKIfN3X5axlrr2pdGMGz1R82jmm5xyJ/AjLhJlBsmOllrZJps/hIP6ZQKe6qokeT/3Z8YwhDo+7GS4Jsz/TygwxQTAcHtmMRVjeD1SdlVbEqVEQpDy2ejNFyAApc2F9C9TRJhVHDncidMbFKs96VaDy9BEnp8ycvTYZEJjilk4tN5g6g7s5G3QKgCzc9KfcrzQr6Y+ciSw87moTNPcgTBk89WGo8xFp/XaCrZRjkKRAquu/BJt48lBfAQ0P+gTtBKfDGHii/4v4xdiC8wCB5s1cGdC4DJ/JSiQgCy5Tjia5OR4je6Vk2XA2gJUOccxbRuXJmY9RZdXiEdKDnQ4x2ZODGhn7V1VvSGnoopJVuwI/vg1Wnpz5nNAkSbKvfhGds4K38NvrEcRR/2p3xcXPfANYPsvh16KCGy+zL00rJOTbNvzpEKm8eqjAWM3ku6FWNCRRnPJW7brYC2LqnqVjJABWhrmVxx3j/PhFiMbk8+Bq4hLvBUkJV/JU12gU9Ud+BHFNMzhGIlceSNLicvimoXx9ABeOP3obx/Hu6om8t56JszCEZ3fXLpITKy9b0eeqDgmVb36QrifD8lKBhfYHFZ2TDwKnEVw7rge4j/LCsnzvkK2DCWA0yW8wy09Gee6zDhcnd0Jg3K9BWmf+H1a/uANnAnrIhEtZjbhdf85DkVE/5Nl1cDKyQQhSd1JNPs7Cmb7wHj3IlekamujUP0PCyZxR9GkhMotYyUx4jHrn7las4stsA/3FHHWdy+2wzijJ2MzuWVss6xiXJOOizh9t3MpFZOGtgixQQBNq7PdUoFyYgw/iDuzAfanfQrswbZAMPHOpyhRJlwnl8rho9uOZcC4ZJH2wVjvcJ68yMBVpNFgCAx1VV0s1EXsRnO3AbtUqIHl0N8gZhSI1QPvDCGr2ZmzMTJUQsX3vsZOq7No04rPHKwWNWww4rRFc7kdUGtrQaLd/VJMdvLxj9Krhezgoj/9Obk/j1mwPQDpTG9kRdNNrzvQIBaoJNATybn+5fdtg+cRwfXm1UpUQwU8Npms473KJ3otkg+rVJxSy5PM+5t3SbMnV+DC64SyRHrcoYUhOcEIlB7KWc2VFravWgNpAFLVS8qUeJQ77FkWyyQDpNn55t+E2PjwqQFSe9GXk8qwsRGuobJDkjdXglbLo+ZU5pxW409TAfQ0ppIrm7b7qTsrbFNmdsX/5h1fv14VXBRQmvdQx5nplBzVnuVBAG8DSb+50wqKhwzdyO0YeRSGmwS4PwoQBfg9zleu6Lu9YYl4iwuD+De1Q/FGTL9GBfZFO+gQMBL+j1VjIvrkK1hHeUlAst7XgMF9/o4mb033n7g0nVvJ7X0tAHroB08oxUR1O3WpwWm8jFttciYo3rV3nE15CsKqYHvUKExkDayuW5DTPGQP+0fAmAX+LcikgVPvYJGT8fOPOlGgjBxHfj6c15y0EojLoWLleIwlMRZBSPcpFltmfTnDpF6wLLKKUAr20wm7aQ4meUxxILa2F7wk8GI'

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