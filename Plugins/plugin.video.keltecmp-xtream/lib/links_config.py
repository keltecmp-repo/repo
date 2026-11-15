# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 951799 ^ 314207
_lx1_1 = len("2c3acb")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-214989)
_lx3_3 = 516994 * 0
_lx4_4 = 406208 ^ 275172
_K = '88c0f844f10f9e979547f0253072d0cd38d4a5298374099d64a90eb51edaaaba'
_M = '10o3NJSMLgfP5AfeOcyuEH5RmKzX8c9NQgxFRLJ8iYvVRXwyj5onR5GyWdo4n/gUewHKqdbynE1ODUQUvyrS0IVCIGWJzy4WluhY'
_D = 'ogt6mf1HOObeWxdTrr5UZFfka6kFSdbM4UVexFl9vMhriFE5kc+hPmizsdxZCIXvVAUc0Ur0jGoP2cmSKf5Iogi5gGqo0yRj+hNGzsWyu9yf1v1c58no9ysR8+C7bZds0gy0OPtbB1EDacmY2Sr9ZTlqRUv8zM+XNDCqh0t9DFdM48VBA++If6eYXsSFcTOMOObjG3f/P+ZO72WTRwCuWX60fdViDmST5vICrF54DSCbojMiXk1Z+OZ/owKttmu9TxXFDf4aTGO9sF9WCohEskGHnuoF57IwVftChdT2Z3bMfiHRp6CL9WNEXQ9TvG3i32Qun4z1mci8DJ6Du2Wn68WGOFjVaSY4kmREAo8I9U0RihR3pSC+Y/tLP13pIpz9Iw3JG2e3qz2EhL7TLGysDL+dkWao9++R0F28rMr2E4esmK9y029NUGbZ7v/L0kZ7LHQ8pN6Lk0xeywwj6kqomlJj79XevRMiT3J/ItPJ2yezQgCzm4SRVJun5k/1YvVKOGKxoRfH/Xtke1nwhnE7O/OPY5aXX2ulh6wInNjXy9z/nhUvXXDi422YSarlktNR4Gc52nGOJmRrU7vXMGEwKb3YidP106GFJduk7goco1vn0wXaVFuWuGOVIJFYZx6fvFe+hPq3JImXzct2s69hRmZGWLmscNtACvJGi+Qo7b34PoBX519ogVum7HIFG2XEshuIJvwa8L3x+uXYRMsD84dPO3qm78VJccJZfXEDs91NN5JTk8IntJNfS8onwXhzFrBjX1JMWM0cj4gv+n0oqHXZudbyks4kSgI6Hpl5N/htxmiht9wSQOArs0cIreG6+OphoQXI20THbBvAdfo2IPuoA40Lvuss7PiEOG5zZZU5s0h9JlUkTXJzXU/mAIjzeC6Ni7q2pwkAhktSk0TE54L42dcQxlMW/osTrEvp45Yz/BxWMWPTFcx6NEcFLtoOdo8k3fq0oyoXIcEYH37Pg7FezeKyNYBQc/I1yp00+90nJNSf2DTcl8/1SzybA1WVXtY0n6tBZsIh71F7eFRuYznDgVIBWu57Lh/+o0N0vqkwLmxK7W35eaelJOIG6K7aRAJm9WH+eJkgq99xjW4c74Oj4QazLneZpl4BDjst12rl8W4fbR4H+1nNVb+EwXMmH6Ea67YMm1thcEqcmUDl+9ybN5NH6Y0+Xu56gXcNMhLXI7I9cIcYAAOq5O4zWoUEcjiPztr3EXiDQ9uDKwVjJ7GkIgY0eIUjWmRbpTQlPGm1W3aV7kxTAlM+/sNvtkzRzFWJaNZx3YvjpB/v8zJ0pn2K/8DWxAEp/d8Xaa8I/r4AOy+bmNv6AkghJ0fQzn8GsDbNs6CX67mSvLWSzDrtEPzHORJt3LaCqoUFWmjDud/KA7cbsRpufPBixJJUiY9wAzzWfLfWRhuNahuXT/E2DDcc6rfOy1gpf/z7Kz1AfCcJbYbQgwuCn+ez5oSz0T1ZgZp0aIqQ3m3NvF/9TS8Pv43GkLZricKO83HqULZxqjMoXHHFqLEDJK5bEyaDtbO6MEY3isAzFwlQZrHdQSK7tMbTy7K3oioG8BwgfciAV/XsYCtryvX6w7fpdcPpYMnvNncA/UOls6h8k4KvuSQiEfYSwyYHnVtAn5Q2CcGa90E+hB71cZ1MUjgNeFlArWDt+yLabyviVXn84CJQp3SjA1irpiukGsJqx/+48Zx+HQTcfDWrjeqAf53HDbmHvgc1drlnAgSHBbCeqFtF2RqdJS7Tiocz5FOTkmya3xrabW2KEPqEaZ4CHJMOfUiLGL7bIv1Sbi5DJ3VCSsjxF/eon0PPWOeLVcOEaqr0XUybymKtm1jbGNQI91ktd9DzNoeQNcdF'

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