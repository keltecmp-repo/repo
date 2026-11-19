# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 449258 ^ 307225
_lx1_1 = len("daa5bb")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-897058)
_lx3_3 = 756260 * 0
_lx4_4 = 934837 ^ 429389
_K = '929164d757b22427a1d280f5d0c371fe1412b91760b100bcf962a0db72a62996'
_M = '8bAb65XyZdOElWBaEWepQChTPTO/03s8BfBta8Xbs8yj50C0xrQhl47FPg0SZa0SLgBqNOyMej5U92holYrjyKLiEbeRu3CXipc7'
_D = 'aR135Si9hvTcOxfWFx6zTbPpa/iO1HtNJ04YAUL2Nhg9TFcWvkqVK4/EzQCqiSaLb8hWr/zuRy3dhW0wfPikXLA9ivrpAxO1ffLeuBeAAdMfAN8XYkX/+0c/7o3r7MIDnAO7d2B2VCh+dSPVVr3CsE2vYXd2eewoLdu9kQnY5RyXAgM38A8/lO+tN1+tnexaSH03G39XmZzX6dAjNdHpeFNkLEOBNiqwCV9l/HtqdZe+6rIFUGZ1lXnw3xAnp2YJAjmBylDlakQrGipfJNgETD8R0QPRZLprx+M6jxWvR2OwMyS1WvQn4TSdGg/85uEtDMfp4/nAN0m/paGavtUvwII1NsD5p3an+D4ywgECbGt0EjwNXIuYGZ3VZy0nRFZ+BIbOEYZipTwh+APn8+GiV+XAJeS7YNVeHn2xVX+VTdUA/LLOQKRYDXhVGxTpXVeHCvQ+DEh6NxdMGxEvXF8pV2fCE5LZuTrOAqftgmnXpSKdlcHqOCg2uMYieXKoOTJ2Y3n0HaaNmCYTwFjTr5AZvFfVHue8oDshIwF97UQdiMCaAxmozaO6YvbJlQ72kOy9nyZwrbZENsVgOn1Z9H3gIaIFQjA1NqAJn5mi4Hs0Pcb5hw8wBTlnRYSoRhOcP7nvr/5zVKjEkwO9DTC25fYgFZgr4sU8J5MKHLwktWuOim/PkQpbFfiKVE7ed2IM/E6P3Gs4rvw4C6Dy7IwZ8BEET7HlU2VRslpBPuy+5Cz6wAR1TwzrlfhHvbZw2LgJ6VnioSfJQweskbPdVd3WkI5fjFVN3wWQtMrWWzQzLz7hDP4n/N/X/bw5sc+fLrRGV5OQ6YG+QU+mOyOKlCIjgbyE+AEhnnC1qkfSikiK3HkOpiz74hUEVcUb0/nmV+K2k7sbDtKaY6ur58zesrdi6rz3WpjrmbpbknSYmX7en1gjHQPDS7xQtuKJR3fTP8rWNedvlRwrmVMW1yiDQ3unPWPloDq8nRb7gmhHrgNc6/Z2SWJy59c0aekhtO/EAoHzklxLfK6kICl3u+3hq329HovvVq41mH5cjeVazC5Uj0RqoRvvPleuN2e4hRAC//AFgxA+EcD6iuvgdTp3I1RX6G8mGnGwNta2eZUoaS3mYwIOvQ2cVpdwFr62YMTTpvfnophPyXWz6+blFENByQr21NjABb94R8yZ4G3RHNJkVCAC5WXSYimW64zS94bpSIzf+dbZ1Yl4qU0P8Jm0kHPi5Y/perY+RXXq6kjVcSwVKOcEWtghwSHRPL0+dPuZ5U+is5RK1+dI/BrgweLvgXH614qSGu/FXq9qmqQpY2gevI/C1cu01H1i8UguPEu1AUWFCN6CH4DNnj6o2CKDh1rPWs5YfCLKKZYQeG3mexNN8GmeSC0BLmXYAoNk6qByAsSJLCmZDQHt5Rm9uCOvSzrL1bfdmDdVh+6pdZGLAQxTNiHAir5Cxo0ZC+1xi9Rh5puDPqR3PTV2mKOsxPlmAzolc7ezRBBkgW0/alKWD9L8B1hm4wDlHPkaqwIW7OJ0JVAZYynnHbKVaSRlMuu0gZjBIz5q23XEmcGCzfFLSYKCPNx9KN82AqnyqVJ/1rXeXAmg8eibH1ZzO3OyCDOYvWOMwsEAAkdxKLFFcYqUJGiBTQHfraX7ct7tAM0AZ6xWXkRWW/iJjsiDQpbrAID72blrhRjOTJaNbndN6kScUZfeY6tQkeKnGr+KslRNm0cl4PTcMFx+FRGwv589yvrKcuIfy05cTMf/cY4Uc1ePDwj6ichdz6L4hw5MOsQfJ+UnrmR23kbjFP3fApTEMy+n1Ky+40wMau66GNbQoFHcRa25rBQ5XE4toH+7AmXg6LC/+gXu4dBbAwwfHGoV'

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