# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 653453 ^ 218749
_lx1_1 = len("77a168")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-863702)
_lx3_3 = 584802 * 0
_lx4_4 = 934105 ^ 484097
_K = '36c8742659e13c4d0e2b31ae3edb06a29672b9a2753c1f43bd663f9cdd8dfc4d'
_M = 'ov56viTKyS/lrtco162Wl6rZ0cZIUsihVRHhpugP+I62tDX5eMHJebv+3CGMr8SVrdGGxxgCzaQMGrSk4FP93eHiPv0swcB+vf/V'
_D = 'KcQL3u2ZM94yaqPK3HkfNjgWt20iAX6EUlkwa6bCUCQCMCWOu5c+09aZljtuNkbIxfmoj1ee/gPyLDVCeUC3FoMyK/He3y+RoR0Y44B9SDKPAPMVCnH5bVE67NrHj3c2tJugioFxSJg+XBg/2cREvu1D3b38gKGadlIiipipn24UzKazca/9SxXkRYklk0TuTxLl6KJ14wfhiFyjNMt3jh0gkDaXKHeA1JqaXR3F34d1+Vrj6bKy21X7d8CrQ9JzC0jRx02bH9SVXiCNYBt5EqHotxom6CI4pFfVurCCbBeVJJaN8v6bUKoTnvsQSLQNMb7gTC2ip7SzhLJx85hjT9aQ5FDGTM2aco6dmX90r3TeinmXSzFFcmwwb+i/YwZqwf6r6UbI5qwuXnfXsy04mZRtN2ST2MvM1hReVpjXyXJ72OebV5oTRtYo/ID+1hffoXsjnozRWCU6mjUpmWp4lxqTVrwhA0zv/g3h68X6/SOrXNb0K2EQciH6Zfd1rnBbBDPfobucYGqY4On/phJ76oiF4bVwpX12Pe6koFn5B4yvoxwiqMNCdFxl0gOGmzGdAo7tTxKX3L2PQay4ki7Z/m4oHiE4+45OakXqeRX5FITjEFvkvlB8wQtTfK6et+ol1bAaUhrvR1J2TOYWPVJSkCBM0dA0r4+IAIqfDpkU5DlZ+7PtB7zJgAqRkta7f1CsRcFdzB1vIPcjW9YrIpXZsql7rAs7JIwCzL99placZPMv4a7hYHA2FHNpVEsqs85/zM/Uotr5MK8SE8rbwNQT/dV8E01vOVqJTIn6ePpI8LOln+KX9g9R5TtBNwHQr4u9Lz7dIgGURMEROo68GybNYweAp71MzZw9W+QTg08rlJgnyfNXKeqNsEmYEzIWjCmxcF7jAbPCf9Z1u+M2NLTk2BH7L3WjH6t6++OyXlFiaKAY8yzRvh285nHVU9rXcGeM9DsYGoDsyTywDLBBv6OK/SNDFX9gpM3gD0Bcly4lrz/jzqjjcWkEe1SdfBa3EeOzSLra8tvtStLQf0ph6+oeTd9vqkxjh50PyfTOj4BJuUv9r0EMimlTkbTxH3HGt1ydWP5PZMC004bo00RW4GkW9Xyw56kaQvFTSvvsVPkD30YdgDoCeuMp6eAwdObieqanLDzvq5AiDmvM0EltMsqL3W9tZ/qf7vKKqHZ/Zx8XG/8FEXbPzhElNjtEe2Gn9ODf4Y9Y08wLALM2IAGq2dTVau1BiQeupl+XNlsNM4CQF11EYtXftt1l/M8L8s9bsOPdKkm8j2lSjvricPzF+QB/fdpAe6GOwKUgK85KUq3tMrvQZNt03I1LpxfQKJOnISXyqaKa21hjS5xcmZ5Hqplfj7YilNVO/pgc1mk0QABuf/LHai4kauWSNvHCfxKIYHvsEppAI61ekbxo6zZ5LSUBU3SfQu8UzjDiNZCirThiuQGeNixC5KqoRkNdPn+dF3+rhZSEOJ++4KQNrB8pBQ2BJQpliVm5M4F7bDz9Pt6id7BthOg+o0CNPowWT3Y83AP8Jbn56lgUCJLyUWQiUDmUQ8CKJmmKm2vY3u9cCZIA3b8O8hVJ8jvJzn66YY1iov9a67Y3jy3dfBScDxZIZMIFovWBJngQ2sU7p+3mob8EM9uT86dyCNqB+AkJsMyrY6PqlniJfUldHHS4d9dUwO/+tphC1hJD3oTlKcZuafV4WOS3MMLM4OgrIEKlI+U3NYr8DoJ5s+mrSn90raPP0KYNaV4mPsAkeBxh/khoWju7dQy4U3l4fyTbUaHXX+Pv4US5gOwhUYM4nFnC44jiuv0fds4I37p+sjesSY/XuRYxckzXLcIfuQp6NTicI5jHbjtM'

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