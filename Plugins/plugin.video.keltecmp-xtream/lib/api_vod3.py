# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 977357 ^ 465143
_lx1_1 = len("7bcb1b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-832328)
_lx3_3 = 852980 * 0
_lx4_4 = 477070 ^ 785630
_K = '999c78ecc26478c950248556592eaf43e85c3b30831e4c605b89e7ed89e23f52'
_M = '0OZOZGSkkHI4mXmw6fTER7XLH2g//RAqeRxKjIGZnhuXtkg/MqOdeTGZdO69pZIWsp5BaDryR3stFBKLgcuZQJCwT2RhosAjMc5z'
_D = '==QJ365FTuxvJHIARxYFh7n95Y0+KAaTAIBN+jkVWY3SlLQK0QwqI2o/Bc7gL6gM/uM7dY/H+SJPjdHXNvE9/+o5O3UT8gMjLURGjk9f4+Mj+viFYFGF70tDYRAjmz4nT4qOU/OAig8n6VAnrEibK8XjSIq9e1dVdfeZ6hFkGkA+Xoxo853D734H7yHVe42B9Wtuk/SFNrbrZF5OTn1YEY82Xf2XpW2z2/kQHrbHnufZyicxeSZV0sjjQjHtUkDNp/QK/+OLHLu0gOmrYuFXq9pELwEHwvdYhXFOZoxDM/l8icqVidkORei5D4JlH/qya5KeqgWCUOdSKeJ895V/F8eOmTDWZN95xEluOhCc0Yub8OXkP68dTWBQTm+EDYPk1Mo6gN2ogPoWqyaF5it4eDlURKqv5/BXQQTO1GeSt6HN0ojC3adNs5oqeedf3CCpvMirIArY1JZNFUOynmTl6Sit8BqXYxFHske9wRpx5x2+4D88I6u0mVOnXZLyuo0iXDDY3cuTxdgHIvGEmJAbHniJ4cCjeNK+wH9Jo1lZDKkF9SEmGWTq6VbW4Z9LVhQl65JJS754uzvRMLe6TtqmDc631973NhjYJTdfLP783RRQzddlwWqC2y2lXDodPJWXpYmRNUyuEJdy55g/o9Vx8VanQbNu3EFO4FuQlfP7L1VZvu3f+PoPsBShzK96SWjrfHx5Izc4+auNU5j64Fhh3pVh5LEl+vMa0s+2Gs2WoKMUvfiSXMhIreOvN5ysx5GhiGEQJBO10P0NMyf1heVWxy0fKUFe36KgBNAnUIVTwCy35hq3cxzTnS5svUYxx9emO9vWs7WVX2SBT3DLnxG8grhbrk9l6Gh+cmV3llVimaCc7Gk/Z6APvpBFJJ0kqGuHFnYjg/VnT+CXVvLl+s57B1NgU2bVbsrKfm+Ru+jFPjOlcxXBb68Cy8YK5VGzSlYSJMehpSMp9EQEr4btbVqX9taveCz02HGtgaUX+FDlyVCoH8PsXkgbHDVIz7BbKPmWGXmTjECYcNcJjJ81msB57vbAF7KoBi5Q4h5hi6KhWxF9yipd/7IZ55RUUyLSDx9Sfyb/BTZ+eW0rT+/c0FiHd3iZ3ueG9f4/AVLYE2StHiJqP6JtB0gVf4RVrX8lXl2Xn0cyLtcXyDkvhpEK7ZORQeTMTEzkVOsx/ZjCQ8B63AW8JZCUeT4fzgMQyFzxZv8VTNGdQWXWyYwBRAWQ8ICWlR/X+v5RAbbp6PZN0YkYUpofjOuhGuZJnCTBMZMxVT14j2IDs9aCW/NbzpIPebE8uf9aq/TIQFmzwwvR9t/JxSYg1jdpIgv571CGhvWwSwFexh+PYex+m6gUgrSVhIxFDN4SRz8gSfc6/OpUREgDClPYp4L9AH5x3S17bm6jbdvzPHZ17vYray22mJHNQK1BSZwCKOEfl/Pw4XnxSi13DHXt3YG29pV/nmMaZjijz8eXWVnkDibGgIl4SXIutfUrsfRzQqZG+J2WFO2QwK/BR69Mufib3p4rsAQh95HuFdY8AM2gq9/n4yhpkr2cL0SeMaXqd4tsT2G5TPzBSX+zBue0hbY4K3YWIf5xDEejXunSl7B+lZB1YkxXxXPhyypEDgRWWq7MI02xtITQgN1Iagg5BBiBm1ow9vjmIoUx6iBvBwdROGFOADVJtc4T46WYaEVkZm0lpMtE08nOhVEubhNltxFrbnS+CU2Nvvzl/65vaWTYxiPL2CYU3cByDq38mNpE+T4GmQSs/ChKWX66qUIm0r1xcYBpv5gb3LRbb5G5hWns5ND6OJhHdIi41v+9ZFiOLQyR/f6euhrEpOsws1AlqkBntGvH+qsBNxkhPx4il6P2dsly'

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