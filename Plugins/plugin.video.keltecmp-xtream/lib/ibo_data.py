# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 498414 ^ 543929
_lx1_1 = len("a25e71")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-880577)
_lx3_3 = 597167 * 0
_lx4_4 = 820548 ^ 227675
_K = '3f58c287eb2f09b0cb6f668972ec3eaf646f0eac453d32ec198fbe135b8466ed'
_M = 'UpCv9b0YPQEbfA=='
_D = '=odKUxWunWo32kb9Fx8zGA0+4HjY+BayzzZUhK17T8ei0EkR/uIefhZeODxareD6vzZa1wGsbPW3dQyGc8F26pHGCVjtvUQwxx/0SEHyzQNCGyueqLXsa8O9x843TZrz8xD/uj30wLVw2/xfSG+EGz8s0R0C3MjiBG5e0tGmDTh/IS7+hF9Z5hFvLkziszI4tftbI1FXYPssBS72RNKz0UqwXewX06sGD4uC3TeKage7KhLLYcZgI3hl9FXaAGieZy60Zifd08GOR2aOkBvSDHV+crcOflHorWMiQfpzBUVCpQ16FVNhkZpp26hknSXsx2FyFvMCIy3r55BrCqcecjysg4hfotUSwiLan0qV19xEREfyob9/+Q1NfGtXEu4u6rUjHX+ygsMyf7SFLI1ZdBEOnLGsBtMjf9RpRuPEcgU+eo8gjuzspj74AurHf/TJMMUn4Ibj1qgKvJzkgDgu11r/V21PENiyflgwXu8VrDLEfzfDL+gFBGo5EJRZNoTSdubTuTUv0OzFqzFr4ungweLtb8IbbTTLbR5U0vpicHZ4nvTrT465JH13t1vWXG1SiarB4gSVmgG8D3aUXwSgAFlXuKa89t2duafI8paxxmab9RVM1Ajc0Z3XRrcFCsG2UFp33HquWheIE0aclQRoSk4RJYcci2CH8hYFLTEfvm4yjh/i7+drAjhInv7kHMVGR7A2Z2HL5jUoUKQnfzq3Alnd7iGxyM0GJcrvIoNBBwmJ7Xy7Eqge/V7UCxA4TTS8+8ttshmBuHg4smTUz19WPbvZGEEi2OS8qBWWXyvJSit8c8hhlu6FQTNwgN5VsX92w5C5MQY2JZh0dPm02kJcmtYY1vwgB9RXqfDJCX7lqJ1PiaMUoBo5foGiA3xiuNm7feycyjMw/l2KlIYrUxcmay01ICvkvpGLuQxuvKGO2CU8snKEXlxdSjT6kV3Zv/JImTj4CQhx+g+g7n8sv02Q85lGk9XMSO/jFJkIsrnBQg2ycuK8dkV66kuysPC92o26EDNOG/SqjFN/9w87LjGB17KU9BLPTLnIksx2CdXjpaFPjZ0P9usgMdUPgPX21Gj+7alxVZEiaillZOIvTx6FgBLYyWrhmgIPdH5+zYtFiqrm8K6iArwJEExVkPWlJn3uX+R4Oeeogl7lfcyeIAtwgPE9rqr/gRWAFRApcSz3pk9Ss9pUnLXNIwmaPYhj3S/OJooOjgbQZmNcBnHbAUXyzAm41pA8IhMEXhiH48671pF35O/vJGdyFzMxQMZs3ELIaIGKi4VUhQi199oQZGFYXSOdmT4nTRF+T5wpWm0XEz+GgIUiKKHKSExiuHMYmyMH8lRPgFe7ZoawZzGI8l6t3fktGBP7rFL0uOWhHGRlnCX56ALs1vyEfLMkeXcblr0uIbSaRsS48jjIBBSWlAlLXkF7jIwdTfWxAV8WBT6tOpBVPe+u64ACZAmos5tO11FtyTuCWa6slHRqiEhxEqhdFKlKjVWUxuW4I71jnMXSW75JvDBoIiBR9kj1Ytta5ILhcRJWzSAoYUgyq8q/gV8O0uSlUJ9U+q9P0nR3s3miZqIm/hGNqx7H9zvXOqnik/Eq1Lqev7GSuviHWT0WQe4yQCdFHPXPIy1xvviIk8brBjnZtsiNVhN5a4OIvPfRBvbMwvZdMwSF1xiPNMpgYt5LGlFcjqMRGA0PfexoX0rRvl3DBiBohGbgQ2rfr5TGZKraNoAVOO/ngHqTJVnQMcVUpdJCuGuIvBKixmHUbqChpJVejkI5jbgETJ0EcO5jjjHU5K6U2EG5wuBvOtS6EYzHWSOeuyoEyrWzqmoy'

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
