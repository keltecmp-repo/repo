# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 937864 ^ 912168
_lx1_1 = len("aacdb9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-160604)
_lx3_3 = 375401 * 0
_lx4_4 = 610755 ^ 723351
_K = '8898629561d5705f942dd65df8bce0dbb54fca86b12e45d340b5b4c0af8479e5'
_M = 'bx21qamwoxSBuekvgivL2eNBfgXVecp6//cAZbOHMTY0FfKm8eD/VYm85HuDLMrUthUuAIB7ni//91Qz4IZjYWcepan04KUMi+/n'
_D = '=AZgq6cjPOq/5AxZ/DGHCaG8lnt4149bkpyfMK8Zk8cOF787i1oBPf9fzH83o4e6xEPprsO7rkR5OrTbQ4QePFcr4nbowkDyIJz2utixTYV5OJaHoewxfAaM9gfxNplMwxdEFJANAac03mgGE/qDOn51TRn72r1r4JZs2/B1b3uXGQ8RCGhmFZBxAAqg6ytsEF2mFtNTEYMqd1fmUzPMFYiHKH9UFXO+9V/urdort0H2yEx3dv+65EMEhgvGQIpkoX7QjYDdfDmgZAyVTUmaS649oIfoxqvUXfESwHMRzOZJq9sUHCDwC+UwPIzgECYzrYQMZP7sjIWvo+3tJx26W8Ch6dyncQMerKh6UrDHQQ6I5PVyuu1C/MJRUtyPYlIeRbFYY/i4UE7vVES+YOADs98yk/OPxM/z03WUv+R8a2kNVQ8N67cZXq4uF0kSnEjXNzMs3lBjRy0/avMzqOuEnSyTTrQ/hWC5IadO4c2hhkn6s7QgAeYSdkIc2znMCB/oxprxxN2EmtCqoPVC8xePW4sDqCK6I6GfjDs+Jx+SeHquaPCqwWkXpALEqJXib3T7sSW+QNdcZwVSEkaa9Fxo6pjkVaNOtpEH4Ut1+l4nb81aKHCzZvmbeWaGtgbYCFdg33K2E2CZp/BQAFpQBpm+P00oFQmqZKCoNOezaT+v51SZCAj/wMjVDx12Uxd71KWAGJhG9Hmq1w6CQavYZpznzlHOSpx/aQwdfza+M/kFQACu4425S8Zd0ghstzLxcdPHvIHJLspCP4wcnivOtfJio5rlW+YwMifLHvgOTrf1C2Lcnb5TI6VoYtU5KakUpai/7Qopw9ZPQPp75C6neCXQjOEKoiHAovFTm+tfpKyXOMvZWf7FIAgWnWXjgeGpw6Val1OAG9M6mhgJd7rbDBDLae3J3RhTnzfAb26U6KxrympwS0UzROkObCBhUjaBSpG77ezVSd9VWTkNsVAVtdDNUKX3w2LlC8xJH6Gnbe5t64KgI6WMWpI63IJxPQggG4kdt8FEHx/6y9WDaQmIK16S7VsM'

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