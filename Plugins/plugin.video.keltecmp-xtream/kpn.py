# -*- coding: utf-8 -*-
# KelTec MediaPlay 
# Gerado em: 2026-05-21
_lx0_0 = 871415 ^ 637135
_lx1_1 = len("7552cf")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-892973)
_lx3_3 = 879853 * 0
_lx4_4 = 730512 ^ 742423
_M = 'oN3oUA4GpdL8hn6DDqrl/2q6Fa4Cpr58aKXXpMH35aX7nKcVUgTxxKLXINZe+rWobekfrlXx73Ruo9OpkfK196rAqRFWVvfC84Em'
_D = 'QpuEGN4yDQYSiRMVTQ1u/Y0y9z4GzNf0nES4A1DfO0QCLCtUp9Mx/RFNO2rpFysBvxTXbySx0Fz0ygFhRiKNqZ4NP0etYNnVz/TBEQrszWMYW3XFQxx0JOf0gAEedy1a1pj2+pOe+VEbh/RslYNfeoFYWNmtuoBvleO6w6of1i8Cnyhl+pfIHY5IZ18Tjf0XwgMJaiAa89Vh7ua5za8zS0CalzK6MIjxRHg8BE2zQIWittQR5ryQSSFJ4p9qo7OvD+rCexXNZTHr5+QYe8FiXkXqQVNc+87Keu0w6S4oGbbakPwkWdZjrJjyeVfRNrQwTUkTr3ghjrw/QEZ0RbsGTkvKlQkXuRRpHZ1UFW3LYn0gPCb0hf8r/r6VwPz5+TbHB7VSVK5/39LCWLsgIpz27e+zksuomufXGxupuFbzKbuU4hiZa7cWNWBYPhG5YARgKSDHrHQwRTbajF9ZFcH0p4GM54Q1euQaV6KjiBR8nhc9tOVCiUgM5xMb5PhWodZBmZMHtdqvge4GwqzdL2aD14OP+QvO8Qyc5Aq7g2JF5As2/D8KHMH9AsVe2ZNId/4eHAM7/BaZeP4FyZIVbRxzdowFUqef5SOHTAfN8cYRcNAbJbk8MKcBqF8DWEWbg+qN5xEbJvPhd/x0QMypwILogzhBJUDm3WDBJjz/RO6VwRvbGPtoLkTU3upY9lwpChkgtVA/W1HMwnFYCadIDPAeevpqaTmy7G92rQ0ps39uZ65OsYCdsRLbvsgHnj4QTtiqGqy0/N7ro8su10iHVHetbQXpAmy17QWwNp9CUu7nAidHvxXLg85F/tepSZV2XMHZe8Zl5yW0HER9ic0WeMzh41mdc5M0b1ZnCUgPFJdbffhJbe9fqPlqBJqg+wnFk552tZI2QJV4xKtaQGqMrg4lkM0hEdRoh8SRJ5OqjSI3E+/aicyrSNBYVxZAC9p6nYbGDqZWd8AK77e9QuyjrgQD+5Gvxz0O5HrQcSifXZTBfvV++1JTkdtbU72A4hIzDUlgj2J1mk2om4m6bnzF3ZQrSAMW9momaOnbh+Dipuqub1L3KCYDEi+e7TRBwpR2/1ViRZQEDzPMq+Oiwf3l8AKAdU4fopyBZY+zSnGg3uBcomlGyRjo8HkbUBsr5NgCqWnIeAgZNxuhLQRnhb0gmd7sS/KuBZKq3lPQyPoRCKq/Zir+Z42jxQK+/A+mebBEWy0x+YF4AjhqKVK+fbalw/wdL74kT4lEWfVVKBsTs9a0k5ieq4XwvWUQgVhMjevQiQVFYPorgprJRaslWNVqj1knmWwxJ/IT7THGddEMskE3bnFaClsHNKcEGNA0svLWHfOU3KmfifjoED/j2dkUVyD4Gvza6rSenBfCPAjk6Ac1yU+UmoijcKUG1hQOAfqvimPdNdlvRMy5C0goZjcjZXgpKjQZ3iUi3EGtoajRW/2MR0dTXCPbkysmK3Owjbyau2/YCwkqKzahHBcRhgS0wS3WoO0cj/KIXxaWhPgoIxhxOZO6drjvbsZb'

_cd88=[92,107,85,132,241,153,63,120]+[15,237,143,27,211,61,224,221]
_0986=[216,172,207,13,221,171,49,1]+[74,199,93,63,110,123,198,50]
_b9ee=bytes([a^b for a,b in zip([46,14,38,235,132,235,92,29,124,194,235,122,167,92],_cd88*8)]).decode()
_e19d=bytes([a^b for a,b in zip([187,205,172,101,184,133,85,96,62],_0986*8)]).decode()
_d74c=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_b9ee.split('/'),_e19d)
with open(_d74c,'r') as _f:_K=_f.read().strip()
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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()