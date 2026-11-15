# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 223860 ^ 912432
_lx1_1 = len("796c99")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-805443)
_lx3_3 = 703672 * 0
_lx4_4 = 296006 ^ 710970
_K = '00eb7e86a85420fa84d7db612648d622659bb4b663ad853425adb0bf2e711884'
_M = 'XbA0hneK99NDf0pd71frweevbwI8CdB3biul5RQBv1JfsHXQZN/z1kArEQnqWr3H4a0+VG5V1iBqLaq7QQTuVArmINJmjKDRQXgS'
_D = 'TpeRMzhI3GklAWzEhA2GSPhQR3dUyJ3ams6Rawuk/E2dHllQ4IN+5bDQQO/lexyiRWEzlBGPCHYGR3Fo+RGoISXT0wGBuaKZDWLMYbI1MmY+hfRceHs9AjJyEroOYHAGQa0mmLOugUy2XlVjNbdcAoJ8F6HKUgfwvxBcMHEHEFLZq/qF95Km+1Ax4CVHniGN3rb8TEAwibiR9idG3YtcXcog14CnoFn9Hnan7JFfW7rgKpPV8wWJD9ht9dS0v2JlyZOx8f7/ad6Q9rjN9HNdG9vQKBqCfemGn/isMJJwET6kmvaeiVvJb3KlhiE4tl7L+4Ir6rAEk+rzd7ZvjDtv872KFEbaCbwImpH2Ob65BBsBzcJLoK2ow5IZh0e4+O3ufB3pawxbyiTrb98gZmRV92LSMIdlM1u1gUfuQa3iMX/SqE1IUcN/fDD8tuqa8Y199t+rAkMGe75jDuELX9irwkMqwxdEg9OfD0cJYDe1RUJAB4grP5s56LemExpqHGx5uOd7g6Hy6G1rpfqLySteLrBl7yBhW+S20SSBRnIzAMkwszNns3Tr8b892WQWzf8VBnOmSmzIsqCGn11ohstdRKCITtgmubaaUu1othqBI0ITIhTVoFICudDnWUaWmKpHZHFEhie8xehJ0Y1wbwHQ1E9/bA5zJK5lGV0TBwiu3GzzgGUhq+NgnLPZlDBY4qSNYOWJqypp4pwiovkFf8WWWHSOPwg8J2o5bTXTSa4S7dBF5QdDNdohsJJYY1o1dD7PzXbGq4F448toXsVKzNThPPV2Ay2Ha8vwT6tm3ryLalSmpXBUXY7KPye4M2QW77qvXpogUVa8InaiXoWLzXZ69U878391pvS6VvSQXNO2F9hR02DjS64TZa+dzBCc0zIqcfsx7MLyZscxoy+Wl+jzzzVH4gMinjhaLzPVykUlmp5/XpcN+XQWNk+xff5Vyat5vrQxQ9+Nq0NvRz8XhjDNqNTnQePnahzFopWkdvE2rSSi4e4Fq6+yyQbYHyB13phh6QcRRzN6w6rS8rnelqjq9hnzFAsgm6s3r6PeSg57sHs3aBS0Zx2TyX3A6n79x4BFZaOg1BoFQRwCe7cndTXtKXAVKPdwpV17RxYHQPxoE0mxLzg2OB5faB9hErlAglG2JraWMCA7rWE9BNSXOpCYZVl7Wib7btpUyG39amw2Fkm3KTT8jq6I2mQ15M/BL7u1M+bDzjv/HBed4aFvVtOvnORap8uYiVkZEcciQMtFCBKwzRuKV0NwrRTkdJePPiYYoW65ethRAemp00tNp7EfuAbbPK7PVUXRBB24vHOorpPjY7GtdOfnU5n5E42d6mxYKcP/PRWhsHGep/CTurXMx285pcTNJPFzIrDQjAx3fhYUG+5qPJhMYT/hGvOlxnGiECgSRuAZuTd6fZ66gCPSgXkkNVWApTOlNDBsw7d45xKPkzpJhTltNuSOmk0a/wa2HSFkASruru2of43gFoDjqi+OtcPKV8m+ufhhbg4Pzm4Mmti+D3LZi5tYyzpk0Jf/Y5RKRjP1ctXdDfysCVahSuyYON5NhT9XOk5KRcwW6HGepEPeVc4pEBjIv7NTjDjZUXrqODabpjfRtRLK3qTDLwdQm/Fbar2Ob8z0H6/aMt1p//1ezyHqGI1BwsCYEtoqnHicPF77CivZaUirirY0Z/hPFRfrzFZsNX2UwIKC34gsL2mc2CyV6oSYfW/ae/rrPybjWXcxaQnSOujd8OoI0bKiBXBFtBmvTH3bPQe23upo/6ugXfwFVuoG3jsjWHEoxbNTwGPwJAn84SJfPoZsFQuKcoJcy5XUAfR7lvNYMeN982+9xu7sKJQV'

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