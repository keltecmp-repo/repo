# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 648196 ^ 454120
_lx1_1 = len("ac6d3a")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-446988)
_lx3_3 = 906949 * 0
_lx4_4 = 702425 ^ 303472
_M = 'THOjFNWriGB73jJhpjwxW0Sm11dwdhluW38zL37c3exHdKNNw6mPMiXTaTilPDUJHffUX3ImH2VcezxzcY6N6kgioRDG8tk9Ito/'
_D = 'dGdey3uqMuXyeIEAIAWCzTLDS7kb1/A5LEJz3N2Sw4kf42Z4QSOBuvdCEcoVU6Wgf4jTODp6roj0AYEQKC8pEENHkWaSb9kf3IRqeaiYdbQJivZUqdZboqhkF0JgyV5pfPoBQSVa3HeKzJWMx7VbtVRxK1/4ETltyoHeOmhn5hWIsbXrnsxDLlGyI2PSOSOcB5kdKqb/iSUWixNMn5qP7me5Qrf+Kvv9vgx5E7GODwSkQdcQ61x8qYjm4bHA38dDYUaHWX32V3SMXdirOTNBpoiYhqDWStpynLlOEtwz7OtP9b+VaJliXaQjC6v56JbmAEYjkVv5b7DTk/5MpYE/OVFdbORWTEsGEK6s1zb6b4oYLmgg1y1P/2KbEp03Es+PtXuhkTI8wkH4a5Oimqt/AFNUp8GEqjmJ5hoe4XKCmr94U5iHsq5nzcMKPoV/2YxgckjEb2OqK+h9APD4lA8qLmvt6O7hR+7RaWP4LsADS8dH9QhQAF6GqiH+d1S7b3YRmfit4k13AYEnLB041KkmxZBYDZ2pfgLAMFVbDbYyWVM1teqDbonnYf3D/DVV6Q+/tFumG6dmpVXJtuMT2zxHr6Q6AdOdaALU70ynRQ+BCBprCZwiJop1QziMsy73x7lr8o0GZGhoIMfCF5anXotdV4XQaa0wkCnz3/Iu91YjU0RkXT0ote/v2YX1LDEXyUTMUBaqS9nUyamSdR7vWeHXaeKGLzdOcMCikCaPBDe1fTB3qj9GaVAzT9UAzIwuJg+8auJgrvHzbcCJjdgwzAMQ04T0rx0obwc73XwsorYUwd55f0Ga7QWPxPTLH4ERrFs7wtm+FhPXoVGfxqQQRpmAHVSLZVCCz8UxIyv+6txJWXWqy0cpdrrXKehJk1rYoEP2s1YDz/zmL059YdAL3Cf4m5cBcbsQWZTbIsdpURCSsl6nIGYXKXeCgQ+m2j6j+xBI0bTBeAtD9L+1VTomVB5+By08Xs8Jb2WC2dgmcxgC/o+0pcRkohgbeXrZWOl9fdc2TZ0tN64Uujszfvnen3nejryCsxe63cUC3+1ILObK2RV6SdQXHb6MtD8H5TNRaU+2R8oX8OOkKOthRQ1EDe/yoEhfln7HTvmCI4O24u4rfrA7+/mQLT8R3fMQdSP2aZbAz8rGyvLq3YFumpID12FWHSD7WYeDlau/lZdiQYqciP6Ga3MvpKUkdgTqR2WYT7PfxYuF07vgY2g9Fi8Yc3LQxBvaPR7T7svD6Mdw39/DhQ/KXPU4TQ7suB1iys6LKGfTwM2QMlvU5gesh9UR2fTK/lVNSSjlvJuQqxBGG7J0KVl4isyLpALJKkLyQDDmwKnHU0ZzwkMLpZoxpzryikYftcpWU/Shf1x2Q0f33PmYCjrW3EPxpJHkaISHAoEqYumavINBitXS5f9/XfV7z9Swp6F2tvqnHC8NaoeYFsbMU+IlhcYHz3dtpC1YJUyTOH8KR6YMc0Dpzf744FBkffyOP5AQgB1QgHdLIyjkKM5TWpQl9oSPo0qIsqEviXdt6l7PgUcFrCh8T9SZ5dWb2GJ3cSCMuISyQEJv3cttTEbbGwCPVNOyaA/lSUakJJsPQgo18yVDUgovgWYAPYYant8yLXX91FdDe6xQraJzaikwZ/B6NXEOMKdME4FHJyODJEFb'

_6c86=[140,174,80,1,121,134,58,211]+[188,108,17,23,178,238,34,152]
_17dc=[133,202,177,249,65,160,15,60]+[237,130,163,249,93,127,226,56]
_7fc8=bytes([a^b for a,b in zip([254,203,35,110,12,244,89,182,207,67,117,118,198,143],_6c86*8)]).decode()
_10f2=bytes([a^b for a,b in zip([246,175,197,141,40,206,104,79,195,224,202,151],_17dc*8)]).decode()
_8d1a=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_7fc8.split('/'),_10f2)
with open(_8d1a,'r') as _f:_K=_f.read().strip()
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