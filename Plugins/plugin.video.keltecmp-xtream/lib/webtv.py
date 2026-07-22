# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 400146 ^ 803258
_lx1_1 = len("c19eef")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-362475)
_lx3_3 = 165503 * 0
_lx4_4 = 104289 ^ 568923
_K = '735756035592a1f0859238b998c0343b6a155308c05ba6596211efb8838ee377'
_M = 'PTEIKkgc+dboTr8AedWiTe52raTbNdgLERmpb4/tpZJteF06X0Wu0OBJslF43fFM6CD4pt4w3AgeHaFh276lwDQuDGgPQKbQ60nh'
_D = '==QzNchRBgY2SvVoZa2jMst2w5MegXrS1Al5fecDFgLs/8NkpABdkgsYQ/RZY+JGOLSTYiLISOcCQ0PmA0OxSnnlLbpREQzRnOVDvHUZENrWgdNJxM7+b137aRUu/u51YYyjOggLd3f4D/sYo9Wu6iw8hX8DfHsrTwGa85ta/X5Sj5OkW1MT+txAUjgFJAAdBI55xAiRPLVN/HOZO9dfvof2LU45I3jXmQ7LpVSCOCg/1LwKIAYRI+1KyEYCvLwUNXqgaN1s7UPj5LU1yih1AFB6tTtTJc0W3Bp1+eFZuvktPESZzIo74G2sP+oWjlpiRijzSc5wDsHOv4+CjB/j3zYiexg3yYtpPnTN/JBYX5xQeLrgaEN9WLZWmw3REL3xWXiqro0jQRHotjL3kpNzB+/SdAAEjWnwRTTLgOyyBpObDiNxrdJ34GhfdzENTPnXymMp3hJoIjJrQwYoOawPd3ZbrNu+dpMRwWPfkPRAH83an3T3NFm7Wl7TPT50ySgmg/pCYFEzqQKj1pKZ7P2wFiQOb9LQh11BnEDAFCHtv3Owytqnx5Mx2oJ0/xf0WjYMfoqeR0JC+nQ7mWSsopvm4GuoGLrwIORuNLewrWNglgcVyohTfw2KCsqzSC2BQFumrOdLCG78uDygD56oZtXqbytB6zAZ7G8r2EGeagUT8/fPGn0ZDw98QxOOK6zLCSipNX8N07KGGCBitd8pIkw8R2jayCyf+4GrBWoFO8n37/C6aBKZTnV58ACSlh9ShYV9TE1KzD7EVn4PgzPl2jBGpsz2tAV+k0ootqLcOzaMeRon662fFEZQCUM1vzUw5SS9BpviJzcoP+LUbNWUH2RVK/JPHcGTPol4dXJEMNRMqsuJpmXVq3I/kH7d1iriWdIelg9Li3/mXWsoYVmvbYl0TGi+wgfs32Ej3DTABr/P3dpu/egM4mV5v+GrEhEbIfq6UFvLJwahJn2IK8WP++a2mUYygV6Oj5HNfaPjVm4F3WMtfH5eTMlI7qUm25r+dFCtNnMyUfMifGaun7N2COBeIYQKa0f1e9ZZ5MsYSXj2Bi5fcYeEn/81VUTY1iNV/taBRhl+nybTES2hdbhCGTlml0iYb2s/MNF0SzMqR4cwZkQpevLJRMX+CQ1HwhceotTFGxf6lIkR7n8WuQX2fTG5IiUnjR1DhBK6WPlp+6/ZhUNTR+49CfV90ff4yMQci8bm0mZq+OuJFkCWvJII3+zwZh2yqmEti/I+TtOJroyXO1wAvF8WRlWRRgg4ulaOgtM88oTi7MKd21/HkfOGbXdLGktVLo1wP1v/9wBT1cMxJfEH7eGnfzctPFl63M0Z9wDPUp/ECmp7EWzyQPqQ/L4rRF7w/CBO6STgihhhX1v/5+PWQxhqwFYxLFpVPBx28ZKe/pk5B464WP+a41Uoh4KAAIcoZfLBCk/sjnNs6Dw54wJLBdMr0eV9BB63Lu0wmzM/AnWWYcCoQx3WXQx/97I+LSOW51LqKirOvlVybJdXNv8ODz2PeZuVWxAOxiYlON+qurN0mzd2hVx0QrBGPNETK79dl1WkqN/gGfEA656G/e5PkSQJ4xsi9ZWfoQIPX51Vs+Mcy1ZLvQDd6kWKtPdqJm3OP51p+uLZrBpa'

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