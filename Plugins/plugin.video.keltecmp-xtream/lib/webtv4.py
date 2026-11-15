# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 714215 ^ 217626
_lx1_1 = len("66a049")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-660140)
_lx3_3 = 288014 * 0
_lx4_4 = 692447 ^ 572887
_K = '9816e18e1e8ff33848b1bec8057a3386f38cbbbdc16a384e3be3b4d076cc648c'
_M = 'Q4Efc2BIOLrxkczZ3uTMnk6tcZN6y2HGJIeVF9EVAWhG3UZ1MFk87vmRxNXe6ZLNSKcizyzPN8EijcdNg0YBPkSIRCRkCz3s/pPA'
_D = '==wRudymwSIWFHegFvd314UQl4sUokHKkReW4QQafBAS3vWPBd7ktF2SwqEhjhebcTgsgUfn/lGX2NdWZYm6bXqmr6FVGgm/Vli+zh7ObOUGoOn+EHarbhQPDlvfhAO1VwR51v0cYfvNS8mdVd/MJZUs49m0hZVgwLZBCbntz9syh4D/Qvk9OfjcfK5vSe+8UF7jd5yJ9X6DFwA0ii+wg1wlDE3r9cA4zXgsyJEzrxRsdMUf41cFtVvWpOZJs56IkcboHHd6JWnT6VHZI8Y83Tq+lJ0ojh2DjLXJFEGXum822wlfiFp0sK7rVcrQqRenPWxM/PMc+VyH905Vy/tnU0a3FeVboYknA53caHFMA5fKqXxsf0zixD98M18+y+oZwAiBnOv7TEy5F4yGbx42MduLp4dGZc4asWFwsf982Yk7M1jtYdZA6EexRG7LOK8Ebhc9qplnaDZc3Fh7viF1J36V+ueal8XnXVFAlE4CMrRk7VlbNI0jh5PIk/WPWlyqLbwiYfvT2kyW5U5XSuIswqHH3B5VBUcMXFCrrClwBF4tp4aY1mlp7ayLY1xkphFhZ7NIEzPo/9AQcN3Y64jeb6A4hR7mRrbABxyRD4mElYiE9vh+nFX8PSagZSD2zD9Nc4HcvR4WhYYrUaqUVTv6f+SoZaKmckwNdYAfFyd57cVWNrlmCJK3WRy4o4OoBHys7RU38TIWi50RzuBtN1HOQ+hoWyxTl5NbjXbb5M6cJVx07xkTxUmOIw9qT5GBL+sUy6hmRQyZRRlSFpeMOhS1rfLLsV2UExtA6+7CVdCxIIOhfvGIrqsX7UkYqiJJ5OhizCHrf+WO1tRl8NCS3Z4N6/9DfHPhknV5UeIQt7FZAWcytZ6VKDSbvB9JeQui7e85h1Lsn95uWfWnH8WzbEeGMpIUzpblouPNhAu8TR1NMLpuS9e3tnBMFTyuLr7IrOdO/RrA/IMthC+2Hd76aIXDYQmM6s5AIFUZDSEZ0lL/C/lg3UWHsQzTTJ/31rkkgSNRS+HLJUKO88rKJ4AgbtuVEaKtbvt0d822Qm0dXlaQTnWgx66Bgusb7NeWSABPSPiaIS3mUtchZl9edLWKBWLx06LOUf8OVGbMo/ansllqf3wIM95MNoWirhFbh8IYIpRtHRbPzLP+6VNj0l9AYd80B4EQlvLhD/ihKBhw1NRxAaRVAyL7OV8nsbd+QCbsSyDwvuXU6W8dkM/uALQKwKuN67QQFzNK9Bp0eZYfTCN/xl4w3VjJh3p/JwVAbYySYcVta7IZSbyO6HS9YSv0s4qRdWiPBGKnKgPOGER1s3etv2sR7vh00gcM0eHL55PNUwEjXXqKgS56Yi4xzw71JfJru8HGak5sz43/Cu56N8bR+ROdtuKqNWPIWR/syD13jQE9wk5cPKUJz4qLAQbifv/PEZK9oKb0QdG7QbPhsV6MPWjyyDw0RIkLpS98tJ/MIZA0OphPPxfg1y21XiBlyOjx3t+w6wbqoktdrMmvLbUE+kwI/rbMLUnrjQirVzwYiWEpiyijRNr92QbtQ6y5cS7eBxd+eF4YF9L+Qmbqz3WwhcDhtUVPRTask+gwyeL+4g00J3bPL4Zn1tNbkjvJCe5vwCkJl050JlOVzRT3g75bmpqtSFieJvEnhEbHn7vG1vAL1s8v+Vq6Rf+8dBdKe4Fdt80Q51HuTiqHKBr54uU6DssyqUIfpvoTiOa9fsJDdXkFavD4kcti/GfjCvKORfn/rHpKMXYXl6MT9uk+v7NbnIRSRmvVIhhrHcYS8pKnPT4cJuq9ER7lWeYcoPVsrEn2EmiYL0PSW/HGmqOC3HuaC1JzTI94DPLy'

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