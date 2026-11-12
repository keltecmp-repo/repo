# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 820752 ^ 616685
_lx1_1 = len("91dbe5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-315717)
_lx3_3 = 264254 * 0
_lx4_4 = 941589 ^ 962693
_K = 'b0330e5f5e883886da22a31468e21f998371d97b78d3277be0ef60332e99c983'
_M = 'dWEvilUxs2r8E5lD2YmsXhWG1hUzLrF25K2YsMueOsFgO26FFyvsbqMTwUiNiKsLEdWKQGd5v3jvr5G7n8o6wmQ6OYFHcbBt90XH'
_D = '==Qaw8Bz7u9uT8zA0SmsmJBrr6zr/ywJz4OsPJP7SBQzuB2DnmHe9tSudk0cBfKTEH1TFW5keAgrH0wpPZ/Hrz6qvS2EHy2IZ8cObML/6iXAuHlqSRhxGsAQenfQD8PO7Y8E42MEqGDPybxFLjw0AaDev4hmQk+a6eh+N/6W1vRBU2yNXX1WjG6Br52NjPISa+7Gud9LQpALwP7dXjk3cWFUULpyIM7S+Z9Tu9rDCPpjzn1wm0GKcV/9AkuR1O0oHRn9k8vOV54FYHfFAb/fDUS831VMYt5FrdsVXesjuMP6ECzOcEOQ7mtWkaK+OvnvsB8um2fhy3MJmZXj/dcyhiO+a29tgxSwWk8rd4+t6Ajhr/zlBFr+3sds10aLbYYCDUPEWI0/msrPsZllBvq/UvLF5N+4kVVAMHrJQb/d+l1YnPrJBFd0/NsLMQ6V6Wy0ehRRDdKiSd8Cs8hhRcgaY+P7oI1CBjXQsIDRsYNDwid0gjVEVtWzZDedA1FEKOTrgJLw10cdwDU+4f26NjoBUSxWf5WmojyTFAXd8DZv9/HA14XhtwCliRZs/QiCXe2HBIo3bKl9WZvnaTITgbH08S1Mon3++s9kZqYZX30wxgQwedPQy0ll/q7OB4Ly75Nl4LkphR+/iGDFGTwrX4bqOwMSMg5FuTRxw4FQ6DPB2BBqrHBMpT44Pb5DLe0HMdvKApVbYrAqTJ81i3ixUNpR0UKRJKpBEPKfTuZaoGFpSAzw4a15MO+FHFAAJbGJ2Cnpnalk+b0H1xdI/paV15X7lViQf9E5BX85PYpztCQ3WB3IrE9yITM4D3erQw30NxBo0NQFkGWbf3+XYzUHj+IoY9e4cDxZJbXoEdIlHI28O34n23A7pfdfPCZ52JIywcYnirFLmEcKZPkDGlJtFB9yMikfENNE/teS1TrbsrNtmsRtu8/9JJb3Hk8fwYwu3AVsAuA+dM8+W5dqOU9aqP8Og1nWqF2/vWDdRUBxzmr9iHFIzDiajjLXl/QREd02zZvhVMjTC7V6TfBDsQLy+uryQZs6oyJpYkHTu8LFxM6zlTG+QV2WqOkNpQM7rxr2jxU8Mc+rjyaXvsNAynW2F7fLejm4CcA48kChlx1XvmoyyPp18/oJC56OfL1GgnOjLzJoYQeHBMp2kgJiTs0zYFywtNRe+jSmEJi9mAFPAUGZiUaH7H9uwMVDe2Ejmtzf+tZ77SDpKTmIFrXZReqbPsGhnXzfH6H+LzcUNxx4XtEk2F2znHeK/ItbgbA+sH/CPpMRB6Jywmzgzap4TUVa8D66ieVS25avMKH18JkelL+EHjdOo1FCMXjIN9zdU0Gf5z2amsyRbj3nc2iQsIqZAWAaIqwGpoYvGpygM0Fzjs8q7C+Tke6e3LPpKGQX2b3A4UKgkYcIJF67Z/YxJAjVN1R4EnuAGfXTI1cNYxhFXNJhpx4sjfotOrm8DYPbkYKNAWHMid7Vwgge66fBBb4lRCTCT2BvJJ2vaXYKbErasNFtE8m/2+EHcAW5bEPiuKmyUIgKXvUT0sd7878rI6USpatWcOfWV6wiOpyQjE1TIO0YEFcEayvak6eEr9rfJrb6T+IwmyTWsb6DFga/ME1x5/mvzpXSlRu0ftbXuAn756ClLzzAI2VWMtqw4W0kwWfDAYY28PtApOv5g+m4+9DYKL8Ple6/CJYTqQOWaTA8XJMb2HcETvOXTXPrm5iXssohVuPiooaz6pfWVBSQh2mXbHDCRXrNhOMGPr8J6h9YuiiWzri3P5hk1Vzlj/d22Hd7Re+fUAzzahu8/JEFIAgg3kPiG3H4fWcDv1QipJpTZNw4Kt2Kb1gQv6MgPb+hY1/o9fwal8LG'

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