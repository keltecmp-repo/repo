# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 888976 ^ 734859
_lx1_1 = len("657f52")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-798759)
_lx3_3 = 185918 * 0
_lx4_4 = 167968 ^ 405691
_K = '8f4fe7538cffa473c05796e7037023c62267d5cacc0a89ba03a2576770f0d957'
_M = 'FJvMhu7O6WNpl+T5EGRJZEl5OEE6afIZO6PbAy92kcsTwJvPtYu8ZmCTvKkZME43SHg+RD4/oBJjpYoCeiSYxEPMnJrn27xkMJq4'
_D = 'HQ34/8ObMvh6fA356Y1E4LgbDtaEPSsnefte8rYt/YNPLSiIT+l5xL9dXYHO515MCmXkjC7rgYXgvzOmlQSyaAVTur08RjRZG8kA33/RFrRvYK4NZ0rOL24Xwy4LRuDohoPiGWJEEJft4gxJ9Jf4hbe5gxrIRkPCQQNXfSZby0eKGlzJZuz02ugrwvhiI7fndEebgKUkSk5jYBmBZaMRoG6QELYNpazE+u+4kEsIIQRTQ1fruQafdUUOzYHbrMPPf42NwSeJo8A8Esk4+eIRbwEFYX0KzpGRpnrjB67FeTZd+K6ThfPJfyMYQXlmRf3NhNadydODkr49uM4SV4ZnvCECl+D8sVnw68/TPzxNdZNqPHM1y/kS6rr5bd5WsxMzg6UBL/10IQC5GCbM9dMHKZmga60/w34V0nyTyH3AdRQvJIxOLbXyq2H/+mnp74FobYdxdYeZ9I7h6AhfhngOGEIPOcBtdYJDB0myFDCza4ihvYK1yCwn870xTAPhIBxQEckWw9RgiqmdRl6wsdDfp6SP3R6Gy+aTTVYqKrMkS21VJOIssT0PUm+qm7cBt4BA7EerHFXpbEk+sEuF2ZlDOFa529nAhcXyuK/eUCe6D8OR/qn6MJMCMAKQnAaXjYzxVLqeFqipeWXYdfNE82ZTf5s5SYcHEgyax6JrCfmM+sBQEYUHDjM0RNevrksS0+1mKcJyqqvr8VQ5dDv6UfL6VPsYDfUosl0OnosG2AR5xxv2vIXECbppjUe9wf4Pa0IsHxtdqZHHNdLGdgC7s9laTpvc1PJfI8uCgTQpnJfmz1yquOHFNVH5QMh+edvEZPLbC6IeKZP9n0Fr4DbRql37ZXrGV2Yb3NoLtKlQlxpy6XlWUpQmwL9V3CnF91E0UaKJCDCndW7EW4/pVkY8fJxguUGM54s1OUDnUDsICFA8ImDSlo+qlRHHJPIkrlSZM3GjYCmdPFxYz9s25lEJG+WDNqAkmBr5iStg+sI60sLGf11Bd3R7nWnGVPodGyi/yz2MinQjRVmlXR4z8BMygpMivB7bmzlh3KBhIrl7yNVcIhkPHp4ZfdToRkc5VV17+ZLnDvDxVpKg01l72/z7FwAGZUJ8FjeJG3pK6fOz6YGFtxjoQ2Ph4FGjfqdAVBHsXq1M8WjkjNp8Q+GfAsFW34+bdjSys1xEUDZX59RFPKg4MC9Jk8ntdb9Z0uh2MGLG+Ldi7t4qxwGlX6a4Yo3RjyHeXliotgoorXzGogcakLUumtn+nef29t4XunzvEXA0OJwMA69Vfz2TD9kgBRF7gb8XGO1lQqyu1z/rWY++pVFqAjdN6mMlA5bOcey2QgGqcK4WSaTNU2irnYZuzEE/024CZ47EZtxcVEZNlIKx4PElD749X3CmcQGxMOogOWFRW06Aad6VUvyLiNqjfS6w3XJYWgRaardO1GVXr4Hp7YpxNJg1jallXMhmO8wyw6gf2OET59XPde2mOUMT/RchyZs0HJamm+hrAXMg5D3W763A9OI7WgIWy51s4FeJdEokZ+p2pAUbALciABLJY8ZDDU9l/SgTOB56ocvwzaeUZdsAMPu0ZBp02sZi0MZPGzw0EKT+eVULaQFEvps5ottmePop6ZyeXsERjMa9a59F'

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