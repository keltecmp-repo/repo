# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 676169 ^ 580586
_lx1_1 = len("83d358")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-467094)
_lx3_3 = 444255 * 0
_lx4_4 = 562206 ^ 204011
_K = '43b5ba4a3f91bbe6f4f7126c256c1347fe610044487ea3020175289728a06687'
_M = 'FzkW7g6vltNiCg=='
_D = '==AIK4ToLH3SkJaRteOZRPtTDwPRf3+1hHaADOLO3+E+JPQpW+amzcN4IKIDhQrmnQcsWqy5LnrqQ7suowAByFqay5y7PKesXasV5SS2tJtu1m+B3vRHdTkfJLw2fTK3VC9floU1KSOWu75Vy/I5uFaJ7bYsquP8JLfhAjUlqQQOQW5ge71qKCFbUt8Un0JaGqMboGmem8gJfXRKpMj8fubDfKszMFr/03X+5dnZKcyeYOV9GXoqppvvqx7aIJQVDVYM3g1nNcLidQ5kb0T9mUgHmawM9cin2eoPsaso/cftiSB7p10bg9AVp2zEkuyhHg0hhpfQyhuCqaHXbpHnV7HsvAl1/kJeT1Y56A5ow08ghHZjcsEvw+JC7oTX8chI3iR/EdiQeoFWID4571MMtcr3HG3sgEbGszEOLoXqRYkf6WBx6zIvlpbipO5oarxIYoEUBH3Hu7b1MqJ8yCrSzPncikotWktdWKFfIYAfQyayoQsPIKwecPigWI5otnu/9Pc///9r+R4uMdLAw7XGKnKkzI1ZDUAcqQUiU/2/ja3g/bCpkXKZ2BwxSXomrnDe7DLya1PySY+iL/EUc+AJqjqX03louI0d8VEv99v4OLsatyerc5OW5DLg64dRAYn/aXG7F0uVa23h1u3Q2mQNc6KyMWR45+XICXnrX0z6xotT/0ad8JSHxRWFUc7caHtAqjpzv5kAnxaya3bYuDhEm27lPrZADjrpa+teqyV6rzEqCSrpDXaEIRUlDyIiVEkSIrCcrwU4x6XHosk66Qr1iBGnOZTiP1Pc4Dc4sJlMBcBlVx4qHuAes5vq6cyNTaZILrnDvvGT4JMTvqeBJ+dET3ySvVtsGbR7C4MeBHGZxquw3PdEvVB/C8Skkq5iGbcsK6CeBM3OcV/Ngc3NlT6hS2L8RwfISRcLLyF+MdLaOBandya9BUULBE8W8KmOjjE4qtPWswpV4CBEwGjMI7nwftqRRqQPC+7RidVnvX4TkuuKZ3iQi6WcS5eY5EK7MGhx3jCrWFNcDqqyR2Y+1uwea2xp2+RhuWxoD+FFnmnYGOVRm0jL/jVy2P/T9f1pTwXJH68hrOSnT+0GM5BMdOwC4r9WO5GV8xbzsBwJmcBhUe9fmG0gL/SrvyBulBNS/0TtCKG0xpzS3gzzc99aO/7r1NPU/LduAVduerr5bDHXnqsFCFvpj8qq2QVXaTDbFCn3Zy+QDLVvB3rGRInFrECgHzxM1hDLKg8/S/PaMQBfedZ7E8gfIyGo8YPvHPYosiEQ0GJwKxU+AdLCPEX0aSNNcTR4vxUgsx6bgQdBz+iOY17qzibxLh0b5Xr8d8NLG09VEvKELSnOhExv59r+bhIQ1mP/fjhwOCfEEn6aOmkHLUqPVERsVuS7RdocrKroskd4GxF95Vl+aw4n0Yea7AbOfRt/w6qPk5v2O3M7MltgZVj4+4rfRzDxuFLK7YBlCXo4j1+gF4YIVoJFNO0Ok1ZVvMiBMCvN/0MFjw+tZ9LgUih/HXKL6zwdlB45fWC7WRGLsYN/MKNQJoEy3gq9A4dMdFCPsK8y/HKM8wI3SxFQATpP6RFV9/ey2ILRXaS+aTf05d5omax3BZCe+gHf7fAWJNHUoIXFUdOhtlbYCF+ZC0HF/OMZ1sVi+/tc4x7E//XtGSJhSMfw7tj9ppcQ4oEmqp9Ct4ZJ+KWhA3DGGk2Tb7WfB1kuhkQFMjIiXH2q0rWWXDwKkRBa9HPzKGvdmZYuAadJQ5APW0fRe8yB10N7gfZ7D7Bu0tXvNf7+ZFFVSMDaksHjWLs0cHcjr2fvRKPT32qrEaI1b3T7itgjg7DW3mfg8EOnaBJr'

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
