# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 172997 ^ 529479
_lx1_1 = len("8ca4bd")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-989906)
_lx3_3 = 154033 * 0
_lx4_4 = 764194 ^ 345077
_M = 'YnTAqi/DLoYwon3zSjXBLTAwCfBOPe+qz3kW+Swb7W4vc9LsJpJn1DyuJqBHZJB+az9Z/R5r66nOcB+hck+6NXEn071wkm+HPKRx'
_D = '=EQPbBDHql+6Eg0y7CAggqCuJYHmKVkvxQjyNiQTA6PW+HoCoQu86qyIDsztkUD2Pj/8L7iUK6aP0WhN97Eyf7BNRlNiIAF8lqelrEFx7lihPjhAitDpkj9lXwEUn/a5BC6L/oWNnVnRrnFwlK0fuMsc23Bvc+ISMqvtcCuEpdxLFeih7wGIquD10WeKSrlzfLtNariiipNtI33Ukcn9flaymjtKT3fFbv2qmwWT8RPM9Op6ZcgO7klrROvQ0iLZ+W6yi3e1NXk11Exr6x8r/SSVXSscB2VIpoHJc5UhcEroSd9h5IxGyT/247isDxyWMw+TQBj7n7qOoQTv6ONMbDsgKTY6kGPqqRb58qzvV/9L5g/UzCAUcDcRRyTRDVSUI30kQpxm0iGo7y3JA+8IU1V9rWyvi0xJAc3yFVAoOFz9YRg71wK6SLYoG9vys0YVfVKNEY0fAEECDv/v5+pNG20iLrlSCiMj5siKjqTMJi3MJE4O78qpWcHhrz1A4PuU0dKLOmpPf1qlAG0A9S8+bfCpWUtiX1862B31RcSJ2zGqmR+0BnziDfwyZxh087f9CL1UVGDRCfuQgCbecRnKDlcdR9j3xcb/NdVq03sTzLa1YSfSNq0yAlPqFfaRAos3c/dxEe+p4aDtn9aOsrjUhMQyY2nYLj+FAPVxZI+waSKn83Lq+od4aeH0STcDJYmTgx4c0xzDuN5KHJQqZnKiM5jN29++uuQKX+EnxV1bGDgsSKwq4RiYf/sDY2bjy1AU8o5tetgSlP0Cv+GWcn50PEcVif0572HQYOFabHNcVheXLvo6wq1v2tmEbq4of8eD8lnQTwAvbhtwarzbV+aW1V3NZQ84pLrP5x7SoWJ5cqeFOWhFuUXm4esrPeAB4Tuqtz0+VKd9ZBhEWtluu3bxg+EfWkYeI4vr5hz+Udc2CoU1JXizGBPxTCa3xKFmMEUeaB7v9FjtOImFrOXIgMYLNjaKOj4c9BnHSyOn+2UXLOQdJDDocVWFUBLXUi3DtUDdw7qQ8IiUBvktgh86aBWQzNE2aSyIra1JuV4iRjWwzACX/mJU+Vri1RnkBl+HQapNUMVquNmsOtsLjE98AHNzLfl/o58+cGdM0l6yTzngRuZiaIydcJ1kaz60ryr4heM4JjyBXoNzxZ6d8dPf9O3W+wi/IQx3S6r8MbTiqsk9Rhb87psiafXT7aeSX7yfzN5nAl6bE4M5vdqfvxFaAb/PYQp/upWRv7rCk+LRPBE5UusWMyGHStBw5XVDtdOGAGEtvOMMm33pSBcLGz7Bb2ElfObBas9qGngU/ogmmbyd8BE2OGBFcJ1Kk4oeLJd+orCKiVVTOEr0qhcg9e1QllpdOz1+XqUilh+5IoFScpBGU39oHyAjSUHuMQs8rXycnI9D8qOXFkYaUw826mdnkLdCeT1PyWyYTCRdS5D+BiQ1WztE+b5IFE1VS+duVZbCiLUkcHLwDX4Kg2ZOfb2p4G5PmBe6DK4/w6XY4X9OTpkbh1zINkR8ffWhZagmUDF7Niyhq3Ga5D21stQvbOPR2ZtAAGCKQSchWzeE1jcH5riheS7Yam78T0FQQcH3cEPMrDcWC8gV+x/QidKpKYhK0bhQGqPoEfLpQD2B4pz4VfcM8T0PsKcDOCrOycYEhhyyLA0OYO4wcLPg+vwyPzPC82JVxXRBLtGN9DuGpZnGXLCd'

_ace4=[88,127,189,62,168,183,141,39]+[99,17,108,197,205,102,3,239]
_e851=[163,81,176,147,13,109,106,250]+[194,187,160,80,106,96,72,185]
_2c1a=bytes([a^b for a,b in zip([42,26,206,81,221,197,238,66,16,62,8,164,185,7],_ace4*8)]).decode()
_a666=bytes([a^b for a,b in zip([192,48,211,251,104,67,14,155,182],_e851*8)]).decode()
_d636=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_2c1a.split('/'),_a666)
with open(_d636,'r') as _f:_K=_f.read().strip()
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