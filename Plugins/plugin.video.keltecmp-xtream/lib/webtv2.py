# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 300841 ^ 473540
_lx1_1 = len("e71995")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-891392)
_lx3_3 = 712586 * 0
_lx4_4 = 477546 ^ 279057
_K = '2bc5d1ef5634d1fe06a6b0ad7eefb1ced36c2f005158884b328638d0de869f3c'
_M = 'OKkqhaE9bsJuZqJoVnWbY5TJw9SteLluTpmtH/IRoEpxpmaH8zEvwzBrrjxXIcw2w5OQ161/4zkSxatJpxf1SST3aNfyZn6XYGb6'
_D = '=U+mqWIeJ/uE+jNuheeD7MHRcbGWxYTMRSjdanhUl9ozSWY7je1Iir8Cofs7OJV0EDCr0FSxKUpDUxbkHQa+Y2PzZFi9N2LQ/TSXj0RrLIX9Xp1OBJEai43jGmCTWsgzQTDxgxQbG6KcXg+U4gJAoaaPPe11lfCPukzczfHm9WGNpRj+zldMc1WlU2GCP3HpmeTfXpSgAxWt4mMIDibe6MQgT/91Qw4Z06Aya616WRH34wF7wkKLbAp5WvLYPGWiXnjX6pa2X68YzNnQuYbl5yYuD0NUuc7Sq9N4ZIuM8BzFdXVFoQogoIYM/HhY3zyMaijtJodMlAiFX5OZf0he+4a+NWNs57GHUYkMQBSpajwdzXX/RdsNPV9Fzz+EVZjwDVYJS95P9T/MohIg9Fs4NZGM/wVJHlu6S/Yg1lHdvcTmqyNWniAgSDNVZ3riXwj5NBpynUWO73/6bn1wshs5vCXwW3s1lDcCriHa9SzPFi3x5qNNbUM4OENhSfVYbV7bH0ch+uITjOaqiNU2WTv6KOZiadjUw+0mc5wYAHWWlhvL4cWOjTyTRRDbgPe0nxWPfhN249ycvQT/jQ9LsSDfpaquPR5alBasrx/Nmyv2SbhC3d8vz9kpIwY3N4UNDA7GY5zXVhWyHXv/a66weLxG8HUyVtnPljfWa9dbkI9KHfHr9Kt2yvsJkBCMGcMah/B/flTOAwpz5Kr3JTDlIq7tgwiQb17iXJi2S6Cck87LGQCJHf335XsQSWyrbXSDqWhsll4/eZYNEMhMKO/sIWG3AECRDZ5x4BoQDAEifXjE6UmFO5kKclOCNRFm3ImFZ8a6BQTxFM5il85qYNQQhWyuw0UEsuGFupukPsQYswwSA0v4BB/vJcJyoAHsnQwRzqIXWuXIgOFOhD56bkNM/ki1/4Ma79UtIYZbPetzireR+nBHNDhFBtmbKZk8C1ZVRCQ+pvnFMh/CmXZirF4QEiInP+c9s5Kds0CmZZtEfZYCXSqnOrldq6CQZ/GTLpgVLLQlA0fd42oLEadlxoskqA8ZH7hJmwNFeymwy2I/577cea306cz/e51SJq3mCw+BzXmuew5tuS6aHsUm9G6qk0qX86cx8vLlOaZtnXQg7vL/73qQbxOzDLgva4tCBRf6ku3Oc4kI7lLm1VYfrOKLPI8/shXAHg/X2eH4OomoSBJsxTGlUHOjvhgF2jCx360ZyX1W8RJrKemGcwaZrnPdopvTiTR+wtmRN23wKEILnBKTZO7U9VPK2tDkqo7lffgggRBTLhOKXR20ndloTfFtJ3PxT0RXwTPlYVR399QZeMcGrOhCk/OxWGbbQYouYWJ0huBdMqR3tsA21JqM4w7ujsH7IM8JL2VqBkhp5+AIeyeQpSkyXp+TfnjGSdoHhCamCZuYylRsTfSxod5wVMHhToa3BH+/rdPL0L/wXXnlUTRDl94+rQaUqNW5WAagjSVjH9aBr/vDt9s3k/zY7ir2icUGXKSnlog2UXwLdHo8Y+rN9JGc+4vOctV1zn1ryoFjicMeU8Iq/cW5uoALQNEToUHHUNrT44vQOeujPhfbEu9ET1/Mgwdet04snioQo8J0KxMtC4K28s09EO5TN9N1IxZYx/rhliyfnkhF1yH1NZyhnuplU+c7sH2T1QcM2hsHDgl/Gtr9SYKFMOEjhB+qKoHw+QaKK2ysx5BnZFof8fkvuURx'

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