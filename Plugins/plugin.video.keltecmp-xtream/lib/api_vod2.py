# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 726334 ^ 813503
_lx1_1 = len("561ad3")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-529952)
_lx3_3 = 305824 * 0
_lx4_4 = 350209 ^ 376422
_K = '39d3385dc175557acd0e874c66657a518c6f265618f3b4e5d20caded21d29973'
_M = 'hiWQWggzRs6UjuI0b0KovkLgBPHNZiPwyuVeSX6kmYnQMMwbDGYcmZeC6zM7F/+5EbsG8ckzffiZsAwSK/TI1Yc0ykpdNRSZnIPp'
_D = '=MRgClvqlXxF+ppxmiScz0wYqUbEPjGXZhykvbZgVoKtvF2aZdyrgdvCCKpiolSA01xRm3IGn1YBi93/t4+PXeh4eJe5z12C0Jv2cfYRYhaY0zd77FJSF6DaEKTfIxjbuBtvx+RGlPR4XbxB75/e3jjOXVWrYypkVEzZPgP8cDUD7QPqiJ8pMfkNhN7CdIFYn8BcZRJL7+wkI45rV+gqc9x3H9tXaSJDSKlp2YIzPDnqkk8wmnd2vkcETUKb+oAoTlw8eaI9I2DHbkZ8lHQxehhc4+rHvsodNK1zVVrh02bMGmT9y+/w00qhzxUN/+e9MgPtNCZtM+pUVtURrRwbqc3fpe9xphTPt/TWmF0BME8HUQuDyfuhyCNz+px2IkPCRG34P8Ujv2KEEVF4s784gIEF8O6ahPeJPLckTvblueeN2AsvHUjsPNDut6E0iubWLsCCSdNVjHrqIAgNniCVDgOfEX4WtZCEdX+f0mvQ7/HPvzfLI8CkVMzTKkngR6ZBF8hSP1nasIgVBuarYItAhwtgHMjQbEzcggXyhaE681m1IW57jcutm3pd990cUDuYJeV2MQ7yRVnwVWZ6wGupdp/AJ+vUjuBnThUxNH2WNKEmsCyzE6hHDMTfzvORBNQfUYhiC3f4beQEoTy+VW/LhXM5HilIK1DpxMzJlYKUJmmMTvpNoY0q6I08M/FkVeXWba4cjQq56X81OOvfQ0t41vimmoCbNdt1xKdkXf8/whubMh6lpQkZS5Ld7svHTUIqKlmdkvjmG7PbSLJ3LpUym+JrwuJqHM7L+/+pt/s5i77MrTLoBO/+wXZ/XdmhqPx6flEzBbWz1M4rpLgMEuvFnSYj4q/zuJeaqGh3sRlC9+XDoT9h96Emloe/9XjeVQZS6Z30reg/ALZZSfldDOphY45uIWrv0NQlVe2x0rgITD4Dgri9pG5DTJC62KIsYuHRy0/cFU8QT3099vLDaUHx3PMbLamfvkZdIM4+5QvQ8MUqyDcg0lc+/Qk6lLEv0IVzdodLh6eBKlK89HE1rKQJ1tYjMEI0HTwI2bEMx9DHCTzMB45aWBEe5RpmCl8H54eeuZeodU1gzW0WxLQXE+QTH7VT6Uzz+rhA2sBUFA0UUxzM3nq4mRqrj0fFm8hFMcLE6SvTMdouaxYhiTbDSX2t3CMRmo2vALoHsL8Pr6dwvYST/GOUvmxalNxpY29gW5RaKsIqOAFYnJxSEjuLyjNIJmQVfFDLSVK+FdOCQkNNP3rZZiQDJhNszVk5+Urv49muayAOZ/4CLX3sWRmr2AGfr31BWdKDMpI0SdzC4C5mPyS3miAl1/KD+969pMJcno5qS4yOsdWtGp4xVeHEeSMd3EDkFLSmFzAb3Dngi1ZGIAW1Ft1DGlgAlWxYlv0pwfeTuWcymUoGKj+OYWGRmgzJifPGMoGazduG0JDcf+6W/Arl1PYPVM38zXqKSosqV8cP4Xch9lrMa4w8ro1UdcuUaiku2K084VB7DVEnkT+PJvnUmGj8i62kMjlLs2uRpgsDueQrNC3hYgRoyqIkhhDnGi2x48kD3iWUXDvGqKx0i4rVfbfvuYYUngGRBFEWsc9tdpIlen/OLwhpMAWnqFbHABnjEcyfNjgy6GRZCvEKpna6fsLxZIcuw2gJhbk5FkfRqHU45mfZlCLF3604mttV/+oe8q8Qu5VoKbZrT+hKmRfChklT8WBL88UTvIjnuM+wdKNTY0H7OzbRXSBe794VMfum+5tJ+bt+26kgozwbqD/zc3AWzYRF2irhztjnZSPtWYepEymU8x3RVsDbvN7YX0Wwt94P/SAul+FXz/VWkvyyHs0N'

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