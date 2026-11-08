# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 184124 ^ 223083
_lx1_1 = len("93f0a1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-505349)
_lx3_3 = 714380 * 0
_lx4_4 = 140797 ^ 478751
_K = '3ce6a742b975d5c3e2a27fc6be625b27d0647c015cf158aefc4526e385a22d03'
_M = 'q/bDb2HgTEQwBtvHy32sK2mXV5WTOXFT8tvxhweNm+akoII1auMbHzsD1pXMeKouP5tQwMFoclP/ivbXVt/F5/CmgmM4ukwcPFLR'
_D = 'MFrQrw9qj9aIfFXHlZdbF7gKraZJqfe2oJwfcasgnNJxcxJdtx9fPr/OlujTSiuMfmu6YNw7m4WMNO9xK1QRZGOBWyKNDmc160OQ1vFaJdel8stLuDGAmCV2OzqaR9OUX0ae4aoJParjbdLBeLmKNXu4apqvXVwj46JePBWi5zRXSUGTAQXF0WaCYGNAstaorhqwwEbrn1ugBb8Ne1yumiZuV28TIX+SNHwfluzkZtXn5X7JuFNB+3qhdr9K6p8GQXXH+/S0daNqkyjCIxuJEsiuXB9nrSBvjoVEsp06SOi6DrqChKSa5d9Adhg1igj8ruFo4h+vLEpm320MmKH7mae/+osBrCAZAPQzMHXvSouhU5g5ZN+wsYbMKvlguYGg4uv8qcJd6/qj+mD08jBP5gigHzPp2imqa1e/776YJPkxjlaH0JW64LWGrP6NLwhAosW93k1TrmWT+jvsM0THaQU2GSoNZ5P9+/eNYF/bzE+21SjqBTPD9L6DU26rhgkHWKZSjw0/B19PxqZ4kAZrDCeTKq69nheiVxKx/chZyd3UyeQiH65BXzDmn+ai8pmJs2StOMkR/fcPw/qYe9TyTD67mBi4DyVljquB5WPSVz6rgNSBZFjLMok4dQvlNkDP4zhda6p+ebmIxaqZ6VqXMvnFGfAgcSKAOEhRvLYC9KWlgFuur4dVK7HIW8qo15UGHPoAVSzxShVbyIN29+Q8DLa1gPlwrnPNJgQoG3HFHZrn+F4FPUx2aW7ty+vrocJfsJ/XljIDh0id5HMXxyBwZpoyPzo7IQSXy0cWBv3C161mIB53/J14rwYRnlgXTeTkhtVNgtgq6zORhcMGWVds76rbKUcu8MtNWo1x1LjFSywRFKsVOq2ELK5KhAeNrTdsdRrVMRfazUipk5gcXgVDSh9j+LtnyixbwPtrUzsmasnTyVdknafyJD3jZ1cKpf2NM9FIJ3txlg35PTtgklnBz0PvLFaaWBNxq95BSGiEuuw3FPQ/WqMLUYe5uZbXbNavuIdz5SOQ71lmIm6UbhZQI0hPQtNlaWo/fMuZy/q2ELBVGNgCORHzkCkml/x83CH2SadhoIItykXJkGj8AUQg88OvJkdZBSeAKg8q7QZFvzbZe6o72VwiY8XjVJ3eGWacKfHI2WrojlqvmcHx0sg97GP/iNUTX2tfA2jpKLah5dzjP7rA43naOl96eRr/mq6maeC+RL3+KQBBbGZWWmhR3haXHSweMMKQOaYSsjAy6fTulSVlWfGi5hz/0ma1a2AAHxFhqYLR/lOfYA7z86ah19jSkVRFiBz657qkxPRKLHpY9n8hYLcycXxDcDfytlKW78DusXc0GWNHK+bCxZrb/x13gfcW43Y8K+vkZq89E9Vyk+iNc9bbvYI9cZHEY2NFi0KyVL7lcZvWS+Ttlsty3MN75F578YZjhjkcF2pqXMpjAP4PLOG3a+0ojT+Z4H81AmJh5clz8zSBb73pzmWandBbuCvtNh099MRQi+lCe0IdE/rjTXAecjOB8wg3PG45zYkAfPVkChGWPLG1q4qeOQuoJ6VIhgnTTf+JYlc9Mis0SIAisisMaVEGELm1JUtjP5M8hyX3YYOXSN1CLy2k6ibpsk/Zg741ZFLf'

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