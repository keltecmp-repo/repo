# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 751507 ^ 351507
_lx1_1 = len("1f1184")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-980773)
_lx3_3 = 183155 * 0
_lx4_4 = 140082 ^ 106643
_K = '4342b39a55ec483b60e5d5931da4cf89deeb818e82d622ea6caa76da91eb9bb1'
_M = 'CNwFwjGhvVhyhUxW7WIIorxWu3nPntTYh7rNtjS5i8EJgQubYfT8AyyEQgG9Mlmq6F7qfsTP0d/ZvJC0Zb3dlF7UWsg39f8HedUU'
_D = '=cT2n0LceqHhK0IJkrUn+y93nWcxoQxGOrnFnas/4r5loQ5Xjyxu31tEIPrawV7kk9ljFYwE7dRajyvZxZpuHMeTp6n2DE/OLkhiQ0rOt22SPvGIQy64gw+Des2eeJAO7q8Rw6EDWMSsGJg9JckIqqBV4LcjGIndaZvT/VNW8RKFkp02siZy64GGvH+uANOheHoAM+KvQRjXVB7Sbu7PNZpMAiZA6jvaEtNCruAynFIv8kNmNR/gsXn7uO0BIuny5eQ7TCY51LgRKhFLZWxINIKFCyZhcPfnakEk3tqwvtyWl+Qmgk59Uz1x733r5g8haeGX08Sjf7jjkYYsvTFfTKCtLdY91CnENKnU3iT5wWdQXkHHeEuuklD2HkiIyZ/sASg3AALY3pNURnhUeLenQNm3mWMc+YS/hoBICb9HVtqOtAt1pvAV+r0uPt1XXjfzOKkgh3nEqsCopBWlHEP5dsgSCBVdGssZSEU5aOcjoCWYqyQcmHJ6fQ/Zi2/TwvuR+GzAiVdkBAW06unzhFIR8wRYI50Jmify9Vz3oYC42WOPJCHqdIgHebiuiORmbm7eTLS1yPGsJ4CTeqKkGaQq84GMj6P7VYhLqrMMYNsyVUODeHyfLJkOOJt207jyx6KRSG2Fj7cj14gHLDcdx/4w428pC1Z30PpqBRwxpPJduKtkpq1zWw+S5MV6UCbjBclxUPdgxjFBvnc/j9nCPIB44vMVAJ7raSdiRJrMb4lFJASNcNJaog6VEJZJH6iMtaI0xhRLnxXXgf1jhDvaVmye6iv6I2qeSLCg7E1A86DaH8jT1p++NYLIH0G1wohX8e0atp2ux+1zKUmRdgQ1lVufTanxS7bo7pKsec0QtxfqDKnaOpL0i5Z5gN249ikjlaONs+KAW9dS+7miKChd5PTtdK74GtSSkqWvOi9Az1p/GBxxkTGpv5cl9Vc2Lhb2NDsg9if0sG/nttiaFUDibC9URPUyusXvDWC4FcfSunUf6tr4xdzJBsIl4rryLWGADdsMqd4slZIRYhOiIlnFZ9oegmSgnDv+QprzwRNcIyMZiEHyMMgVq9Gcbf4ynFr6FWvLbOEAFcTFUvTrA0DkI1cHX9o0g2Y3Ppg8Sbape1dQRXJzy+TlmdiCR+ZCK3W6kaP/gRbT2cjo4QTfxbYyy+kmPcfuwkN7EkuBso8RIWA0kulP1RvVP6CK31KrWHnLkgP7GgZq2g7xPDp9WCEYXm7aGwGM8+ij80lXBPvB+sI3op7SQYxFltMowBicQ/qCjCHpr2Nl/CXad8ybcW0UFyTtJaIEKvYEkfR7Yq35RvDpaFdMslNPtNY9SpZc7KGSGRYT9EpHhdQb70jTgYEBGZBmwvy1rzG9mhZCZfbFqn3OjmiXykF+50Y+qd3EL8TrpMckMeGxHJSSthvplVH3wYw1tkSlHIeLd0fR+4l5XxSZPplMZzoJdYLYb/hyLXo6wScsmEkhqYD8MXH6jg6LICBu3y1dLTs+bt2/GGmDmtvuGGRgBMbxkMMiHdmkUKedCNAsdumXxGh2CcEAMgCHsuE3RkXhXMD3tzClbfs/3+6aGdvuF+ugdeKHVozPe2nAqVGsIsClhZVOfiHVFaKxK/m/XRxk2IEJUPt31uw1SgPMiwXVv1Dzj7J6I3Glnd8BQ1PzLOhiVHjVJjN08qlVJb+29CbItn3QAfmkzquL4o2c4CRSa+awhlQRAKEh4jghkfEm49z+BD2fPZ18gL1oYXG+Y6NjSMnkqrtJfphs3dFR4/bmtse4SLqB6QzESpkzAt+LJNjGcMzkuCNuBGbIB1rRiXB9xvPTSG/zYVf6isoyZWqb66/0ChnYsufZkmqGU5RO'

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