# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 610505 ^ 430118
_lx1_1 = len("b8963b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-252490)
_lx3_3 = 852639 * 0
_lx4_4 = 345935 ^ 652249
_K = 'c7d3fe6d5f7b5755cca41f61a71641ca002e13849c0165a6695cfc720c57009b'
_M = 'QX7+/HDB2a8RpA=='
_D = '==ggHEGUp3TqXU/L7DSxgQ85ReHvDCNzQ78BNsKqFIEMiJrSW+qE3fRakeI4PYRXke3IK8fe5xBAOCTXTnCDwjYelJqFFDNcQ/rs7yTml7/7ucNvPlHmTKkje0Yfkist01G9Q/i4BNOFZMB4m5gx4R1BV3Gq7k2Li98Ekv627m/hASsPIA3IP8yEvGecoko9u9/w3fSDuxCjAbEtt/GpAL/r/Tx8Kbz3kKrHLrwUqCp5l/tqLQJgeejfwF57mscj5dDVsAhijqhdZQMEBJPf0RiD78BDTXBk5qiTcZtycajlH1Dal+whqh2EA11bA2v2ZU5oeaW3y2jyDZo2t22hJWtDyPx8fbEBo5hEGnct0o3jm8JfqHIQbNmAz0lenpm90FstwtqjoVQE6IOJKJuhcYc3yUGXdfItxNS9Ovht2iW1D4RgDaklaAvoTqPuWWJPsdK2hVU27BG/ymSpvq4YFlL6yVq8BVoV9qyNszc5VAkUDE3Ej3rIvd9DwA5OsHF8X9GtTXeJ5tPiXTKEVxm4OekrWv59Ep1LYX577flLP5wWyqgoTSOnPipNz0y53u87HGWmaA14NyfawqWN4us5ipdWa4qWplc41D3cdyucXcxJjA2t7s50uObwhka+idBbvkT6KVljbOk8FWbbkPy9IFdvASwPuJXRyJOZxyGgcAmsN0f7ETp6DKOYvQ9dfc50cwprMr750iTN5mHwoZ9aVufFeXiy163PBR2ddmFR7XhLj6kmlnM11hO9Ks4f+OgK2R7IXdDdRJ9UvD9q1aSC2lZ4QVW4jtMYFWAUDheFc35WrHiR4vO3MmpZpLg1sAUktWUN30DUHaLTPgDmVlB5Tc58HzzqocBikLV56WrTwWesu/OxZzYax+R0QT44SwESdFFpsFqyTRDWCvbEAkLxFjIdnQq1Sr1lvzP/yyUHkpoJ9IHo6l6Vsb8naR4lWWwyE4ETYNw849Lli+CZFWX5VWqWrLnpRDBLM3HE3JvifF2aKUoOt9zl+xhE7gqXaLDSNL1mFEzWOQydsasfPbRP3HGJX5acz0bzRwtsuIm/aWo8HB3vu33Iz8edTaUtMGbY0trH6tXAtRJL/idHrQsuYtU80pKQ47wgeUoBh9EFG8jDsa8As6JNGjAaC+YuiHohfl023U4nplgr9xDcjvYerl4TjwZ5Axo+xKbj3jPiYZsimlu/m/suwrNebE9JVb4ktvf95fFtaeU11HDfkrhC/vAkjrctkZiC6iSi3l+OUMlaeGMsm9xEcjXC1uw0MflZbKiDac6QHn/kjmz9dyZWckrT2cmjzhO+OUciq7eeseKxYHxUWa+ANYguubCwZuHbV0o77Y9jLdOgS9Ou7gh9NWSOinVHbZ9bEgPvdyNjSAlEO7vlK5PpkAWDh+jFEXPz5zCAiow0zxzV1fPdQffWyLgiQoVxSN5luodDhKy6iSYCIDvek2gSz8S5M+tg/FZINkBlFT5BEiq+4OZltZli58v6Vb0FsBQCAMZnV/PVHN1E6QcRDcRaNGly+EzGkusBlV1exOAmtnQIu5EdiX/Cm3HxeWq+gf1D2+9wMYpumoOanjmRGP2tIFkdvkJBd1JV8RkEmRRoXentvwkqDm36RzAJr0ddJqvKqqPQQHP+76uI/haJphVHulHRUDxbghMC0s4ooQM0DVlZMZR2Jz4nSJ4okusLmX8mzbTa6AVq7A7ApwsSPgq9ZNjMQxdXy0g8GhgKecxki8I/emNLTK95fr+De7/00sJUfSeFJLMVG+84i211Ds8i4QeoC4jd6rnx+annTjpEuPFU7LywpqfGj4BH9mQNsqrr48cZ'

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
