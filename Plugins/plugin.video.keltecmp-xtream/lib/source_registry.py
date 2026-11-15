# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 818640 ^ 415088
_lx1_1 = len("5e7309")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-262713)
_lx3_3 = 380428 * 0
_lx4_4 = 302058 ^ 296579
_K = '72d08a1ac7270e0778e67943ea2dc031e9eaeffaa376276a1bbeda6ae1061343'
_M = 'Zu2kU99rJRfsudGg4I+VOjymLNlKBOyPwf3O6pCAbZ5hvqMW3GgpS7Tp3va0jMk7Yfd6i0FVvY7EqMntwow+zWG/9hKKPSBO57nb'
_D = '==AW/BCZmoSM3/XDDY6qmGH0mc7PhKZ5azq/LPBUR9tUtnTko48NspP6y/Jc7oIh6urdMvH3CRrWlNOHbrjNgeGfKR/SlVsET2uKzJTDYnxpaUD+Ga8ZUOryniJ2KtCR+dkjIS4vwUbGxWAvZULGs9H6uROM0Dhu0fCP/csEyGEka04yauuZtAOyOkXWMK7JkfMxrYkoQA05ZEyUn2ZNmE/8U92FEQxB213oAxUMjaCigBZlD9FJOVYciDQVBTbq2DopCe/5MAYKrvvP2gYkXzlDtJ3HjDO9uEQ04pGAO06gAUXH0cZRm5e0G8W+0js3TI4CuERYLjQkxFOQ8wtChIhScs5XWK1tunqX0TM8gr2Cy4TOhiS83XIh/tFwsRzEe2JrhzHUndtC9cdzjJsZ3wL+fyiRK/7ruHBZ3w8BhyTbW3hnQZopPOfH0VCIxng00Yn84rYoIV2nEkv/h30VqlDe3RUP8YcZkEFeJkQZlAnL20MDBq1sszOt9grSiIrGZkh+YxaCjcyDBmuMf/bl5finF8LHO1lEQgXNPZ/Yv6Y9G3mdB5JMWGKADwNWOAaQyd1G7wQsMheN6B6QYZeAIhM2oasLreU0R7NukNY+eEW0RXWpsoZNCMc0zSdZonPcIg6taOF0VlhK9nFipUSdeYB5luwNtyMpEBnS+0uTcd9VHTc1jDspKDXHZgGea7TQjjPAb6uKkIsEvyvFdTIALiO6j5qP2Rj5ck6R/GDMsdeDt1tDZKvP2EXeahX6avvnEB2NAcF7QDZVXsA24KOQ9Q0DfsaSiCVkKvsGX7A0+mX4Ohz6bVexOg7PjNsD/VUWXq+LIQfWMD6sNe9RBhAgGH9yw3fEZ98XjSC8+qdj2BiWUA6AfMeqwxdDoD7w1N0fbpU52RWAtD2DGi2E5W/N05zTBNRKvszALBLcAQvGfctF6p8CcmcBUvk4v0VDV3XVOPgmy72IERKjy88CHlzHVwjrXQ2sDDXGpN1fUHWaxDfRalo3ABfCTsqZRMvG6kTDFDmQteXuh3JjVa8qv/SOLggqCkfbxNqCNTNKOsSHuZ7BjdnfdyGgtSzDkhmB3xaWG7o/re1QDPxyZyWNIYItudIEUtz85EFTx3QEjkVK0gXE2zn5jGVw0T53DUrY8ny1Y0eGxPYdpz9IfhckIlasIXlfWGIYAUWLmoV9rgVfQ8lRYUFhiCSetMthGI9Ux21uKgw4LFvRjiswwGQ/WHaxNm8veYplXByIOscprLlIVJ2Xt2Ej42i1p9Hhli5hdS+h1QHvLBmkOngjLVL+ZLDJ9eqZUZe4QeZnusjAR4aTV5piDfQ8AxhtliYFhyIxRxX8GxUcHX5vo72NLHgS8kRLJL3mPjwZT03HU5ht/OLhxzRFKGQvD+r9tkpa2DawH1iwX0yE3gWHC3pxxvroLr95xFFB6mnXGJclN5CFeNqHGty0Wj6aE1Z5HCjJyZR4bq23Qn0mN3R36otyHcpaVGW3ABdHPdXAmIKbQYtKyYAcbJFkVaefMl4J5rZfZRxgH5OywrQqkOWmrxG3gX79FdVlFVtq+dcD+goj6CP5ylVBLDqZ0z9kr48puQ97FLMzItaE/vKyahjn3fM0th25IDpuDStE8du1khQyNVeqioHToHMRIUJKYSmXLqwk04Jva+TaWgeoy+322XXR6FUm1U01o+/rU75r+jnLmtqejExr73oVDJaxGl4SCTgM+3kAiPWTHTdKPAChJFU2vTXUIETHGMA1gakYfkzAeS+ggdj1Z86kp7/NIq3+Cx4dUBqKiiUE29TMyu42gXNZBk62iP+bykzQ31yN42W4kJPsw9tfA6fvjjzxmZaEqjhUX6+ttjEF/GZ0ta2T'

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