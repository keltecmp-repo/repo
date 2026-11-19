# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 160352 ^ 920870
_lx1_1 = len("608313")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-775359)
_lx3_3 = 233889 * 0
_lx4_4 = 284035 ^ 422407
_K = '8dbb00c93f0c4c6ae08a71fd5587a833c1855b518b9ee547ad9e986c0f398c06'
_M = '6O/paCVvjdqOKfEBB0WyZXLS+eSP1WqEC1QTSzIOflv9vrs+Yj/bitIs+FNYR7M2dYbyvozUYtMNCRRNMVl6C/i8tD5gONqK1Sz9'
_D = '=E0dqo6zcqott7vxLAPCuYGhxiy26/rjnQBZ07xPPxKGaLA/Ei/IQgvJVHHxfIe2hwTnVUkc6C4A43yTd3cHaRIWthkl5ZQRFgmHWTvlHDEN63mpbcqKL6WelbraS9Pre1NHg4HZnfQafc756wEjTBEOIlrgDrjymC6T/fmEu4DcHwOxji5GWHWY8BHJG4CVshAiayTGU5oZYHPlOvxP5W5R3kD5Ov5YpPOBbG7zpRoIMTYQKnRU7tLiS85IiCmFGFkr+eiA2zUTX1G/3sjb69dgch81OkZfRaKDAtfvTPemkS9gTVQkv5Ihz0vEsyUbpw3VhmHXlshlyYcyhxsxWxR2n7xelYK+sn/upXE/qNqqdsig+R9VQDvArr8Dh2ktLGp4RmD2TSjqRaEnh3KCHjaZ4qtgnYVEAv3v+oo5GYSByb7NCHXmM6/aij18mkzHfkexmdhKRGPl0lvW7PkpDjQMH3BTj5HNpzDQi8LXiBLx5QOaWMbHBK0ydfSUaTwkQjI+aW7paqukMJ/EWK1d8utPZhb8Ds99Xwf8Dg9ak/Fs1BFjOsi0h80CWxovmfFCCbBD2zZWiDxoBfsv/qyDUC4W5lIwMY3bHpxhSc0QHicFi1T8AeL9JfIqnSHLXHdPPIUUWpxX5TubnNvQHgGOtQu9J3EsIX0jqymya2xCbdXEpKkto/ad8HxQSvEJ/RWSNrGDNJbzO5WQmxFJTDA7Hdm0Y8SoZRYYOMT5y6O+vkUIBFgJ/yldnj6HFU6NkNH7fxbi/oYbei9BGOjJp3q56i6D8ShLXckwMv1pTIUpIw15P7iPgkJUKb3ZiHrKXAR9Izk4pwNmbX74mQPkg4Qh7uLkbMmo+JuMGwypGLM1h3s4L+6qWQaxk1DAub/hzVk6hmilOAKnetQIfLMjF7QyBdO/Zkv2Lnm7xipjbbK0FLp3WAFWeH+FszSC4UL3X50PPPb3m3nxubAV5K5W+WpaKtAAN3Cf7dQnLEAaPQfLbf0eEhFZc9hybo2wK+xaRyTQLSU8Kb/7BT1FmrajoJtkVR1YCJXxXTZ7mfgiFKt/s2yA53WkAPcYhJPpEYQhRrnqW8tPwJ00i+NY/YxF4z0T/Oy1NP+7vU7hhhK7211t/bd2vmeAjZUr/QcYcT69/1cG6OV6j6NkwcYQp2svXPCBwnoR5TC+QteldQwaxRgjzf1p3uV1gV7alvZtViy2QnWfV1OxHE+/aI/0QY8WlA1I2rmiLcUxdVlo4Xdzil/VWOpDuTEgj0rBzaiQiH9eaLCpRFYSAxYt65XgopbzQXjVwFkseeaddCinaKNkNPERnv2wykmoq1m3ii9NP7U/Zy49c8LF/UF8IlJIL+0BUNK5zjOLZTXxWT5Blg0Mj9cpI2zlU5kFYLNSqFz2SuJORE8tBRLjbhr0f63nCVQ5kCJke2xpfH9JaYYnkFKZPJEdwOUHU0LVrmeOWF6IDYM5ecM1YpGj2Gy1f/DRYla3o8hwTlHq/X4iKJXFH4eY/kqaviTwKDQdNNDbOqy++SPyuoxZEIRmeSZB4ycDWg0qqkHraJU7Am44pGJm2Y6KMLTvyX+X/3fC6FQ1HChX3ry+f7PjgEHBmbDmecJCXyg88UyQJQh/8peEF2LxSDcPy0tEIM0BYDNa7gy6Yzhu+ucU2jgWa2kj3WoTciKccA/Zdac7r/REbIb9FizOi3FudNZY8gl7nRbWlc4ap+rovL+JQYovCG94ZyX7lUkFYw1htC2uKuWyqsQocyO2+M9f8IeJo+aMX1qCd238bxK3o+lwqBRaKz+FSXjc7JozMnUVrstoH9hUQOIEs+0t88tYI+LWbcfPedFOzdL/VjTLxoY74BgxQB6Mb0RRXpXpDL24N5xr'

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