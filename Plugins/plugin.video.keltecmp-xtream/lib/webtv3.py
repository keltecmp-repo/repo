# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 430611 ^ 899479
_lx1_1 = len("0b1fd9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-972801)
_lx3_3 = 566265 * 0
_lx4_4 = 465328 ^ 772689
_K = 'b0c6b3a67ef6293f7fd5e6ee72e11c31fa3cf85b8b1eeab5339a3a990c66d892'
_M = '7MgAokiyvCGz7e8ytIDwwAN1E5KQdkcSOlrZebBMwL/riFWiDuDueOjpt2Hp1qOQVCVAzMVwFxk1Xd0j7UGSuenbBakHvL54u+vt'
_D = '8k3fcm+JhUkHYvH7spfTD+lU+hTy3E6YDtCbVVdsC/kKyEIeQyrXctCX5+2C/Y6Ge2LhZ1xIAT7XeZEfrnk2suNQEohKrzk0TPat9roqXfs25rnHAa6qe5Un+mz7GcqlXhFnZMWZpSLlzF6+fLq5jtCFAUV29oVQqXPMrtajNH2YlnNg8Z02wJX9XRQxjA+tdHSYV+i8rubuWE28MH0/Xdtkz0mWbMzxsApBs+/1kATI7DVS1MnvSuCk8M64R586dsc2fHbJ7Pv7G3e7wX7DMEeTQFCWxLqdz2N3b0xubPFQ861WPuhSwsf8FcWT+UbdSKruAxKH7bBZ/ox4b3xjhXdI9pdWebP+aFB5R4YMEJwVCRLl/9hMIUA0bFB8z7ZIOKDqqy6en58s2o0cKKqQkeJjvcm68W3+qPgOxzWFZcZ7rbC+LNJ7iSSzaR1jqcjHrtyGLC9k0+wANWItnw4+h/2OwxYvv+1XMA9xX4B/qu4vZv5HU3pmaUwp2qrnUnFVe4ZAHb7qYOlErzGzlEErMO1aeZsZJGFIspD7Bxul8auL5C/PGMKgvNunDY8KSp2WB45On+BXKR/pePMQF1zij/B7BUqoNenSzy/e2nZI/yeK/Z0G5cgWhcfLt03kkPB/1bs4yQCU+hS+CDlbxKAD1o+r3rDpQJBwX9y67jja3vun97gzB1Eg9FwXLAALc8dXrz1XcXgkHPczHxF4BcSeEkGooK9wWawGEb020TPwI6BwECK3MDWAFiNnPogdBj3g7ddjsmHgUkUVjPFi5FUK+lDTfo7f5RyLEoX0z23WIIA//5GmtRFBmmei6OjxdlJV8r2W4DhcGVMC/PwRbO1dvl+Jl4Yr6a5qCpjtvnM4pU+TFcMIhzWe8akv3iStI+tbodESHeV26fp383qJZ1ZOgsgZJNLrYJXOo6QSZCMy3JlKibxyHBGWJAqxARREPbybOUECncGKTYVoeGpTKpISC310L5kbM3i6tRSLXqRw7cKW3A9O4jnyIhd+XJZZEdmi1paoSXf+mgPYkqvhws3m5foQtxYxDSVXVWioY50TLNHEeAE8GO6kOFLuyQwvWoDC2cLflUNCWxDn3xDQ6zb4r8TXbLvIWdICUKK3ePUb0ekt+OPRguNZKDgWSLbgNoHQMdn9nlrOerJc1+Fnei9/VsaYC+RCErg3EeALkUGdNupP/xuL2rjG91PMkr8xZruaHrr+NXClksIOBrw3GgzYkz7R/SiLs6FVGB8XIfZytGkZXRwimslUgsZTSB5iNzIrEbqrQXaxL/f8KNQkTltluK/wGav1TTqg9eVQ0RR3ro6QcR/c6Ikq0+S2rpYkIrc2lUl/X4Vwwa1d0JuKRdy8gj8CkkHwg0QKnUOzM0LuCvZ7vDuop5ozeEBDlh/9AtR5LIImUjDRGcrDCajhRa6fUMc4HuCWG70Z+RjU3jNek8g18PDzo3S8xb46rxJUB7f88JTs6bVuYGivwiQYfJfeGxLk/uJNuPESKYiMwBsnNoJvtcIJIonyHaExwUChz5AONH1tKRnKloOhzO87kwfxNlH/5FsdL7oB0vWHffgGRJj6m8rX8xbo0icLO0ANXeSajIlF8rs9iLK5irf2dsCs0cM2KfElpMXgi9j+ZKT+fiq937GpeSN/'

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