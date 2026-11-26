# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 553670 ^ 222559
_lx1_1 = len("796d02")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-344196)
_lx3_3 = 919619 * 0
_lx4_4 = 818560 ^ 712649
_K = 'e0dc987b6134d785fcdf8b56b2f1f201fa04ce3aeff5a1d20496f83b88ad6259'
_M = '+76v63kJnh+7DQ=='
_D = '=kpH614Ma+8LSPswNMnNTWsaHECijlbTKNfn6/5x3BGnzd80su051tWM+yc+6Z2hF2RII/5k0ovbiuVlI8LqzWJozPv5eAVByEEuB+4iwKjnL/zg5EVObfPB4Ibk1l1Dfz0Dj9g0F1ggTISi9UYvNwdP0XhDMBrilO7xU0md3f3Wp7aKNYiFSrew9E1YR5kJtJ7EzrVJYFK/f5iXWBiCR618TEZ+9Pf8XA6+eam/RPUxlvQqWBA2+ha5ULmET5rThS1zBBOkz917XCZD06pbVPBmuU1gnWGAadHRxHqeZxY6DmeU5xqXZsstIxod4BlEB211dXtnCNPT0SYcJDAKKF2yaxJ6LyJwZMueyZLR9P9YJqryMlDpIm7dgESw9x+BGzHhwEoCVW2ShkV68++vGBnnE3SsuS/BvHh/UIO0uXGcg5MovYhUjgpgAZlzojm7xXLOX6u55WTGaoIHE4IFGn3c19mNQQ77EbJF5w03n1Teu1tHLRLf75r/Ygpqigpa7zwGow7X4KCWOyeFwCFjjMdxxrnLv5fhtMH9zYKkrk8cuJFjcZvco/D9b7fF+JXZAhzOUBo6uvllNV4l3c5nIUrdsaCc3FfeTlE1nhcKOl0G6jrJWqmgq6yKReYlpvAOdDdWLAp596ibW1PFLVKgDJW2D32Z8sHSemlpSeZ/x2jZ0nMRfxBv+P5F/mlQve299eRxv5jcfP2ofR0+0If0uK4C6YQY5zFVBNyIXnz9oynIWGbt3Dp7O8gLj0P1OiLBY3QxwWh1okSyBUf+gUsLG1SGssrUYhv3vHDh0LaqecLnFV2OT02JqnsiPZDQr+Lf236tDZB0JwQx+kygJFDzEqykIOdi/h5sDG9Tk4H2OWwrwgpB6dpSZVpDStbJCEXMBs7V5OIaNZVwRPiUVufXhH9Ycm4/d4N+Rg+ufctrH+5TeX8FHznv8G36qIR1LXggUPqQDltatgtV4UpJdiDcdj3Il767yqpZCe2lB2u/5Fkw9fbccNYGMOyscbu9VfnbtyHi5YQm79B+jOU55AFLRkuZSmue22IKQTB3ekyX3SK9M2rlxbK4DpB+FfOuQDRTG6hoV2ZrMAz9MV8Y4VCmVwMKc5GXmAV6vuOXhDEJxdlffpfnld+XcURbUg98pQanwXkLMz+zgAoA3rwKF1znKUrW+EWOEyL24riAFfJ0P4ozcXUER5LV5XxRZDEyBls3FtoTyiJ9O3vUktYvk6i39e+OeHJEdsuFO2OiPQqrat9kqlt4OYX7sH69NYVEtIMRiqCoaBZ9h/pjS/JTn0Q45bgN5q++bRFD1G+h6w3NkLdJ+UcurTdxUaUbABvRBZ+dTlwu5bGSs+taSq1Q3HJdql4jHvh5KttLW3Z59gfyUNtAXYOs31/ilp9A+rYqrvyrhwUbq5Phh0jv9FzX/IwEY+vL/nAjJybv9KC+xS3KQPnJ+xMUtsbvMkY20US5b3/0FTifAiu6G+dQBCHIJiYzj0s5s488USMBFysM/VKlt7ICznFDM2sdn0iaW/quQ2sslhPjj1JSg6qUkuKOrrOy2dp3BzZj38Svl+/6Y9YpXwUlaMCzq/coDJGKOk7kSGEjuszCb8pMjA4Mb+D7cHHvKCzhIEdmXESiLg5P4L0cJw979/NtCvpFlIkzXQ6aQNjq5Z10iV7kOjf9ZT+uZQYRUhwTXfRjoel2wZCj1/v1rWKtc9ce87R7TsdisFOufz57drLxd8HI/w8KW9xwDeQ9IYa2b9mHPQiH9tajkoLCkQcegixoTxknP0HqkYsQAv6i4bPVzA13KJt0a69Go4IF8MoUD5hZkZm54A/AigmB7W/u'

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
