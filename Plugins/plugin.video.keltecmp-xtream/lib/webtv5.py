# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 399632 ^ 151028
_lx1_1 = len("84bda1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-275175)
_lx3_3 = 124293 * 0
_lx4_4 = 954029 ^ 700708
_K = 'b1082e1a8c6d4493c339d92e139b725745db82e3db78dcb22dcbefd4edb63f88'
_M = '3vzyQh7zA+heAUpx6ksccpzNvnLc8SRADCTWCe2arqjb8fVfDaUGtQENQXPsHxF5nsy6dtqnIB9fJ9pZ6p+nrtyr8Q5SrQflXAcS'
_D = '==wY3dRbNMh1CJMetY+HQqyT55fetj/lCuNDvhG6JqmuifiHEhu8HpdmCL3jRFeFQb/avhqu+OFVnfyKDi7BFWu1GhvV+Ok3DsIXWuZSa9bqXh0FAooS6TKXJcdzWGqRUJ6xzKBhGO9CrfconMpsUDRCcUecMaDZyO8jaZ1MWbvgg4Rw5cDyRCy42mltW2cR3hzzhis8mYvklPelx3rjgf4zwh7XPfqO1NxN1jLwYCqKaEwGPwZjHOVcjAgAcYWZ9dLTVI1aCJTqBoIjVTUTQhLtDhRJlIn9OUr9qtTrHYZgEahfYYn7jYe2JERT5/BzVp99hJRoVC+ZM58+5WfmtwMxzUomFsCRSTMXjHRqmMFp1T2eRsMeDdCGXNMR/EhQRLTahTqOv4PWl2v2LNp6pihmRLhh8pXIFiATVU4cwJI/N+/Ot0sJtKk/1ukHcrptNAznOtP/e1bgSlTPR25DkBEL+MGq626FuNpc6+Nxwu927xLkPHPA3oBgHfUVEfJPDVqzjKV1GJgcWYhIZxbzI4P1++Leka/59s4aT+DkksJjpwn6JcP22Sm9KJMC2dsHPaYEjF3kM/FqwGgliniuFC/mUP/rrU0vTzhZCywdgMBcZqngD+8ijqKpBRdwk03zV78HZJTzgqEut1AaBusuw8AYLCrbdQmS8Gbo7H30NrF0qRcT+gu+d6jqtIacjSnnT6p0q7mLFIrpd32m+LU8xJDZ3zjhAJ5ou04SnoWRhLl7q+6IkEyVZlKt8hemCzzuqFJsGtnfUdRE8NA9Umz2xMW0daW2ZCOc76ojthMlVENcPmSdSHLm+wtZw9+I2AnMCTeuAfIlpy1scEsyxkdfm/khTLDk/ofXCdqCtb6sycVL38FvmLKiSm9oSYc9+hNkNJ2D7HPZ8cKCU0KterE5RSDEsHAsrHaVMC36jJ3NSgGxMuju5m7oB2fd7oMCe+oIKkhF4QBx1Vt78lo60DHCa6rCjsAxS95TLPgmdbQi7dYoKJk4COl1GxGAFhDspPqapjJul4Gy+DDtOeKZYG1XgtMoIpmF52UnOdtqqC8nZqhAyjx0HCR1tSsuee3/tn+FdMjdxxc46xL71tRTSjytEOX9jEAgIC5q0EdXs+NZQLt2ZRQ1xNuSBBqlNMJSF8Jp1W1W0tXk4x6Bj6IwcYWu7P4y8zQbYs3o+pYT9Y+6XmNRgUtmbz0FvU55o5qHJnDLF5oXh6grUAlIERxlJNR75J4bkHDRb2LIhctGfs6Q7sWGP+geKaOP3MeI/Xyveu9wdPKVBn6/jAPlOYfGbWSwIymKddocER0K5vddRHcOlAl+JOt1YCvfrK5LY33jw5l+I6e39HaKOAe/Xk7L/HroqynVsNnNjkOB9JBQy7X8XxuyBvzY4ZzZobNdx3bGf/6WWzjByF/Epm47O1glKgy4HmNKOGtduWPOq4VwdU7eANjeUJIzBjWuZYSVwHfgnEu/m9lEA7Ir0Iaz6vfBBhOhIXdBf9eykLcBUehMN8+EJl7Qws6y4mNZuSxKHeQ9VwNEwqQB1blT/MjStR5pJt6vAr45wHQPKVdyHp95CeMwkaiAe1OqF+yAmIKGyEQGLw1SAVV90OH1PfNZu3AulMLpEYPzI9kH4Zs4Vzo6y+ZGhPbRC1nV2h7X7uSMcZdL/PrWjJPIOUe1U7nPXOxfZFYjcghEM5QNjRtrZjLY44qeYWZwE6O1/pVuUBtGRbsKrqMHwxh6qx/krXZpzGLnSaLKn08PxcAT1Ib6kilriy2hCaiGingp8B/nQ+OtuoxKYu9TIq/U2CyqKBskZ8zfSt+0rt0O1LkmcTq495sUh5NgdHaifhyVsMtVqfqnZ/0dYwDJ'

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