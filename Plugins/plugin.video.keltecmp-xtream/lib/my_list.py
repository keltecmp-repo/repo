# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 329527 ^ 263675
_lx1_1 = len("63d2e0")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-391569)
_lx3_3 = 148165 * 0
_lx4_4 = 578159 ^ 131999
_K = '89b35226e92e90ee584322467d09cc7231826dfa4304fb2b88c8a1fb75311021'
_M = 'LKVitcWioyyA8w=='
_D = '==Q49qyGqNblaD0XO2xf4faBywEMHsp3OZ65NnRfnXJzCT5zVQ6skORKj/4qhRb0c9LeSyXC/S7w0tmid1RlhzXOw4pXohOLwAkzkiahGA1URssTjV3/qcF2392sKAGyKEyPrZfVdPNehjPjD4cijGeXM+7w6CSM9ldWJAWEnVe/CSpR5o7OVSfPAcrnpep+8VMDX2DO9eXRiawOO9JnPOleF+1Q2c8r+wixBxyf7hiNQsP8s8WjQxf8FgS6zvx1EKgCF1yMuzD2xSrzv/CZhvum4QkNrJv4mTI+9R7vuWAaM1WyI4QRidZSkLg8PT7orhRGdZ0PTsBRZk8Q4ex+zB7BJE2vqlP8EIX0bxzqmhegDGuBojY9EZIpbEsLbtlAL05gbgL4ot4U+x6ScKKSzVbu0m3snzpwyTLhgrVsLVX7X9C4/Hsbz2I+yUxCFgdWRyYkzsLsi7FCJYnqAXfPjGU9PNVyClePOkDNGAFRf9w8WtciD8i++MuE9DokQAl2dNczYRRExm+PRb4v4wVh95IziCiQ097zJLOnLtIMqJQnL0P4IMbkj2bo5z4Ytf2WDARoBjh8VoAnc6sCR21EGVut2aZT6cYEpHT211IaGvpuv+bSeTLr2+cS5QA89lno3WTCQsRdUvVZS7f1DNxFpY6rN8G+iUNN9tJAiYukYQmXHEC6t+x1YU0fLMQ6S40sVVGngTNS36TW9PT00ACjX/N09cjbBHyI4ExPMqyfhjptMAy6a7v54ZXazbeyssAsC0Aumz634LXCmm+Zag1CkYF0W2zSFfASLenvdmY36cKGJ8w/qShcc0ywQ8crrEndYAwa7iXqCFiMkleOyjQwOcR+5eciz6bGsJd5Pvi4A//y0fdv8aKaINtDK5xCGyROiBW+1O5JE0voZQ+bBK3si32Qt7TiWeAHzE0T0itMBKB5ZeXTdo+seA9hJgXfxVUKufufp9Bi1d3C3QF0s3FEz79IfVSr91iHR5OPCG5AqYKJ5iQm+oBNiTm+GiTytIgvh1lJcu5jAzKRgeOBNkLM4LPubnWXGBtZ7VL3rnWdGGXFOeObFw99lQd29oCmlCbS6wdrrikH1mfimOevDdPHmG9HqiwAoUeamugHpXSDB6rawjiR3qI84f8Bhc8Lr62qf5g2IdMaeHh0SByWfASXZXnimOkEo4dEg4QQskVQ6EQchSVqU5Mk2YR31kbBw63xAtX3ooeXF9SopJ0iu/TLS2YEG/c4Ls/kEuze2IHyJiLIkGkSO0dohwY6OoIxgfL9YDNLbLAcbnZvs0ck06j5VjLwiQCUNeWDIioLjxvjce5NAJVJo139XS4LabYMamKUenSae3JBiDI7z1Ss7FDY/hk0Dqg9iqibDv4Tx7IAQkMCUln2RMD5CMmJwnq/yWEw1TI6D7j5eZr7bP8gssnLWEVcXMi587gMpoGTPN08nb2mV2yoCyT6ui0miKEBp7aYlxu75sxwF6di/ku/2tS+Dfpcd4BFm/bDuXek/9LFYf9wKv8GN2JZ5CcswiX7Zw33+TCSoTHqGsj3QSiBkLHBvdTDeeuBToAzWM4cufEQ4yPd6R3EVOR1+KBYCli0GK/9DO3jcV4aQgJ13GOtHHvtkerI+8/Kqd6p/3bSSHGTnx0TOzugttqEu2aP2oHiap22lyk4pwkvi0OFTDxlDB2GgCOdJR9bvCtnCVnZqEz3Yg5apq2eDAsemak/wOl988lmS8JwFk9Ir7Afd7LLu03q+WY1ayfxbMrs+StU1biymaRozXa5Gm23YZFoju96GHE1kXFa1RUCAUKsEJFtI9ypKqgCgb/a5JLgK5dGRtI9'

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
