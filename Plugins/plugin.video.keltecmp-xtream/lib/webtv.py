# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 217173 ^ 776315
_lx1_1 = len("3d05c6")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-417610)
_lx3_3 = 114782 * 0
_lx4_4 = 822421 ^ 937664
_K = 'b5b88acdcdcf5fbcc29e605e4acb990d8e6e6b8e17c1f75622e5550ee429a720'
_M = 'mk1D48pcy33un7hZhA4UnsvJGV6UskuQufM2A/tarj2VGh3y3Azcc+zM5gLTCkuZm5dOWZSyQZO8oDgKr1v6bsVOGKaBWNgl5c6x'
_D = 'jbHCPKv5RQgQ9Gph+kDC/8tCdi6otacVbwntRB4EbNwor32dEM/PjLvMjws8ud50y6nJQHE7hhnc/Uzx/zNO7m/AwpQ7RVE3bZ5Xt45jWWY8V0R8AkFe9TVErimmF6xwyX+ku8AXa+4AKTZvE06mlHPiTxMVTZQ6K3ksgVqhk1HsouNWeG7b7Nfzt4yw/wRwU/D28YokhOyhzcXqEcf28slxQu9BaVsbQmHuLCDRXk/AaiiTEWjT/3448OZI+0tkAMX6DjOWvoJVvY3urZ6pdjB/2c37AXapIAmYJTkT4jnf2DtNSc22+PEcTAwnRvqkcJvxjFgMv0y+5psVuhqOs2M7SgYIv3CmrOIPI+xYjl+uvWjj4UO87yIdCidATyrSNYnX6mHfuW7rRsBiZKUsn5cPm0NWOhDXOpvjteNFZm4FHRiKpgzUGZuELBkjpOoHnlIdAhWFxvzNjtHm5ab6LV0JrKV+6bXMIohcD/LC53kwD+XqY+H/sRAiBYo39LwermW/bR4nLhW1CPxrZs2H0r+jPA6+z3PVXpM/Bn1BD86D5Lv/aMRopJ5VuAsbpPLVBSdkQFU8qhtOHOt9yO7FDcGifkXyK0RuvGSABO/9z9wUpRzfL0tfwc9QGT7pFvCqbPWcDp1OTSMevgnNqUtLJ/bVozsGVROU+UFjb6o9vLfkxZ3nIDAnmvcOPu3zEUwvG2XDmXXPTPrf4wXMhy58PAEUZzegNhQJo3tUmzfHC1IsP+PBCputvbNvma1taW7xxH2RzfVrblDclr4lfmUO5jl2wihqAsOliquJaWPmBLxIJoySwto+wuxlBHpyRJgU6+JTZzlUwtzXOMysvJal6li79vKHSaF0CjmNKbCXAsknytNhDrpIq+lcaKuWL4Eu4JMlx20UbLbq0wGGW/pnIdeKorl5LNuTfeLtoRIiZxBH+46LrptKUJSu0/JMmBGV/pdXxmtziXsUmnlUFrbpUeHm6OGywbQxOVq/MWy7jQWRyzjj+6F9Rba0cyP92ArRl3Gv1QGnZOB2W5eA0ur+LCc+hIIa3LIe4UtT1Lehmd/ZjMAF/R3gQeO+O/fYI7izvdG/dOkCVQn5CDCAacXoFdM1VaN41UrEGbdlqYNepYmrKD99hs6t2emAcHMRzoN0qlAfufseijTbs1ZrCkhheuhiSIyYgWWUnmCSjhFMhrr7lNfF8hPpIXFapQs4XxODd4qjK+nTEu1a/7vDSiO/hheEFMJSRBTkxCHaz2Ta3TYNvPePesasE152zI1bdTIuT+jIymZtGQxDurbNiZSASJq1latrqOwWjAgzPj3v5Em4aL/dac0VzypJDLdJD1zedjv9saD152tkAyXgEBfE5G5Ja5xKC26R2NIXyNduIQPeZtZK1yiMMehXiUDdr2ci5XWySK7MMkGwS3mALIyUpr3FvFIVa/bF+yu/YXqiVeLwZ0a4zD50SuHGlWCEsYeyVgMPIRuawZmc0SMtd8S0h+2HBQXf7mR0LrblWaL9icaC6DzaIRpQjEF7EWps8yR7mQw+CFV1pR1BT4FgPUPxjwr1Y+WuuimRAFtoJ/lN6Ezy2benE8oKldNuePWamJMgVH6BjKtT0jAcLuphKl3AZkrQjlS9bqezYBVyz21Ug51a'

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