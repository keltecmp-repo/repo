# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 261524 ^ 389122
_lx1_1 = len("8eacc2")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-642160)
_lx3_3 = 673210 * 0
_lx4_4 = 881754 ^ 560159
_K = 'f4939b2921e7c1a3d999368a195dbe0c3090637042573a80d286b310a72da88b'
_M = 'Ks2ojXMsF8WWJw=='
_D = '3ZF9CVMuUp+OdMFUNkL5BYOaPtm+kSef/3tRdQ6SzQNfbFPV9dLJr1Eew4Onwmq9zvffqcfR2spE+kqrm5gRZLzABvV28Coo9vvuv8Ljok0IYfN4I/YK9nS86H7YSvrf3vDEM9gcrlKjOLIRO31blBCk6051Tq/JMoOxvj5dWXt74IzcNG7vXJxS2cbBfYFcLcVRXoGmjdA3jjRcRvWYEOTROoOfpn4/JbRlMydnJS3RgqvlIqQI4MfJgVXnuhC8hnRZd3FbfF2BtEo3wtsWxLIR3woXNZwWOdoMLF8+tMNeNElp1vigLzhB0YQTmUyPo5ZYbNE/IfbqKtA1fERi7k1oirGVeTN9BDchcR7lg9+awD0YmqL/CuAaJvsf0ix2YP5cvJ71zgb0CKYnsujRJ5x3dVC5aVWtskRjodTbBnVRhfPr423ZE0h36S/JUGnKhXjqwM0Ona4QwVYc9G6M/rZvU0aLrNDVjHlmWU/2DTPCqrXnpTGCwprkvxOCutWzfWs+6BMemcXjezHbvMXzxJil9cuVMbzs8zxn3a2n5vJyWNTEBHAIHPSWHsciXNPa7cydbRvhKVnkwHV8OWdllyMCShNKqrbqWcw2rBBj7c2Xh+s+Yj28A1SBtYn82UyX4UnW+ByfP5uHWnHwfFYTOtavPxnW+eot3h+psDfeFyPkW5M4w/aJc2K1PEtV2wsp4RErUImptqEc6+0ojVkNXOKOuh7dgCxON+yrXcymsH5nHW60VYIpL202JY8OaEaOAgicnhyl3xqqk1XrRamNhorr/bq4GKNXrihi6kd4LEr/9iXGmFUiv0ZX20zbY6JYHsftWT5qK9Kq/99L9Tzkeazh6xzzuJkgCqTWRe3ltOZFfGQgbZlxgCfK8qnEA84Vt/NQoKxNgfXb0ZqReVZhwPKfWkBY+q9e8FM0+n+tkgw7O85KmVq4Y6og5iyYwczbmXIZku0j0le/zA4dllCHijo9qS08tVTdTdlAsq5+bbWob/mO8Viy2Rgu8O/xxLyK0fbiLqV+dJgPuwZmckRvLEMul+XyTStmPoGuQKGAwyuomjCqjeKvOkpQ035H2uhT/BJXUUK/sXs6Da8J9bTL6zF5BM5G1oyWOr9zGCSLbreoD2Ufms5P+r09ikCBzKLGLjHHPA7kuFV3hVNPTREuseDnPvMqIDucTG353VsqaZ8BVXTVtNB6E22ChFDegacHOyHzkOqK5zJvyeYtH9PweMkO3FkA2DAtVEhM5kW1STeA+eHsCsxLCxFyHQZlAthlScnHHXXv47s+KHULnkHMTnbxmXnHjEBXtTSdiS6tvpq2VHXsuKyaJ0CQYNrQlkkMwH8Xnq/CuvwNRb2MyrT2KWGEEJIjcE3CaHgAXax984nv4Uf90rOEVVDtqyt1B9EPq2iUJaPZFlSTEUhEHTU1j+gv1t8UFZsFaeLsLe+VPKG/tvQs97FpSoxAgxoCWivcrpHOUjD8c+dGkLxTSgpXMBrUrcKH2z1G5QzsHJ+tkd9bPBpVBz8x4SdT2aDyx/Y9TzyqjyC4c5pJV97nhnZdd+c1GvANeQPsJoJflclZVtV4bvnuYyVSq+J/DadhHWSS5E0GalaS8+j0Tepi11PW5f5SOg7xaqRtwsr5gTUtJ1KbeYJLFpahviX3O5Y6DqgiEWoqochWCE7UUfHN2wfp9sTP1r3u4XOgHmdxSGikY+H0TKVF6esuBs6nniMUcBBvYDBzSPljv5HF7GMFLJdvU4TXCsOP8DSmqXeaayPdzvQdPATDxT+sLpnu5IY1NJJ6KaKPNfK9cqs3E+S19PbRUbkxd+x3uHNvkbd1FdybMukVXEPZ'

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
