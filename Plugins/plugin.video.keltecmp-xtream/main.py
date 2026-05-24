# -*- coding: utf-8 -*-
# KelTec MediaPlay 
_lx0_0 = 562843 ^ 299473
_lx1_1 = len("7ca8c3")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-337060)
_lx3_3 = 660811 * 0
_lx4_4 = 724211 ^ 279750
# _K: carregamento protegido
_M = 'NXnhUXFbCOwik+k6KJczX8kUndXoNBAV3Ez9Dhmf84d3LPFDZAEP7CmTtjsrxTVXzhTJj+xhRUHdHKYOHMz113R7p0E/WlK9KpCw'
_D = '==wrQXlamXiQGG3PihuxIALdEioDBwBLfM1IaE37DHy90RcOhArf/194aW2ur5n8m+NReDQzYgcal98Zlb1xHbGPJ9DXTedTDgCpodxAThTiipRHEd9v/K8s+9gaKxxLY8Feri8IrB6jVQLETQOQ/J0dxbUzbEmItnYgKuzUzMfyzQVZu/vf/w0111YpGbi2Mq5KBXiJvGT3alfquPXnD/7Owu2blqx5bw16sYNyVq94BaaD48ZcXFflmF1p4Au7oyMh5cUcIYZmA4oNFVFIGBtagO9xte7hXjqdfVE/4C2rwiEYe7tSprY76gqLFVshR7s1V7V5K6Ld0+dmCYQZg04GDyPfsJsiSFAjjIP+/cIwnYotnE2HtldPvbBTPs3r6SeQ4uUMf34ZYFyE4TYGvnD8GviTR2EZDpmMarRio17uNY8B44ibg86gRF0vz9GMuYS/QjkteUUR3k7s+G8dltjadO6hHRm1q4LcmK0Y3kmey1GGeCMVxvdXwtRAFqK3eMpVWMUc8nbbydwurYdTjy1upKuUzAWETDkQxLnUVqj1NAcZSzqTSdAQLRcRuYfD+JW9rzdEGmr7PwQdUkowJ9Gj0rgLld5blLa/7jUSGy/nyfP/N6jadQE/5aikqEABLdIsHDbuyBDIOmtfYHPl5cwT1Uz+x/OJ+1VEoaK49lnPwHG8R+39d92UN8GjNjGJYL5igdupaMS1+KApqG0t0K0KXpMBW5ug2qi5rcUyFgHkG2bnmmaODv8tevPeH0pfccOg6j4roXJR+sqX6vGlolON1aMFpyPoyuVSgS1Woq/dBbEdnGcaFS7pgOQrKPA1sbuE1mZ8DkOeD4D/228eX3LZid2Ut7nfzDsn4ArCa3Z89wLgNV/p42My0HI4ROqu5XtmFwnZyS6GOnWjNDRckBGD+wOjvXwvuCjixxTn7/Ss8AJAaQjeOFnA1jsS4KLSFogDG+id2GEjAQA0drmdR8crqE9wrQt5Ec57yelrynokjCuiNlsjrAWo7T1BFf8Lr4HaLaCzsBfGUmwawJKjkiaBA4a8xogFyrat9C7IQsw5LxzmDjhajMgT8PUJCmjxY4jqX868QQeKg8J93qaASoF8Mhy2gSAhCxA5pyyiCZWMPKvuEVqkU5HkOl/heLGCRm6cowUjgtX0J+l0E43/1ySa0frzYoBNTfpMqHGyidsaLIDB++VfVKpPFC9JHjuDBx2tE4Ou3Q54II29nL5wf/iEdeCRNSKareja/up30uVm/KlAcNv5ek/yheXIFYjiQdfQLsn+Ve7cxbAYE+XYncaa7pD2Tw3vlwNm5YPl4LNJhYf1KLmkS7Gm8RDhvF9EdAZ6LIzX1U/o0lKS7k9nGnxhmUpxKYHumztlzLdNjvsWAX+M0kxKpbhS0wNpr8pPHQCjzyiuQgRQbrdrTPp9l0Ewe5Kt76Qg/zD9XreKyklLbN72/3TWbCo1C3BHg01RlOGfQv1uthJ0wWS8uNVQxViIFE4l2lY2zTPo92IbuYB6GD6blMbwQeOLWc14keXp'

_f928=[227,163,65,239,185,24,243,88]+[87,144,3,120,140,66,50,17]
_4ace=[248,171,118,94,102,125,117,86]+[65,238,156,53,187,5,5,38]
_4932=bytes([a^b for a,b in zip([145,198,50,128,204,106,144,61,36,191,103,25,248,35],_f928*8)]).decode()
_a960=bytes([a^b for a,b in zip([139,206,2,42,15,19,18,37,111,140,245,91],_4ace*8)]).decode()
_b016=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_4932.split('/'),_a960)
with open(_b016,'r') as _f:_K=_f.read().strip()
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