# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 575031 ^ 429275
_lx1_1 = len("79ca29")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-667692)
_lx3_3 = 510622 * 0
_lx4_4 = 770981 ^ 301392
_K = '530aca808583ca53bae94f77f8587c77ee6bc7ee902659b4fcb9658da0390a2a'
_M = 'LX6ZZ0v5gzEf+/BK0fmTSYCrXv6mBxE5mJPwRv/5wZokKcloHrHXNRf8+k3frpYeh/sM+vQFQmfLwPdG//6cw38qmGwdudJtHKv6'
_D = 'KaJ0bMgqr8VrsV+NNjdgHq/crJFVU5bfhfG6+vshnMH5giOoAKvlFlFhuUvB0O3IjhLNK84C1zYEt1CX9AcdKP8m99iK83LxZrOgISQszsRKduh1kNEv/HfKjf/aSH4kihFjPvzGPFPKRIXw2niJXQLH+b9/oZH73RW/4O5v0DsFfTTIJ6teIvZEvqQkN+6sjpFMZvvtsN1cKLSRrLG1lwm2y53tJE5yd9riSeoKdvxURINC7cLGlgcisbZ6Dw/COS5k/07mLxfISWPx6QP2b09P5il/QcRCX48TTb6wECyeurJowyepXA1ePMoIHTrMiWHGpYw7wQZV5UuyBeftYG27rsv8l6BhEBjNkwn0LqaUy1rJEirgc/E6t52WJrGicSs9IKrFevVIB83dvZioZB20Rn8Rp7AmxpCT6jjhe+sza39oCaQQHuID8AClp3tHp41e2r9TVGquGS1ZJX3EBh2fbw4Av9WjDILi9MCyavZah0rp9xowmqad7LgmTWFogDsO266pl0byLoP1iBEo82jsqt3ZK+9QWnJn8GrELqFDzdQGLaU6qOkWezWEgSQFgWjQRt8raPzij2QjLRwmPvNWagTjmSPUHBzsoWTrofraYLd9Gtqxn3zZ+laxZnkJOX23GccRRg8EEFOmBJ/z+ebwyo/+1tvOoGvuArp0B6OiM+WYypK3c4sW0aGs9a4YnNmaLhH/7nWMbv7hxSDiTvftYvln2THAPuLePtMzqPpS1yTjH9n2FXv1L6agSBgsUaLFGPXma07C96c6kpEOWY6KZBqSyrixfyEWTne4Susf1CbBSSX0It5Uu/BulYPTtVmqvsvQmJZQ3FCDSV50l5ux3iEPG/OZcByHxEOXrIs9XDqaiVjkUImpsh9kJbgdg2N3xVCiQ8DqPs7AgqiR522wJ9N5pNVOUNnFRvcJbjKawof+NfD34MtWSaQINvJAqVOsFAOPKytLm7/Wk35k1sme2NYjigsQfu7hL+jK80RWfT4qJXBAcIHVd7QtRfb0mYAGEFWrrhl844H7eEUeygS+3hXCJQFYCxplWIYtZbnN17LNaJAr012fijNbMH76M3Q2sNvKtopSB9Gji5frm5muMl8R3il6x81KA2rTosudPWy1uT4RLHzrICxbkUkCFuUs5xORTTzC92usWCCl2hIE9V4ihEfPwPhNyo/uXuzM6VgfLZb3ts/nGK/b1QAwQSkRLuZ+Qgjrak4AbPx/25jzxKMrE8wx/O4FUmiPFEGMKqedZxqR2uZUIEzyBMCCXftSprNC6PXgOVHb5EuAUnAla11MUN3VC3sKUrBWtd3DxuEd6wpL+jEkUjy7DJp+WJ1/ayDs0QZ5Ah9d2eNPASqC4z1/HdgGiaPz7xVdvdGsxYSkwd9I1AVpXnAu6vlaU6/q9Rt1VrhyDuPj+imoLn6Z3eq1ykEFrfdQlI5fBh5JjZVG+FSjj1MMS0adCeP1qxOcI9YpNBy7Cd5vARoF4hoYz1Kdsy1Kw4spXX5PmIhJ/RVL3NDU/5U5J6TWuJk3CZqpsMLWXBO3/0P2GSpukrjghns24+YXHWT4fn+/dm+h+oPBRkfsSFuBELoQqS/XrDLc9RCn2UnS8RMjJ3J0pomhR05l/D8ibGGQ'

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