# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 128526 ^ 156790
_lx1_1 = len("dd4c05")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-496320)
_lx3_3 = 375526 * 0
_lx4_4 = 346813 ^ 104201
_K = '4d4c9ce4dde1f64d7ad2f01fc003a181c391cc5d170bcef760124a87158b63c4'
_M = 'hNl/IA6TXHW8yRXOUUYTnfVxGQRIsJM+xYR7vmaQs2zWmnk4DIkEKLaeF89XFx/PoCJJBhW8xWvB0nK9N5LrMN+SLDpf2Atzv8gW'
_D = 'wDOhPaBKumR3NyG/glZT4uA9cv85w/nkBoe3EY71iQ/AOAjQjJESpslWIMTBcykrQtR/v/Syexv6GaucpGAkpx9arYTdxBcREXXfq7wuMySBJOi8uGcQFz/qpEn/2Su6sGVOTkH4xHGgE5DU0d4sleBICs9nGSEc+t2TwaRLXUTo60zF027F+LA2NgX3JJS0farLVDsPqj955rrZKspGqe6J2g8oJq4decJydYFz3QRzSMAa43wzWjLM+zt22BzCg1okI4h12kyqjriWRtjOpiGLGrlPX4XRDde7BGK3TGAOidVTp6vYitbNH6+r0atpxV52QqUYD9uZAdxFm7u6uJ1xG7Mov32nWubJfABeCsCVAepvQWxKq0l4G7NxiiuPuooCfddhfeH/G5sU5CBVEWsRE7iIdklMsHYK39z47KbMi0umRzfLKkBt9rYsJLq4rFy5ACphIPyQ9Z4esJzvHzHvF83sbKfRaMbSz9Z9CAAv/P1l6uoldcNq29VHFA34tghPCzqCi/czYM2uaVLCaGWmEIJWEmh2Z1HDBJfUd9P37rLiLnpUwqJZwGnnslKJN+MjtOCi3972rcZROoBJTInk5m/KpmWA6uTkj067PSmidMzjwoIobUqXjHPSu+3lDCae1BU6Y3LV7+dJyKyOjuPaQZr+AUlUKkeduL/AWmQizsgSmXPJGn80u8WVz7yuFT6g/PnJYX4x+6kThDmtZVH99Qew2gijUc9kbZkblPQxWkI8D7GfUyWUHMZBGEmndtSl3Ov7lcPZ06m8L7IrW+xBZhajOiQtf3t1ntF/dYqxvuQd7Y5xF/E45PveAjKdluQGQ0X3kmGdNQDvBM6qpxWlShImCNiRHcZoSlwTUXKWmLYS3/OKXPXakib9+sApb9+qwvA/X4tCpAAb0+NcJmu4NjEfEyaJMDSvXtA6RxmA72m3YzhEKA6tgmz6R0V6+r7r6GOLPpq6f5MpJUoQqH0irYC25DYex8fNVLJmjejQlfvtu480xs1l/UeVNvqhEsbcAKtkEYg9+OWg4oqk2y2LdGoV8hiD/c2qfyPr3W/II0N78esBjNH3oD0wysOtz/rASo+UWcfoGUQ5Sn2A8vGgtRG8U7Ci2K38BUUfpbEY2cZgH+YutMZHIjLTPPN7x7j0vkBo6pLusAgMcIeNTwPhkQnemt+pdQvgYqyVJDZaXRRphLZ0sjxYEShlDCOmYjaiB+kQTBNFkZnbznKmXoleYeuoDR+3dOAOj0xaX7zNrzTXB2DyALNpdTdDe5Wi/eSUXrEvobFuwUSPbreVeSb7MpnLtACTd2mbuKHOcKbO1aw78Rf3EmFcb2xnUmMbo5yL+IhQUJcW/RvG9DPvqjp0AzZ+Sk23MPNp2rWfhea5b+O1sqGR85e0ntABg17sNjFTK9M7rChcZ1JbXSi5s1yXe+IekaXwK2mtI+Ll3N1mm3NgxDobFI46zxLY149GyQ2Dv1FPhiZR7fIJ3uiJmKDnJgihEQWeFZ3n2lzYiGEMRUpE3vhL3Oz3Elhgh/d6LWVBjWKNrz7dRu8IbP7A2AiXs91NWdO3B0qvvd6IXS92M4M7T6ScwTraTikNBl7LES0dLJUCNRMyYi1k13VcBuoKoEXj50lU9b8HOu98Vj2HCdUKPGfBp3bBA7jf'

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