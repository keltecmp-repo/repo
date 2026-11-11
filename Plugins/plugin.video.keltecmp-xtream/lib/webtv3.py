# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 226723 ^ 286083
_lx1_1 = len("9eb1e1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-596024)
_lx3_3 = 702415 * 0
_lx4_4 = 953723 ^ 499297
_K = '7fb4ccdeeaa7d4f2f095c090eac946fb31bd55e4225423347f7e33aebd25b5e1'
_M = 'JU8FiSwHUrf6iM/nXH9T/nDWHyzm1XNt52zgc8XIJBxkTQjZIgxUvvnZxbpTew74cd1IK7CIJznjPrBzn8YuQW9MC94hDwLjpN/D'
_D = '=slRDGZfc6r4Xc66CZVhK//Da6k4A7FfQqCiirkgYXSGB/cy+TROUqiRx2qBD5jRgNI4jxa8atCYgjzXjoH0MWfi1lw2WKzdXD5TKn8aEoNhJ2fED210MkBVrkFdMkSU1Y7uUFg17sfIq5FH/z/9Pwm1pzsVsQ3Rc0rFViHBYGvIBwS7+S2a2EZzLDOzzZPe37SZ6OR7VFPg4kBFdO3hhxJjMA3v3oSimNxP087IEzpr7C9pqtHCKZqY7Fm1R/Sads5ZW306bqtZnSFN5vvDaYdvW7PJ/MaeEpss7E8iF90w6fZAO6kFIEwVbueGV4qgpFOph3mvUF9t1E6eWk95eNj/sO+P9mpUe9EqaBavc69CATukkGyNBEiWeZNHktsD0mpNkuxTcmI/gQt+xo7/D0uvOaGUTFn+kTZvqYiy6ETWS3mZkS8cdDa3z+zu4q4Zkjht7cJSHx/VPV79G5juWEU2w+zGib9LgbbFh5EwsiJSNHYYP0l3AM0iiqaFvqNUIWOj84/yvu6Rb9oElokMyvhJW4+4e8G4dup4sztjoZKqBwJab2C4X9yi9EZPH9NZkitwoanUVfakpOyp1U8uibwCzaWjgOcNOJj3XOhL+P2lVhIl4jOLwY32fEluSyM9rjqnWa9pI/ysMZAnqGPzFp/itUXhT8WSPb2Vc5414+2IUA8W7dM02+4sAclzfogwdmhDS6K9VgHRfzAhhe1tJwYmPqnaCQVTEF9QQQg0oi9Fe+6OR89ceLZgmMG/ewpsP2JiaKRF48WohUzOyF7eewRwIaQ8/VTR2iXUMclMXL1LoJkYuS7KTeEgbCS/tXGOVVCYkUK1zvXnlsG8KK1NYu0as6qFFuRx5SAatrz2dv3QptmjjVZajJ+kOTuYGTX+GpoOspzFtdWA0MfWuCJdoGJfj4JPcKGVEb2FrisyGBxbLYfwQtfP+dGMI6Gjz7UeUBKAQs+2TA9d2dMocFgAJe5xkHu+UuV5s7GAYtd9536efCktxzYlSHwNSGHkQPLK3ijVjDWmgT4wrZXme5yl3/goSpLMQo8BB/Isz80FEyEyH6SRrtUf1awIQzI7q+MG5f414rwXacFG3U/CYbdQ57DeUWqGjDRHJANZm7kta/5HnccKzsbPVCXKFlZzC/Ov3bYNQvoWJy2vMRv9iaErVMCcbeC5p9V4RZsPGF6OE4fp3YZusSUyU51RmfRLsqJQKIdp6h9YAL04WeGTpId1qeX+BtZ0O0izcRV7KkSfbKm/krDl0Fj+M+91DGCm92tjzNr1eTwS1OHnKtPfpo2bOV4L/cIeJ4rAZ9/5Bk8VPV+inaN774dig2Iy861Ddfka/39hhFnoURKFyKVZvEr7TLFqDO9wJdYwWrD5xKCVsmQYXVvOyrloQ+ZH2TeJnSKPteuotq5zqav06lbrWUt9ef2auS5dugSo4KyX+XoE4omnRCi7kyEFSbq6cRy2YjbP6q2bdnTTkQrmutnWOOYJ+7hCRq/frE5cYsffJMPoo0X803frJuixTGe1+PC9DBAAHb/d3Nf5Mc2ikQCsvzdKCOf8eHSwxKnRhQTMF/jkij3lgh5ukR4W7WeywRwdxNKOeVVqH37kFYFkgNgQHwWeGyrW27umtaImudR2KqhmMjUJkBjOhYvgsu0B37Ahe8RWi3ItNeXtBaQBhDHf7Ejy6vr+/96vw8E1YbyKX+r9vpK7nNY3KPep9FE7Xd6nzmacpt6jowQohgpwJjIJ4wvvlpBE5mJ4iV63XVAYs3DDm5K4jdqhQyJ83RqE0E0Qztqm+oLw1r5j+qc0b4k7caIdWtFfPMveJkoQhGYsGNG1FhMKN3EUS9k9sUDK'

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