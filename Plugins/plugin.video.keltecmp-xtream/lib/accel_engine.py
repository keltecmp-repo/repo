# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 371514 ^ 599379
_lx1_1 = len("d75a2f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-916646)
_lx3_3 = 145776 * 0
_lx4_4 = 986646 ^ 630728
_K = 'bd6aac2acec6b199a16a23811b1d780aa48f6b963fe58280108078de9077752e'
_M = 'Z48dCaEn9CuuelSefol1b7EA28QNoAnsSBF/d1bmNy4ug0oT7H21Ia0uDZkvhSI9v1Dbn12rB+0dQXskULBgeCeFG0DufOR3rXZa'
_D = '2ut6ChG0FuW/+p/5jNg8uoPPI2gWjdarLLZGZDx32G+gdYggFFzwdQ8dMw82X3W6iaRMNC3gqWd8fYvj9/bxf4kV2B6v2KbxLIK56McxicoNFUjvU9pW3ICJsdE0NQl43Nz5zxK6clydY3TdeFkMLhLJO8AMytKXD4S+MsyO3YSnmzRgs+h1gERMVfLT3w0u2Fs+9PF0SKfDTXD6VSmmKdKjEZkIJZhRZcBN/K4u5t9fECOcqSOyYWw2Jp3IfxYRKU9BxoUnWjvvYOjxGqh9wzS2FKW35Fa6BoRmpuSfte0pCqZmn4YZGj0PX/BWcejDtlSZCXl2Tq3lHafEoF19wm38yxcx2NvBU+X2hDX6AbycexXiFeTBy8YV9EjBc+fUOh60zjlOvoUNRcz/4SC1zD64s+vSMuY5FhRKTRumd954rG8+T2zsupWI1KBAm6gc3Li+YCeRrfhF+1z+ygY71YkXTi8I2S8HqlbdA+szKLfjkr07omWw/WGI4D76PgqJ7ixW739K0IYv2CmIAC3FKWZMqLbhnw5YPebuqgPW4eAci83Ukq3YKel5d8ZdWojgsSj3A5SehLVwS/DjbuFFb7pbwCE7Zdu3LQtd7IHl3KnliMHjbPFeFXYMVo5I38zj2+XV//YaHd8EZN+DTTXtc7mSEDf8OctWtIZJB5zkTD061De9Bljo8u9MaojuzkV6jSKoHT6s+kfVMrEsEaYadon5JTkptygq2q2dgJclYyvHNX7MwqNPo5c8XUqSFwEKkDz2ql3oUmTjPiI9wv831XUuKavhTvG1JPhVL/iHtiFT9dRRq/qtHI8zDsC6QTca1Amh/2MDFfLK2qEd5AclyQ170r1juuN/Lbjmvfh0vliSECNGHYhbHEb+eLe3pLFo7jLYb+0oAA6WoFltV7sXuMigSx/ui2goUw82NG16Ph/dx8iFfYpZ9m+qhkuwga16I7c+pwbbUeQZMuHjdq6zcvYkXTcw9be6kpo613MO+lV92Kgr4X3DorMgKcR5LGgZOqzAyiJnGYmw8W4OViThFezJd7J8CBd0VTi/wivXhDvEs80Tv76AMoo8qpQ96sVfa9l8sfC3ZCNcdX8+aF68ZVPJdskKjtUkCLdQPycb5It7HAeL4qKetg6uJX6JV1voCJy6+FQ2R8I64YoPAPYTsuao60jLuZ6tLWiqOMCPCWADAWG+uyXsEpU3vWmSEniBdbyM/Ezu9I2tEjYEQxb+0SAgrryegoMRT+skGH2KAWisFaC6H8jqayqO6U0lVxHxxmyQhHwhn3ZSEa9GRDa08wHGHEXntfr+XSoaGOKsTvkR9V80gPg88iJoEzvzyYwvqkHDPB0YaiNiGtSuShXnP1XXxd9qNxRyuqwE/wbWpfQPPOTZ6jauXsYMtmsmwDRcqyAF1kY32cqDhHDwL/QcFsbDz6Ji/f1b+fqAmsQ4toFcvu+RwhocZOX1KIRPm2CLKWxcC4cUGcKrWP2th9zndRqeC7KGbBMemCIkImZ3mW3I/F4WPWlp6l0CmXpsgIiUy+TSxM93Ndfu7EfdszR20B3gkDVFw01V4CRAR/Ux5CW+tr1XgJLPjAgLop51sAFSCJ1vw5jOl57/g3ldlSopR83PtHQYMRRkdffu0N8PNYER2ZpfIbJ+zYGgCwsMej7ckK6O0NMWCfeGm2YEae9hpyJASplS6OHLe/gMNEdqTVuJPiZpniOh22mY71VvDKCGD7QVO/2mZ6JM1JXPcWuIzJxEb24MJPhaPDzg5mQknsgg3blAP1kkH7+IgYN/gA9JBL6KyRqoYVAcJowzpbp8SPPFpFoCDWVtINzRPPyLOZUmdgc+UjSbjYEEmKMZTW8MYD8d7hWL'

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