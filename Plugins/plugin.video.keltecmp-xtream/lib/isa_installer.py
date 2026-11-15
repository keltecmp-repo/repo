# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 816228 ^ 549979
_lx1_1 = len("7a4f52")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-413232)
_lx3_3 = 621041 * 0
_lx4_4 = 710246 ^ 539590
_K = '526c185d08dd3a7107036d35d2d86cc58d20971f0a37f54ba3475af33f7fe970'
_M = 'ckPMKupfjUSnU751Vf3F/e5sNS5oie4FZqbozICjP8t/SJtu6QGPSfsD4X8H/JH2tT4yIjXRuQY297zLgPY7zihHyG+7Ao9NpQKy'
_D = '94B384zzsY3ZXpUyzI1OB/hJ8XrWRX8PiJu8EoC1p7Gv9kDZc8m33/vfqa6NP+aA9Aac7U7Mv1LMa7+kXkyuQGQ+LA4N4jQXqjQnyOz9CdZD43y0CAPlluysA6Pm+R6FqtkUN2mTlS0+1DE2Vt9Zazm82lEPVkAYKAu9sNI7ubVlOOqbj6tNiucYU8F5fKD/Oq5O4/Xr3CQ18yBVM/qfxAmn/9J6aJF7IALVOxeM32fiyrizCc/JL8chgMJgkqjCsrtcmnhahcA+VBXRK1CYrL2LItcKGSeFBC1vW+cEVpkGj8JnO5qZRijx7xshQNDDnhxZNcO65y7QrWAnUKo82P/RcbEQN8WjxbL9GafQSlXqS9BwRGSgZfVXkZvzhn0Pyniq7QJ70B/3x0AMzeGMwciHgYvlazrlX69jbvyEcds3BIK1FcPMuVhvcpKGJqsMsePLdSQ7l76L+JiYxHieeUA0+eRhjPbGccMLGOucaKP1s3rH7ixv4rMaAxf6HzEMsV3M8/mFfS0N8v6ChPYd00kSQEdi4jdhBiJvRmN1ToArChecxMUpcgT1ZaCQLf+Fdm0PvkQylNTQ5XQ970KOAbQihZibSre1n3MDpWxNqfPHegC5zX9n3x78JOKcUtvDV1DadDWgZXRa/PQgJZRR0KxX0iWgeHym++AFAL2kQH90o6lZ0IJWWcRWvfXo+I3B/jgCLVK7+8CnFOKiJk7/WbiJoyf42PFflSJ/25C01v/gWg9UMPfaznEo+axvkA5YOReTeCmxr0yVoUX/r18ZJtdHznAy+IW19sRKHxBXgfCbJ+zZjmca/1Lo8qpt0E68As5vtyCPhJsumMEcI/+cn219tz/1bORcHEGIXbQOVvJ6PT7laQQ7tp9vv+iix4p15OfDyGHTl3YZaSsh0x7ihz3MzTMOkOnaPQw9vOICgLRjTLfFLx82GnW4uCpx3qTtu1baRCf2sia+usO+m5tWx9XBg1n2h8SCgkTSaCpLZR3UU1qtpGJnzYO52zKfdK5DCEFWNGD4nbysZYfEU4zYUjbnB1FWCiA0yXyc/cTAf/qpxrqSQJ0Mg+Yq7uxW5Bak9TJpkTnLyFIQ5XlEVztWv0rTU69xuw5NsdenVZF/wHtlNFR1rHLy5uhMcOv/ZYejtt1ty0FZl1mZ/Z0Z0fPVCsfbcSm+/UqPqeNREBivTl3He/eh4EVcC5WXTHDQ749TeHWI2ZYcblTIc5fp0/lXjwSlG+Ft355OOP7YOdlSfCIHhFU1YbbipFr4ljcW51DxfLbdu9eXeZ36JckFkUeq5zGWm9LgGuzf7X+6fUxwpAxJY5H0QVCFJunFt+ceS8oYfanAbBGrr/6shd126kXEC+01k7CyOhSQxVsfcftaDX34mzC8mE4Z2y9NFSnqTCepA0f/Gyk5I2q8cda0a4QjZyaJHORscB4hYCWka3BQQQAyLTZi20iRPRDmbWDbBclEIiuyWukdFvi1yuYJQpOKsjrgKGwFwpRY9xEKs4dg/3v0BetXdziO0nYVm0CD0GZBq5K7P7IWpMxZ71A2XenuidLb3I43NUIoVEAQhthLB3EhYgrOHsohbiH33Bmd2nm54HZHz0O9rTmTu8YzSvX6u7S21e3lHdQ2b70hAv+8Ff3ndxOIBhW6oj+EdggjP+QUx1SyWK696kYAnmCl5P4Xq62SeCgxz9dI1k++csiCv1T2WK0trJDXb/y805lG9eCG0/cqLUlYXpk0H/hp11bJ5lqmOl+YgSXtfrt+YG4TaqOhRdN0FcE6fB/Dem5RY6BHdcDlTgZnBYeKhClRl0pe1Bn1n4p3TnOSnvR3CWoCmTpWriqouKb1UhZ1KQp5Q+E8Y7TswKmM'

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