# -*- coding: utf-8 -*-
# KelTec MediaPlay — Fenix Format
# Gerado em: 2026-11-12
# Camadas: 5

_lx0_0 = 906614 ^ 276082
_lx1_1 = len("4a6c1b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-351638)
_lx3_3 = 690011 * 0
_lx4_4 = 869601 ^ 589621
# _K: carregamento protegido
_M = 'uQLmJVAmGORDNCmU9iLt1ty1Mk8fUFiJfhSXuDV1iETsE+t2ASMdo0hgcZjxIu2Bh+EzHhpRX4coE5TjMCSOS78X4CQHdhf3HDl3'
_D = '==w6YuI0OCG8ymIAv1egip2/NVnl9DNsfSoS9A2XeAN1xZ8bbtr4MUGl4fleqXoSLUlWKx+obZoA0EcZDKbroDaL3dpXf8Lg/x8cCjCaBc23UDw2rjMHhy1VPBT7TGR0rQHtCvtPvH99CQ1J70WxGEksKmkwDVkc5xG5f3iOtSMNUL4MFIy7IdIJ3yLJ1iYidv0DqQEI/BmZ4Ec8HURi5pSoxwp6C9ieVKhyVwE26I/6ENFls8lfuBSFwgxnpCdBprWKyp+k/jBXYCATJ+zE0mfdV2STzxKeB9pl/io7TathDt1bYN4kW14FL+aGViolPfBtMyRCNE/DqdZ4MFAk1qbUCbGJTg7lXCbdHUdVMRTzbSfrZzKFF4dZoBX5NwJcgPNG3gjQU3KUX47vvE9b7zREWcZ6FYWcVvOU8M2+Doj8NqFO7h4l0v1xbcvjPbpPmCY5+W2xm/VLoQrQn0dsHfA6bD9G16q/bIA8yVHo8cjNqGz6L6FUOb3N0Z4MeB3Pq/hMh5Wn529NPW8fXo7rb3FXK3zsD6EGmuG6OK78sDXpvYoW+vsTHX1b4D8e0tj8C6gXYBAvASG+rzrPAQdfpngVF5V927fNBaZdtsg8PO0w5BJkouyYJVXzObN29BUCTihCWJz4Ugi4NNS9F3d7bcxXufOadq/mmZrnUl94uziuArBLb1xw1CEqV0b6n2DpNIsmnaEmWN4ejNopXpNejTe+B2yRaxMRtBV40Un++L2TeSs8ZiI3irAo2D6rgbZan3AM8pAJAxg8EpaIGSThFVg0sSdryya6H/aItXNc+A8A9uCh2ZoeEX/IX0Av2wA5D0FvLfL4r0ElY0rnRMGUYbPd990sdqXSTDlptkSkk826spnhTDfUHZRZvUZeqIXdCercZTu1KlBNl+VM89jX4rLCv01XYOPzVB/qCQfYfr8mI+8CCS3bOyA7lJo9aLfdqNjmQlbCuSJEW95Ma3PT9zeNhSviVNddmk6Kqb0sjUj6Rf2hqgIsCS1AWmkuNnoKzVkwQkiCx5A0J+mj2hF6ptTIoJZTxn0HefsslUllscf9c/+pV/ABPCtTfuUtQT0Lu32vPV4COKoihd+zia0JaVHtnDbS6Pd6XqbzFOjfPwanQO1LZ8wwYusBLJS9a8+GDOe8N48Q0wD6RZpJwyJ50WRa4QFjNtOZlcy1dvff2OwGb4Vw4gN5rif2L0gMKU9Sbxzi7yDXTxEHjtczFfYyqHAt6z/qrUMa6KzQpiY/mSf7Snxj8CrD2ybb66r9FShXmp5YalpQTBn2umzlSClXuwO6H5+usKtYd78vsPwIZSbtdUH/FvtQKlNgkii8mvz7IZqA04M77iIEHyM2QRA8yCuWiAf58alURO/ZED2c5oVks+eNVyeRkaSWsFCCAKipDltLMlA0Gpred/XRROtW6UQvT+LrFr3WLWkLMNRmT2BLh99+q7VzKSJmHAfAX1xED+jcArcVPD4skRnU2SntpEzqqr6RBYgSZm3O7uumxx/sdtbDpQqexaWd44me90id4thtgIKGo3LoLNIkCDDDkY+WFQPP7smLTsg09yyFOwbWVmn5YhUL2+JfE05RBtKYi+TUGfXhBB9WZz8UebsWiOXewBXTByNRXbUtKfOccJi9zxw9RwPst5tcfEQg'

_ce8c=[72,5,23,35,81,191,126,207]+[206,125,57,200,15,225,122,82]
_a309=[158,58,93,232,1,100,172,106]+[5,144,176,160,249,56,32,245]
_651e=bytes([a^b for a,b in zip([58,96,100,76,36,205,29,170,189,82,93,169,123,128],_ce8c*8)]).decode()
_6db8=bytes([a^b for a,b in zip([253,91,62,128,100,74,200,11,113],_a309*8)]).decode()
_18a0=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_651e.split('/'),_6db8)
with open(_18a0,'r') as _f:_K=_f.read().strip()
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