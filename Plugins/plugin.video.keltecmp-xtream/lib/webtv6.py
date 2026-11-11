# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 692769 ^ 400589
_lx1_1 = len("7d7aaa")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-990653)
_lx3_3 = 618206 * 0
_lx4_4 = 237058 ^ 634934
_K = 'd6c7a74019727f2225bd3428e8299ad7d26440fe6551d8cb5ffaf53e1c37257e'
_M = 'UbHjXtCBD7m0pBwzzh7X7kJBGvbmjoJXnZd0n/tzLxYKuKpAitsNvrygQ2CSRYTuRUUfqrLagVmXxC7LrnMrFwy5/B2O0l+8vKdH'
_D = 'rCp2d6XOB7iru/2XP0eihb6Ku0tnW+nPUY9wun2c02yczYd/8tISDERbPmdK9O2voGLdR/iZvkgRIf2ZKpuLJ779aps20ex02SV57Ljf/nZGqCcIqDdGJrmqqwY2VX9MwG3Qit3rcaUJ8QV1oy1K5WSKUnSTT8msqwQZ3/vaVXdd7vSrwUfSkxxMkDunpwFHGLDg433qgyMyP/NpWyYeTB7MwHsRlOE9SWTNJXtdwLMum+csUwMg5b7K1NDHeeVRAJcM5KTqRx4kPK/i32lv9mkgmtfF/1cAtcfiU/AkOw600Ysrk9o7Ga7YP0zNgEIC+ZRqV3VlBhZlUKJMpDVPVUuj7gfUSjOx6DKbsXpfrS3XB9evctyHRVwxcQ3U1rtmKcdyfAp5PqLqOKj0kiy7GRVckWdFgyiC/6KSIUWfk0BQ+g5UumU0wgNUQxk3DQCF9NQY6LtHeMFVh1JvGfBcWJX+VGA92xV0Ax3+adcI2bLVkiRER3FseivmAIr5ycR0Fcmlw3TQJb11zOHYCzcloh80UcS7eZArJFgOJiCDi4TV8ej+R+eS5QyA59iphAbC6/6VlfPVRVYH4TDU0YH9gRO4h6A0WX4x1QTfra2YqTkf5Bwswusx95rzCBFvNPHTC/0+ay03/TorupfxEM+ipZjk+y+afXm/XT9rhlY395BjbiL3xiCfMvMr1liPzyX9+TCkzEymaRZGg/dcckQ0amuXd19+cMngx8HP3MjepvOK1wE9loh8g7E/DeZiE0fwA/PtmgKBRVd6V6zf7KHBekU02N7f2mFOqLEJuFcoKIq4TvdEkdys+eRoqnaMzJIcu5CSCXFQQ+wketqIgOeHZ42Bj9q/kxr/VJ0WMkjccMOKOJaMZnC/NEUZojFvzzVwXgoBc8VxL0Q591gvtekjAQhrhbIbmUav2zx6y+KmkxXSGmgTcmQVhq/LM1tvR+ZIWFN7w0b/kzu3JSrpbvf4sxC7TA76hOyDjKquCjGTQDI3cFqWaErwC7sC/ps0zdNWAJ5GAC6Z7C3sSomr3zcRLkQFEVb8rLkRJiR9RRsiY2byV17bvJJpl7QQC+NreyWPk0537d09dG1bsL8aFjUrnUxkrcQG3dmGNbQCq8F5kHlJt62qmIQRxn7LWg976vOWOIw/FNdRp985MVHqBl9w+3RM3umwad5gsxt8Qj+Kv5rYGTVgpPGOzy1jksoGIdOU2V7dCbsMomaU+Q5pk6JiRFYr8vNVErM6KtSes4nFKezTaAeAtLxaXYqFiiVUg9ewvyRIwNwG2PJWyHjh4aBPIS0HSv5abiMnksvnCm5S5wBXsgOenazQujbBLD60EkVCG+tQU+sRGgSH3p09XDVW9mgA/3ei2CKziwoEQbU8lKKUxoZiuEfYQB7IaKm3J0itFNcHsmcxr7/pE0UY2vjQhl/PnpqYKB2V8l/qiXpo/OnkJb9WuyRoRKH0VwpnE+bP6BUq3JxjzBdMARtF6GrV/cQqbmq/6s9qG1hp3iPWOuDA1TphFOO5ln3mEtBB79xUlTJjd+UKbtGA1bDHUR1rrKjLmVJByxZMaHMfsaSbSnxSPWs5g8+CXair83/+IqRhI6ex5CWO71gXmRmrCSpemw6beAn0Sl8V+kfV/7VhCSWvLnYkqSnkDthd6vDyYF2dG+tKytPt89GS+5Ec3EMq5a/St7Gvf7B9Eeh24LZutG/g'

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