# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 698149 ^ 176141
_lx1_1 = len("5d7222")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-434775)
_lx3_3 = 118073 * 0
_lx4_4 = 909498 ^ 110415
_K = 'd383c6059337bc6bb27ed06e32ebe15603f1f26d99308547584ab7069e3223e6'
_M = '/mf2cuVLfXrldWKlTPP6UJ6L1xG+C/7ZT8tugFTfTM6hIfQspkl5e71wbvMao6pWmdLUR+NR/YhNz2uGVNpGz6h3ryiqT3wk7nU9'
_D = 'sVvEk2643BLYEd+9ujWhQJ5GwW82i32yr1Rhc+NUBolDysLEhsE9xJ8qjBecPb808PC/9GgG1l+M6iaMNkO48hy6FpB6cWUWWfr+3j6VBNDcdISrN1OlA769OCMJIpkOLilN2aA0g1MhevBR5A1odMbJHd3cxTawJEyIY5j/7WW7ViFauBgtm6dKaKHpBXghAsEDRIR152RWsRNhtRusW40CFZLvpZboeaAMPRzDFHUVxhVwLrMT7N3GURXAJjzF5zclRxJk8HTnWe6E3vl86Vw3/CkkdiCslnx8mgIeaJ2f3G5zLyD36FpFryAtGtovn18+ntK0LkD2WBOkFdK4+PowS+ZGjHvhLIjFODEsC3FsB3+VySxTKTnAKHTCkEp2g2wLFfDGXfqz+p5Kgt1FowOS+lPfMUz95hKNNaPBQF2A89NKlSO1XXVq1BLfPIgtuIbkBkcslj4BY99auvlpT4gGZ1XGUgZ951Dh0sQx27+8E/BuIgsPSQNGIFH3BKE4nf3aW+xZDonGyrQylrgjhplLzJpAEFNWs/gv1KARSL9B2FdJfzm0vxX0R5KLqIQynSlkdGRohrex4vcw98o2z/I5t74mAk9RXO9KKMuxET6Ugv2uDDUYF1otE3JQi0LJ8CY0Zjxusjxi216+YjaZaXrXN9FDKzTeeqY0ko8GuouifAPIbMPplykjSTEjsU/iXf/lKWtMQU4mrHe5zPi266YQuGiyBfVYkCUpAvNdwX47ceZ0/MSeY0sQfJBUe6TkrbTNwCAFYMCb2Xa3VVU3kzwwVlLtvuUvWC0Ml3nZGRjy4KWxFDXwyX1I2ac765yS95cEoBVgV4hm5HqW+bhpVdlHkrtYhihPud6zwkynlC49DuQyQRf1ha/hKdSp8zzVpGclTzopfdPIwc50szEvdz7lwceUYv9SBHQiCOUfDnOkwcDFyUK8yrPhsG2/W3Gt9ZMzqp/MpTIDift/8+KaCpPecsXFxkESrSl1FCMfCrYcNnv7RB62nCiFDtJTCcb852B1mH0BOjNiFy4oZRQC1NeUoVIKBrZwEyMrJ2cTUBoTMJzP9XN1AqhSdLKnyGY4aMlYiqhu+7J+eKkOtGeIa8lzyWZNxscI6C+2DUr/7e0ZCC3N2V2YmI/v4/A1MrQh+aQnNtE2ZDd4pV7i/CH3J1YAt4i0nPLNkX0pQpBk9TOdtMuLnR6ywWZI+SPgw3AAHHnXeLRmPwIkuVfi2gM2ZrM0RcwWYqx/P9l+26DV6DB8RvPEPa08ISdfFCnQb2IO4aIYfQIz+oQjmS+MxfDVpKRdijQEVyHEprDk6RM4h5YJ+T/fLBpVzv2XY/RKal9Om/fgmYh78Y/XyjBdaEK3I736hffhY8gszq1uij/B92hpQKrkoDqsi1nAojMBkfChDzmL3I6B/xfZuhz/RdnzUwppKTKDp9PcwJKcDpgoJHbNeF4kQsSxMoo1VqAycdgzJZe/XN0WOyUdWdPTAdDUxkamyzjKLhDxOdNCb3SqXe15IyLuKlpi0uiXbFDbJ/TN6LMeYkHWA5qc6dBV2mqPtx2vT4bBk0pSsDK+zL1n/ygH0dS2ypM9RhHcrWPZTsYh7tu2uDEXXOqdNYbfLZWHbXuz0GWS46ocgtyvfvdFciNQ1F8qlomTqQvKewBPfj1uRRdaSkS9dML5L0aaHrhY5uYfGdiC4dNSgsyMIezvKx1tN/4+gqZXNBx0eI6Za4uGWmW7nC+y+a+ynCW0p2QVxpHjWOeg9ctElGmT7w+qwyXeY/qpfaAgulJuZmcVWAqLMYtRYsPfdOJZ2dCxC9oFfJH9Sh52KOJ+O8wDWrLNb9oQvWTP'

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