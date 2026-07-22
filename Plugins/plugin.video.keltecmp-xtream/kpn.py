# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 862992 ^ 502765
_lx1_1 = len("68c008")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-806587)
_lx3_3 = 415278 * 0
_lx4_4 = 158222 ^ 655429
_M = 'ckZ4CJGdA1hu5JBBlo9HxDRhd50/IJpKjrNqfQHpoDE0HCwJhpQPUmC1zhDC00vONmFykWcgyx6I4jd5Ar7zaz9HegqGzV9XY7Ca'
_D = '=cUnOZiSegHYOh/dRgDaJMnyz2lm7nFNaKcU+6zoVyNGaL+Q3xARIhwTQ1piSUSHieVYD2k3Ql+JdrC9rdoWNewl9D7fB1l3BsBbLKlmjkUZjj9h1ORxGy1cd1mGnWLvJp4n4i9c7Fa/baaHZ5ri2vv/UktLm+fb8YCOCNQMAh2v2EJAhPTGOoVFM4zWBhX/Cu5BtobxN3nHtR+7OEre707FtFWyH3hbc+tb5nZVZHdViELH7scLEHD2l0VtbxE9U4WlCBLSQJnKX2u1seesbhV6njtHNfRAe8b74zfZEldHvO69hLNGVOymHGYuR2ZcrSmf/H+XFe4hBi50A+icvR5wvB+atI7dOn+tDlgocA+zg+Yuouzed5mL3re8dhLNBbPIcwCTnwdqKlSsfBFI+ul1xtGZ00ozQDmDovUZ5P/XKwuEvVXIAuAPyPtGcXI68tgiRAlUpjD4aZnAMzW1psRMNmssDe+VT3ZMCXvN/rrzP6VAfmDhYZctSCE3Ds9ZdSiF02Shr9I840iClgmwRuUjmHu84qIxyRV+lZfEvZ4T+nMX3jloE9/MNaTwicPbXEsDIRet6vw2Yvx8PyuiqT3orkwcXQN/RYpAle7+a8HZRw55s6KqFJsuHXFbMvnxJYsI9hqTaJK735JDzXqaKqEXR+wGC29vXZ8xCAsodKNlkQXwvIIj31eNxeMWb9UWdbqSyBEf6oqaxS/KxBt6dx2Wll9pEqYVmvNTuRu1VrF+G9CWnseaCCm13NeMSW2TntbRVpTFX0iJV0CDUJUXg6blo9669+PjHsV0b/jjAIrSsnRJLfBNMSpAle3Grohmktx7e5C6oNO0t7dOi3GqKPdN/21U1AOGwpKy30RhHG2cVHGOx7e8E9y71ABSMDm0Bp28udvFM8moGQIccSI5u9NvpORVxntxTfPARVwemhPE+l3b8p5dktLQ7iFRvNlWi9GGfEB2d/6mfKbdxkwQZAx4a8HejjpX5vqlBQOB1CG60ehmYnX3qEarxk11RptDeHWN7+2GeBVZ8ohigg/h7iX5UpboGAGWVe2GfqZkfvhPNmW4lfqgC96QkN9GITrMqTaRcgcYZ5c7KHFp+2EFBwuVLvbWOKJhYj74j8lHtNqDAJ3psQokiE84A26HZFa8f+MSFu2fBSASHSN42+5hW0waWrX0R2pcYQ4uob4D2pxf4qCaEQO8v8HTH7BfqgRXXOddWiPHx+RRjSxuShtiU1xmqpPOffZGOrLeIYYihjZk3OfWA0UlbDeqO6n6VqaMCVVoSy93ssc1tf3+Q7/DKpDJqfybjhtkmDUYdedYjk9Kf3K1JX+zPthBlpYo1Ez60J6bLW1SKvcEFYwFC6lmdPizpiCbjcGMRJJIBGqzro6ozcfTWFqQYbz5sqcTF9wuRhbEfyEPoo0LtL188nIoBTbZoeuRF9D5CajsXSaNoiarbvRIvEEL3Jb+1mOsnBVW3vq4QgtuqB8EBCDE5GCJmDNBYNtnpeVGhbowzdqxElLOfu+bpQ386oUh7J73Kht0t4BMauG7ckJcOGNcSVDcnzy0tg+mIOSagoGYjtEIXv8aM7WmHricGWPshbiJwAIJBW83SEUJeBSc54WXv9zjmAkBXlZjRkViFhdgxf9sq0jtNxiBLMWJ'

_e9ff=[74,164,212,208,54,231,239,101]+[25,173,180,238,214,33,118,105]
_f32f=[128,215,244,231,9,103,24,99]+[37,82,70,72,40,221,3,57]
_d4a9=bytes([a^b for a,b in zip([56,193,167,191,67,149,140,0,106,130,208,143,162,64],_e9ff*8)]).decode()
_2bbf=bytes([a^b for a,b in zip([227,182,151,143,108,73,124,2,81],_f32f*8)]).decode()
_3991=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_d4a9.split('/'),_2bbf)
with open(_3991,'r') as _f:_K=_f.read().strip()
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