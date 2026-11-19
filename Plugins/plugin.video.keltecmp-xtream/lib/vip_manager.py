# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 210199 ^ 765765
_lx1_1 = len("42bc52")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-977159)
_lx3_3 = 138279 * 0
_lx4_4 = 476969 ^ 902015
_K = '1d718549b58620fa9a08da5d2d8b45d0ebfa353fd640ed14a33700568cb9e329'
_M = 'f6kRVcfOBR0LDJw+K1lth6DGPcjjccgwKs4iVYXwaWpypxENyMwbAFNbxDsvXWuKo5Zuy+UpkjR5n3AF1fRuayTwFQLJmhxRAVqW'
_D = 'UKw80U9c7EelgLX+u+FUaZs1pcMI5BeoqBiaLnoor8OwPlcofkSyI9JVUKm03ddG5D0QJ6bbBj+ORWspHdeNx2b9C7jqo9/X0sW+OkCkYSTjDZuJgH06YFlCWad1Y6/PbaSvk8zgUmVJE735UjrR+wtDQ4teGmqKN2EAL+0+ImDUAEILkNDV2vbMwiYZthVmO94raGXE29itavU+6rytJ435qRmIsz/gfzr81w+/qzZIYdVm/YXtmQzlDK3FK0aszrL5qrt6r97zMH11Xlgp9fpCSV2ZAOm8bf2d50xWuf37x6Otzd8z67ZhnbZ48GCNlFXZZisvVlKJ8aKD5CQ+RA+Egdfw7xQrhEiXxfJCw+D6xUVKAYNSoVzlK4zfHQU6UuVxxLWQMkASr9HOybWfsBUqesR6bOiy4gcugZ+C2d4rCdOn+mw4UmUtJFm9baDw+vSFj8Lst9stQ9rBnSt1x/YXLCWhPV5b99XdDBV0sve1wvS8xxq/wnWzeFMDNLXKgrJmgdbJCxEt5u/BexHUcEUTxPF+/yXGVE+iMUQ53o+O0w/CDontHBdRCtw/H7DbSJaWuQ08bptJ0xVCB91FA0TfYHlnEjtrdHNKoegpVwoob+TIUl2cOFS6IW+44H7ng9oKvLz5VweotRsi9Dk329CHNQG5naOkU2WzSDSKl0sr5pMLTozpmUUcbAKWoCzLPCmHwtIXUDJaMD+EpuZHFVjDuF8y7MSdNhdbGdnogrGYlB6H2BixTkXf4tRkuQEzLiyPYvksmHu0gEkOCP1a+Y8mQP97bzzsT/pXirLIadiULW/O8CURDvvyofHXILWoZfIPSmSEk1M9iorK/4ch66SwFrQ8aH30a3pxBqD8tqmVHKJKNoyFLWWT9rt0XyXi+kcUl5wGKZXzSbR5+/EKlZedmrtvFCwhHlW/Di9RzxYOr5uWbD3eCO4slMlczGl+M+3539HVZImkct35kF4yCHGlMR8K7J3OPBfLiwcYNzH8Vyge4wQubHWn7QywsEm+cHFZgYWOxLMhZiJwuYlSWytH8AOLE5HrAv05iiXttrAVuPU+gTYeuB8rMzWR1U5/Yii4YWERFPz/f4+fVMnA7LXKfQCBlx9G/4zMN7BTLGoaU8/3MTwOfDkJ1waKadfhpRwgZdNGeUk/4Pqm1uDA+NQKtnGlHHYHSEsQ4O2SNkfLalkxvBMvExyD5wNu8nxWB6lRTG3yv8npoUJh/ci6JkuehtKHlAZXBZocC8ytNgqepEO+MW+lfUEjV+4iM/0/9lSo4GkwRA355bEE3xlwlhBCFzNeX/NkmgwF5RuwA7ehpVDbzAYSFFJxBDCWHAu67nnKG0LTtw/pDiIWxynbrFlwYkZG2gqpy/ZOvSTleVhqGMwwOE3v62K09OQ/GTz+HVRDBIOKQCHjWm2Rb4pBkBYi0N871DTgoOGbgzy1WzjyTAR2gJ3GZaBEApd4edxzCYdjqyiuZoaO2Dv55VPxWNhluC6Ok38xY5gH6HcsZl2sRH1GBCUaunFHMN8XmwpVuz/c+hkMt1L+ML7m6Q7v+FnLQtldUpYc6kJ1hBF7+10GXcNEh+l3WlbE2g/uPwGj7ktjAgd54JRI+oWeK4u4oq9S4GtPRM5cTvOAS1kGYayfpv2Viegoghl4UHwFW+jPhJgJcxMR9zy2O8uCXo1ZOyQAyDqp4F5tDNqpN4mkYtH8zNco13K+YEDX+FERYK9/Gq9tf8B/XeujePn8HsPoMZ3szXQDgqVWRURWRDELgVf7Xvp6JVZTE5iwo/vbPwP8S3Hz9hwB+QVzO7tWUHzArPJSvdAvGj280AszDrxw9xeRTvqYSKotA+bU2/IB34NT'

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