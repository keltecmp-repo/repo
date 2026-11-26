# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 565095 ^ 492391
_lx1_1 = len("df454b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-757075)
_lx3_3 = 299992 * 0
_lx4_4 = 515327 ^ 309221
_K = 'cca09f04d1ad97a08933df25d9292f68f80df967b3dc93b3efc4e622cd0b3993'
_M = 'Gc7oSNkQIaKXiA=='
_D = '=InnQd7TiKeOA/PhH6eY9LT72RpCynVRcRQL00zfdS+pUv5/8hjYeJg6mhvv+oWme4Kk9U3c4O2FFMCnXTl9WN1AGPMe6TQC1OvSzDlPr/5Nqh95Zxi2dMYltPYUB0SX3H2x8fcj9P8caj5iDs3lFH4/5tuj5ITjbzUYym7TJQbqqO8jjo5qTOVcMb0hyr4Ql99A57wmoG2mzzQ69d3Vps0LJHf/DYQ5WHGBm5g1a1DGv76RzJDH6BmPRUTpFjyMMHQG3ieYSlVF7Q7P+SKH75gYVNHujdW57Ks6WGCqq8eL6Gq/wHEc87yZSjMoQZmVpWwyVMQa+TV8TTNj2xp+HM7DmIRnj5axS1ztmQVUnN/Je7VIqplV2tsuRklnx+AfcC/Sde3NJpDT7VYcJXujFeV+4ZHMN0VhEH61AqDHmX2pXihn7YSVnNDVyL4jiGxMl5Ovcj7j2zs1OTsKlCcp9QgoOXZEoMn7PWYjBImeR2jv3PaoIJ5uFDa72ZLGRgafpAifongSdNEA61UWqfIIqQdcEPYV3Go8+oYc6f0sempLFdFvzRsV4By0MMpQ8ZIOAb9xvLASjl4uI+FYUK+l/e685rumvTrXLXjj+gLY3tKQ/qioXf6ykd6kIAyzCSFikR8cdkIoGbnuFvhYMzwNXT9mIbs5q0TcPPaVV8onBq6ugWnDBnzXCp/TGX4PR5sf50bl8/qV62u5DIJqOa1TCnt+kpOez7dTkoJuBZL2XS5n3gT+MMmQ28OZTUfjazRXf3ObQtktZf+gIWw8uaDTlBf2Kl8UlXeZnvE4Uus/nC8Jkh8N5zk9/TAzqjs/tqamn/bBmGwdTrfoeXwTZwktoFbe9LafuCC+j9jZL3UlPKIpd8MJyXPCct12D3K0xhI6PWCkpoaeN7cp3U8ggvjCak+VuyE6/2mnDYWDeOq9pA4ysRfg96HKq5DN5pQiAlklyUOp+m+l9mF5aZZik62zEwjrU6coaYQk4yJkCe+7rzFtccvbWbzOpwnd9se7RZoDZIPsJkO7U9mGgafPuiG4Q+QsX6PtrM5KjdEPYYrPv4q6B2KlBPc4LfAxrFFepuBQIY72NS0q69RP9z5n6EiIec21WqI4nVH5yaAlIInGgR0vbOG/M9A813RxvexwwGS6SinVa075nzS+/tWi9/rSdqAaRAQdzMWBaQ1wERmFlh+Y1lmT0ESeVkx5GLf48DV5cYpJMOhkULnc5kPN2eq8IHX89stx1Qk1XU2PNDIicOs7LrlGYfTmlWIDtLsdimWyOb+EerRBMrIWXzah55BRifGY/lKDo0rIz5UabjM99y0xSnw6BSxnNJy+tETw+fQfibElbYwW0JhJCl1hv4Pk/1FDJ/ULiGlP7XXYjOl9OXxXTXNrE0JdaU43ZzWs+owXIXPGauXUVc4Dsitm5/7Ip38fxvqnaIsrTWxx2uybE5wAUxRQouok6QZ1Q7gJ9r7yCgovueGIWzZomiW5Z7NQx36g6oa50R4J5S33x0xezue4gD/irreoo4EMVX7mDOZnHdI9JIlOdupMS7X6LVjXIDVkp1RgEGPiASq8CO1h3bFOq7y81XEupijKm5TLL05IXObwgDE07yGFyiAAHiAnsjFZKkCb+Xx19/ABi5O7c4Wrd8xmujCfq/TZMtnkrNwn2CB88EiYXxHns3+c/5EvSDSYLiQw73Qd5XqSFfYHa/YrVkqfFyjFfEHcZOUMrJ5qWKcVdUs42KoNY/YI1WlVRNBM8jG2sFt/FScwWmkIlgsQKHkguVnk2rlpHa5zCOn9kPvKnVYn5NesMsJrUeEGtMPjSc4Bo5tZrsbu2LYqbjVOkcFK'

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
