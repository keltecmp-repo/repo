# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 674200 ^ 853850
_lx1_1 = len("b42ecd")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-136349)
_lx3_3 = 869029 * 0
_lx4_4 = 905447 ^ 724957
_K = '1c3bc49e619bb052a4d2ec383e93745d08f2fadda796a30ef4f01bd82858f4ac'
_M = 'KQ6gPv6dPpTe/w=='
_D = '==wITJERhD+3qFgj+99k0yTjISnMmz4Q5Pp8FiNM23A6kRy29GDJfcvC01B/E4Sp5YTXM5BeP/uC1jPZ4aSlqmZmyfCuoszt0kw6+VTawDEFb7BOLKvSUE2VHvVzUWfMFnLa8Vi1LV7f88FzQxcMOXmR7g4i9sy2pY43dBviLP+sfY6jluORMHEZNGZpNVjrHYNTcXaRDjbQviEzNKwLiJch879WUpGOAB1a+sSczVP7BRk/bgUpLcqdjdjI4yDuMYC85TUW9kHNW1ofa/E+cVbsajPle9KsZHvTm2ywlwkKKK/pl1ccep++D50Hv+Nvt/rrPyslJMx6xf1kQFI5kMvAFtmaaYyzlBYNdW76+rbof8YkLc5q90YgEKYpogTuqMDaSyzqn5jsrqKDB6HRRmZEiSPZx4GMcJIdidcJm/2Xb4i7G3YwmLITWBcV6QxPLI1Kigdxf5LQw4jbinsUhx5G8fmgLOnWwfwoplpr74e5GA5tNKSfn7p+5txN0JekJBgxfxmC17aarkgZ65zvURvUtt3q87Nv9+2mJ6cwxcVTmvJ1yqMItps7bWEhk9bjl0j+Sj/V5GPA3MYb8wCj9zazX+aoyZ6oxLZz5L+0WVjUpLgcTCu8U/0X1Yxkrpl0u9nXbJDTOOKnGjuRhUy5Tf4MRMfeXOEj+BgQYUoMeXXXuD/bswSid9FINeEV2rl1Q7YJX7QPO6BaaMfGbO/0asb92KPgnIivdiVj/3wUjjhJc49B1OuQSmy3D+Av1CWwIM1nWkcAUKS+4cZuPsmm/K7WDYfhOaMJitYFRE4YRLxmPLMDZg27SqGT9Yzi84vNT+hTMZjy5zM99/5ZMBHMqh6BNlTV94roFo9ojINH8lgHI3RFy9uP5r4Gg+7dDMPny9lArS7RzI2i23l4qTv+AoPl0csdbHESmZzBy6K8QwbaUsng+vaPGG8vwI7epcca7yeKySuXveckxas9/9oC+BQh6JHBk2FAivmO4QmkcqykANYZ7ELApJGyaeVsVXxpvkpO2VlBkmOVK/6685dFOeyJ4xNjCyAZfZQCfM5egodbza2sKOJgPDH31I3sP9VTlfNnNiS8qgqSnCgC2nPKKrcDJtLSPV4ooMQZ4dEBiaAddU+vij19RAiaahe3jqLoFeHapKAKVsXh+r4rFYR1BqsKSBlC4ldYa6rBbiofgxKC9zcI31XwWaeA8tMImB2IC1onG5O8lYbazDN3QJ4m4J/9ayUeBmpniF79OS0P6FKiyRC7c6+U5N0SLzPDb5CRQoiaC+r5rCA0qgMm4g/Mp3hqCan/VmptQdbigffcPvEj+HU6TAv9q7SqEM289/4ZP1afPzLORxf85AAVs6Z5F/rS6hmfMLk3M2J0DNZqiEmqQaAbDxFY9PnM1qSN08nDpPsnZRvo7OGVChfUaVSjf4flIraTOdjgss5DjE+1384Hl5qQX0GqXurOrodc1U/dhH/RJPPAMcQGIJqH2Qzb6UlYW30sVNiGToZVvL/ybF9et1dPizkY6/2TZbFu9c3lAHMAcslEeUP3/2K0FcM0nkfdoP5O5ZY2So3ldkmCFpoK3sHGOHpNTE3ZsfOLfpAdK+l39UFXIh4Fovq2Osk/4D2SnjVJx9OXClp/157HLuSzQgXoD+W4UxUyKA6tgxXsa5i+upmBsoOwc2GrP+YWN6YlR8OrtRhMV/AUYa9zYjOy7X1WRyuoA6Zu8CtqX/Ujm1k0YopN3GdR88vFGNeW9sSIoilQ3yZayYLoh7I6ri9W0XmOCG2omCMPtYFyccVafqFe5SYmApxIRM75Zpi0HNYm3q/HQyW7hE4q1Wux'

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
