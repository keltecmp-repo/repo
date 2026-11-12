# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 996802 ^ 655934
_lx1_1 = len("53dbf4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-745924)
_lx3_3 = 298858 * 0
_lx4_4 = 467895 ^ 865245
_K = 'e5178a30b61a5663fd5919d96ed51ddadef9b342bb0ae2c5366fbed9ee3214c7'
_M = 'z3iB+8MDaFFVGo+tEfYnuhrmyvEppNtRlLrvUM4caFvZL97twx84AAsdga8WpiK8TbPPoSSjiVfD7L4Gz0wzDYx9iOnCHTlUVxrT'
_D = '=89BZVXx4mgk39DXf7DEkVaIQ7LUf9rLCBV0VUr/8CdyhGbOz5mqCLQOE62jgIsEXBInU9saH4xKKICmpzlFzzRAMFzlYEMa+RS2gowqR0ruaaPmeaQeMytRoq8qXNBOBnreRmv4tvYLaDkfkLnUukukG2WPamdW8Ua782Wupk0TIKq9TUTDNGbXFcN3weJXEnkq0kmJhpyw3kn7CPSw76oMCKorvYQ47W+BW6Nb9Zx927sRJuEctgnYWVRTtpuqDyMzg1UaJH+cunHXdbj2NfrZoGmQpUAGJd17sJaEVTitl/tQGanalGRB2nsqmjnqmJPIs9Hl+oj7QR2CrKWtRPHVCt5qWn6+f5XFCm2YqbS+FYqV19tKg7WB9e3UOGCI6SX+dX0/g3cA+phRSrI2syJ7yn8ZJiwxOf73Ztt7gs+FgAIWJz8b9Qy7VxUpY3gW3fikuy7lchOfy3cNUxkDbXCVLNkMycqUOGDeIjjCWM1t8r6I+pZDDwzkzCU5aih52j7bc1dHrsww/pOGEMb9tQrlo2yUj89I6sE9et1UyUa6fdQGB+CjA33PGfNaahXDw2IYygWeUzD7CXIV9q+dHUcLXhqh5PV/DW95hauno8A+d8ZFUL3Fl3asSQFPZzXspXVciqvMKnVPL01qcPK/4iO4bAXjxaJn069HMUb/xRl0Erl6LUoNMnWFy9ZaZpyKYRKfOu6s/2c3gbiBJQVy6Hj8wJnnu/rcp3IZRRWhkVepNqUEq8vLUKzCwDJGqB7gOhlhHbsXibVz+0ws9M1gC8nMRF5WpqtQs6h+odmQgDwBx/nPldgXMA1VbiYrBsaykZ3HeoMhmeLAS+Eu/dgZ+7xc8kxx7zPkY4CyLCA5aboWmlPF3/xmG0I2M0zNpFVE5jNTGfibDxM1b/zje1j7+X5AhLQUlbe9n1wAfHB1gUklMKkt5bbtZWRludXORHNIf3XxpGsjUBNfjUW6TjqHTLzJQBlIo7Jk4Zo1ECWPV5wsPh1GJgytpHXPPlfvGdDpMkpcEjPg5OxuRCr34wF0KFIoC0LmM4Aq9CcrOorXvLunEweiyN+bNsAt/dk5TQQ4x5PVv+90MPyJWw2uGqKiEriv/F+xLTCHtfNdTHfb/mmUcd0+tluFEKnWM1qVhodW1sQcQEJxY40JZGUpEwT7QqQGSv/DPJs0mdjMduyFtPRZCkUtxouMfv8R7Rw4qznXwQm3yrxE2c3zlPkDLJpBb92aLZo+nLeg3TywAq5Pa12t3A5qnv6P2I+cgip5LBXzLBS0pV4G5i5FXn/szMIyUBXkYrAn1xqVC5J0uwSzSb1btY0aIhVZJ61AtmBuebtcpGiqx9gNJT13swOLSrtdg3nkytzu9mIZxv6epjBO42EXUlyMe4hMDpmwpvBIsaLE6ZNn6lCrCKvSX7pI1zGMekxy7ui/BFSHn++/B7MeL47yxVMM9t7yugqLlOqrL1VlKRpSNEkSQoHLAciUyUwmUOGSo2nicVRfjNVpzp4J+tOdQvfzGae2cXPSdcgy21f+0MbcO/JbgVjk9WxAKuaz+Dj63+SV5ckeszdh1be6ElU3RPvn1aA6e1x7Jfa6ZdshYJSQKef7upskr+rIinhSJsvaslBxHaNTo1LcTlCY/KvuqDLKp0qh+k9A7SzQkgRDmJfiq1NTj9NNfj94rONTRL9m+gEc6QOd/Dw4mGQpVrp3nHhfoQGm62bHH3k97G1L6Gtot2NkcpRwr4o2tenRyPf+1wfubFC7JzdG1LFuRDfrvzWH0k9VMy/3pcrMtJYJdILEO9qKkYzln2pn6NTxvaDRJRBw4hdCWMrV4r3jnopa/ZZtxxQoXVXzHZsMHEMe9tFMx/I2'

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