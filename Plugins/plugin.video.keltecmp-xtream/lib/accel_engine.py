# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 496434 ^ 259474
_lx1_1 = len("c29cbd")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-501928)
_lx3_3 = 415400 * 0
_lx4_4 = 842395 ^ 720386
_K = 'f871b8bab616e5bf6baafd7036f34e53c265db460f9e403147bdce0cb212dd0e'
_M = '1TlChPRWpRpx8tBUoLnclDfykyPOmsmK1S/JXyhPYozeNhuO+xL3Eymh3lbzv4vFN6LBcsjJzo6PJpIMKUY2joAyEduqHvRJL/eM'
_D = '=MUU+THSadx5K1NvqkhicxEU9vcuQ+9Ua5liWbPiBpD3daVw+C2+z/RfdCsSqMmBMIRe88q8iXGat0003s9sHGFjLB9FFic/uH9AmzjDAnmZdqcJGiBf1w83HEGSEzPPC58NFjrRW0YsySg1RBkMgNOkWedUIcVRyjkj1I3HVI9vHvntRpOG2Qth94ERdpf9df8Q9RjDDQm3ide6g4bNN85PNMjJ/8fPayRbvR2Aqty7GQyd0bMvpu99CHZIZIgKI2/zGKWQSUpi8/KOPca4gvIGvb5CabjJEOcjHJOuFa2q4LVKTU7NtLyA8a59tTltwvTmIFvxhgfXZGob6SCbIINISa7/qdDTxMxXsWHZHGXfM1RHCkEEj/GZTU3IEblpCCV7ab3f9/OGIIdg1P0QmMjnMgonaT1Wly9w1gaEoigTqzTNTr+J3olAu940uM5zqVq1h8YJBv0TLhwPAKlle5vmnH+y9n5vxPbRtfgLOeeSyQvph/iXuqFCUy9voE34BtelTzjgMhvSgSDCNs76WY1rWeeWDyCxzdgNBd2FpwTuWckBVg1Gc4Xa3n11hslGrnOiK30/fL3zNTQ+wubfmUzTiuWn8x2XfmDxAXN0YUZqSNCceJww1Y1z0XsYhrKiEukT5jWzhVN5juR/GlflMFAmZh3Pf0xbRpb1d/0bwO1VOpWgW9wrqMBYvm9DtEbj/xyJPCk3QpMg/uJvCMaSUMc59AcGHZbToPjbs4wTzVbWWICNSMTe3rdM1YYNCOtqnUDWNZJ6ZMrkozwZsAFrK5DNI7+pZPrtbYBuwqhYKtQ0c4F/BX3MVp+3ZfN56Pn5aOPgZM8CHrwQV+d+ReJseg38BNoOik1HkbHlmyqEtMlZM/v149+U5GPUsiX2MwLAB+gtpiZfSqXnFIsF2x1vZi6rb8SteM7tEY3YI/rnuKMr31cPuFRbJrAElpmSybc8nzp8J78lS2hYuzQY7A4PmOPrx5SAhauJyg3IVgcyq4b2O6KaB4CjAFP96Ys240DUurYIumWt9IKia6LdnNYk4Hsr1DWa2xx5dagwLVYOD890XqAi6jMORH3xGfTOSqqF8FHAKaQKCR+TSc6zr9Zi2W0ug/UmWjC2A5EM8B2SkMBZpxbOH5pYooIycXzu/oYYpdVUA9LIEp1sqloiWjXjVn6Yt6o0To06TO1qD5hjSdCkbd/lZw9FS2dnvJGqJECYucENPpp4uMdlD9M9fyZiI3k6AQay3p3mtwzcQAXx6Wcwf9Z8UtF4AHxTj742kjRiZwYzOjWYNbf0HioWcbcFVyryo7PpJ3/ADftyJ2LoDg0v7HolWhXNrdJxdncIUoeR/nRiKa6FbyhqYwyuh5pa9yaSilanhQDyvcL172Ku96GLTKl61nXFJlfoOG5YaHo85B+Zchsm5lYgs/B8Rh0GwNFwMTNyrsXqYS5e4gZJj4VroyJ6eXt4IHEXCJo91Kex1RbJgRhKRtUCVKphtDcmfnlDl8swFxEGypHVNf3clga8JM1Q/QvTWW4KSQMsLo6lY9x0YMjeDfgEuYvP/ZBvA53hx7sdPiVHw1bN8HBxV3Kmje5d8kzpQ8Xoq4m9pSdpU8qYIa+NC9fG+QLcSRh9uP1zmIHjoYGN+1A2/ElpxXuq9FpifE+xhAxzeoWs/yEdPI1lo6jnjr4UpXhglVu+Q5zw1nd7lBiw+NXoi6OhZJFLDGN4M8zYA9UMENAhkbos3hUqpWKdYEmcXh50XivJdB66fputm7rTY1x+g3K5RWW+fMUQzY+gZ42kt4z324OfhnlyL0RBPHt9v5pD/Yo9xTDcDANIHHpKjqxnHWJqhrrg9+9n/ZPa4TQX6JQPC0ZNnYPdvT9OBbAQs7fm'

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