# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 744107 ^ 755314
_lx1_1 = len("32b73f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-973866)
_lx3_3 = 582021 * 0
_lx4_4 = 546743 ^ 815296
_K = 'd240809d38ee6df3cb364c40e953b9eeac5abc1c98e7db936903105a1e3835ee'
_M = 'kGul2tLmm5E2Iij8GjAx2QKDlGyjtnMogkO9viH2wYrIPbWCl/vV3DUkJP0bYzbXBdDEYaO2InHRFLLmcPOSi59rso6Wp9CNanJ3'
_D = '=AHPRdZ3QJ7fBk7eGCFfU8cqUMX4Ko6EUEQcz5/UT+OHuvoyJ6q5/AfEaAKFvxTudbjES3lFgh645yipYva4FOZ15m65w0edkAt10QG/x2d6uRQ9946+nnpnSw3wXQ5w2YuvtufbgQwXIj43HYx6NZHqUSkXnsR7eUvSnN5iOmNvEQCEIv59UASZabz0IGLk4hF+dKUT83ocrYIf0ywP57sDibN3mzsUmypaIckOC5T2zKTHfV8FDyOxWxPAnWogR9SdYYcMD4R/YUi07qfNW28dVnzRrpdWs+yTDo/yT9zFXCYbo6ls9dgaqv20aXSQ6RKdindFQz/+gNNsxg4XL2AjceYV4O8xwYIDjbRwm4dKX3hfbofRlVLEiIlO/mwG466HFCj0nc1xOMuFDfHLIe8Yp/9n0eNR/gsfVoWr0u6+zMcMdd3XDvsqOP+Lkc+zsYqLJDawDRGuQ+5BWi7oH/qzTP2j4X8k94YiBwVTONbBHb5LD74NUMDMYbghkKRr+ksa2BTQxPq3ocCpoNDxMDQs3bEcNTPmnlNOMhPGORRtlBqACskMY2iXsXZWnbUuuy0zbFDiQ/LnUg4DJKCI7yxAb8UdK6PhHYHHcVhtlwShxxXinKbcmV6aae0Zg7/91QRyEbfOCN+7YcyWS05HbFXgrFLv0CBtAduOcfF94oK7orBJdY3MKjnBT6ohwZ43PLYmAqD2DXV0atY5uwk1yRFo/ymjgXmF+La4kdIhSAIe+2CQlAHz9XKEmBqwGp7s98agnzMHnMLLQ8fLXjHtvsqU459Odg26vYmmxH/bJgZZDzsaCUkH27jjSLURO21YyN7ZhuuYQBFVU6xvI65thulnf6i1AM6ANsJ/2yCiBu5/dyPvu39dyW9p1cQ2L1z79mWL4+EnCiHVxl0PHbG+/JBWUEQpg9ZxynCWBvzUdzqya3r/byikbE+M/BAJy7uVfUFgDeAboPgiIn13B3HVANTPf92ZH4rIVJdFE9N/n0ipXFWqqZz0LixMsi9izVCIrlutt0uXHIzBDynX68RdVAtu9LBPQ0+wCp0KkKIK48cO6LtJ8BYPZZIDcI4x4REMDwjcPOFbUE3X5m5ehH58yYoinTenEkeOTHnFbDHdJ64RSzrfjjtzyTOXg3MYIMmOkGG1LGPf6irkLLKvgpLQoa9I7eNjR6iglUflzePzDoS6GWGgQcMXSPS8n14M39iTxeGIbmnL0d9cFnFeOP+40Z/no3YAtz0uz9JoSrdb4EllO+SxAzXlNq9fuXkNBI8ABcInSSmT7zEo/fniu/7Qw/sLETWKHeH5p0Ot6OMZuVTG88zRvCKI0zLiR+CHay52ZI2Jy+Mo/tAFsGQWgbwhd8RHyJVFv2M5omVPX2iV4BzhZHTiojM47ru+u2My1h17PyJJcVXL0Vc+eCcLTmDtfCh0vHhigIXSrZbmQLXv+QAXNxSiDg8u4eLnFGPvtG8xnu7M552gfIQS68uLNf+x1//ICrgrxSUqzjXPCDINdgroq3P/z5ZgNn3QO+uSwdRwCpm3Yjskui+C/PTayKdLFTtWfx2negNezw3OHMlIP3y3Mfc1rR6iKV1rCdeqdcaBEUWgFAOUrTsOO0S9J7MjcJROFXo0QbkQ3DZ/hl0DUug9LkOqP5o3v9ZS3orZ3iDZc6FKHNtf6GnFk4tMWvvKrnB4c81yfh6aNWyTxUbreaBl/i7r4beyQiMtbKep6UpPVdWqRtJFRk4puac7GQIrRubT6tqSF+iJy+Hdu+EAcp6wVM1Du5cAHZ5nIwRsXDIhUXQnckqxC+R3hI9QBarbAV0R8LuhDV/4xkTXelXD/ivNTNNHh2aUd43ZHAUUevP0'

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