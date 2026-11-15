# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 341979 ^ 496681
_lx1_1 = len("10e5a9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-747950)
_lx3_3 = 765579 * 0
_lx4_4 = 893717 ^ 467024
_K = '914bcf6e150c80e6d59e9cbb2aa9f20fc4c34181a8f7f86a7f57d10401d0d47e'
_M = 'J230PA73Rl7he+sOD0Kr+muASY86PVay+B1WWnHfubU3L/VgT7NCX+8q5w9cRqP9P9xNjz9oVrn4HANbJtS4v2RypmVN5kRZ7Ha1'
_D = '==AcLJ3yFejRm0LHuK3h79kOXwNtbvtqcTFWRfAGHnoeKJv4/XcJkS7ycP8hl1StyTrYIiuWtRI8eAJYzvChfR9ph0BKKU5goX8mSto4rhDoZcVZKHj5g7JT3jdk/bLRG/1Qa4ai/IVa1m1/Gh4Ua2WIeauqZ47nbGldAU64iBO/KRSvVm/9dp2t24eYE6J+DKdzpSawh2tQJuX1/tMZSok3NfLHHhn87nhTZkrVdgB3KzMzmKT39O9YRQrTUaFxo3qKeirkM+nT4l+dsk0JLPfRgVfsnbspm2JkRyxG4Yn83WUpisK6/rVoOH2gNCW53SxheE3eloJzL9prmirNVxeCm1jIH7JUr6kTfX9l4oAzKZwaFf4jCr0KQ8Luw0mPbAjhpS/1sIwlzVRBr8k2uhR7DsjntagRW9bT3Z/r00GWoz/Qvyx1FmleHHOHIdeRSxp01Vc3/u12SQinbRqUdGaLi8NY1sR/fTOuHuk9qu6FQsGSw2KJxm3a/mDddDu4uM2HWZB+k1KvKOwBOqZGdt/M/CfxPZtJFtsS66R/2rwSaVyDl+ifd1PZPFaE+DSfxvUozC+O34NSKQ4rklHp9hdHzYAROC3Q3tQcckMytdTabQwspDYCQ6yprSR9gFW9KXtBwpnMP58ehOuzNHvxptncTMeebAvDvEjeJzhAtCUEOu1T4ofiBBoTJ5z+JwHkcL/QYhjjCd/cBiB0gPWCXqWdwJIf8hDvleaWSl5aSzGZqCW7gvuG2cYlm+4+YEFNeS+NohqJdk+Xnec1OR64MndUgow7cJYSkMG9XLzDwTLzmTzSkX1ZDI4jhLEfD2JvtHcVpDtYNI13IhEFRB3ltVrlSmwzAB8znnHbbdeNuaR+dK69jdUdUEky3n3itRNO4DCHjX/Nvcadq0dTKB4a+LvaAFjZ+EnPQqazgKDAOeBMZ0E1VvH0Uy1hyxGajgQCLkkXzTHznsfPBiEnoW5tVYb/f/MiCdBcrmnWco4ciIWXsUZNvtJ5dK8pqQ/ZOdVCWRLhwHH9yPX5WptObV8LwoBUPpnVqfMAFgopn/m2OaYSyY4ysmDXWDIqUhvOV3HNFAj0fGPSasTpacS8hH7wIv586hn+AOZNSK9okVS0WwphJEt+4o2AwH5RNT4OQbkBhKTC7T0biX0ZlDvNeVbaaK0xK+YldsL8DpcQIfatWUpftFLuecLGS4KgorQKD7reNBfT3mmhGJG4oqC3xM/psJidgJzOkOQFzGrfbI0+Au4cp+oMM6TuF+4lX+/w5ZtkcDxz1EoJwBShUKqlMN7pN6zALPrBPS+Ro2ey0pkGrOfuQ1+YIz2NqCqYp/6JXI2pdRoKAqftaInxd+4Kpryf4a/z4TikgKYo/Hzd7FaN5ImmCt9QwIczG012gJR+uuK+rOH4KnCXXj2W2d+chjMP3lHTYtKxmbQfgqxl5+Hrq/j7xdRMRDX2mXlwE2Ab1hvALpab2f55E/eaX9kFvSjlnpMCtzge8t5JbcXOWo14FHAGpDAgONBwaAE+OT0QHMoM+0a2adn8v9iT2qaPOcPZEMPmBXYWY3CY7V1I1yKBZE8GRX6u/cUkJaq1j8XN43u7bSATNyTzTU1D0u9kS5gaK0ny4a0zhRlGalAMGeXqHfgd/7jSAuasr57GJVHvDkd1thaeGHdRYQ70tlIt1V6ctFyY/WX9pod9oKb+Bpdkk0Er9BpUzeboTRVqy9pQNbaxwtUqGqtarb7i9NZJtBEQUR5rhG5ECBfoKnQsAjdyUCr0+YcoID3RrXp6qpU4uJNpnGlVKItacST3dWS/0Ywj0nysAvUZvtWbyrpNFIeM78xHjXWFKXqL71DmX47u'

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