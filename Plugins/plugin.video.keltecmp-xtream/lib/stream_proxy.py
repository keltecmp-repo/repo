# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 974040 ^ 587994
_lx1_1 = len("9e7b06")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-879140)
_lx3_3 = 565837 * 0
_lx4_4 = 948911 ^ 328382
_K = '61492ff12c4be4f2fc0675fdcb8fa79f3e4d32c0b389d28ef348adf0d584d947'
_M = '59EpwjHWi179Gg=='
_D = 'sr/tP0mhoPx2c72OMhaNLH57x2uTYHUciN4CLx0ZRGJUay0DmNHrnSeQK4xHkkSv5WPIBgT4W1UAAiKNtAKxzEgUILHrTexO5Vu5grGS9sJ3l8Y5s/G42Ksu1hInKtOm9r+inyhM9axrqaF3LeQ+a+5dCmJ09Ir6JVmiuOQlMMwT2YCFuQXl0TLQWynqkHkRCToI+TDzYDLnWQtrSk5KPLiL29rh07nZRKoluP4P1qVxdMAbysNETDpPSyFhF+lfff7OFveiKQMpVI7JPXJO95nsQf2iTDmulAAClqEmKsHRL4wkrFWyJm2G/a2gAMmruCxEhr8He+fJMfvnuyIw1YAj9VSdC9yltAHbZmwALR3/mau+kLhVYe2Hf3iY46Anhq77BVqeZ/lyz73aO0Qehb0XKj/u+Mh0qLgT8DQnawxq24ol+uz6TsaihBIsdq4HGhVLtDC7rLTWgtCS7dDjvaSXcDOGwjLwDckwY4Ka2J9WH/c34pqLlPAs3x+Af1KVDomARryEZYX28jcQ93RPNUP6VQcaNAhtFDSTH++rEWLh8Ufq3Jpy4iTf5FVx73aK9P0NAtSWGQuEytuPwv+GDEdFHpVvbiRYx2uQ/dMjJba6c765qAf9KuzclddFZkK16seQExERLoytlAB+mtROUeOpLPAMq7FWZ1Buivpf/tKqUK0azCnYtFgiwMQX6HdcSiwChplc0J7xxEiOhWvwjqnRs4lHggyTHJY2/dC1742JPnU7tJ1VfMQzGlAXbE0gJlK5V/l/3m7DykyerXDX6tMrfUJCeeAOYpMENEJkeTBzABAbhZSv3Ke6AQm1ghGRI7oKox91+1XctgUr4r9uPWyauE8Oeax7tgGGTh5pQ3+CzT2cePWhpIlRHkNB8+B/Kq7sGmr3DyApqlRhIT9cTDRBYy5P1Kl/kKIcZYVvamwOGIPSR//NjFeQVwHi5HfWyb0gTJAVRBN2rw6m+dNsJbEpY8ektw6zkp9CEWO5+9qbILRzZDxmfCsKywNOmW+p2vlmO1jbq2DqNbYo6NbZMKqjXl5vyaKibAfOc7wM+arDEG3kQgLN27xg4qchipwYmen5AXrFKB/Hjr7QOl2mg3vVAoLDoRCxXJSG9gqfssUk1uqn2JUF9CI/McJFaTq010d5hMr1butEgrgNK+8apNEeciE0fXyDjBMTr+Ojx4pfEsVcqKgWTSQmVoDumne0P/VraidU6tcXCSBCkRxzYg1bHy90dkId13Qm9JHMrGEsdRHS00gMNTKnyE/i/TuATrqUa0TkTiO3+3gm1HvyP/euGcDX7ZE3fBZIMhS5Tkb7VLaHad9HJC0o3nWbFn11OXN4Osp8qdeVSS9DOx/RdDqx6ZfBRWIgYeZgXvLFtiR5rkxeNGD/awwqM1ze3aX7TDHV8+tU3BWyTYbm2is6DyFenGHG2cyCMpnbX/s40KD3+SB+6nfTP9JS7/13dX1saAZxLhhZ/OZC7HvYCqf5tSWapZDFR9wgL+qkvWiDWzl7badwr46A5iwF1VzfWkdrSIHfd/8vfT6thMrOX7Ve6+6iRdt/t93TjIiu3pg73++/8ZY13RTNK/yafHy4USaM1+H6TKELdsSC61Y6a7Mym7YfhRljKzVUezohs3eM5byWiZMjNN1wnTZLKftuNToLmKVJS2vZXHhXE4fs/98uJktJwRFSzFZ9bdctoA/tvK+3b84kOvwUwpW8i+ppC4FWEkLnrSYUxYeBrF1zozXKd6gCuE3tqsNZXfOcmILzVUELA2VtgqKJr73lPsVrYrGgOmpGLwVZIbSvj7agpS8oWM3y0Dtv4tPfO8CP6ZIu'

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
