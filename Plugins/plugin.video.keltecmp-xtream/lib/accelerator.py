# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 745450 ^ 560646
_lx1_1 = len("f052d5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-571915)
_lx3_3 = 380197 * 0
_lx4_4 = 433083 ^ 225433
_K = 'cda30cab35eb0666527d5971ebf2c7ef91761fa80bd72d7b55b7f04a06ef077d'
_M = '3m2k/QjhmwBKQwfvYizAHykPNbuh2vy9HA1b5bwfy86INv2zX7bbXhJCW7gzK5VIJVs36PmG/O9PWlqx7B2dnd9n+bcL7YhcFhJf'
_D = '=kdI6/9Wb3Ang0/TqVYV0zgTt8QsCcyUz64hD64FhG0k5VHCICdPEs4cUaWBkSySOHGvVLY/bteSofgtUvw8Yb3CFz+g27d53TIF7wuaoetA1qoXuVOrV+jQyHmc9gee9xYyz/RL9i1+5ou/ROdUlvXVt1tB8CGLpdxo75fi14iwngkgfs7zrWOCFdciar8qPep/PqTYaWwFqFcp7nV5DcrnCqvrr4XQMGVY5HsT5LX5Qp5ceUmZkXHLtIKU+44h6kTHDUojbGKGmFvALWvQT1+2wvU4zZT2LdOlJuDWfKc/FEqjfvOk16nWO7nafWuoXfFQRuUUpj+NQ7P8fb+U4Tm6bLuf9YqgTZsV4i1zSuC3OujcbAjm1aUe8QeZ4j/BwsQeLNOXaNTGDGnm1Jh6FXEn0skIVkldQOq2DE0jmmz1BevkX5t35sNAI5tipStG9A1OKgAga9GnFv31QTjH5BSylGV3rCYLXqk65PUtVGFU8pNMvDt0EkOzfCSNxl1yu1Bdd2anykjOJOHqg/CvFJuvDzNBpIouqkh/Nlvzz1kLXHX6+QkTFOPEqyiy6fT7M2W28qV46rJ2lMnglvmZs24Quv3MOpScgDIPocntRezrNhaqrTJdlnmOYuZCf4xSOje87GgBMMy0oI1n/XOQ0zx8ZYukNx4QJRnD9FeEQZRMOftmSDdfLJA/TjAmxR7wBxpRSrakkpnPzBfedpxt1Ta7O35oMk+uXlUkLuqZMg63arJ2Ih5c2Yrh/rXkFE/wUKra/CZ2vuelSy/T3MB/I88Dg/XqwDoLWEsm/vHFudYeZQT5aPrMV6igdBefKkpyjczpOF9tPDMb3Mi7jhcj5e+1uax4PqL8EJf69EgqlD5zASTzL3XXD+xe4UiQ2n/SeoL/IT4Rkx1krqnwmrjYOKywwvHbbQb42RWvciztx2PJvY1h6GL17ANZbw6xZpiHmr2fyUgCVRrYa73O5Y49l+A31jzBBzyGyRjHdh9CmgdCTVkx5RSvmRXCr3ZycqEiCItfmHz3Im05MUrYoSq8NTgiqvZpqSVajbzatCUuLQ9FwNfzr12VXyPgewhT4NCtdGIgy0M8Jo1LjGXtMaXjPrauDz160toOmOKnuSXCsIKSWYeRj7fQXWAOx4Iq1QfW53IyvC38CdQh0mmVTizFSru1bHIlHr1bIfdhs3EUnooTEvdEQJZDj1gevhgt0VAOPZSXCpYITCMqKt92Dwz0UbplaxIxIQbj5egP8OdC27zvzjlg30s03J7pMU92EPxOlJ3yXh1GzOW6E2+VYEoqii4xvCodVo+NybVHykVyilUeAmRCy2mIhSAxXPP6lI3FfRMc1tT+rhEwUT5fnM2+jsjN8XAihjRJcw0dNh72vzCivHnbJmPY50qnSYsSohn5GcNnv4Wpa+RagAY1hNbtQDb89OT2djLcwUNKWtBk3S26gUHnLqk06ka8cYzChWP/gDad/8os0VajV62Al3lRXPsJzNtQlb94DHZdgES32gGPD/m9kdBWWEg3/Tc1+3j5r0FWRD7JTgqfRG9JP1U6qF+cqPNL3p2x9/7AH0hZgy+D/46luhppOvP9qkkHqr+QWFP4KG9w61sxNqXRbW9XLRfdhGEFrylIEDitRTtjiHsjZ9h6PYR5df+PW6o3fiIRZsMSkJ8F38VE6qodOSKj70Wy/zEMDZRcxHICMTLPkCM67rIEShSfdB5XKT1BZ4oXTPHo/HMuWqolqro3MM2nMkmoCNP5FbfPB9YZmY8v0mY+CaqZcZAYluONVJB3FHnRayhkhRZ4gEc1MfLeaQjFsDM9viehAGf1e5OusNBQ/WeOG770SidT'

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