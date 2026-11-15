# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 914737 ^ 743072
_lx1_1 = len("f9c921")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-679625)
_lx3_3 = 383987 * 0
_lx4_4 = 392038 ^ 477655
_K = 'dc968b6d7d5debbc1fa2ce9c68c6aac9736d91b47e0473399c3d9f6b9a0b8fb0'
_M = 'Vo27I4GsZmDVLFjf1vyLgRCSrL/RxK7XoJ8EPTIGEe5bz+hk0ugwY9h4Vo7SrIyBFMGi4d2f/Nn2mVc6MgAV7g7PvmWG6zEwiilU'
_D = 'esJKm9g2MSUvQsm4mn0O5OxLzdFDBMm5QlvtUG//rFxog2zPuWkN5frEnzWcC2DztiXDCCiiE+EkZlspJsqdBZ2J5GhHVEs28XOoODPu2dKw9p9TZuYoXBoatLEoCp0vLI+ML7bhWnCuTc5nGDbtd9PHZXRr6WFSKz2ssEVcjt08L/inZf4+Db7d0voUpTpfjfPT4ByvLRltsogUnAFAiPgRyz47oIVmkpSb9GJltD4ku6FdMsJXXDIfGw7pYYxgJd0Y5fX8Y5QU4RQxhA1wAj1Xr5sy/SBgNvlLJ/iGeSeMpIDStyZEqrHphruk/T+DCH/zRTC7QE9m5hho+0dEOID7WEOlD8DCMLqaK1nk1M1L6fdvb+lc7hBE2tgJ08bKhmkE0ZA/6Ns475WVrf9D/oEclzg5eGfKk3VVnGK9IPb0zi66WoZ7IW44tpUUyrzaurEzVC5PyX7KDRxOy38c2z1sPDSqMtJf50bAhcD6X5pbJkfyG2mo0rlysCFlBl/mfWSH9/dCO3EQWLdaMmSCx1l+Pw2Un1N+mhbTdGVxJokXnDcjgIFUPjrLYJwt0zUfZMliuEvPTR8NLmkGgk9piPG8lw1o0CBzwIk393WIMLOPcmBFLY/TcOAgYlVtRFRopClCUndUYp346X1FFUGKkCOUiy49uZv1pK9lJb3dA6k0cKmGCumJRdoQcrVG52upHy1xqUjuzi3GBMZl6N07xY3j1kk2Hqo/G9o2KqMi8WnLVi4hFKIodW8QJgswlUZwIhQREhVuKG4IhRc6wToJz/8eujXJAVZhYbSw9tHO7ycYSO3M1gOErfbhSXbzu6isWPP6yHoWTL+Cvx8vtyBQShU+19YnhsDGZwKL+07mdCGCABPuU0+fQJvoyKRV0PWeTDsjuwC/OIKHmOEdd4/PtoaiJcKjgXBBduXZOXvm0+WJVd2lbnM+ziqlQnFeKd/2qIeE+++5WXhgJdRDtnnsUDzIYsDASjIPQBAG3kLsxakWw+U7uINf8Aub0sylEEXWhNgxgFk3Tua/kVQwvQz7PcSq7a+9J1h//QBoQGLordMWAMpzbawMlhcC8r7qitnIEW0HPLC6QvAzxrG2a2C1UhXnJMvgIbsyLT5RdLylhsrV7d/F3SOYNMfzMeUAZ89JRuvdKIWPCBzL8sU6v/FofrLcGuDVJhpVMv/frLDWveUAtxp8wj8/sGXAhsKjkL6iUooYBhPnfy1VcGdAlcVvJuxbBDbreq2i5dS866SSzRJYcAZwz/n76BC+LGrl32tR8AExUXeYpYXcloaSJemzaShsIwBKwAe9R/jut3veHqS5zX663s+4BOS+2QNEJdKNV5NklKcncSIiCkb5ep/DsdDukOQa1yNN3edrSM/MDCYx/XjlBH8ARR3qJj2tVFm9Ep+hjcQINlb+LZRtcdWrgoD8Y+lBXYcTvldV2eSm9jCchaGjsfpgAXOPC3Mx9cJTxCDunqfZAw0ogW7JzXdm2Qp6iQBr1CDXnBbzcHuGXF+avWFH/Yiky7JNMyffzETgPXb+3QbScuFMnKmGNLPlCMswcM9+q5etczrG+p46shDZXyM/uxnybsmK6z3wra35YF51slfLpP4p59SVZJzqQv+eBG2ZiL/6yXX8fZR+vnri4ohgYvVbd1MJBt77+z97vxD+++AsB/8MtSFfsQWKcGOn/7bXLSlhV/ujIyYxvDNPTuUcXazfVry55oY1x7IQ9iX1y7iMQb+pdDjsWIKlfgkvhJMM8m1A4VrJKPnPY8kftzr87csL4bm1cYITrIaEiJzLFK+XLCdtPLSCQvHZLgANf5bak61mAXuRHUtgxkJkArEZG7C3oczVfPDby66mxNAF8n3I'

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