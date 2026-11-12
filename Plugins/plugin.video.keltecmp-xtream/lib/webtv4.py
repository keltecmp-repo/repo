# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 435486 ^ 841452
_lx1_1 = len("68ad0d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-935443)
_lx3_3 = 580907 * 0
_lx4_4 = 168676 ^ 974649
_K = 'b2f6fc6f295b1057c78fbb2c187733433a69b293b9b4906910c8a47a647f1c2a'
_M = 'Jc5bRzggoaWiu1ROVK01NSNMuBLc5g4zTh6iZBj7WXZ+nllCN2G1q/7oWk9U/jw2KBjsQtO2D2cZEvs+TfdcdiqSCBY1Y+Kg/e8N'
_D = '=4KSaFeLZsPtKBJUYYOtt1vLHrQQ3p0dFlJ6FUKrNuruuWbbWN4OQKAYivhOKz9Ll0vrSvtVcccGwsA+PxMfs7wLAbw75OfW9ZR/CKmrp0yalHexlF8xFtm934b//O5ysi9KsSlGksdbr2soyrSyHSVrP0jXxA55zsg9VBcmw31OQwqv6XfCKCK5jyos7fpzgxOSMrx+A7feMSgeqth6wE3r5sfoyfi9ZCMQIfykeehc7dHW8jDSQ/RgF3v/IQTC64ST6WauxVMFx3VE/NcOWOw7tvlzdB7z3/6gOK9HySwO5MOmwihqawSHzdbpFEsc/1E20rwbMGJ1FHkpmc0ZnYQyZr34LmpNcQzkSy6pEKpYsMRXYrMkI+JX0HQIw3ZZJ4pItUxyfTfQQqcP08V/hqAca6b6yQDp79LbrXf6SsOd4HJMm89HaETik8nsxUShqQvzwh8+66/yiD6SJv3swt9sfv68cAz7Cb7cfdFJWBh61tPWkSIC9CrzKrHYs1CP0QRYHU94jH0Ie6ox/dqanS4J8NhoERM3qjnqSkU8blE3elbb05sWcaj7k2GEz6X+otDZW/9BV8vNRo3yDsliiTKEu8uiZDZabUNXTTlRYPR5hS9HLP4+Qf3WLOvFUw1OF8EPGwV9iT8ALDiiV8jzix9mDmQA2gjivjr7qfj5bR1dsjcXmCr0k8ZeRbyYIGLAM62QMD7xtwQO6KsTVvlWwiyeJqyUbkniwzHVSnnorZLgKB+oaHShUN+VONVkQHoHN8l7s+j0KU5iB3OoyAF9smTBSc/sAra4VOLeNSJlz1cjcAIMWXSv1jPZzwnumJufAo9Ayjb3BBScyL9OMFpjusjCdMHCUHHq2RI7EJG8+mSoG6xqzQFBd47RfLQZtoFXKKFB0RQq3IFu7S8C8d8wd/43kSG2amaq2aIQGxhhVj7n6ERggqi/4SsVIcAOKWzKZ8hvryHT/yUeyIAVIYdhVhp/KWL40omFBwyjoabFlJJkBFzXr9M3BEAc7oqEEH8k/bK9qLkuCy0IVjWlXhuUnKRFUcA3tDYVKroSK11xzTTDaYW0y/AagheZhYJA/onVo/xCoNvm4qbj4FZCG9rz64OcadSNkuCZoxSLNk9MZsYkBoJTycAN49yeLdb1R3YumpPW5q073OXhmOCZdiea735MQ6Z6he7sicRiPPeMCH7ZUzISu7MdyktvvynnJRUJ+LEMmS3jDwfWMsqovxeCUGQte4bp303xKKQ95mUYxfTIvVcefaoBzv2p4dyMD9iGOfKznnkQMOZJOV2Ho8sXlK2SmAUfLObicJHfWpIHlmEAATt0Zw2HsruIrOCv1J5vEDxCH6i8OMYpn0I8cPhxy4bFgDpbw13AWbuozN7simS8zA7NXlnLHCYxx+crCXhemwSb1dwrn6Gc7tCXlCSrvF3cPXv0Q43p21+J/zYFzuBtmN066XFFOgAbGYpXsxtWhPSWIZ8LddNab9NFQoQTs76Nqjmi36HR6c1YQiQaDAVHTtQGgMfYyg8UZ/Bft08gsCTra1Au4wQg3s7fZPgVzUaMyFhK0BFUF2KcLjGlVGKscAn8y3LYNN1ZAjWfxm2Db4Wm/TYdtG/tQg7wsp38J67HPQ1asSRIsin9JTikQ61PRTNVtVYW4yYEqOxwWwlfuq6hIfD7abOuVHaBxT71dDR9e7QpExtuA3a2VKPHa8kYOjOiO8FRwee9MJocjHaCB1X0o7quhheUvRqcuXn7ls7TuobfNfz0Wjy0npWQ3b5NU+Fj4JDTKSZqyMsj6o7F60RQON2xuM82UBzxmrhHdQuo2CAryHadU6bBAVK2fR27hodrCALn'

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