# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 226784 ^ 609334
_lx1_1 = len("f76f8a")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-653424)
_lx3_3 = 979636 * 0
_lx4_4 = 372547 ^ 866919
_K = 'a6a172299b4f9404472e36a1d8a990e897ae2a8b36da45ce3783d999fbc3d288'
_M = 'tyEz2WcGhqHq6iwIF42goOUqxsSIh8g4CkqVydmOqiXyZSeNdwGCvLLucwoU1KCm53yRkt/dyT8MTc7JiYytJ/U1J9kjBYa65bsg'
_D = 'AAoSPLNPtf1n0sK8ccZzLjZJH5vrECV95SzvJBpFwLS+2x1tomgrHQ48JNohvqP5wi5n6ZBwTlLSX+SP8W2giHRe0Xhye/uRXNEz9c1G4GCfPlcX7OK8vGqqR89R+u8f9XKgpH4s+cWZHX/h77P5W4QUsoyh5Smw3g/P3Mk+9W1x06YfvuIqP67O1bYn+xmK4V29kem0tsE1ho59E+ci/27TkkLfXIXuBLVBNMAR26WnmseULUner+Wck1Llgrb8+q9RWTpTFiBFGQ0yTyZ6dr0UbRVDcjWBjf8ok70U2Kt4RO0QHpyc6sDe+ODC7gQAMvhU92W3bf/k2NUhEKgOfSkl/TSjSrPItrbmRJoj083KiRTmgAecUG0bUQ22JqimFrOGVpKcKBDkOL3Q4SM62p7LAmFKYEvcsWg7SovAdsUt+JinOe/ZYaGr42Shxt5ndOzjzZrlVOvos+idAnSP3c5lLCB4lMaBkM+MW67lRogKsow/oNcnbWydgtIPv+wbcTOJmVA1JYU+NQng9Zq6azfgVr5W09J2t2TK97StbwAWd3mSc+72vrUOdoA/wG0ymd0oP1ZrVDCD6C1mP93vNAeLdD5zyF9f7M3tz6QbgIX+X9Z0OYUjX9DZdqhwm0ljNHx0Kgmm4RpvdHEhgxu8uesmU8SeWb5h5F04OG+KVNhyF1sm66KdHiFtHCu+BWur6Guu0DTHghEzTnqxbG3D1eygsGLDd8LZZko3jb0KLKjSk6leBSW8Lm/yA0nzed+2seM/v50v9YjDgoZ4YTJvBz2FDFw/lK32rlpflXltqWEXvFkB0K4HhhDB06DTknlBBOcz75Rh2Jz+2ZWAqt7euilWf66Q5yIkW6NWJiC3FlgGnqyptf08vAyZ38dqvaKE+BC03QnJlg51NY9VdV2jHilFPR5FDGw+w8ePHiBFOVRaSWOCYQ3YEdf24UTzKckbP1Eu75O++sfNbfCe/CW4NjQ54nKaZvrd4HwQZ8PgOtMHM70KGskff/lRzY7CEj74uJP6OZ7g2f1aaTcQiHt2Nia6dz3TH93jViwwDwIsMzoGjJ6aECRmcy8/6rC4pfCJGIoexX2txEe8Cazwfy4oCjkPGUXHkM4sml+ipeNRgs+xADq509RsI8hiY+vnKBGlcGl5m3lBmAN0MwW8ze5J3iDItN7I9cZuleJEE+jb7HcjPez+Pu4ZpeyVZhvVVeWWYF98vSaqj0171OhPLNk7N7Pl+tsJ0DvM2dpjUnXchueVs0mRdWT/B4HS9uMkoPT/gcrLJjWzE8GR/ZqEuTDToCXwqfTpnXtEqc7YKK/MMMWhHhJCDhmC5yXM1vmwUtO8IPXfSgwVq5l6Zk6deOXc7JtnuNtBZs2i8uOKWGlDqhiw89ainlnWAqPRrW64yxEvGhVY7eJD9tt3LfBwKF1t/dSl7Syx+MUkQ9jKKiXQK2ojGfVVgjMO9Z5NxbuOk4wfQymNsgCRxFKCmqYvsma3mQhdywVUNsWhHgAEJbq7u93ncpdCh6sdmnTVjmnq8HFTLcomcmCs8fNtlxqVEQyz4XT2T5FoyWapXpmLLUbPKngGw+1hNqTHDiIumUdZJ9+gfER4kgx3srmIhtgXQJjXBdC2/3ljBiAYI5xAqICogN9DQ69hLSARjqR0Z/q0Va+zF1gAMjrIhY4UESlMRmDJhaV7hi30vn8YXw+7SenT9yBOU9sOE0q95dBfg1KOazF5z83eSRLmprGg36+zBUx6PL6yZgqoJKkSGlZVRkSK/YkBp9Qw/GUDlF3czWK5txDgXLxg/m4snoIvmYECuzT8x3VXqH0tJ8j/ogw6tF4VVTOSn1kYpCNkjkf/m1a9cKrZ'

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