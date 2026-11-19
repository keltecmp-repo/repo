# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 904633 ^ 521486
_lx1_1 = len("824328")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-963510)
_lx3_3 = 287977 * 0
_lx4_4 = 571642 ^ 444208
_K = '3f91455a791e4b1e6654f3a0e5d5e9dfc029e722600b5e86e0c498fd3460eca0'
_M = '8ky7mX3HDnPF83BSx6qT/SdvQhlNzniGH3b9r23v0ICwA/mcPZMAO8ygKAfAqsP6fjgTQ0/OINUXJqymaOzZgbcC+cltwgVhmqV4'
_D = '==QitclEeeW5quTL6ka6YGT07QuifUj0ksLAfKPbqESYsKOPNrhVwsa6+082swVUXrwcL0U+vZf4Ts9sFiBREccdnKE4mvJrybBxeMinjBAXUTVmR66DQE80uFQrSRf9ThnJRCfNRkbgaiQUIQBPO7eZYKGF7gJivwOTyzbJOIRHpIb2JkwJTbCmzxkdEvoy/pRklO3esFTBfU2Cg1pFXbiw7wTNyyXwQNrRZANNVb3pqxRJ5vvdmxlRMi5mdHk9tWKFPui+/YRC3g2a52sBCemyAjd9xaKlkRj32QqkAZx9P+gkndRj1P8v60fDTI5mr4BXQGS/vHfuRuEPDwRaSAY07j6OK+zuq4qEDXugndg8KjpLHpRnq2euS3fo4dK531CRiyFFKO+8trp2aEgceiG0tuPtVhOnq7O+NJZfZQ+STa1r7cVP8jFqarmTbuBZkNuRrVn1HzJuWUqDAGCvoa3AgN386e+YYh2MBgIk5qTmPZpKxmBaZWT0y4PkyqUt+bsrCpLTPxHkdPyZRUcJ/DXSE38NczfiU53KwqdnjTkTyhf/nuzoSpvJF+l8yhg0suaRDoRlw/vy1Iw1rlc6jZKK9BApoRJQXn1lHK7yZwE2k8iEmcMkpxJvd5QVyd6upVq8mooH9gZy4+Ib3jwx/C5iZfP7LOgjDf7+bqSP16tcqk0asvNix1OryV55mJqpa0phr0cYtgFifqJNtJtWgOrDbBdzf3/C/G5c5OgJwRUd7nzwj1H935KwxxFvbHHvLDRcCkKjMwXFMXTwcL4T/UvqhEbOGy7a3hb/bGlY0N/uqVQxLWwOooUWQ2VWMtqJgf2RodL7DBuHwBtq9xzjIb7mOyYp14BL3A56BDlz3ExIUzczoouxSldgMZcEIVBHIrvDIJr6r1RnXFi6MMCnMXzqjIAB24pmuN4ihczwEeA3OL2wAlj5xXbn05FGqTM+M9JtQbBGu3KXpzILVU1kd8GL/taxnQk8ZTK9E0wh8df3WcnY17zvU5IFiMN8q9EnETh/zNybQ3wb7kQkh2CKcLn2jnbw9YHQWKg9Qmmyt64uElHr8vDFtvWeEn4Cwt5yR6A6R3n8eIXF4Ae3RN5kN0UMSpT+j4hPI1LgHTMFgPQjpoJulJxEtbWZsRpi1zI5d40E+nu7Yphi5ILBviWvg1CY2SsvKIffX01qJM2inxyLpAeFKIA2nI5Z1w+IXTCvpRDjIMib2XWOisk6Z5SpBd1zF777rZikFfe0WXX2Lq9KT+iLIcbFucgSTpsPL8Nb12o0vgJft8OWG+Skk3HIQ2pVzwj/TNhsfVPN4qhnWTT/qAUPn6HLzlChbcQlGL/LQuSebmdZSjfdTUrgGQi5lUk5p0NXQeQIVOINrl6WDo4GnZvkKoplof9P8Z0R/6HDhZAAMSKc46iDf+YgexMFJT2jrhGmZuBItq5tyzxxLFlEXyAAFebja3Yx5UJzHCjTklOtc0GF42NQ8/YghMoHStgUB1EH492OiSp6r3PSkZv/kjlwyHzWJNsEomkyakZr6YVRTcBz1PHx1jW3+k4v3HCNz+0k2mEc2mBOoumPcGkqf2PEQk4tpN4fjfSOMkDfG5NcHaHAWOeO0Jbbpc/LxIoAUphWsse7FWIEl7TG393yE1gDv3pk9gYZx43I+rZrz3u9/BI5wtwO3i6pe1yhO+QQ2bpBrK37kPOY79c4Z0pZSjGdAuC2OqDt+bSHLMOnOrRU7oQ+/lu6cCWztlJWmnwXXuVKfc2ye6ZDv1C33mppqMzRdXlTUkwT/QO0DMPX0M4R/lo8gULlOJKOwr/y1MNsvXYhw16aVdaQ+ksO3Qj8I5l0HDd9Megv'

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