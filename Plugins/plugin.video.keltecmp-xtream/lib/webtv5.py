# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 896542 ^ 340028
_lx1_1 = len("1349f4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-657447)
_lx3_3 = 420992 * 0
_lx4_4 = 782018 ^ 223210
_K = '3b1e3962da1f57da9539bddefe068998d92f4eda24c306bef7b061a5d878dc01'
_M = 'UPB5w4d9Xnm4faWW4uA4BhXfR0sAPqOnbIw8pd+QT6gOo3WWjCJZIbZ+r57k42kEENIaSQI/rqduhDSm35pIqwenJsCKdl8is32o'
_D = 'CAI0KXzwdhRnkZoOkfi7pvxDRdWQ2NssFdK5bNuM+ipZBBjtqMF2izaOhWGiP+XXnv2JuuoUKkser4JnkAa4vYLcB+kS5LSfpeS9OwHmjtIKOKjaKAxJxVZQYRCn4rhtQFGw/9YwaOb5vEWili1plV/L8x2N3E+huj4izY8vpeA99/9tJPPfdGh9zGpTbv0b2fwXsp+bDNZHTMUFdqbLd0DzvKM9KhStj2qPMTbqfriiQ2suECLFOuFUGemzfsYYdUhh7vuEdsHPugGZCN6gAMUycVXRzVLEKKtKurJWyT/ZD9DKUY45WsdCbE6xMt/eibVEHpiEJWAZfiWRYHXrNCP5JXAHokLyD9h0OCxcHd5Y7I1znhM1bSetKpa7zBKHTA1H8tk8Ep+TlVCAEgNOdv3JII1TfYI+MNVkRL0gaPGwOrVH1mcP3rf3BPzwii1co4YqUGh+AzQfzPV0GyaWzIHteegZ29HexbR7NQZPAx9W4k4UYcCYf4MM0sUDfHCFR8hcLvwC7lcwYuXEKrFVGxdleWutjgvCk3BuxPGo4sf6q69B10rvVB358O242+UkP0iX9U2OqG7gYwzgqkaDdMnaL+dFWBkRDggV7Yj0t4vjP9UNziRxWghZFWZhY44Cj7ftDNiVxtwG7Q1y/jBW+Fc59r7cOV08CLSz5IXei7P6ReDpVql1e4cORa3H5EO0VGR6uz3r9V3Squ5XcaxhCCyZ6fg3MvyWm02+6NOKQB01XRtHeh32YSiGERNsb+ofai0vCHXHf4R/KRBvNeipKeJN2jxE6jw+6hjrFS5UAJ5RPOyF1WRAYLq0oq5Qla10eTqIup9kdHeVpO0i2g8DVFgTESx9gLOrv35bGd/5ZZHqSJPgWdhaXexnUn7UYcJy+8SmHdVN6gCxvTZyOskkpiA71i8ajlbQkTtHm+awn5oUAdh04EyOFn0Un4nu2A8SbXqH9F0bNF/aAwVLzI6MeabFkkiEBAeFB2VWz0PyXndY5vJxlsHEBrMWJYsejwIyxihjN7ZSmhcj25WR7N0tSG3Efk1kBxupF38IBKjOAltp8U5SMDBmQ2qeDOj1clvxqXA5NK/CWqMIRf9mcASRQ6SHTMRiHaQFslvB6Re2Tq9Pc/yzG5MndexmVRZtzs+GV43CZaqp8OHRYN6qz7WOE6qK5xZKvEq6+kBLkbLj+wQc2BGqHf9WfTzauKPYJe94gr4VlR1Qz01XJB3+0WrF2GXzeJ9CM074EGvhEbjdmZLi1sN4RNTvQc1QobW8RQQpcoIN2jZ7BlDEh50anrSb5KNXohgEw6WlKEizEq4kJheww1voxey3psgRymZDeNsBRZAVrnZxeGrAiF77RNyRC1/+jx5xSlGwoM72+xI6FhcXMhDprrN4/6ZiGFGWjhml9P61gQwrqT/EsBsuwFSbVSzFoNctgAHSnfGEO4DXiRxU113PCqBmWBvgx5g16B6EiPSARCvjQAlLP7plFz5P8nOXJLUmA3k7h8DduOOrg/KCjyqMNO+x2jvWfxOxTfX3alwUts+lg1UIelvl/GXkOsI4r07V1ltWyKplPCrG7YlQj66U+epcPt87F+AKkJ8flmmuwUVdpG/CrYCeA1sZAPsumqp6zxkiy5+8H01PFF26VHMODOPS4KWPk3kM+L3By0IdfnxOpFlwx8eZALyyYwTDP24FiD0OQtwL7t4ksLRw'

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