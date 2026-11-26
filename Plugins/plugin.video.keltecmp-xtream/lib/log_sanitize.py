# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 793679 ^ 912543
_lx1_1 = len("d2f778")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-461089)
_lx3_3 = 146869 * 0
_lx4_4 = 787148 ^ 931850
_K = '1aac3a8572acbd35c751e35269eb1ed4b0b1bdf488f528e658d5f8604d4c433c'
_M = 'c6BEPgle113FRg=='
_D = '==gSEfYuKYaFN1A4jXJ7wDvG/Q07S6JqPC9FEo8tI3x28ybP1KzggoXytjzhRk3TGkrQp7a5pRmzV9k3mw/YP0ECzdG24SM8IcENYfgLDH1mtTv243lEuaWuPE1oumDx/BMG0HHHu8Lcc2Ea4ANeR5nwaaWJx3z5d6zqJOY3f3H/wuZ2qMZSgwhWAVPUlyzD9bgL6zuz8ruU1xdaFGgG+oiwbQxJdTr9rBw9b5ebVwesHe5AqvrHy9bsXrUEcgDXeOy9HUDj8qBSbZEhV/S41nQV2i6UDYUR+2x5ffdRwp6fEK5R2WCBzO0CVVzUADpxzRhir0nlN5miEcZ3w6lY9R+U6dmproL+ikm8pS2OlyPsaXsW0KvyZ59cmuM4lNu64N1YNHgLYQwYmJQcUUN96PF5GIntL8c8+F7NWmen6HU3wqRK/y8+itG4o/QqNYeozb5aDWGc8ZCOo31acHrJd1ZImCG6TGa5DDgaHp6/HieMQvJvpBKURteNZ8ClglaHwk3QIuR98+Q4WDnNGnmUIDVOC1+NMCECYdHk3M7QgniuOm20QeCWfGRZoLV94zfjtYZJb/6Ph/WCwIIVJo10L9mgiqK8C/OVQpohhneSBlGUHkb4X9vLXTNQ3yOkT3PQU0jB6gfaaHSjQk36YoVFD1Nn4HuYIISqcH57HaHKADLPBiiB1Nu14yYLJJz2E6kMyEFUWc/v/rFpTpRH3xCdHxzif8jsgDRBb9tewQ9fjJikZJfmch5VQlWC7mjkpTkSHao5nzhZzyIYWPvfa/8TnaZZFEEgMgkfFPkG8it5EPBK0GZfNr/Maf3FUFKTZ5Vp9bANzpKk4xnQBSygsexHhOeN5INZ2wF4JVDXzNxZd/2Gw3/UOkxonddEawz0OQu58j9p2VVSYjQveYpwH777FWRoZ8912aEQKXGtc4atYkiy3bS28mB1sTrjvixTMxahC7XdDlQqus2PrBd25ybLu8Mp9xxRBrXUfr3LH4smWl3z5w8xjyP3jJTT2k0KynJAu7hizbIjMGvZRftSQpw3QNU7D87IhtfKx2sbLttYuojWpuRnKnxfRx52rRly9yWtJ4whpwm14ON3MaAgDRks5SlYWlbIw9w5xIq4SIPA24Xki0HLumTT2UqhhPpFvCMjuJbMrszIXTsjd8KNt/Y+sb8fV3JXMHo3hbogvYYn1j6wghaoQG4xcWofahxhCih2uPuahIuPzCuITs0fDYyHffNq3u2gG/f8u6tK2Un0oJBaEh8E/Z+s5kok67DCcnpRxxIdxWPhtSqVJE/S3PS3OuyuNCVxQpb+PVk7duozT6+S3HcUgTGd3pdx5liThduOOhMSM3OcOs0psomM+fgsbfF7zszw5SR6JtKSOVSap93cE4lWUpmqz6P57/MuP2FasCrdnzzAtaUMjl9+6SG2bsamHQ/kcgfqy4cf7VxswOYdTQs1nI1PV0ao7sCQB1UadMfnHnM2sw9XotYWNdtSMD7c+IJNN/WNisb9WzZju8ebNPdanKbAJFcDEPISQ7SiEF5FRDv65EpRfkFm5FRFtae18qdwaSAM06ZuCuXkeXWM7bf6GM8BwJZPjGOXKcyW17aow+6A+Y5CLHLMSXl2vwGhtFspCyOnCCL32uG0blPDo3yBsV4qoamuQiFI/8w8N3Es8NiQvcwGryl3Y2eKxEJ9ogK4XLLX813NXmwvKOfwA6EVYsITgl11blHI1M5Jzm5U8LcnZj6cTp+yaexVdJIzbGOYm8layp8E4x00tPFpHLx0ko18DDXIUwzQ1VaiYA23t0Xyuk9JdyBoBkNZb1GLg2kHuQWGhOYWSWoR'

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
