# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 115797 ^ 785837
_lx1_1 = len("817e55")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-745129)
_lx3_3 = 509426 * 0
_lx4_4 = 295530 ^ 690338
_K = '37d97b24b7f3c3742b3f88d5845a512700067ac0ec9873008ea48a1c137e6167'
_M = 'ctP/FkVbsOxZCw=='
_D = '==Af01dcm91bTDFtQ13a3qN0F7NiPujz25mCZAaeYpz90JLF+v76O5rG1+ZH6Ib4FSUiNrh5bIVHY1XHPHg/GzuqSg7wO9gOsEwt6OAIsUDu8fAuyOoJTPY0hNWbT0TSwkDN4hbLTqFfSVMxQP5GorUr/2Hz/StqKz0uznq5dNy8kWwfHZ+vr6llMt+Ek1+dUPPmqCSsefSTd903wsw/A8l0v6w6cOH7dNGcuVqIa5BQc94SWF0NywJpkY6w4/g+LU7R2r+z/ldkSMv4N3fMmspDXr92xO19c5BHh5PABZZITum94ntlCV9h5XkHeU5P+PmNQFwmtHI9+7JXJz7esuWHARpNAGNKkJvmbZfVg8+BB50uiyTl+pZtyT5MUcuuMLYwKmydQyvCnkLV2BsyfiSVG9dDrzp6NU2Jdz6kn3j6Jx1U9dMrH+91fF1j4yrt2m1B1HEriAKAMXFnup+/DJnd6GWIz2y/+QRDuyCeMnnKZqSl/ssxeJKE7cCyWq1IRefaNsJTCp5+kKUjmxQR/RxUSTPYpU+Xb8JnRa+lREP0OR9TDZ14FkeOpU+L2/s5Hcz+xJuuNH2J8lv3XhE6TkqL0ERwGq6PeQc/0pkr+t7a4zDd2TTlY/qgsTiumYcpfvNN4K/TVIfIBhSc6Eb1leVjn69XzYqSpVh5y4/50YOBXJlbMOItKh03TojFCAvqCpwZKi40Gb+FoAyzIVdvsQLDkl4NYuo07QZnQJgm07gxfIX9xQb8ZQI1IXDTHkKUEf3Cp/JYcYRDMFqjtn2k/G52/9SNCUlPLWNcyNni6LuAOOtykZfAzWuN6JMAtM+dukA/Klmn74fMCd/sPWvetDT+7CWeaI0NSSCd0SKrvc1NSDHCxhiBAEtenxJ3EDr6o76po3sirKVDKsuwbMOVFob6sMA67sr1U6LEUvHFyKmDFrUU6wf5zEfppK42CXRdESMfcLvfEXNLfLlNV9BTkW6sNb1TNYseiikaVQ1W6eTPNdwCzbIfjNya2b8tXqBEaZqFLZO21OGImOssJ/hmWlPhj3Wqoalhww0K1H3iMXTLUpcv3zx9uA6p2PlIcpjFCYQ8TcZCPOuwK9tGP9Ys5yss71cGdpDRHgbTak/7QplBOZEj3XBgXc+7MijPKgFLFJspk3xaF3eytDJljXtKMTQH9OYjw3dPIoGAeuA+1mthHmh8ccw+OkBY5t3WcNFa0twu7wCEdruaKkgtIxwdRhPkmTc6o0nkT6edNhW14Myz6iTuYGPy7yURQdvNc9CelqBo0IKP6H8UE58K5nXZCCCCOfNxirHsGMxxR9QFhFoIy7rnkFkhDoHQO3clh+37PL8ntBGYQ6seJdrZqyncN6FFr7B8KDW9Vu2Rmg7baGfRgYjAKWOy4WPP/BG6zU3dWKgjh1+pYzeDpgDedooVpk81QTMgQkRzrcOuZykKkc0bd9ZbysnDWw88Gx2iNMh4bVI5vxN/fM47Esyw5ZFl86yauxY/6B2l2dc8Q9XC4FRkBDVvJ97jSBui8Q0rUxKXy/0Q+75fa1NUsz2GT508Y+YI8oRT+uZy1ozUi+l5PStU7C5V3nuXPJY8l+3V6dMa8F7M5IHi3972RUI8nDPlkOk16ENPeXhRLWOZz+sErU8FtgOJwwM5NEjyvPDJvZdlMYimSGrDL7E4eFhqWH8bwUM+a5QERHVg9tLFqOWRmUCZyH++Nne7U/Cn5PK84IRpdYiiJ8PM2OVwm2FHk6GPTb1Qkk7UTN9ze45CvEjHIPjqPyXUQHzMFBdwl4zcGnRsGXOHwExI9FxaaMW8vRJx+npO9GBLTbBZMqQn2cECeQie7AgL1AQw2sn/I/y1'

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
