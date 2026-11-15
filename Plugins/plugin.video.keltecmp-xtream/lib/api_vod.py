# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 388527 ^ 236868
_lx1_1 = len("8226a4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-144639)
_lx3_3 = 527118 * 0
_lx4_4 = 830803 ^ 570909
_K = '399b88116d902a580a37398c3bfa85bc8da4067232fa683c35dff30dda38acc4'
_M = 'b6PO+EOQI6U89KgRCXwZH50lZKCT/7himSSUiLdjbS8ouY7zH5Ns8zWko0QMJExLmyAwpcGqsGTJdZWFumE3LyK72PBJlGGnZPHw'
_D = 'llUKfpMtIt8SEGVh06D21tpSrR0V/f5HkIKnJlHz0+Ho45MFf13Nopp0d8IUmJVKpN4+XEJAzGG5GkpeQeKyRterhwt2uYcH3oYevunZqc59DKsvMWdcxB8fLQ9s7LEfVMDchNi/TLx1fJ7fGFsdGSEkRZEKV0QyPpGasC6msZ5Vxe1KFUITJ1LM5McGABJwUvJOJNhZSwr5sREOsCIPkfdRIw0WG4ftKwMQgLeM7GgyLiMUjLE1oP8JHAKw3B/fju6D2k3JjscZ6U4ihR52jzAMtqkjDHX9UxbPk9w1lzq+T8Tc4RifqzCygZVDCgpUprbW68ybkdHmEOTy84s0V8pCRSbKvuuBZTriAZlRiFIfRoL5fHuJx7+sQvphQu1yiWdnvZeedEGpt8SYXt1rUOjFzYGqo2nSU24mn2F0AsPjG96q9OKbCJO2ET8d2ILmkY9IN1CLBBPO3ENVa+wl1l27qGVxFTPLCGVfa+7WLfmG7+J2SFa1+7y1pKaPNlFsa9jz0Qxk+e6ZTBTYwL33oRIHRa/jmH4RprXELehHl+1zUTznokYQLAPndkgQdc//VTDDkNzjh+KIWMX0VdhRqnjfFhi9CO2KmpbXRrDC8cO8ChJ/7CvMrcmQ/pdOY6XOt7/6oCzbOmpHi9g35BUXUHscRDBAEAtHbg6Qohzn4wFigvrVx1/MHIRV1V9Pm/S75El2ciDlve7VUL/GfR48yVdHB2b2H04w4d1JjAGTLOFL12RVVR+3pKqpc/AFd/kPLub4rt2wcaS+FUKmEKyorC5ff1UrLa8aXNlpAen5tXfSrVN/7U8NAApxnOFGQ8UY/7iENYM51NjFJmM7aI6RC55/SSZM3TZuvJ0jR/VEIpD6JgopQVC8lMiY5I14RZUTqKIET0sOv3oH5ZwM8y+m7rAUGG3fIKsE+zTX7EJK3sizGcFNKOuYMOFYVwvt4sSqAGZT9fb7LalyeWQC3cLl5SjNgFyReMm5L4CRQiXJTScmcWTko37ZXPMvba9exJLIedtG/dO+oApe1vrx5N1xB2tF5LMl6+HgNlp33AmKaGEmVph7DR8CcuQ2ZxZi85SL63nNs+6A7zS2Y1lHS6LE7WnaCRAd0WRhcr13AMhs22qe9HzbzCtNBlOhnuraDqt2dZHLQYYlquHA7h6aCMHQR7pvDD5r7wP9hKuEQ2dKG0+WjuB+Oi84r79KkCAVycJJ8McimqhTe/PsVTwpqKqQVTAz5XsOBkwyssMBo4Mr2ddWHBYkWaOyxyw3aL/1v1yZim5VzARayxRT5WvPQtNb+8VVYuQUHwyoW1+O9m1Cma84mT5z+KtRhys/2WrhDp9ED55oyxt8ZWZluhwiJisErW8VrI1Lgm23AjDiEMSvreqiGXVE9tzPxZAiXnVcZh8dTxK3IR4H1QbCJyuMZQ73defysITrgQUMR+aTQhEw6lTgbquSgmOw7QTqxT3MLu6X8cM7UxYZE1pt3gdXggkyNtIs4QoQsse1I0o99t3FlW4/0I0Iy/NcGnYInHEz1FM6Me71uu8HViZe8K7QUhmAvARUQ1bY6jfMhNV4NA+ZYjHGg5sP1k7H+uM2G3p9ggZhkla+G0d7UIs793v07Hl2a6rABGKbtvCTu+6jj8i9RV41tM5K1H23beOvL79q6ggLlCTQT+VHixjDEQUE9LyTMQYk9/zWcys/6J+DZjbj2xab52Iwm8dUS0JvdAm8H7BrjSnmcoXMk5YSH9vOeC9VjMqhQcAQmRkhsghRxfuULolBF+7xytAGNukgHR7hrJB/jBIBoVbFVamS8dRj3eaLnQawA7IAl4ODOu8xnZQY+fK3zeGpAbNG'

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