# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 697402 ^ 317138
_lx1_1 = len("2c6ac3")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-941717)
_lx3_3 = 113564 * 0
_lx4_4 = 898085 ^ 868058
_K = 'd99a42976043c1fe71ef6639e3eaf7ac6196af22b5902789eb90cfdb0669d859'
_M = 'hXOqktHcHebAQUPOUIPrIL+2yxkK5l67ztZyY25ANGiNKq7b2ItF5ZwVGMlThu4i7eufFFy1X7aahidjPk85Md8tr93Y2EGxmUdA'
_D = '==gl5vrPEFcp/x0ijcwzkU9Wq2+pEqKJT3ZvEq5liQYbqyzJ8h/mmToxw3R3cQTC6EAB0fxH2dlkodBZMaeZ2ewKtqUw/9SJLF118K9tzoKBT9zlMsQ+211G4EkZBYe8Ub5mqTwSele7FIvmVZ09BEIENQtpKqV2souF/i9pAKz7B+kphMWCCRCM7Tar1ZwFhicosvlmlY6igNS5iYIGj9nrG7YWZeFvjxz7wPAvX3xzjxUbczJgp1rO+P0eunKGsyMphJoTf3O+8pxf92B6bPeKkkDZANvYxT9Q6zprlXyK+VEICEtSQW7Qz30Dd2m5AjhS0nq4VOkwevsrfpocYdsRCmOQreKW2iCKUoqCoWU3hily9EmmfjPguyfXgjAUmfe60tN6ZB4hZsZ2VV7Yzrpc7fZ4rOEcNstB8SIw8uAIs/bZWAk+L3f2qjEA1BMUZToDjB/DGx22VU4RGLrV+EUsCt2CR4MBl8YTbeIXlytEKyrBE3ETnF3Qv5/sWBqzSK/ciWw7pkA/GBM8YsqHV2FBXFaa+7qzlSejK7aHr+kx+rl+YLL7uBM2eoIKgWitv8bueOeOGsfimDJus3OV2AakqkYTGICy3LHeQsAndU/0suo4zRStGUg8sqJlMHUUp4WRkwnML5bHMReiYnBf9UV8MFJo4dCfUCbTbRzhtmFRnmMcErAteTMOow690TIinxk/HkHxbAFaaUF6AAwq3k3o2+/1OshDiZ5gAPm6soshxnsDJ6nSTYNrvmTruXADi9ukT8tnG2bZnDrrC17JOgk6b67TyyMT2MrmohCs8bE3VIVkl3sYF0FRG4i+CzYCoEnCl9gDTNIFKX7Bb6PmHPzFKOwZdhJMeW5IWaY93rDhw66PCjv7ImPuN+IBITOaABtrBHsqlPDMLJ3mX81Sukb+UAXm9Qmq8p+XggrdvGMTd6lYU9arouPho6cgLmC0F5cwsHyUpULy4ptEGnGyNr+lPcRX/HySDXAmyZRnC4bHP1a4tnPh2mlwQA2tUj67Up60N3SSkg2pvFIrCAh4AwqOheEXrXmRC9IpjJoFiABtykAc00qXje9GM3EvhyaBSY70nLhYfVCP8TJhs+HLwwSKNmd9CRxU0hHE8Cpl2RiMSJBlT0ehPoogV+OhwiVtm9fzdG+P8AJtnGcKgcOgg9ZWJB0LcURzqzAaDc51Ka8rqv657PdFbdKKqXkLK14m9ncD8wVRNg1Fj70QOQEIF8jHxIdSeKkhbTyDk4eeun6Fgsf2W3E/W6zo4Ruic+ukUs3OSUNXxdpeveLTEA5GDJwqLKIQ8ucNIvcntNr91tFbbx6dCxPxZfuNZd2y80/GyRlec00hbB4xedTduugbLtnLzq4X2/Zkq67EfwlQEG37N52tzuagklcd25ZKy0OsIn5GFPZv79BjHrwrZxLeVA2t3Ev2rIBSNQglIahWjDCmf1qDSiG0w1R7BPxoy5P8KGfa4iAWuGEH2aSa00ntNNm+S2ocPDxBnv8PY3inaBoLfk8gqpBXkRY8tHe2//koxNuy2HIy+IfEuIXj7IcSTiJ0qPTGfkzbFFZwzc9U2sXRfX5At8wHII5g17o+gQFIN25NNBMJ1sSNJVjP7ck3pNR9QSEmFw4/ooyDArGnWZ6rU0PcfdYOhcN0x+MUBCrj6+ZX642yWbs4hNOepxL+VFkF68bGcgiLHhWxYypBnlFFzRiT/DM6vRt0pDtBN8tM6aAzKcrBg85lk4EQik/wSmV2Om5fmsw/RfwktMdFQRETCmQB/c4jcRbgY+Zu3QRelbPUagRjFnkUZarwq3xEZxRXClcwn2cPHPBkto3y0iHmQfl3YHKUa48ntV8CXtpOorF3'

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