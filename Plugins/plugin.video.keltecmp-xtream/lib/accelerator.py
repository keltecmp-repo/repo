# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 235023 ^ 813605
_lx1_1 = len("4d20ea")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-865166)
_lx3_3 = 767744 * 0
_lx4_4 = 370815 ^ 613501
_K = 'ed2943ef3f39feb8cede353dfbc5d4468bc2a46bbc7e76ac89501193463c07e9'
_M = 'RW8yl8xZT1G2RwqqHaaf2ntZFCfouTNliQm43cyJig1CZzDC3R0ZV7wTVKZJpsqMLF4bJbq6ZmSPWLjTy4uICBs1NMyJSENQ6hEF'
_D = '=w68ZnsLpoLPX/+qwHqRKTZass9LtX5D1FHORF3UE3Yl8OAguNpjzFH5SlC4KXZpB/wpfifjIG7fIkNN3pyl2LvftP01lNJYXUwuVvyfIO4KT/RVVhBiKnPtXf+QwkAmAr6cp6aXYkLTO9x45cfpj5VRvrmsO+KeFESZTZ8812ttsVQNkuV0pKFuu5XKoaUawrBDspPKvupZU5lRGx+ylrZkvmp+GubgunclMnABb6CU60Byo/gjpyUI9+oGsI+zWIidhShmMUz+hZGJNbQvwHFyL+ywhUTErQsw6NaWSqTYqvnrRzQB1rnVv4lvCfn+eSvTZFY3qv11ZrIkepXNsGKow/od4e1RXx1s42/LTBmIIvUCOYmlQMtyDfwEg6y76LsPLMXxTiFFION23PRLeDQlbMvRWPVeXty0OGGZR3j7UoZwyFKFpHBvLoB6WE1ICkCbQZLQKWefRL6/+7hFY0bIHO0PUaRGWU9CvGc5CofrcTIq1NeQC3XVbryE9XQAQz7ITu5u9Eq4iVGcrzlwcgMmT+/2Q5l/sbaWZskK/VxvDQjl9UwC0aAau3aIvITIchT3ZLWPkCK6WteSsxKSLkNch3kP5ti/vXQfQBFcrzBMTQbSa508obL2B+ZDc9mqCODRxpnML6kDja6woKqErl3HxSos8Rsx0Un0UvatO2KeyoMtkOGkr9PgFudpfMbIiVD0s0S3OH3z1PYNfmTffib2m/FNKAOJZ6mjs5zPfjpkfELMCRMPrO3WcP3T8LsXaA8EiJwor49l2532Tkh75e6fNpBqAIuvVepzfJbXclF8WSWNzBFOdkyQ0FzLdsuPmMM7a6bnDMdaqpCWoNQTHlVMBTZeKfyqc+FTOLQ3p+KM0bNPLHUWdahoBcv2CFvyMAuAoQ6lSsSe0hFm2ExYkbWE1DaK65hF+vVYsgBun4BIjpj1qii6j44miGXz1grDoM+NQGt+CPxj0fmyayGXPGKcrnMio+TLz514kYB/TtxtbwZX5thJq63ZaRKix8ZCn3z0QCNxcxs5ZYIW7vP4TQEwU4Pqxx9scZazdxZhW12jtD3R0lTvvnMTC1ljpwjtEg96k575fmPQ8/MufXN5JQxBWlxmNMXm9XX0dfNZAW8LBRUOAfrkZl908De7CkkxbBrzxrQac6BSF906QlF1txvSz9P3XRQxZPPArJr0OcPIzp2/7RE9qSnDmKy/MlTSYjqOBBRtP3y0kM3xctzAUuLa3yMx59g7NUiJXU97jJRYpViT3g+nINAZ/Wcsuq8m0A72WQjj6KcttHtt2S7nhnECusrMqJEfZ//sDWRg/UBZuv5+nordju2YZX1vFFZbBNIOlxItcFL6PQcwyw+eVRJKsgv4J/4uHC6YohZHrjPTguimHqj6IvexmPSmIwp7ba8/5H+mOiESEKYHCXMUAabrV67SGO5FcKlq9Skok5FHk2iC/xvUd/zTSvlmcPxWt/vxFrexSSmNQLwzgx0gEQPnO78R3/NJgX70iR1lAVXtnU9fbRvEmAizmHl2Jx6wkIAl+4YS4Kg5TT7rpOQkes8VzIR9/vfW9j0aeuTZTchq154q8ewjzOb8X5weGh+BwJ1XRwlcn05h6A8vO/0WYzpzjrvgwfR9TGbl1L+su8Y5VFrNrksLXCnVdGhvF4r3K9BpXGC9+YbkPVSQIZPp2AtNj0nZNu8vCVxD'

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