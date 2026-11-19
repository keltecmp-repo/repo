# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 539364 ^ 166252
_lx1_1 = len("9f50ca")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-335609)
_lx3_3 = 386283 * 0
_lx4_4 = 665343 ^ 202016
_K = '5285090663cb793d6cd3b89df23f1dfce5a4d6dc9a4a8816bc2a0d765a75a5af'
_M = 'E/73IDrqYHlP9lTg4EEhnt/q2mgKOP9kPA59FVUS6D0R7q11M/ozahOmCOezRCbJ2enbOVluqGo8DH1FCRTjMRey8SQ9rWFtTPMP'
_D = 'vuL8n11J3crNKjPZI8qFo6rDUN7+MTJxuOaFlmT5kmHVWMVQ9jha1qgRY2gn5nlDQUAK9g/JW0j6JCyz96Iw6mxro6rP1BUkKP6JJbMV1dnr9mtMMfZuG/roAe03jxeyNLtXJwYdjAelbEa6GpNWIS/F8dbU9kw/GpGffPy3P2u2982nyvVqJFVNzllMi5wh0UwrokzMS8RMLZUUCyTusMVDT83SYqVqtHhguH0hw8+/QcIP04kkGliN5dqDCgvfkGoUx8IFOTL9uyyYxAlHBC8izW5BVq75b5cg7F/8IJi7oiBS/wwBlwdHXyvCJ8dBQpGY156A/tPStwlUAhr3Hd3sCD0t6MCY5TXSpOlZTEADygjbzPKTzONbF1i4u+K7G1eH8rcDnekXW7JXtvrvzvu3FuZ9T332qX57rFEnGICQKJurEhRz/Bo7WEY8yBKq5NAIJzbbO3+RidZ+K4VgGs29xmgiMIdgknq5c8R9lkfyZQXqlI/MXeflkGVFt8Ko7+ZMltHd91/nlOFhjiDBmxdk8ZdhlbIpXkwsBZCqi0wWG34tjrpHnMfWsbtVI8gUxWW6pbyXX1GSZAur8OsQpXCoszwYL2yPz8fNdoz6lTkqqvdARPZipUC6oThFv2+0KOOZECyvSKo47fe2Ght70utrcUy8oz63ReShAOCa0DGg2iZzLBhyne54RH65WRLlPLdwoft/5B3O2EbGp+h9CaJgGnaCpBvkdzOb7cgVfSW3Wj+IM7nCM3rKOWEogfUh+iS90FCLtBnaxceuyLScfmvuliJDbVXzgeTowLKKJyNkP+sm9b21xMKkyvaRL3fctkf1MJUCh5AN53MVb4pO6ejgUGH4vZKAVoKcPjUPJJI2xHA2xSQFO3tFFnfp/Lz/P0lYIjOqj7fXcHkdL+fYbZh7CtO2wS0MNyc6M8CJzjNTv6Ooi52PitEK6dMleoFTU6FaBs3U5mhgt+yri9TIJJ4fgm8Xxx7mxKZDOJk1wGrlVvTywn6gxAgfNFaLlvUhFmfNncSJPbQywu8rs8EiWkpV04RgUrf1CiTRDX8vTK2/QcTn94hgQ1M6Nv3u8Uj2rvI08VUNCMXJDZ0p/0yYfVBobzMSHxBg6w8iRrz5ZRj+NcD8nE+YfOsFJG3Wky2oG6U0lHQNiAD+X0eZUS30TufkO6jskEGeelOZeqIkBYVeENwK1lF+ZDuJ8CZ6tkur7yrNTyWru0CR9usxwy7ymfjEuzeRJ1hHSQbC5MP4FG7HxslHbSCQ0Zn8DNxiw2/dtA+7gJDVHsGUU1I6nb54P9xPGxEZuM4Ps6ATkx5JndNPAJYhbEzuyjVJMf2tbOxTOcjzyjMJ/8q7nFMKv5r1UvbGKExCO0JScv4DfXvtr2YkzH1zTF2PzxWUhSdhp639Ig6o/uT/VIdAvtlC1VjN2KS0zgvc7ytCvSLzjL9ax1fuKT1maDz3+6uPDm5MA4j8100Nn5BI+f+R4dQh6LLgjnPnK/iTg3Op3b+o7dH+oksK0XYiM2vYYuXSV5SOmt/XJbkRzE3mdLJloebvlNTQ8OGxBM9NSItuWMFXOZiy8Ye0/MwtIonAJObmVsIfTmnLOUnkJUaGshYcMjjpSYo92mwN947aFubABd+4xMgw3aHLJ75x65K2ULRffFRsyMeAfK7UI+fjQsr9TkgCclTa7oRmb/2/1/acF80tas1Ta661dSHje9fDfEl8vOzVOWUeU6B+YI0gLui2BixMzGGI08t7WtdcwT5uopF3yIbN36Z2WLwNr2unsb50oiNUX3aUrhjHwXBwb+kTeAeXUXlul6UqaTinXg/S91C8sjIiYt+JF50RCdpFhtOg/6rB'

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