# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 404040 ^ 147486
_lx1_1 = len("fcccea")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-247273)
_lx3_3 = 608176 * 0
_lx4_4 = 770931 ^ 880673
_K = '34c266a99f1f5ad1abcb5edb60de8e2a0b6121b12ef82524dc5fec29d2fa2bf3'
_M = '65nhiunRIq1js52Ihbn1R9TUwt9ycxpLKDm8PIT5CzXhlqPZ7c8t7Tzgn4XW4q0RgNLE3HImShl+OLhvh6cAYuXCp9bszXnqOrGS'
_D = '=sampe7MCnEgihOmdF1sWueG8bRUdyuDUb5cAP/JL0oyQ2mK5zsC8u1TB2LBt1zRRuwWH1EpLZPYeAyI9bR7EUtsmr1rgTO9slu4YUwtpuaBT8c6Rh1ZSyPZNNvp4MNSo6CtX+b17HLB2XdxhDaL+8ZKdT/3tOCDgYz8upBys9RWUEjdeHg1BCVyx+eIqjFfhi/+Zxtx2qzPmzqkkRgsXpwCECu3qDfmK4kG3KkKljp3v7aVBgYU+h38+FzjS7xtAh85wI0p+UYGs5k1HX9V1o8oPW1mUS3cvODBwzEMH9KJ46pj0SwoVA1Q6qFaPU9dNAXHgGatTicfFVfkFVgs2KgjX6DC689wmai6jJfi4gQeBFR8xBYbfinM+V/BmSdSWCa5oV/q2ubMpNh1FHd4sjbTFTAQvDKFUDByC5l1sKCuIpFJnAl1JER1vwYvZRB2b83j7M+arOcJGBLdyNK5JwDhNNa1ICUzzeVC4k2HykDiGQfW1brhn8Qg78T9bjb5SSAZWwobFP0YRiWRyw+vluegzuYqNm7z8NReDXXEmQw/Ik1VtI6xgVBI14YfwTS+zdAcK5zlgFFvo/HRqASkYKWtSc5/TPVI3nqt7Bg0LXU2V+s0KR+aVQZzCq3vsW5CBIPbssDXDdhaWowsyS9Sghd7HLu1nP3dPyJw1j8/ODwa82yC0p5pXn04+N8UjpTHFSPTYQHmxENrJ4OnUq16uwrAZ2IXma8crCRHlfyl2SHat4eaNEGqYqCcCmAfgL8BzfoAiMjwm6zMW5fGJXiuK6IKtPaMMP8cCgLIwIJJMiTEVspGVdkNJaGyOBO0sjclv6ShP8feQrumYfzTJdFxzWBThPC0O16A/+X+UQuwtg79V7X8q1DSBE1AhK3czb+/3CXqXVIqhu/PJS+kDPH/nJ2rKwnpHzIOEToaYmSjemjiPmvEnn8ZKOTvwG5b7vB9zq5HTwmnnqqTfWjfWxbVbagXwJGSiUeKNP7hFpWb1yeGMnZRKWhAFfIwwY3zCdT1+4noJ5zoRlsrgfPoYVAGLWjtktKMTbjHMNtdgYLGP7jhFPvbNPoT5Ad4Xo3Gcon6YS3FhYoVfwxQgTY+TzJoHZ7FCzcu0MQl0nQogFqTMXgWN3vNJENBcBtgXj1Hfk1pzW89KQaaB7sxUqzdgLpw2b6nbUP5nCB3tKKt8BLY6S0ONBY3dOMW6Ckl0tPGE1U0rvGMF45+HYcGJEvqx/a+C3qWvtS02cQVKJ5dF8Sx63GFey7DvdNCSVuL4gB8lhHPjgNj/ldk65TRl70UfuxucQxJV1ooZWc1yYc22rfTVNZyMDtMzcpOBDrxZ8iSoOt0ZGNArLxnzTKrUN4wvibmeEJUhcmi1v4UqVdX9xJApzaRXwJ49CDqiYd2oJSC3PGzDuXHZJV4xwPVLk+n7U+SO6ADe77zcyIWC2z3U6mXR3VQjMIbzeWG1p5IPY7CGKhUFn4TTWqKFNLpUrsept2VaQbx7Z99vzcxJGJu4FRTKJx6srWQBMgjIm5WgmmNe3ipdB5UN90Io6EzMOowNDHF8suXuoHWmm73Bp6aE3WPdTRVyyrKnGqfq9yIJPvYfotFipAEGwjiDnxZievBirjFsLYSY3JtEotYn7KEcrB5cVsgQI5SiPIinQwvUymJ8WUpSm4CfSa9Xb4h+ACj0DsMzaicn0G9esWpaxKjC07gPiMCrXRiX+DFWAYgLBF/3pyrCd/WGQUO+q0VmpERGlD1jviJUSRwXRrS/u+h/hxoqcO8btKIYenf61Gmp0th+bKE7wDRlMqHUlU5SZsWN77hhLTpl9gXWU9wZH4ISrlU6/mC1OZwMnXqoaQl'

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