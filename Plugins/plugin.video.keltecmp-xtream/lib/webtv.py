# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 715968 ^ 443563
_lx1_1 = len("760c3c")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-152506)
_lx3_3 = 747115 * 0
_lx4_4 = 642914 ^ 400298
_K = '65e1f179e23148ad0c5cd51d9316f16df57273ed4e262db7c4d4e196783366f8'
_M = 'JGwyE1W94m5r5wlXsrz3PS9Mk0dZwsoqmRs0DNBmONY3aXgeBbWib2XrUAHmuvAwLBbEFwrAnSyaHToIgmVi0TU6exMOvaBoZOIB'
_D = 'G0EzKfYdEA4FWQn/EsNTGmJaZ9wfDlDHeHBCLoZ2HXxAK7NuqkGfb/f9zGvgdacdRGfErLIvsipewo2uMIpUu2JPi8VnFZVH4+KoVLpQGN3eQ8aX1EV+lMDrViwiW+yt+Htyi272pHN6NuRVkqRQ3gVD+Xdj5lQpJhgJgf4skzOd4NlSzWO0fOZEjVYXVKLmZww7K1Z23jY2j68QW0AM8y9cc+QIqp1UiYFTsWr3E3HmFigOcrT5SkFezUvJJKDNaXfTxjMbXULHlE0qRo44WUt//NzzR3EOWOX2u4+Qnrb4o23lCsTaBrZT4AAiXflN6ztUgsVcWPmbeqCquA75PO0cTiwgDPKvY1fa4mrYyBd93viJqJXmpDX7q+DKZfvOJXVTR9kOuPEsP6iZLmVAwLCXaebvxAtxQNzTJC3YnO4RSLsWM68qHzVdT9ATI3H4+IOerfHHq96ym7wOTGg++KanxBy0D1EcRllkY1fDpJOT2idfhTXRli6pbeqQ7iFtFd9fFepnOKHjjYGsxVKG+5JOk3x3mDf1DX0W1Ws6EMC+dBFFpfa3mDpWE2cY9fwbrBUACyfi71aUMrkCrBV2Ps3zOXFZj0Odfbo41JHdEU41KnT/SP2veKAFTk3LF3KNBwd8OwsmBU9TkXfvtx6MXHrWxIM+6v2uTY5XqnTfxYbZaTpLUzuqTLLIO6eNLvk52oOTRn+DnQcYQ+ykCCKVVe5/LofOrlZ+8EjN69D8Wt0sYDr6diQ3nnppGySfmw/PwusWk0WcIYk0N+MmxvoPTrLu/zS1U2hFfQngggyC9/lPV2aD4lYbIf+sz+Wa+6lDFnPScEQFoOQVvZ7xCafq60mtz/VNXD+VSU08sOc/Su5KLz9+pjmOfiHh/MtufgT6GBW0hXpTgp4SmhV7Id2JK172jzMTFY9Y50/4xz14pDeFU7NjJFEFwO+g89oaIBMXELTKPNab09+EfILj9lfX2ovbH4zYA/RQB+4+/fdfFcRgL5sqVEkDqLN1OIEsRdTOapb+Xe3KwQSsbV+sscTN4wklGWrhQDl0wM0t50vaP9IDRS/YC7GWbzZOWiulyy4ZhIxxOtBMlDeVH3iKVmLkO8jWtJ+BgVtqeOZpPCdlQfHkXJKc+xnd2ocCZzD3CV3gVwLeLVXqbUMfcAqU+MDHVfRl1vV5jfA7n4GF1ICc41pCkUHAMcA1VFaOG8099ez78bvyqFZMzCnYBMMuEhPbGOpFKW/R1MqE00eX9ue8LpwJqR/R+T0U2xMebbBmYyxXmNJupMgyorxK/hBepBmPAVQxACG/w5BGNEUeBlx3UtZcGNXoDfpS9VTW7YYYjGdqTwVd5Ebs+i3I/t8AsGZHCD+876BADLQsfTnAFbh8UBcGKALiXLSVqPy6lNqG9UH63KEimlSahp/Wm1acgHv3NFz5X6DU3nlgbq3BbDbe8zSHp2mOCSr8ZMoc3kZXdRqUIT1PUmAs/tMczdaLym5cyvURWcebLCx9tUv2IzX0bWB6vKMBZcrbCaU3RBvCsCtmvIoSgm4AbpbQsX+5Hb/QfPyuoY4yzXFls9GBNsmxaZzgrdnnOal/NgrT58cNf+wvekj3TapSAziA2cBwjHJZEwlJsUyT/wl+KQFgjrwWbhs3oJTA+uPwRLL8NyuOREe9scqoi0BkFSJb+l5fb6Wnr6B62v03JM9hHNhD0aEnfxnc+zpx+dlONOwxityGv2Ervoy4oTbR5LxGz60VOmKE89Dxn06s8iK6VrVFh/zXITVC5IqEciGKTIktrQ87Tg3EUmAm9dotQLzVhJwh8vpAG78/Ts27WekGXlqOGET59NldbM3d65YueLvg'

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