# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 437330 ^ 859898
_lx1_1 = len("e209ea")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-750818)
_lx3_3 = 903524 * 0
_lx4_4 = 389398 ^ 674632
_K = '59b923da8c33a3c36c50e0689f1e1732dbcd9bb5c5f32a7df7a548e49c9837ed'
_M = 'H7xgQ5O79Vz3dBz8IH8vaEObd/j1aQaJs3ciKknmps1E72ZB3P6mRvUiE/Ihdns9GJ4p/fVkVI7kdCV5GrX+mhbgaE3S/6UX/3JF'
_D = 'sHmB/dDFHvmt8JcsYtcqUxDypK+pFXz/6vPB/l7UB376lfa4DxMGli/G0MJHPBsVmosBsvts31ckzKmF9PVqremAgjHZ47M4dZM8HdHjKbLvFqOHeZJv1Y9ynBDrebGKi4uVYrEkUXGI35S110OTgZ7StKWPwdR8tcSBAOJt2n7omACaZDYL7Smd1hnIDnOSaCjvB3rKx3k/gMxfCUyvVWzwYfwKFRy1Ebx7QveRGEXDlwGe65LGkGOcmaSgFd1uF1Zbp8gDp5c99KnE/jA5A7NcBhexeyBm7EreY1wzJnTmq1QezRaLVoJg8f2jVala6CfnwIlwkbnjCrBcXR3dh6VCCw4uqZYD0VCBYF3aQPAa2zZ0gYbyNovMBLbatgU/+PM7tsqoCci/19e3a5vIefmZnU3N08I56/INd7PlJfNM84y3kUwFmSYuFK/cx9SANO4Rd/do1vJJ5cb1CRaTsgF9w+0ZvpviQUk+92bRJMq8w5PTsZqpDNnyRIQ05RoyrZW6lOZ+RqMEvtslT07I8jgOwOm/Ivd575YlAzGYEacMtOO4NT3ffPU0A3CRWxbOFBFFRMmrNt2JGFkm2EA/0P4Usi4XzYsoYQf7Qp2Rs9JSViFVAbQbbn2htH4b7Re2hu++AtE5dzQHYRqd5PHARLwtygjbdcjqivQK1+n3h2nLomWr3VN1mxgQkU9o++ncGUnRjCDsKeqZvtvAChi1jIcK2AqH27Sb9IE6sB8xCA2Xb9WZqvZ5LmyxPAqI1UiBf6z1kxY6tSQQT80H3cjlTYV5rc+NsGVkdXyUGSl5brYPVL+unfvL0r19alOwTc3N2Gi/r6sKB1uLk/wa2BDKJDKxBl0MgdLCGisxAVP7AOEDzmY1pRvdckg1WlM54lxzPqQaUYcDhz2vmpLMAFf23CvIlxM3yiTbG4HVJA1tZrNxpahUpRTZGB92LIs0G/odTrKEVew8r4etscOH8mCtuNN5JswuTaY0K8yMVnHbKSoaAioGmmLp74eST4ZbApYkO1O0P0EnpABuMf6YF44d5zpqnD0XtDhpQhYNszuPdmU4uvoYA1SzYnonBlOqRwa8EuzRAW2EITQ99Ri9FFaAex75LAlJ0BG62GsgM3wLA5k7CnwzGN2BPo5q5rqirnLkCAkO6rpXG0arpqsNWsPw9TZVTozc212oXSmTZuURQ6ntcgRLO8B3V89uoE3qrRApL/jC6tW/CynFtX3dLbOm2wswCXfirJVv2EBThnIYPZRSHR4Qj1H8drCjsuT2zPzd+tDDz4CXLXh0GtxODGv5I0UAvluo+VL0t+mWYe22CjmFWoLwUCwdHCq653rSob3MW4TVBgK4FkRnX8zOf6V2DLDBlJf1excea2NPKxPhYPUbipQ5EXMo1gq+FdpLtaCm01/IO4w+xmgbRRcluiLyFw/pAsv3fBtJa7kd3c8QTS6P1e86DVipXrmRoWy9jD6IUVHSG+2Lp7DVvuycLsaiXJWZMLo+Ol0m29585vrPiBNS9KWzazKECxDpS9b8m0gYtUsdCatqPGKA6czPHsx1Iqfk/wMvTyjtwLedxR3Gr1MbritpQlcqN1Zzts4/RG/PGAI23kSDZpbq49juoYySf0HaJxm1Pr0+1+q8ENJo/e8aOvnUBTKx'

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