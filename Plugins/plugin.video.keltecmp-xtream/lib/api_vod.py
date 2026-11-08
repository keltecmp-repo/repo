# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 175683 ^ 234183
_lx1_1 = len("5faa04")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-554701)
_lx3_3 = 938025 * 0
_lx4_4 = 735569 ^ 774948
_K = 'c805f5d893100fd0b13ccfcb8cb4e958c9efe605359b9eda6f8ed05f19fcff52'
_M = '4jR/KZIS7xHnh3kS9/j+OaIoljjj/6qMJSx+rZYmn7y7Py9221HhUO6DJhyjpf499HOQOLiqqdR8d3P/knDC5rpvfyKIUrsH79Mi'
_D = '=8kFPAaeuTXg/RhAw/JvOZRp8yb+kPqljAbNtj7oteiLbXDuSnqihX8twOjjwGSOXB44ErjtB3HlsvZk1yYOxi8/bFG6kW3ZSc52QlMDXNnsQVyFa9lgWAtD/Dhpd9QnU2eLvHwI8wkE91dGSys8wJW1M4vVhIXgasZpa6URucxJTfk9AwxDQQApi7Zp+ets5ADw3J1PK5AcDl109hE+nIAB4UAG/Ud9Pxe74X0kQ8vvjpGXnOvI0b33jabCOkXWW7+Z0m42zb+q64GTuOcTgGBuLXjbd0fKlWapkM2JJwBmMnBPivRPFvyHQiTeFGyaz1KnLCPEDN8zs0sLWlsXEAgYR6WE0RsA1R1/lAosqL8xuyh0C+EjCZmfp8Gr8VZA41R6DIjV6qmYHwuCxmzED6aJeAgDEMsmuFcmu/tPtpZjnh2X5MKZSi+fqRSeXUnVHETqFcS1Fz/eyxrIEc7oEtUig1g3W1IZCVMd++EsJ+ypqi6DglQjpYUr7YTHkOEKa4onIY+gJ9/V3O953seansiYPBDXLvG/56tY/mfap/PuyeZt+DiUlFMxzmwb17+4kzFEnTUpgEhBXmoa876aULm+OJOLu/zN51YrxMuEx1OZSkUuuMc/5cc+1LaH49WNeW6kcYfN8rYBgu6uYRTxsre9xpKpgeiNG7VM12yDpM9SQEACOlBLihk00MVEsxhaDUJeuHPBVM60YtK+vNpa649PjwA3nTl8AC8ShDCKLidnRNWWjZ5fho36Efufd+H6DPAKHxEUrYVgRrexTmzSNmgFpNIVZdCXReJBWEWjrWlRj197D3GwTg/ZkONE7XhUgpgebgbVKongZBviFjo/gT3LDPih3w5jXJEdYp/nGWuxrWcA2IXcCz8QEtj83R1RqCGM1OHlTETHvN2T+eJh2E1Jzdt5QxkeH2QIZ+4c0FOBp20aoDhHepwIj195j2kR9jrBf5dIxEii0YkpYWo0bpiLn9A96wPRXkfNKy8OFclFmHZ6Zu4kMa7SvItvoC495u3zJi9IgPQa24/ssM93GIAD+1A9CNVdv5kMEO2nGjImU5zCyH9gkNAHl9hGeVxVfLqmqxSAn65HfXuGDrZOJDZEU0BqOkKuIJyJbIqUH/sWR/3qcd29y6LOk5yH+Zsb5sLC6vFoa0kmas25DuwpG/4D1ZNyLWHfcIXEAMEgVlCYnh0oU1AWse1T4l6LHyTqUnRO+DuOkyFO/wjKUH5Mf+QprTubohm4J3nuGNV6c5IkdQeREqRj4rrU8uBUqbC3RNGacclGu7N7C1whcxUepnUlqMXlap2l/3ReF4OxK0ldgo56XH8IXSLrr1+XyKuwWZ9qUNjbnHJGhOTFyv5f6w4fMDqdOfnnWjq5d2G/Zc1uoEDgxvEUG2T5ECL6hF0wuHmo8QKIdr79cH3wkNvdpY+nE00Agwy3k7xeV+G5KRwa3cg69xPzs/XYW7DvS84rU4dymFbAbHtp0eeCK8LqUKJmme8JQvetFbYtUaZCjbkJVqhDLnvazAtVpGjhbVZ7wrqBsyGI+b9T1R5FoXpyV9355AVcdWVHZ60XiYZiGjDcfs7R4n/t7r0Q+2uUbtlei8l3s83Qcwh9AKrGffCHRYFq'

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