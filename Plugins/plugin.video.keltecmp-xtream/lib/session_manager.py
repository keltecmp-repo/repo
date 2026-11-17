# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 246047 ^ 455380
_lx1_1 = len("4986d4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-641178)
_lx3_3 = 111223 * 0
_lx4_4 = 488483 ^ 584626
_K = '6ee22c357babf3a96a763b8f7b6e33d9503385e7150087e0f3ebfaf2bae55296'
_M = '77FfpVynR8zL0y9Zzmg1mmHuEB5Voe/g9ETerFy55/fqswiiEqZSypCAcQKaPm+QNepBGQD1uuPxFtuqC+7l9+jiVPkUowKcx4Qj'
_D = '==wOuua5ZVDeC02AexgKrfJhxeMWeFfAIEgJYXfpjLz03AdIVkcioImrsPS3XAWEWsZhBALIzYxWpRSxbYWg26uo6YkXKqCCqFXvb2WF0ykIR5uKHcWYk6ugjM/IREALWF7cGxeHeexamSTLejvh9CNbmU/Cv8m+lv6twita/Ts210qF2Nvo0c9hcwN6idBXZZjUDGElWGYAdXNfO4IVE1CBM1KA75jUmdZCiT/qQVKn2y4HPIe+RMEAfZk2anDIRAIjcBhg4QkOCnhMJq/3c40hsdomb9/7gEfIGgPJ8/TtUUsUqWjLaHaZxdsfT19TGdJJgNly1EM8EWX+8x0VydotqFo7XlAMD9ElkJCJ3AfU+bCFs+yEeqJopXLi3lECCL+cXNJwwCXEjLZfy83OVj1ndXAoSQhq+z+4sQYFd4z7YdAGViHTBO2tBi2TEdktP60k68PcZfDmWpSMYQXsQthwonLRIcEWJjWtuYvbcJzmYgprfGG5nI0RybKWJmb5bH07y75o/FElGtsgSim0vFvNOyYDV5eeAaTYuHjMwxND+T0n3KYqGrQuwKKv8P6yKAc8EpUk2Bjse3zHH6/LpMGz9fylp0gpPWDb16Or4fR+1YpmqInZT08nvLY0xZehsgwX5BUP6StkDPJJpb3mTwuAP84eZpgjBWbbb64asVB9Gx5ObFI0yyy1qIu85mGxEzhpEZ2aQaquY2bl6zHj5835rwwVeEC6g3Tz5OaKibNSnCdnhJWyytChlKdvssZFCev5ySVm4TBnn/NY61xeQAlcXvVQgxfljWXWhPt6KzdugbT4RNdv9LRNtMiSDqGr2BlMv4w2Ia8k582zCpK9RW/Skvk+8dNP2Uvm48uWAcZ6e2g1WdqjNlTGSCSdzDfoqa48cGAGDhqyQQSdBROVaCSEUwK2eJDeZA/AR6JSuV5fPu90jeYPOqJxLWn++sDBw3bUhInMbtTb/nrluWirIymONqQpxW0v/dMU2Rb02GCe5ZuRiYaIMPgSkwKtKHaTdpdzmMQ1JURI2Q4hoizUfYzXArbqbZ/T3RSvkrfHxj39PfQBo+MZ+hihUsHrcG59B60kpmubBN8WCuzCeSps1/eiVrTNlnnm6D/EptEfuRl3ED+ujEOzi12XRyr1INj+iFO1YHfFIQ3w4Nu23sGOHgTamm8YJloQf7iP+KINhMNIWEmPRuMVfM++sobPXVgJTXcEDobAFr2XvNEz97rXokju4CZDf8mzN8ifNncrq/EX9GN1tc43dj47VKzkfNOS9KRvne9wUyA4S/tWJtesd22k+ZV4QaQ5b+2By3bkUhH8oJxmR60kNhgSkQ+xYN6HoZZBfGPYpzuzTQUzQmRWCiPwi58MAAiVlL6RBiesSm+wQZqHE58Ms5a/obd0iO3rYCw/sp9SpPCTNktU5VcOcxKDTRkzaHgnzrD5FzV7AGTpNNoc/u0CxwoFWb2dj6/19f3cVPQcM+Fiz/VpjJIxMKMX9Z4NkMzF0LmLf/hVDilXArkssPgvO83x65mvAvvXDicjUeLvn/tOf0TmN6WqF8epiRT97fhJjnHVKvtpBB236xBRqXADkra07ka9HVuvWiJwmd2fd/3sBC1TJkAE1S7uOysu4DdKzLrm3R9Se6WCjzqcBfhzvLwO+VKZjcVdhummcIE01e/e3WIA098ttPKWOaQi6GCYpmSWIOsIdloxuGnbyAgGgQ3Zvkj6ik9gqSI5mnyAcDUQ+rJT7qQvEkGNx6quEtcjNe+Lzj5pUoksojeBJ+Ui528wFv2PL51vnQoVw9uW3OA3EgMNn75z73gN068tcWDCGrK4TUmyUmMiYIwtLSrCw8xt4cdD'

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