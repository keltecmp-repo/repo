# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 436212 ^ 485049
_lx1_1 = len("fa240f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-709521)
_lx3_3 = 706907 * 0
_lx4_4 = 352232 ^ 505370
_K = 'd325143f2879c8a72249b37ab8b731b3b85fa69933de2f81a97b6c81a8fbd0d2'
_M = '7iu/dnMIpErNikOHSm9Xqq/lxT8UomkcPLTtvz0XmLqsbbg3LwGoGJaNQY5IblHw/eGQbh2haUA447y7b0Cduq9r7zByU6cex9tA'
_D = '=oa97BSy0/fHDI7T/AfJsOIEoR4tqrgQnU9A/8XAIdFHrWSm8Aif+KTr9P/FKQnmDGtxrtIbfqstQ/X7LeBjTpUk1cGM9FusMEf1WtLXfq2oE8YVHCZjHbhDpVZITGXKApG/4CnPBc4nkRKch242F/wPKaoa8mQwbq/+Zry1+gAEyaZnNkWpKyIi4OlXJmuTthNf1urXPkQvrVKLYLaCXLowFOirqC0Gan29wTCTQMCBtkzORueL6ujqBqB+eY5l0iBfX/DNQfmnDDojUlrh/S66DWrDdqs/B0p2UcgBChnGl2OAdNo6S+gulj+N5Oj91xZYDk4o5RC4etA3h+0xnc98ZJ9C2hYXgImSDFyLzuXj7su56WL1mPvmpnvDitnKy6g4/a6Zpr6YRtuSPC53as7MEk0nC+F9aCs9MlfJR9g//U6yBQt9TehYWfOQQT9KzSfNHsnaGarrlFhWaCPaRnkJF8laNpcs4CPUNDapSoNevQH1/O3KA1HIR4a1OHaXuY4ens7D3eoxrBqXfmAXAq2v0EVpUREic9zZZHRXOcbnFhiPYiHfeVf5KfrvBPXGu67wKJ0/MO4M/J2ay3ul7Jm6AF5nNcl4P/G5QZy0vAwkKhMz6zldKCoGHPXxywOkuu4H+e9J9hPUWZGKFJD0qB/evtll6wrDZ4/136FkkeKfSjxk0hecpri5JSy+21kKcb920S3RvbDHTETTfXmqlhfTP4o6KLDJvvyuVOPHYWZDj7gW+wtjh2ebzq8ihBHApooluiE5z/CoWdUt22066GZHx5WagOPBSpJl5mXVvdc5zwsnfY8+xB5DufInZLcWkvtx7faqNUWmqfdVIItGvkGOo+N1TMQINLRFJBWgyNS07yyupT6+E8jCtF1eXgLf4c75jwsu8LsnWUPxt9WHP5Ay2Nv+2FRlcunF1KhWeFlheaiaAmMtYX9Ex2RmpKXffsodHzUgPMmyr6gKlkBMsQpjCeCegoYOSMQ2K2z2pky8pChloS0jd7rlTUrwGxQ/ZNZZDeOGxx1VPgJrKmyNdNCJhUhI1Fo0hZxVTI4tbVOX5L6vUUOEUsOwe6YFBI/9mKEZJEmxlqZaJASrUOoDyo2ucKGMcNYup8zbBhIv27do+uLbMTky5aXzY3SSfNW4aJAFqELx3Q6Fp6cXLekyRreaEZTr8poUyGDk+vaCqcfmRIxCEEDsmLe37uAHiY3Od6Gg9zqP9yZ4tTtSZKYKdlY81vgD+dvExreczhUsadq/bPKCxb7VRd6fBKTvlFcOIiBbzqHAhy8banDeA8RPFHN8M/WUQ89AEMK0HoWSEVT4E9iOzN+lG26aXnpY0o8TjwVDR7dawVC1cao42Mu5f3cm3Hz/dNBCry7wFGWVChb5S+ppnF24BVMRyA+Myc/vmmLFRppV59w26gXTevIwqdrGqcL3LapjJ4q7WfIDBUIZ1egycta1CRyrQ2IxNhJOEX53fMNSzb2maM8AmWXHu9KsaGjHZ+twEB60wtO3wzzZUmUqdHcBVCGYUFuDMf2uI0QaCzogrypo0M/MZoAh8LouukkApjzWZ1ZXuVIUqjOvlbYttszPQkf2jLvpBCLo0Ee+cI037tEwP3ZcXPgOjQARm1lLjjSHeVCO/2oeIzsH9HSGj3YbmhL+BaGOsa9ytns+20EslSc+vfrUrIUZH3+EOzMqi/uEQfkebD9xAYAIerAduXENzEB2i+AWhw2FWysyLkY4odZ7ONTxzToyvYGNqJuCh8h0So4i4V3/nIMz5ormUUS1VCTIK8nLU9poemhxfP2qw0uwYG01ACoZBnKQK2cwcDdMIkASpvCCBcYzLzJSvRkJ/Ee6MEyxl+8ozwVRpywx'

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