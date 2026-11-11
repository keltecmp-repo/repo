# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 362775 ^ 182911
_lx1_1 = len("8ab3a9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-292805)
_lx3_3 = 897389 * 0
_lx4_4 = 577998 ^ 505546
_K = 'df3c307ee9ee0e7e1192cd571bfbe7373703ab19882d1360fcf8b4f9f02f1587'
_M = '5KzB0cXNymzbajebQRjYWBAwetgBHrokHFxK1ITSG72/rpCAx47GMtJmO80RTYoKRzd8jVEd7XtMXRrf1NtO7Lr9lYaSiMsz1mY+'
_D = 'XuKI1Bn9AG+vKMeKz8R/a4aPP1kkdyd8HM2Ts4Qnt+a/3ZJJahfXzFaOT1b1V/9usKsIu0GniDc/bG70i4DxyAEDdwamZvZAdjY5uTJqeeCvLMF6fSElc93lkbPjQwaIgeCQWIeLu3X8AkMCbf7Ufg0vLjE5jGAVJCv6oAFRc/kYEl/0/6856pu6Z31t3HvKJi80T+hhNzzmgXl5PP/zA9xSKsExyID5Y1Mc15gmx2kb8CAy4bSIg8AalKVG62eUahHQtTepT3E/ZMqEwSE3M2GcJ/xe8K+ZAReWuhS8bHfuJIwQEZC0eUlmcsFxOJgyicCqDYBnz60Q4f/rVh8I2hUaxsooh99LqUs8JWCqLGK74c9u0JSi/EzDUcTtwjpyAA1rBZGNn9R8aUawtH3J8BZXnwIVe2VP5BOWUMCsozGz9C2tI7qUCjUwJHaiig1vi2W16y33FUD+fsR4DoFD4NxmvYDLoMAfuMUbQGhI+UVGM3QgdG5FJOZj4rlsqjzoQuDaF07G9JVFDZ6DpmgRz+Q2qtmjQODcPJavtumLal7QTfWm8cMb+NUdizYdq5WHEDZ1Pn9r29D9kTXwTJhRGfu0Qaq8ZTpCE6MLkJonlO1yTUmhETQBOh4+sIPnpM1JJ5J5RQnhu9SMSOP+STOHsdBp9lhtgOPRGBkj4LtiI7JfUnm9YyUQsYYjNwquI8NL5vh1bfW1n8K8qkGzzITSYpjMD8MC9IukrBI9WPZI22WVgb8HFawqfMtc+js8qE6DzNdg7E1WQ1RHmrFJ+LFY04iM95kgY95/w2MAkSyOjnhhws/iwNr2QTFR3E1kVIQxGpvOIx1Zq5DN6hvnnGjm3KwbGsqYFRX07EyKlKOqSFX8MMeWFYNOa++ygkk8wB5GCog9Lm/mx8/ed/EThVYI/HgGH4Qo9DrcSop6/9wyL36jZRjfdSgcydehiSZj2vM0l9rQn3TM6W6MyzL8esQQ2wIlYcuZQxbUgatgJOaz2ym72HrthvoMRHuzyeGcxbkUxhGq/xj8be7eBmOVjCxvhXvJbP9t1vVSaTuIiJD5/dZvl46PIW+ibbJozPnw5Sab6li5LOJRzVG4Lts4J+c8mWNEvk+TBfTidui+kA6H8e8UPP4GvlT2+OC35Au2nDbxJXi9FjaRgKBwlGv/QRvx8aFDG7ZMOEytTVwfXlVov+uUEPNWVK2buAMAV5J5e92RkV58UdrkWq/tTKi1Ewe62lGbZ46hYCNuE1TEUzoJiIHxwxe+hS+FuZz4x8mU/oyuZJFgUd9eItFeruvI2JFH/OwbIjJWsF/fovtG/FV9vyKU6UXidLjVkAp9fxJs8EKHx+gitIWdh34ztJ+Tc5tCoOhujUNgDXilbgd3tZCiHvBsdQH/8gQ4eoAekbMq8waz5ApWcS5E10Jkq6vjnMxnob4vNRSw9EcG8mfUrIphgOwnVFlXF34Pdmp96/q0/NwzdNOMlK0lXC9qbdEnFeqdix6LEti58cJgX+MlghlB5Pmkpx5UWx3tIMnVaxt/0mubxBZtMUjHpkaKaRb9XOWzPVkXIo11dUSlRMDrsaEa2CB9/EGpycU7XfPH5wxW/rG9tY/xngqb0ww7eqquWXcK25knhki+DPbgvcQ4cHi+AAAJNfJyX18FDy03Nn3dmRI/I/2JBVY/MvT1fQhH33Foi5ADM2G8EfrFZTwlAi3Od/XICr1VyakIQLEC610qw30L7ik7YwsNggyGPp078I5cQx0J7W8UdkBJ3AP35W+NA/7ftwnupmbssysDF830e6V7AAbvwBvUyGwRc/yE9ESc4b/5+GtsX5MRah8dTbnEtpVEHhAqCsJt'

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