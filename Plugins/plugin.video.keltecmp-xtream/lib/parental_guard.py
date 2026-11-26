# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 770388 ^ 187849
_lx1_1 = len("706a24")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-774324)
_lx3_3 = 925148 * 0
_lx4_4 = 234730 ^ 563386
_K = 'd42d694a5fab0bdb922631f40fbd2c8e21b0962806eab6d42aeae23ffd40ae1f'
_M = 'Xp9IkN6hWD0H6g=='
_D = '=Uo9BiWNO++klAJTa+yTpHWbp/VbKGgYDGjzHNDRNBF5NFQ9v/rGFX0kmnM6Jhn9K6AoB6iE3gwhS5kw00YJa0FPmKvIbcNya35bO4tJOqpVEIwCGequ5n9sw3HJmEqscOmfw1hu/28EsqOahOFhCQhRcEzOSvDQWG3ZSpManE/inQj6E3CxfI9TRI33iyXqYG63jK/lmlIh21joo+wQrRQ8c52f+0tlsLY8tEUscEynwKUBBgqoYlOoYCcYZc1plb9HTPbtW7uLX9dW9pGIb08Vaj2lrB7ANBmNE6RdKF/i4yfJTmzDbOTzLwhUF32aRfpIYfpZ/LAqe0Y9TEePPWKMgUlkvOEQGfw1/DZa3LZ+wOTckR37lVvpfDPpMR4fh4TmnvN6lXpat0VcbZzrgmr3gUzltJUvYRGJnd79Xly0eOQrUc/qBb1YvdrNyQ2e+L2qxkfquUSeVaVjY9togWixmaardH843aV+qTslbi7gJh4zuFn2hAnV82c5ZxM1dnGlYhQYA1pVQ/g2fD3WWrvnaeBYC0w2lHLFwtjQoXxT2jSCx0Pd0n3KeqkRnDIWlS+1cC+Vobpcl3X8fuAl81JRNl53s/twS3/kIRbTXKi5fENAx2C8OQMOM2TB40bLlAsxf0mruKAmytY3W6iX5c19IORKErqXWONBbE7Xqe4vH1AIF2RHTRFMlSoyjgNvkrQFFSlgYhu4AtgKlMx3Di9OxS/CGICJn/qB/LoJURRKlzKdoM8efcM8P73wM1FSY/vDuEIr181wB0pkRfto7nEegKl5g2rSrkaL2HcSM1wqW/hM1Qhmsgw8Ew2YUBvzH9allMW2dXcuk7Q+gOX1jd1VVMXkyVTOhAPFpxwHM94LBa9XcnreczC37eCmya1E9gejSGpGj05HZCi1S66oy2aI/SjoV0SKgSHsf8gwrZjH7Iax2FXhIEbaMJ1QYNXY4Unw/+w50SAdq0KLrocMwgSjI7Y+wCl+AvULZclEzi8g0uK22LSALmkMqHr2zx+sU9lA4ZN53pcyLIei0a0szUHLPhsoOWKZBDXdKnFJarplwXhtvReDpvTQ6WEh+PkUf8u8Pou73A0SXiq8lIaKo9zMUu5FzMIvB0uYtSmEiRZfs+k0g4pVhh8SUGEkYnqItWlsNbL/JHmb2Sv9K36ZnU1+HCaNBMJr/ubiIjKtPAAJ/xK9kVWNdz88Em9T6vvzzNv70dSAYI6n9cPKu7a3ia6VsJ7xeVcGX0nWdrJIBOr3u8YfykRGPBa+B0CP36D9hqZ5g1w/MYNCi8d/p1/c4exJABrMfY+5/7IdjBbcPNin6IX99n0sNkWZBVnDgyjWZkKZoiijnTsKSlo/3lhIZkJ1ddPHUN9wX4lFxH0u1WpAd57UqeBwGu9xe2QfkRWRE9vxIRyr1/eCloRBp5VKSzR1Slax1dr73QWF46LGqMd003Pt3QlaNeAvBwJ37ednVVVcM4Bf+taao/maDgOozHgGmPkW4vkqNsnBKxjQhI/FljnITFESUdao344J1TBUYdS1+/rqZ65pUWY3a9j8lrWDJQs+yXUjaX1MAJqUSZ7Z+JkYHKx17ju3zTR+a5qnWHLAxOhDLftIvvol8z85GZFHz1IP1JhYkva7na7mBhnHQpsPZtwwMMUs04qhL83+DJw0+A+tShBVgOKhlxxMUUxOLIbQlXIaew8I5QXI3tdpTsQV19cXEuEo3qmZXFzaSuL1HsvgDGS60JKxhX6FGXzkVUCFSWDeMUfP6+dL6yjkdkUt/2gi+fB93EWg5+U79kiXbXVqFuqNxsz1zs5OoqngBSSh0ECEi4ky'

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
