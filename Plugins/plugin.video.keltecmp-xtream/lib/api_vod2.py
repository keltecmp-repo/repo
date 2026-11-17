# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 169870 ^ 211367
_lx1_1 = len("eb0693")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-882972)
_lx3_3 = 907074 * 0
_lx4_4 = 763141 ^ 438338
_K = '1b58ba70edb2f0a78516a1b71dca7334f6d7d2bf8d6cf8a3d7a7f382697c85da'
_M = 'qZsZCT5lnoqjP7JfTEsN4kP3Ss/bgATUPzfL/c8LtjmhkUVTamnJyfo4ugRMTFixR/VJntmAV9I9Z86vmwzjNa+WGVI/M52coT7r'
_D = 'X4N5qRZCq4Oqfrsnw4CXAfP2Jc/+UlSbnp7HRcSWN6q+2lLHPiFRHLcsHEq7O+sXfhSxQ/vXOiLV1pIX3EOKuMcay8I8K8LMu1DRTNLvhzIR+FKSBWJTp8nugvmse4B04tQz0msWDsTMqQnTnwigqBakKSPvFtNIxSfZAsTZdKO47aqRO2mLSOeCpYXfAYcub/y6yJBo67Ku//CNC69U8cekiwNEIZ7+fHYDvpGbUZTlPlzO3zatILbhMSH9oEkVr7x5a2i+YEPz+XvA6KMsKotrp38esEOvIu8wBInd0I+wcknARWM2QWWgUIGNySVjicVPdDrfVHcd3UPcgX5J9LyQqmNxrGlLTKxgR1JRpDdygdMl1eibhlAr1CdZdrUt+qszg9zBbUyXGa9PWpPBrnRzLsKgFdpVZ2bEke1bLLbETGSGGo6nUZODzcLrtSK2nJo2+pc6BQwVFIMFhgJqo/O7G2LsQhULwF++I6SJJU4m2yzl/Px5fUI3vR0qnMETia3cTTHtsIHZGVTgOM8RfrxFq8eFRbVdf5YgyBpOFEH36601HSN5onvgBqUsbAejkI9JJ/rcFHtJ7EyI2BadV/gOYdH6CdozPT15wRBM05arfVZlJ1Ty+aPeuhdFeQG5WcD1Net5m++DzVubBL0yuGZL1bX1zvLBqcTD+dTLZ2SgdPLgwgLoGcxSoHKP2JR7Kz+Pv1Sit1+uhjLjEIYqAzgFieHwZ+gjDH8tXXVb/AG/VM+LbPBdH/7anJoTSGCyKqaGGMcViNKMUTubxx8ESeZiNDfxWBbM2zqrrqShMTMfVwvOcfKLvoxC7d6jJqfCLcotft0qAPbxutocmgR68Yff3slclRhP+T11QbuY17D9h+wvHwDdSUbJIe3afliad+vLnf5I2FuozW3iqKQMJvbFPgpLU7d3iaYNSqJXMUXGA1azWWYLCwZf7zHy+4z7oO42OiNcGt1qAQXtTfqt7pJvsEfFrp14HxZHS+b4hOr9irWXGmiadAN0Bp+guldJMHreDri4tsB/Y5bdhPbzRPkOWeLwJYkP6AQFqwFlwCP41+OUX9pt5DuzB2nab07seSlTPHzNNn+th0DvaGnJu6QIIxCM93OxDjl3J2ZjICcwgmvJby39n4T7j8ZwHnbvzcvp2HugvTQOgkKozs1P6RfhB3eWywYrjzGhRf6S/id3nyAZ5bf7BE1XWooxVu76gkOf4GxtV/DOKf+YamQEqvTozepF85fRsxcC7k7i1OUQcwn1wjC5d4GCBfwPgHXJcOzS2R8X8QBf508XgOyfPKc4gKQv2Rv685/RZ6245iJ7LvTrnyXdUlrS+Lrcr5+O0SSUjRXq3QYD3HXHyYeOlRpF/F8d57vjjKPkL1q5ksvsIli+zyzrP+88Xv4kWm6/Re0HeGhFp63y2hKKiJYYoDYZjSZWj3zjzq8589xcjrzLUB18XolN84uLmL2LBRyeEfeSyKCIxdxUQ/G3xN7wb+UYGIQ5z/b78rfW9AeLpjM2w7PRNlkAY8IkpJZ56S9RTVz1OtzmHmggaQWrQ1MlP4vKCEToAc0k1VNKdcINij4gHG9mlFZDad/xUqLgGvvbOFm+SgvxsXqAm42ZMEImCfTbL57vG0qj7o1Vv91LGpE9oEyxJ4hoC5VUZa5uYZUtSLhRXQVwTGMpa4kitA87M0+0iItJ6S9PlgRsDjgCATEzYWsZyVFXnZgWsEYp3kjbhds1wRKDkHPr8VuCVxCLNBFttsdJtC0jK0nx2I/zly4XQ34CxPPxKbpf/JaTKRtlL5Xd2Xx+SkEeC1n6kZECOUiYA4PUmOpf8+T+XB3OK6DrzQ8T+7Cs'

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