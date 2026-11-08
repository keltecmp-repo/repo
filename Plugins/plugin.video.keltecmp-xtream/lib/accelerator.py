# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 272089 ^ 914445
_lx1_1 = len("a5a5a6")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-597760)
_lx3_3 = 133646 * 0
_lx4_4 = 267995 ^ 342978
_K = '3a873824623993962ca3c429a3b18e35bcef1bd4c54cab8fe1b5bf7d9bd0f345'
_M = '+1CbHn9HgW+TKNqqWloJoAopcUCrrgAy0iyH4Qknmsm3V9hPYFXRNpAvgv0IWgmlDiBzE6ivBjCDL9LnDnWayrtei0g+VNI6kX/U'
_D = 'zBK8KA2r4MJkH/4Ywj+3z34IPWDKbLh/g27YyEWXT67RGEhaigFiKABNRvIZfZhx0zFeTKfTkL0nShv0iZ1Piq6cCuUaJGjYm3HAAka9PsWSwW32zqU7RYhWkiyg3V+ynqcE5vWLv5b/2op53WOaRWP8+zsIpJWWZHOoocIsLqmvJSlvrLCYsvUhG/LIEUSoYq9rDPFC7E2NfEku2PzfYqHKCb48bRFjsPlHoyCQCIC7Hnl2f5ZOFCnDe9efT0QxmJq5RgJrWW7HzfX+j8Ag4Ie2jflpCjgjbc2CXCD15cChBDCvHDwndTEB776o9YgEFbiU//RgZ6jxiVJehMeYMPTnjJqs0i+L1b84dguxQpTLsHauEFQd529iGlzvNY201bc+1ULsGp/v0Yuw9cNJK1zy47ZGGXsbY7G0cnBoP2lM/yqXWhueJwJxJ1s/fn33W/GlSVxW4UvFnwGV7+uf+L97WZe1Ub+d8c1vxB0DeFirYGrV0Jb0uaBWPLpq1M24O+x5jjUyO+IiAdSRwNLcRkyRnkJlFCxBg3pv2/izUNL7NZ8F8QV+y+ThYGv1vUFniIoGgt1fMfEQi+lEhNSC11Txpza9n/+s9TTqyzAD4u/hNlYvUyUxvg0TL9TNNsrVQC1jjRkXyw1oXAhBMIgub5HPjv4DLhnps9lVM1bC16lju3nM6jlcSp3YvK1lQ8Rka+OFPXeyCobbWaGCqq2pB1ebxgqp/Kpsbre+O0zKm81FsOsfpNG+rQBtINeWaGKnGTrGaxoBSRZmDowRyxQnDtFWh2VQ1BMq50AeZ5wUQC/8IYqDWjuI2VfIkEvE0X7AmvEFwVgfVNCjj+gZ1SfG3mZIFe6Kzewo2pBjGbL1icoJvDRggPC8kCYdAKnNSDTkAw/cwsQtFRUReZ7vxOfKqKfpEAe4ZJRY1wcuerAvGw64n9eeP6u1vceioBewfZnOPw9HlS8w90LiJWCOKmX12Yo9yLY7MlJGgHfIMM7y3ZyGpJS8bHUdwyW6B701x8gd0SdSDzQCAoHoUPKUfk2igQtF5+DJoMs11dkNQzAj+7Wod5D65cWd+OjkNzz/uKIzGRs359GQmnhIqdsPDST4RnxyRcsNEMCOa5OS/Szuzn1Y4VymGKSxeVJmXWHRiqDI9DhUue7s8LYgpphvG7Ev5p1QQEeYmDdaDSvTvQ5mINitKuBYKti2znUomvoon/8GI8BVvemHtptKsiv9fdbPJ0pvja3DKO2qpR4NsJkPkXRMVBNvdOCJXL2KsOKTzw4+Xn4x+ppaDnzKpAbC8vHjNO52t6VUPPeQRhpcTxTmITZDkUPjMNAHgka3v5pFr0iOC8dCpBPyZKOa/75/kLzQELzHlqbD80RAhBTsQaaTdkfjORnD6QFSdwEsdmv24mkS5E6OsZBfAJL5qZazGoiK/H/eZfKh4QjwrRsZxGfnykxco8O7seJm8QPt+ucALAjzhgqY62jh5GmefBbpUqISImW07NA667Iy5cCcM1N039Ow6K3zR+RxLwnQZ5iEOYlptwOFwxPDvYOoZMAPgqT7xXmx3qTnGGobfdhtvVmrhUXjXfyf0QVlKl98oJRYCfKHh5V4zmpDZBLvsJgnHP0qY6RuQTrOTyTlPwAXYsmwxRB06RnJyLb9NQpEy/Vx'

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