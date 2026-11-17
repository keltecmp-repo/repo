# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 308475 ^ 549117
_lx1_1 = len("656cb5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-650680)
_lx3_3 = 512067 * 0
_lx4_4 = 736462 ^ 356334
_K = '02e7f27d3530457fbd2f4a088be839f47807327f8e6c315b97aeaa458b29809d'
_M = 'gRQaoB6RvfusThx0bzV2U8OPH2S6QvcRkwx1ifh5S1bdXVX/XZnsqacaF3A7M3gHmIlIPuxFpxmWWyeA+H9KB9hVWPpby7/+800Q'
_D = '=YfCosQqRh20mGKATm+wdx/CXuc3As8d5hnTZJAwzuHKvfFJmZ53vsY4/WNR16a4A1C1HRQsufGMKDlsWegjtsbVS6cV8c00q2CABINP9f6je4qmR1FNBc6nM/vruO1z+a70qo/LEoDbgnmUWpYEfwTebmn7yiOjvV97VGAkcJj8Y4IquWWMxmy3zJqAZV1NidIDipW+ApkiaDxohvG5odXTP/hMcTPYe+oLg8CHQc+lfMww7hArqB84kMvP0vokWbAObN6lWFoykxP2qbR641HSmmzMo6v2FjTEXp8tKvIdD59IlXoUUMsjh7pU7NKOUZnrRH23EAAV1Tmu9tKNo483d45P5XBz34eON3sCtIxGjFHTYlFjHtbtCKZgopI7Yz+JbfjMpNfZTVAD1YEZn7DyCh7kGPqVka7YvaJyHxi4bC3kgWf4x9e290ImYMH/UT0+ICOV+V6X1P/kO1WWhKdiOpwi1wqXf4fxQenIErTM6PhL4PZERT0HY/j8PaMhQIHU8NuZsTqyZ7E3XVyYn9RFUcqnwauSsF9bJHqeJ/liASW/UdXYXyqBOKGLXsmHVEEwMzmtD8wSG8t5FOhzS/j3YM0UlEmKoqDzNK4nKHa/dZJmTmkb9TNRz6VxEh/yeQh0ODLnyJ/h+x1EIZDy/umjJ88v1aZp/loxRlCEINcUdYenOj0ULUihVT1vur6hIMrmJaqgz5iwW6tfct2xMeuYey173Jk9C3b97n7M+8sDkK9EAOvR5UJrvY8h9tW2LS1Ka89nNGC0pOG4eIi88qbXoFrWJ7Ir9dFoLi7Wwm1mbUMZC4NF1UpEJBs67ySa3Vfn3IphwwTnYVYVS3+c+/KX1tDTNEpeXcpWXF7KEbTGskZxzou+By11rWSLBciaNDX+bdUw1QN1CJ08DUhmrMn1KCEbz+SOU/VzDXUwrU0HNLjPjFBIT2IVkhRp7vO2ZYBI+SFDuR831EoEvb31jOY/TSB+HLgccyz1uFAQ/01lQY49KBRhV6/d0HclvV9ceYTTMk4d9mA3ywQN2lWY7E6YgUjLREL/KRkZtNPFC4aoOq8+WBf5mHLIkH8dos1x9MwEpE/raojyf8lz5R2cKjWOdf4kjIz2VB20Pzm3fido/uCAV0kvoLmKQLgJulYjZPOesh4Q+/cM8wxRG5zaqU7vgGcgc0dHQq4owyHpRhuLs5JZ7br5OPM/EoO1s5NhT9hGJILF4OxId36Sa/387W4i3bLNwjN2nTHrUjScy+ZCdtsGio8Hep7nzxJPwiWTsA9AgLFtB24XCyR/QSW6PgKCFXbHt3Wfl1K29ofzYQqJeL/747kk4XGcdUYDzAf6a8PNU58+fgaSZdEiICNdfKFuppIpHZuiWgDIStLSUz6rLvW6qk5u6dNU8Y8xNjB7mZa5r9Yyno9urp+qz/mlQRRNCfV6JuRHgJ4UhrbzWhMs42TXtY+fHoC+gfNbKRJ1swxKIVrAG6jT9y1MYcezFkbA+9QKW868deK1EqHIeHYqO/6hUTL75g+GHy5h29U0SbdOKX1oevTPXuD+Zn2B7teXEwj0VPWsrlkNM3/YkBWMw4gdA+DlCUcho5KbetbnimyO7/GSp7epgu2amxcrG24glP0zHZjrHS4rhmJs3qqZ56eej91bQgA4wN4yy0DIzL4/U7GXflYhQhKN8tW2lglaEx/HfI6itM6NJk+SgejdxqCrL7D+lEjLMnnXrRvt8rBmjAC0WNILSZRNanioJHnGZ1GVVyLEsXm41YvGtFYY7wy+7hc+PW5C2tf0kz70lcBvhrqDHFOc2waO/RMVLz7EENqQj4HACVVZVupt5PbEgmrFgboKO8Hi6mG+'

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