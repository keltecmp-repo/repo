# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 187365 ^ 517641
_lx1_1 = len("94b908")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-427785)
_lx3_3 = 929875 * 0
_lx4_4 = 860517 ^ 349702
_K = '59f5c67519091761ab945115cf7d91f33f5a5434d647a97937f3bcfb797b75db'
_M = 'z1aupQ6anBVNfd70LhxzBUlx53f5NZCLxtDZde01QpXPW6T8UZrBG0Fx0/F+HCBUHHHmJ/40k4/Gh9shvGVAmJ5e8q5UyJEXE3vd'
_D = '=k6a6K8ez6gayGr/haUuTYJ8TYMVrc5ti72kIswZXQSnODuf8zgdfmuCneFc1GLQwvl0r8Z3gG1llEIR9sf66R/KBSQxb4tT6ufmTziJGUOK2VwWConfvqIt4g/+QcMulEgHIFt6pUrihDG4i720Mw9zGp6yAKASE6Sw9H2qjyFy0yl0wpJcC/1wjm6hgqkFtx3vgy6wJxrJtGrADVspXWqJS/UW9zR67dKXPN+myKADWNSOdEh3RWCS3iw2lIIFY+f8o1YCGro13Vr3Wl5nown1Gpv9ux35BhjLejlAU7bx/d+hNM/159s97B3mUZdugq7VviQOOpQ0262TDCnIqkmcuHWpSTocXD7yjbrzkkDUpmCgnzaPI+wzN6iYH7JJ10Au2dXFIILe2er8vKMIzRgon7IC4HEXYTIJxAbBZhZhaL/cTNFdvbSa5TUXH9YRekrX1tO/0EzTgfxcmAuOsdtwZOZYFocsF0FR9wOgklYjgdrtAmpFH+c9ym9XtJBNdaGc+NA62Nijsn/TnI6Eat9+Kg1AcwBQUYhIWQsvA8RAnPEUvOvkRWU7sU3Iu6Cag+bg1keB4za5G0jJjr5oNQukVcfsOt7UDu4ItSV5iVZ1btF+j+0vNx1sYKM1zizr6MlRdlpNrG50ZouqtKvT3kAXHEH6/JJzpuM6Y2L4b1cULk3CcyAm5ljymtGGpEAOSZFwQNY7/DKjScun2zG1SXfVlENWcH4zqpxLkbxT1462gEbnXxUIbHYJ96nl/zPPL2yVQLpT6QfxWN/wTBBvlV8RyjzdxQs4o8QUb8A7Nsv0ThjgEMinIau9BgWNYfRkIREgwfuD52Vfs7pHHfyFtyfGwWmUQn1WTppykrcf+jOy8fmXHT+py3eQwzu+tULps/eOzEm0d/YRfVL2ezPO+3fBLEoctV63+hn+79DIK7VMqc/xPHxgEwvX3zc+TMNtCgfRgixymhvxiTBHJqmg219adIyc2b2YYs47aF2Fbcw3WGMQTupmH0rgiksdf4PykWoi1sydPOfrlzKS36WHFzmMvhkI/34bQzi2gvmeNzMypmOeNNwZnTc12pLmEtpChFrF08O2c9x8qw09KxNGzXdKGcII6YXVx+iwyl0PEF/5P9CC94h5jT4Rzjo68wS1pxAy3h4cqQucCJKyCKybFxnjtVa8tPKlnJkiQUEXdNHH4ydeipxnAgClDIfmf8UZ+mlvh4dDKv6MERym6RuZV2+pNXMHW1oduLIBszms5Qc6IxVUa8nRFNj0ylm51bYvcj9UQHZPbVIp6BLd0fd9S2OHkA6YX/ICEs7JcBdoFOB511qmzVu2IRpxwTvAJzg5ivKw1QS2gXZ877Vo92wZyIG58CWr/DjOJlybipdv/iuoTcd3DWu1WVzIzPAT3rbWEDV38B9mFw0PuMfStQ0oYqTAoEU9EV6Nh27ufkWOxzcjy3aLjKdPcx1FAPJFT4BpcA+3NuMb0suyTCgrmYb7ZmKl21GOVy0ZA8hv+k4Th/Mg1232B/2p0itrRj1cEraaPkZEMUyz8B9P2jl5NcrPRindjr40VRkcaj+qEt2ZyhgKNg1UF0RWE/Go2M5WbNjUVOQW9KKTmJ+NNMjH1MvK9jgxpB78A8htSKc64LbcouvFa3UGzGN9loGGSE55egLBaARynGINbsll9tE064vbfQEf4q+gOHv6di+apmslKw69vCCHaZNzAPlUHiLbOJzXvFbCpxBlc1d2AIQxDWICeFGgx8MT+NaHH7g6FE5wmGF6uZKRINQZN2t1sZz2nk3ErzeHGVnxGO6H0GkmW9ZAqSprmo3rS7LDE+DWL3szI1bhcEW6/HTNhHzB'

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