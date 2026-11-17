# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 907898 ^ 292626
_lx1_1 = len("f4b032")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-493294)
_lx3_3 = 689854 * 0
_lx4_4 = 796603 ^ 791651
_K = 'de4326d32a5fcc0cd5310e819f95f06d41b165b0e427c0a3f2cc266a70748a04'
_M = 'Yi6kKqOpVCuNgyEsfRr0PLpzd6YX/N6RWBpP8rIwO3psceR2p6lPaI7Ueid4Efxq6XJw+0P9j5BeGxqkuz1sczEo63L0rRw5hdMr'
_D = 'OyxOZ14C+G1WUjp2z0jHqgV6PB4n3SVXt119aO9kYnYKmvM3Nbvj1+r5RK3/GLt5MHAnXS/qQKacqXSdkvnSdcZBiZ3E6a7p+dopAOryEDXCDpzeyiQDqj3y6PLmNheZH0DBVTdD5HEcmKxC1Qe4EBwp6tgiTnTIoATpIHqbAmn/2ER3E+6KfDKiWRuMFtzy5uIfITPkKC1jlRbF5tgAu+cZNz+JGIn8dZV4ZFi93NLdkY90MtxYskONKcINDFiOvvmyNoa7lWsKlScopi31xn5rGzVUarCjAt1cALLa5WCmaj0iR27FAcoaFcFSnTGy7C2Udx0x2wGIR/kDea+UliFuP98RBRHQiG/EVDI/jSfXz6uCK35SQAEA3p4+NzFf97pFhAU2wUbOiw0ajXxTDmixW6mEt+55O6tLQJMtVanHSQklKViYQGtJr3k/oFSS3lstkSXuGM6ieBx7uceahGsupLdq9m0R3mUznjeY0LPnEP3ujKm1v66Mf+6TNJbcc1fppq7VV/v6IdaMhng8pRRq0xkTRRaMHWJ80x0cAyIp/xKpJ8aT2btdFvOvW/WdXENfGtd0zFcBop+GuIn1rLPHauqBE4n9CybaPTAqEsRMS4celCh4yzJFhdKRL1Ia6AU6IdZgkCCkCCFJxDeB24+fcemBklDojz+qHnuCnDGgMobPrHsQclJeE67Zk0sYRRKQHsfF0JR4dVVJDqwL/mqXLnsczTsNvjpxjkDkZufV1uzPMghpfJe412njZez0Lfgitgpfd8QI61G5wtPLEkuTzViN/U/Kcerz1q99DX1o2c4QAguZdvqAK91ljv2i5T/g3vzWUcCoCmug9Ep5tiUsdkJ+NjPWmpQsjFX6SzNc+wWlDddvZmDutIAVFYspLLDWZfCy/gNlWkFFUk68yt5TdaHc4okCan/Bw1RbbiBgCne2A4UMNCpJVSrNbLhd4kh53K+60v6lXCc57Qkyxr9oSKZF6qeblEaFJL5DgI0XW9D72fYg9nXlnF3wcleZun2kk3bUy8qOkVorUOij8JnH/gBQLaiHoC71/1V7SbTRQMcm8IlK9MufvkhJrsINJD/ptWuOk4oeLG1cEFWOWJtfQjYU+iZPrO+bPF4Jw/5LsxTIiSUDc6wdYKN7tPoUsj3HcMRbTyyiEswKQuvx7BP8Wq8ssVn1yBJIka1iEheFk57QQMJQbAA9/MfvbprSp5+3RudZ3PP5MI+AxFNkTNPxg7pNi7aDTAdTQRrSlbeq2DgURMO76Wpo0dSNUIEc/n496tbVX2ecpv7Xl/qDCZTqocb5kwP/FixZeCBWYkGSl3yYElvWLqs/Eu2ZtgKxhbgD55FbPfp2Jj+l7U3K6wDTot+cOMhkuSsYvIbsGTc/lfxgcigOl9kN9UeJUnJmvz1VEf2hDCuiXj8JG1+vK6rUsOwV4A+DhxFCW/+8V4SiEMANviSZbYI79HILYw/9NVYx2aVb4Lx7Ok10F20WT7BuN7KNjKeoZ8fRX5c+GcrE8eoOya/3YRCHyUmCV9EwF6lN9wB7M2j6J5oIdbX8v9IVjX8pyFCWG+S6cxhRI+pnjk26G9RuYkESLBYtehxfyE5M2tBcf+g4+JUdW/3OEwKoyEaJ4cFN91cKFunTM1qopr3psO0FiPDaVKHE109EZbn83ifRitTLhSMIrqI3/qYtRQtNQAUAmeKr3AhRl4m/QT6+peU6s4VyymZb6zJq8BaSuzTk7xPCHuGRiiFMLdR8UEqPBOxlvzt8RYHPbJmz2/xFRph4BxfFsnutBuxZeeFzLVKxtLl+kcpiGAMRZWkBuiz+j5PkeGsQtmZMzCJzY31b4y+xrfnerRPOl6kXZkUS'

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