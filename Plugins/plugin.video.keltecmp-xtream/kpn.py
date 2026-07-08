# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 354385 ^ 959255
_lx1_1 = len("0b88dc")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-652678)
_lx3_3 = 117166 * 0
_lx4_4 = 109299 ^ 345486
_M = 'urxg/IopRYMfa7gOelNfuZ5+eeGvS7zWqsYHeqeyN/+3u2j7j2JF0RdpsVcrAlDtmXp85vlO5dmtwAUm8L5i8OTrMP/TMxLSFWy1'
_D = '==QYwFfKhZscTEuxlh4uFFMABtKVElKcWNwRMaizkTMI86zKXANRxbDLj+SFwOmOLUzEibGOu24vS4/H4PMPZgsiI0qqRjplfBI73aEZKzLeeNLBfMjuUG1Ad1gA0Ges4rnRV1wm5eTIpjX3NdbkE6J363xauqaSuoB2XIdcFBjXwamLLvarAG/LuwVh8pBTLy5xIuQSXCmDz626daG5id8fsMFQ8JYpUZ/VtRdYHfQQ3gPsRbqJ9eT81o3n9NDwM9rYtmRi7XtCENLemzbd27LcjRRH9STVfF0P5ucKnPSNyQROjlDB2k2bRd/z2tDrg0dM/YyOcrOt3lWSLtll0LbILU8bDdCpuMgNGMU133HQ2JyEgDcW/03apFdNiF2O6m6zrhJ2T2cvG6s4SVNUN6pWGrsrjZpZbxKBSUM/SYOdGpjify3S30+HuyhHmSPFgmT90vnIZy9kwqej5h2uUDLSSm0VWl7n4LvaFhVFCTut8Cre/S2OTlrKSGxBNvfp2FzYlTZV36+LXo49MTK0r4wSh5UuPb1SR8Gx/tQmUR9fEXQPW6qj247ZhZjPjxwqz70IfgMxPEILzNQ7SCAc8+qdVVMRFYyrL9lUNvnwb8fQKhlOC2d/SunH800csJJltZZowpMV/FLYDq4f7OpU11s7TwE6uh1qYWjTyEoA4wA4GJSoznDBKrtI6dLcHjvhW829SJ7hz5zAhFqrHPmj4dImMsSMYsiX0LwMjVsqxgTYNixeSSoB53VxZXRQFoLJ7bNoeDbQd9OAqbFNrWoHf1mc7fZTqOTxNb9asBsbeXuguuYmUELX7IziLCqXu19yxs5NxMtiXoR6muUwpqUuOLAcywyFb7sT4DRvw4jI3M08mqIYmWm4P0PqJ5UTDbRZLpi6BWzHcSjRYYvSusR1mF8/zPoCmFi0JJg4DsUXc9oEHaXM/df+5ie/yfCK38XC9HcAVx3PSvrPXrd4ttFiI0HfVk9dg1iEg5CbAtftHO5dLK8LFpPyxHBHG5TAYxNTo7fv7dSPL1qyutuCsPrm6OIq8kRtUI64ZazJTVl2trpQl4b2WKb6tWSSqkpWPSCzX17cL6lYvSSLN4Q6gcM3Nm8wMR4OiI9N4zaalTmFsx1/occr4sZsjP1hpKKY640Tn0me1kYhOq5X3zb5e9DdvWUbsKg4z481WR81baL46ZgVyPeY6fIVALeu5OgdjVrWb6q489Mvoe+fvMdOTTWbgcsUBG2XJELuDeOLWLAzXdcC6omzAh64rLYanlMmYNcvG2mUie2IhFW4SjPTROAiFZBHGVxT8qWSlG9qm0BojLxTFgeJ5nQp9cvsish2KOcXVLMmjB6x0sj0mxXzRssxZyFCbtHypON3vU1D1ZZvGuGc9E2Yyl5nR4w1ehVYeqLkyn7Uh1DL8JXXBZUgBuf2gJfWiVRV2JB8ggRTOjUGNH+RRUwJrthYGeraPYDgrrkH7gQqMbC7V57R62TkxYisKz2KSKdKLUN1gtNkv2ginGXm+rs8PqojQNBPcxG2epaB1K5txBQjzCdqoaGSpi4gbAWtHEqX4dDH7r09qmpVwUU519sYg6y4vXGW7gsf4wxx4dlfvxsqOQWPWq+keDEJKXesWYl3OliXDy2OzjpikaYhgAiUUaJhJ0TBalWK'

_3c0c=[115,87,71,28,177,20,203,130]+[95,178,95,133,46,85,94,148]
_6b66=[247,232,111,122,177,163,7,97]+[22,218,121,60,230,6,253,91]
_ee7b=bytes([a^b for a,b in zip([1,50,52,115,196,102,168,231,44,157,59,228,90,52],_3c0c*8)]).decode()
_0a00=bytes([a^b for a,b in zip([148,137,12,18,212,141,99,0,98],_6b66*8)]).decode()
_794a=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_ee7b.split('/'),_0a00)
with open(_794a,'r') as _f:_K=_f.read().strip()
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