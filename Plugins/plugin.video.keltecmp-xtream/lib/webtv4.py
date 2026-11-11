# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 183626 ^ 520482
_lx1_1 = len("bb5898")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-275460)
_lx3_3 = 503805 * 0
_lx4_4 = 357555 ^ 608554
_K = 'd897ddedfb3bcbd5a3a6436b08e1c8636aaf0eaa864d8b805b8eb0b6be321c77'
_M = '4yAq3GuIUqyY++346l9zwWRfeU9rFSPvBo4Lk+Q8bEalfnqPYZsGppess/i5CyqTYll0GjwXI7kAgF6a4z4/Q6Avfdtnmwj8xP20'
_D = '=YcPBhy4E+OKExoGuHSS3pKT4Ydj1Hj87JKFjUazttrIvEO4d0b50Xxj3R1O+Vx3BxM0yjziBW+F8A/M5kecLUJP+wXaFKsHR38PKhrPcy1gSCEWPGLUPelBzePrQuEt+oMDfmuwU4RfTvdKhqLgp/IwF1Ya3ftHy6Kcqstut5EOGxBqY57PgB4Ae96NL9Gc2eoQhdwPVjSOQGc/PT2BpQyZEADdirnDmQj1cuXYmhCB8TCRxBkaq7zKINdlgl9DjodVWEqCtk/ZfKB/tvINr36tCKbU3OsGoFNAsNipB2AcZX9oyY0ZTC/ZjFqo5a46jq+kOgWg7jshJo+qo58S2XkNVmgGiuYW+B+SeKaD1JMCU/bg2FyjyrNmYcw3VvPcw1hpR9xum8vlWxVvPQPduzMbY1busgrswKJc6S+t1HNS8mKIJ67WF+5M/zTrY/Exwy7ZDTfkQYyusvA9Sxw5UOvNQazipg2vPdkbHRfFukrT0nc7qWQbYEjMR09W1PUomBU5WQyQXDysws11y3tojKLQt7uw9x6FEV9Sg33bNfAOHJUu8m4c3acusVKarU13IqSXDgoRRGAFsiTPrRZB4ceLos0CVSid4sNXh+jIQgY+mR2vBmYjqSLIJQIeyCz0Svevt+JOPqMuHUtLuvMjWee0ULCJS7wkN3Dz19b6H/PoXchaMYO+taTiPIV+cuPbnVjVWtPJFRfNdNjQjCduygxlumU6fp047JcCvNkGga/ir2BEjMcQpm8f4jpa9Soz1Q/k0uLq2n29tUAt995q7o8zCIN2fr7/jLz+o4ynoOGNfYfaZwcLC3iTXGTQkSIYV4jG2jhn7rU8jLBhIqGFk9u9c6+WVZzw1CgVRDmmNCmj6mNEshcU6sSqMZ9zUMQuI7Wkse+2ad8q0DssMPolExFpryqADYxUGosSzvePihVi651IoYpRhTUpFH2+5/KXUiCE5L+hjzgOhuM1H+EX8nypD5mgPBrXDh28Yp8XZQkWP9fKzWUAgbh2gEMEIfnCzLDtEdSK9Bbu7kzzpitAjh0IIcTgzhdmPzfiDm3yK5Zb9VSLyJfEAHl5sdvP/c2tMJQvtxPk4FpPOwRugkWnT02EzTWdwGXWd0amkuuLDppgTmb1GSbnQC/4+cr0+GuREW2FxJFSkB/bGQc6Y8Ppn6MRIVEUxgZSDAyxSZhf+XJMAQ9g8PPxsEswDl+kbMShgYZoKIJpaqG/C+3uD8RlbonorE1JHZ/tNji9ynLA//vdbzB6D9TLVQJfDRVEWP2yGoaNu4AxAh8OGijbU3KreRzwvse/3n5n0UaLJRsThG9nb8psvx7WhJ4X1AGYNxgVwYrG+jnANcFPhgDvSaZNEXL8huZjxYSSYnx+2/6Xx/c5veetax8oNrqErdTeI2dK05OCEUqVZ5x4C0U6GnJf4wUecfRUVrDD+teSFaUJJ5hQPLDIGhCufZsTCc76lw9WGn7sfqhPutVFe1XmEqLCDZNqw+yd61kdSOS6XE7xTorH9Xx0N7e1O+GpqhKPBDEcE/xQdkBIWvbj7VIxysq7mOGXhtP/5AmqNvWnDth7PM83NaqIDiJ6/pZ1HOXmUhFJivv4O6nCVuA1cxb6zxNAPmyxit+u1XUd/iL1gy87UaseEjMi0daveeRxWado8rdOCGsqFSfajupWqGpHHQiSyW7uDbx+gW3vJC43FqdxqtCje0IA'

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