# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 266324 ^ 590654
_lx1_1 = len("7ff4d1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-104722)
_lx3_3 = 320365 * 0
_lx4_4 = 517827 ^ 358777
_M = 'Ey5VLjLf1EdnXJsUUqhgWuK6wpOgXhvk4V+CFss2vwUeaFFiPo7CQ2pYkRwErjJUtbrIyPQIHOa3BNVNzza+DRo4BzZugpQRbA+S'
_D = '=Qwagrpzmc4WiQz1QESiKvJwLIXwsM11X/+zkssxs8o4w1Xz2C3WjcfO3ghL3jvO5/6iEVAGK88Za+1E9LHcuru8Rx0EO8xZ6gTTwjKypCiDHPCQOK2u9O+AWiPLYX9GI8OgrhQB9kDGv/rCqlimIFLe7y7vl3XHDMRmMwXLMD8sAJ2lS12Hd8DSC2cLcz5FpEcAfHWPOGyRl5UuFrdE/i81nJFLDAnV1mmlJqrpyaybr5ReQAlwvLwKSPFZxgabP3qtDtwVl/jkkPM60XSuo1WcOz7FXJhH5abLuObfBVIYbxUnF6qIie6mc788fu5Dstrzv1WSzftMYfi4rtUIrVgR7WHgQFViLfHjvZo32eor9xbZGmUjayUawRLOGUUPu9uSOgbKydq+t522aMMHrRe3JraF5/6tpIUORwotYYIckmrdFsW3H0l+GPTGIZZDeM+FcyJ8WXY9X57bG465uwaWo/EUFp3Y82IrBW635Bc8ZOblNlWNDu3EkJTz6dMhu0cT7y88iX4ium6VBzBS6Ixm2B7GWV2tNEfo0a4+adAP1a6Xw/0SXkvpuUyaz5+0UDdZD+Q2QXuHmz3EkBsa5BfQ/XGcCHwqtDQ2v105rF8IZj/6vtTK14SFTLgO+vf88FQsmfQFY65svXkwORY7kYJBJ2HOkJWcNmP0cdpfTnBWAFKwLrrxexQo65cMrgtIlhElNZnEx1r72LWKS5Jl1TOCJte2kRS/vRr9DYyJVRYS5Z/gH3MnevNtVu+1nD4Vm4Y0Kyuo3sAl1CDhxQDsKXK3L6NkRtB3PRzNClkN5RAyi2G2NVpy3B+wZwZW47tVR7ibbQA/j2PEtquB48MY5Uzm3QF5VW/gfb327LM6E8pWSpHcd8eC6xHXn7ywnx//VUF53hveNE2NvTUf5N3BJmsa7ZHD07ZgNY4rA+lUSEpK3fvsgQ+krQyoGdyEmhwkgxDuD4EqI1R/IfZMCyOyrNIUsO/DojMJijHaoWPjbps80LCN//+XhJoraUOfU+Y34VPVSu/N8Q7mKlILOQrvA/Oo8LpXkDMEQaoVXIlMv1ZoeQ9v5VV9Nc6nLT0BFMbeecKb3/D/s18B6y7y2LbBkCKFmpeXMbyWxySHuXte9fNzqYmYfP9/8vrk3SkUq+W25GQ44FPVTa8Wmt0s0KvcRSTVKiVM57GAoVE96fwxvoQWjWX4ETIJUW86XqK4DVH7EDjm4jWf+hxapRYqFNccHH3kjnUUU1rgQkphuvS6mk6IYhCW6Mvx9IFdcltUcJi5FLsRHdMmAX3NabI9FK7ekT9IthUrIhnMpAadyYWXH0NowDkQi5LgKZsF3fS4Xo/gUZc6dPNIcywt9uV75FAZx92a7DkCruji0gomVdp9PCyby86+KvnJo4sYl3u6zx36x2fs1uvTNJA6ismxheLvO8MrCG6qj6hjXA2SEJv33yFRvvsQZNLERXUGKzWzEZqljPqG6e6obHDn0eoeObZ3Dk7lnZdHLWRWRC+gmbhQFv7FHIy9rzAhgYebX0SpnXDtuKtd4B9T+f6Yti2ecKdme36zxZNHgv2PbS8NtzDbb+wwDPhk5WKGgCFsFcd4UmRsH8nCRZvFqR7pMGTwDvEXf2Xf10vf6Ajgzi+CjdP71N3/kmSINOypoo/2ivl3GQhtHQLA'

_e552=[146,122,133,14,64,217,80,148]+[201,7,234,201,157,3,244,75]
_4eb2=[177,208,117,253,168,155,161,105]+[134,167,105,150,188,125,137,49]
_cbf6=bytes([a^b for a,b in zip([224,31,246,97,53,171,51,241,186,40,142,168,233,98],_e552*8)]).decode()
_60ef=bytes([a^b for a,b in zip([194,181,1,137,193,245,198,26,168,197,0,248],_4eb2*8)]).decode()
_0665=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_cbf6.split('/'),_60ef)
with open(_0665,'r') as _f:_K=_f.read().strip()
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