# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 432567 ^ 184480
_lx1_1 = len("3e8538")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-142382)
_lx3_3 = 222813 * 0
_lx4_4 = 735293 ^ 268169
_K = 'b0d881de32dd072092fe875d10eb8c5d4a714e59a00854591bca60309351c95b'
_M = '2e7eNGN6UKJGrL/uXhHGJshI7WKq1mF+6rfeKY3a6CWE4YkzZWsGpkSp5rpYRJ10zEq0ZKiKMS65tNZ5h9/tcIzm2WVgOg3zT67k'
_D = '=4tmmm+Suv+lXts0uWhl7Adk+DabtE4MyjLJdlLBsK8+ZlptbbjhtxBs9bYSS0ST0QDuNn7DKnKhv7RTreSjK56+LdIvD7vgnR6RoaiPR5Qbe9nUNpEIjHrWUNOFFe1j9iWxNP8SfYpApJqgojRj60deC/IrORm6m6XIheHuEjvqYwTWdmsqA8gnO1vyi9A8BEXAQVoOHDXHmiYQTIYD9aguxDGn29uKWEtXkKQ6zVMOmZtYsR25mfPXFQCK8lS6iveu2WG7ffwRy25E4CH2oQoj8GcDUDCVV0jm6mcR5ltv6sR4a+fV4VBgAHwiv6zEE6x45eIwIaoZGN1YLtOe0ryVaZ0OPdTNaR1vl5alRpTzqNwUHeaxjAGO/70HFxC3ZHYkXiOELcjP31l165tIjcv3NMzv2RBj+ww6C31roEvK8mvmxFEsbecbRuZs5MXKWX/aLkuztF3Znr52+zyTLL/b8bd9jfuKdfOABhpcapDGIxEDGZS874G4IQnu04Wxht6lZ0rQbAqRzWU2Rhbj0SNoBuzdzz8e/7oEIQC4f5FjxMotiX/h7C70v3RZOh7o3jt4S5/IaZVj/shEZyATOCyT4mJLrruW9PuSu87Wq3CO5qcEiavXl1glQzQD1UKlIbUvrP/P+nLEJZ33wUDyAH2szlLjR4O3OnQbGhWY5c8u8MvF2T6q2V7u4YNzBchw8nj8HilUeCLJOBR8Iql2IkdWXMknjcxX7JDB+6IycMsqGDJeKG8FPdcoQYHCslq4keak75E749yrUStov2Hhcffvk1DFkkbGI7KS7nmvh0oil8RoKv3lu6NuSyfuS6clX2ZuuEN8mDk4ESxcXXcNB+ZT3W0ToHRb+/Pclvs6Goknk8SLP32rK6C419y4KoKK/nSNNrBCptpBr7OGSqd3HZvkcQomgIgDrA7zfZzODA48dB+Hptp8BmWkZQCKex31iP1bbkGPwLyYiXzcjd04S/98d+ftbb0EQyCP7pxsJJ5yW9OW20HxG3UAOF/rZVqquYPoluETfyovXQ15qUO4ueLR48dptYyDia5gt+NTq/ZGonKr6tBSYfQCGES6wb/TdbF9Gwah6t855sd1dUiBPn/ccjapzaj8k+Wp7ftQqFxF18PT8RCRehzqttLvpq45yeaEMgag5X8p5somdM3H5XREzrfdZ3nKDwfU+skVLmnQ84PxY4O5PqJVBQKpW9Vca7TmmDq9LNiwzHJNyZZj4TGKQKj1k20omwHPBMowNfGI0Q6e9T0V7zzJMMpBld5JZiT5oP2exu5PotyS8ZqNd9hAff+lKFi2OBoVAPjwoj/W7mScgHk0X6sEF/Ad/oecseP3GrZ9bJTnS7fMFYBom4574joNCIzMZC1KIpncVclG8lVo8znSkGiyitBAHOqX/yOiMq6WZiEcOcNIxv9i3qmI+O1XHUm7VTVqlSKM7wiIAlBp2eaTsviObF+FBDwHedvflwP3DtSumCXn30yglr2CrWd+pKiCUCX7TG1e3vDML26awbldOWemB90VKNck3LlDPs9JEIvvGR6sC911VjqbH9U5oX3j+PZUgJqgZKY7a+5PX58kIy4VS7bqnEwfcmG4kmn5wl1nV17d5XfQ0Sdho1AQ2E7k/xKe8E17Z67E7WtCISyu+kwDRDJddjoCEk5hqenmSlWLP8imrftExPtglN5Z9y/A8m2pImCn/wpSXZDxi6YQvps8XAENKVLtCz+tUbn5O+oyAPv8AX+TPUi1AcPQXpzXh5xqHPjuZLmrZ7p5LJFLtD8aZ00mwJXRDvddIbXO/2wMzVdxu/yGdI52Nf9WfuvCSs5z66BfszmEcaGvCeLyxSsrX4UGmPrPVJhpBoWK'

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