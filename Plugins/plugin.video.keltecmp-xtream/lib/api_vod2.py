# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 149790 ^ 123592
_lx1_1 = len("f32a54")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-475428)
_lx3_3 = 675007 * 0
_lx4_4 = 969903 ^ 387303
_K = '8b44dfbd882148af51b8851379d1817c58f91e2a478b3542305ae0ba256296f3'
_M = 'XZCCclpalj5RBXdUD61YAGLj4EFf5Hp+ExtucRGYDpYNxdI5AAXDKVlRelMGogkFNLDnGwjnKi8QHjtzQMgNlF+S2j4PBZZyU1J0'
_D = 'nhv0KZTB0GCoWjUQTgBKHy3DncKxbfgVhrpEB/Jozi17u1DR4d4zIn6QJBl96YVr6ScPaOdgE3YOehsnlpzrG1LLPRjAyvay8ZOGwf4dsc3Xzw3oIgfN0CqhUpTmRL+146A27VAN3ntBEi/XXBFvtRZ6dyDyRLA+6viQuNAz/yHoH6T2z605FsG6HfZAMdFmRFj+NonRKWq68X8QtTmHT4SFLE/+1NzYtAdkYYooUR9Flpj+aEY/913+/4DgDNrP1Vy2PbX8twadiyzy/xPNBw7vA1xUp650ZZ/IT3BQazKCwp3rntJwqFInzII36oaf/pHIITMzcJhzak8g/YSetkoxGqCrvNzqnsFuAW56/lmvtweYuJ6J2Qg7a6V2xsb1Jr0wSzOA9HqvxJDcvidFl2dG4sCdz4aQ0oaRw1tq1EjgwI5SixkDznSilTH7sZmk2p+oTP96kaWA2mb9Pk1WNYWmnk7tVph64dlNWNZqwf/xZ848b5uWyCvp67Qu3dJ0HzjKxQnLB3QFF5L2JLNJr2Aw7Ai8+sTKwYx/prWFyaGf+tk8HlALWmihueDBuLl4/zsJ8zZRNzPpo7+OCpU9renXgElnlWBEbDFmSN8Lg1H+7CLjX3U+hYDKJvlVdIoGRAJJtJ5yM5XvfIzzzzHxvgLdCg8lF7I+dWlvGjfmjomJaKD9eRSGeUz/GIOkr+bhUjRVZEJbITRb4nFwzPQzXTQIAaq+6EMwe0XLRTyzS6RGdgxa/ssxP6xLlL0MIi9xSApjEIqjn355KZI8i7X2ZP4xB8QmFMRoslD4da+1oLn0gpmKszgzA92vuShXWPPaPYXg2fqiBs/fqvL7VrLAntOVtPl1momLieM8wDCE0dFGhqCa/Dp0CPXZqTVTGfS1xSNds62pLtnw0Wif2lzoi96hEQV8/lhPMMo/k+j0jSDxPXcWI31Wfpr1Ximy5ftPpjFfy3xc/L1qQbmr1R1Bk6AQDrXPw3iKFymUuXhVPqtW6tKq4LLzoDeYll6NHpzw5LiYo/ztDxXfOfEOQPQTFzZmte3nqNftgKX+72suEtql4inXXpas9r0WkNLZ1mmWyGwOoUzDxOFiXdDuCgD/AYMdN36b1jDPdZOXRiG14umBAGFuqdWo9BuPy6p3iympBEpxxhUKZkenqolQKmlsmJJxX1Eb/mq3ACGZ9tFQvno+UQLJdcppsPf01pLNROXIlaxwOZOqUYSRd+VkSiQLlktwLJOZ9XIOCV2l3dfhAVZLsWjZKXkX5NHJ83wlTmmYGy3hjlvYaNE0QuvdlQBKdMdgFw+PLvSVCzZhSzOOBJmXptqq7DdkWbX05hbDtQuvIhVXYaCCPPFeOa2uLTW0QCvwaPcmTdO0zBNBAmWNFxbgC8dFkzY5/dNSmPadyuvCT8IC0XKkolQXPlcx2MiQvQcREETDItRXmXn4t5E6r/GrAnd5vrQABse1IlT1Ar4nw0Crf82bXViPa6mWP0LTTroxlB/OnaaYV4Fg4bYqVAF+VtuKqyS0Kbd8Fah1LV0WmO8pb22awM1FN9LEgwlL0rTeXIj0Ydakyoz0rB7IoqsoPLGghdUzW97kA4phAHY4E8ZbyWuxJDsOTV+FDoKqlH0nECGCw3VOEAtIUKjDEfuNggD+'

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