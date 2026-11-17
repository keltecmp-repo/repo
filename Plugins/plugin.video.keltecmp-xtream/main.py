# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 570978 ^ 940421
_lx1_1 = len("fe8429")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-977521)
_lx3_3 = 636868 * 0
_lx4_4 = 355221 ^ 145379
_M = 'cZSkD18MstuNP0SUG9U5SoMxyMEOjfubV8LvT9mhtPpkwvpYDwChhoE/SJQfh2hKhT2cyF/Y+ZgMmuIb3fDhomOS8Q5aUfXRgTxG'
_D = '==gd+5kL+xkVx4MRBpz79oaIhUqag4dge5rlAOIQ/mbERGeGbl6eUEo0142J4OIXzSApfirepKZUi2CfjjX8Tr+FtwjIW+3subfGr/vpT0+gSntfIO0fp6Jw+pr9/dEOSyI21GRkZY8a9fThwEVX5dLK+HGbmENS64iLmaKQPGdNnQj6Rz+88w6PtQGpKHTZYNtZM//LSj7hKED5CSxKb1hWA889qR3qv+IcCtqZIIX7NkLYbYT6QJ2aIrrxaYs4c2kkojrHO2VrlxKTS3GRkIlizXLJ1yGvQ6NxcgWH4BgfSHWPERyLxQVZX2cuvFV8sRL+KcQjvzL/mAqqHWhvHSKHr/C/GCwhx5WBE+rDQft/glTntmg8+QAWfETIRsQ2I1MCdCU0LRAXbqKtUgxwc2DU667yzMe9FfGQFFMa8C176FfwCzy+m8UGQo8AllV9offurEdRUhfRZFrORcYyZK3bJAmH2R/ftTS7FE0SRD0A6VUFSKeN1oxS3m96hsZ2OIci+5bdA6BvzNYerBa5Zgw4YKG1AcmcSU921kprSQil43fxeEoZPMMxUf3Zv2f+d3jY9ZvS4ToMum9BC3UwRgXa2BlOxbZQjSV8J0+0VBNMH21fWP0jtyqfLVDpOuljxWQkRFuVp7QgeQroETyV0Ij+NCMxq0HJRKbslIJl1bbaIEakw2wbCbm5Q6T4dxQP9LxpsFoukzs2Mf13YJtfR1H1WtDpwiH3SjoZIRCr+efNgvLH6lAXgvMX8VE5egyZQ8MEzUlnGUX+kQsbqK7RFYNnJYBAXVQNQu2UMv0s7dFa8RcskKbgIk68Jfb9WAjHqb+8oWlm36aL4CYaJSlT2SZpn3p7I1X3JFkqsKo2vThUQPlywFwUPkhL2zA8D3zy0G3V4EJ7TZ3GxY92zeDQM13McpXBZIPAt+KF+Kbd7xWOqRH5bfPJbi5yDXHfolRNpVwZDgrewdNpbAeIDYnuxmEgcc7q5BPydHBvoxm9JGHM1RZ1uag3ZM1MQl1QZXu2nFogXNJKRloXyTxE2A7N0SZWqboO6ajG9RO9Nj+FdWLzJtalXdSqLWZG470ST8eJ9p+VKJQFeILGzqz7gv0/Fnpn36U7s2yf9T9ejSO+/lL5UsycPN2OzNANzITr95DKUUy3/UNivHyd8sSw7qUj5n12JzoayK4eLfAotlGtD5j6871RJ/09+F255tV6B9nEFmw7IbC44bTyTh09TWjwLsC8D5VeXGprfj4rfch55rHk3WHy+GF6MPhf8qxtBxMp117uMltfkUGp9iiM/LUW2xuhVNjulIoHCxKr4gW2/Bp+SRhLOxIHalfB5t2IEXAsf658KDoSI+Ep5sKRSMJYKgSOdWSzUwAA+yPGkR7gdT9wkoxtdVc7nR9Nsd54suvdl/VN7PBD7jDD5mk3erj7dzFZ+eClrt6a9Y7miZMFIhcmLTiMKPMPR3eR0Gt8gjX8XU+GJXW+zGvF55L/oCFrZpdZaeIkG7LhKOYg2InVzxM6jTDZ1+fRLTVxR5zNNHuT975NpivOqILu1AK4VHyK6ah+rOu9TZr93iKt4XTohKK3R9TqxHibCROVsrzYStoxNngtefdX7Hh2BLxzacqfVjYROfFA/a8s3h9uj2rpU96ly0KO'

_7cfa=[224,179,9,130,224,47,141,200]+[247,254,223,202,206,197,166,221]
_5226=[144,21,61,229,162,182,42,184]+[21,241,18,40,253,10,239,203]
_e9b0=bytes([a^b for a,b in zip([146,214,122,237,149,93,238,173,132,209,187,171,186,164],_7cfa*8)]).decode()
_dadd=bytes([a^b for a,b in zip([227,112,73,145,203,216,77,203,59,147,123,70],_5226*8)]).decode()
_8ecf=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_e9b0.split('/'),_dadd)
with open(_8ecf,'r') as _f:_K=_f.read().strip()
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