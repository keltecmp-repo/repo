# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 835749 ^ 159831
_lx1_1 = len("7a0860")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-759670)
_lx3_3 = 105163 * 0
_lx4_4 = 337727 ^ 567661
_K = '0b73ac3b26256661f64ac013a4e0ec18a837b2064da22bd2dfbc1e1b91c7b9f9'
_M = 'peisMk3a8ALyfuLB605fUE4cjS7nrpTlK5OJ86dc5ADh6fYhSdTyFfEt7cvrSl8AQk2PJ+KtlOZ1x4ui91ThC7PqrSZK1PdL+X3o'
_D = '=EtFJSe+8Y0xDu5ao3LGaBlvpRpuUL0mHDnttrL1z1pK3niPQ7qdb0NiuPBIjD0RHrXM4eG6OxbRJ0tbqF08OE8qUbgS5PNMuFSQoRNfEO58kc9irm7W4XQZ1KNO6XXGYfs1IgD7aO0hVrFlNpEE529xiM+AtXS8RXkf0jJukPYEitMUpEAqM51BDv2RV4abTI7s31XKQ9OQy6hLkt2qdLimZIPZuipwyPFBwI4eIGAcBCnTrfh8ojYBNSLXS7Q5IprH0+AzAPGusXGddIdCA6PDfIfm09LQzs1maYm1bl47LggYwMSq1JjO7GfdqOLPRm+LWqU7Z4NjFcIwahR/UOXlQpNL4desQxm4As8S+I8i2IoTXcFq3L7SRYSaF891n0qL3Ow1Qah+c/X2lFze/SpDRCm6Rj+GuMVmxFp/yt76x3TmhlZxyzaGPg0h4XaWcF3JS75t7MysIxID3hAd8czfZpJL/wUvhiLZ8UX8nWfWEbpn7p+hGuK7fScv3Ef4NHaJamPJwC3ipNwqPCTSrak2WLOL6EjUC9UPTrCsUbHnssT2jDvscitZ1XOmlcdo/79H/s56W3se2JJimZghjGu0GWak0jYgHhdvKx1WnQQKkQ7WGs6hWeaa/SJjQ3qO8kOMOSXd9gYVpj77DOsYuywp2+T5EK1MqSm1FLNAwfR3sZysWhiQZDkCCQ4x2SmpOjVBQvKyzdyYHU3QxcHBvE/K7c5lzchHsDXxZVkxpdcBVktPmB6TdOgsv0VoOVvelX+XvzfiRlgLquilaGMBdW2MqFFTfUcAB333zygO9Hx34WPT8lgCZQxdvaRmFgDSD9K27Ntqkc5KLV+CC8/C1vGgBD/44DLp2GETdWLEc6sUIdEXkM+/4aPRHxwh/HO9GeH0vZzkH4OltOglu9ug2MonGUmmItFcL7gZEr9qlBuyMKf00CaISRbbZj2vTXR2h0Hgei59T355E0M1kYECvOtBZy4SDrIpykeyovyytd5fiTpk0X3MfRhwgOlcKypmG4CE6h6PDSFbEUlgJaa9Tyf58ZtjSVDdsDmesZ6INPHmw/EbpgYS19JPmjSPQuoK54x3HFIuKcyRMmKz9lBHOeHOZnDd1n11rZUSKB26JuQABgb9XjPPEflZwUhljtSqpM43LUD1HiipctuTzU1FD1Oz8F2Rm682QPvmd0fBrFjCvB4F9ZIFc3zH8v5XPe2ovnkQRGJsS5u2mMAmr3TSta8n17I76PG6fba3Dz0NfwYSS0Gf4PEvW9gKsuLtw+/mbBsrWEzD8GlFHjfC1iJDmXju2UV7FufZcnwrahDEXocu2ZayDKh2iAkmiWCOk0wX2fI8k12vfFIpNyGHx6nBJ/KnxFvUJAvbAkNQfjg8HVm05BUpYnr/AveC1WqHWx2wka7iu0W9UVHDg2PAG9xiiRdzrG7piS5Rr9DywfK+z+cdAbcVMRHKTI64VIiumR2kVv0W574eGJYC4J0bc1avZobZMFUaoZwDAL4mx6Wv+FYlTOqHZCtgVEr7cHzHYyCWuLWzd5XNIUit4y7eq7RccH1GxVJ5BmFv0cGretWTKoz4OWWE/MA+ef7sR4nARqLDk8RSD43WkMBWv9bsRF9eH+DBs5YG8kW3ELPpuuMXeRUDj6yEnnfgd27btmBf'

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