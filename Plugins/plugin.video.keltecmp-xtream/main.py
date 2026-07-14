# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 447214 ^ 488477
_lx1_1 = len("f621f2")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-626963)
_lx3_3 = 987907 * 0
_lx4_4 = 948037 ^ 495955
_M = 'dvakXx9TaMvsRO8bx1CcQLNe8GtR4enCHyflIOma2bgg8+BNGBQ6w7dF7BiVBZxHvl+mPALh5sQfcrdw6pnc6yD05xpOFGjC7he0'
_D = '1R/ERxN7vKXQ6gTUIfaRBK2dvjwAGgFG3J5BeYRrjLQwUaMqgV7I0jW5cKdnoxL+GtJCV68ywsRcCRXpzoKk9whqjkq23k0rpAvzU1vGXlNwQP7undnWzQLfMhQTEivFR8UIZR87ufI01dFh1FFHjq344VVe0ydkosxleesz9PjLbhmJ+XDI9f5fz3nS3k2931R1ynZ7ZohSAvIpmZQNX7kOaUuSDqfGFRYcFc1AEGRSVKX9nbE2SHAqAV+MzKFb4q7YobL7CgbxoSScej5bo/zqF/mjD67EIIpvR6UhNQwyoAhz9sSu7d1TkSqrdA6Lbpdo8QserULWR5XTaYiS+aCYR/uHwAZVBKvv2eF4azgdh7SL6h2Jl/h1cBFjOe3wXLNQ4imalJ1BO0RBYnR/2XPAXALl2gX6Ys9184NtAnZcToTILT3O4FE5DjCvaFIdc1wUdwfSRTnGHYKvze5QcYeDoGJorJykEeQG3OWxvbj7+nODiss0/p9U+nLQG2SNdo+DbaejSnxuYwoyRzgx4BfnJk9kZNRfiSqN/Lg5+yopFJ3SCty2M9cG9rC7OR4M52T4NOuBY3L8K8yE0n38/hBS+SjgkgYGGkv0l5fWcBeU1V2geZOnvrqlGFr0t9Gap0TlinjDRPF23X+JzesU97mILaUK+EyLcMxk/BnZI6McNatYzyGCNvwn/iB2UGnFDSSyE77FRjp2tdlfAb/AZt77d3KU8aTr0iAjqS+4unFuiN3Sg6uxJ/6Ztw2yxdwzAub8ffVmlZc2RK2jfaP3SXoyt5G8vUDMVZ5yP3JK21tFvsydLVRFM1dseiQgBCZpG2jBq+qOEJ95JgbgnYuSmtkQQYSoS2nMsmtvR6Ql1RaZlzS3f3vB5TXBRcUsougPvrFjt2becnSsQ1Cv7TnfsepLms+iCWPJhOwUe3xvuvqEAHzBPZitx2up283G4iQm1E4Ebl3DEZlQ/eLW3Yehcmn9Dq9Mc/177Arn11kEKZCNmvSqzGxkVH0Eu6mZVVTmt4S8noWDvWS72SKdRy2hHJPbJFAq8l17BMATzxhHcXqQ/g0mqc+79MqzBpmvkhyp5/XCwYnRpb4a3EuHr+T3vhmpHHiRuFHYq1xDV+XTE6dfwwIXss90W4iktPjNJLVqZPhxFEGKHaqO8FqfoP2xDP6V5QfYimAjQRg/dXqGYuLkWQQJtz7fLtBZgalRCaEfTNWRDdvdd6qgThTpVF5f975g7Tb7IcYjMFFWoEBcu1rI9pnVU4rBjgmO23TYzi1R3X90k/GEpakFvFrOL42s88v9JVulMgLSxFP3rcqh4EcI3tc+R0HFMkq/iJpPUKy43I54QG53ptdkLbZ2mrP7bXMEKqCSFVh8ZL0XjIwlkAdxcT+5p1YI0mYYJjRPHCCku8w5R+wJ+ZG4HW/N+ddVLZM8Zbm5wuCAbGVtsPOPJPDRvkMEr+0NimIMRALE3REq8+YW9SCd/Dmj8fROltSpU88ut0VhsZTo/T46v1luGjn3CNJWB4WCjERMWM6OgkEHJP9a6GgMzEo0IfjzNaK7gYuM5oAE3RNWLLKgrAaWlyLZk9Ms60W30wvi1ycb0kLzTxlWPjIfRsqTc5a0u0aYh31nJwC6sSrjF2X2j5V4UmXsW08F3YhK'

_2d2f=[71,45,81,15,220,151,206,128]+[240,2,245,211,85,124,135,214]
_7853=[189,107,222,226,165,12,17,109]+[194,156,150,57,80,152,31,118]
_daae=bytes([a^b for a,b in zip([53,72,34,96,169,229,173,229,131,45,145,178,33,29],_2d2f*8)]).decode()
_0758=bytes([a^b for a,b in zip([206,14,170,150,204,98,118,30,236,254,255,87],_7853*8)]).decode()
_05e8=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_daae.split('/'),_0758)
with open(_05e8,'r') as _f:_K=_f.read().strip()
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