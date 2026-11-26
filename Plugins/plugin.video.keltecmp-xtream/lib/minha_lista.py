# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 662162 ^ 938333
_lx1_1 = len("4ae031")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-963012)
_lx3_3 = 142625 * 0
_lx4_4 = 476855 ^ 186409
_K = 'c14520ccf709fddafd81cef60d8863231ac262815ee6c8f602a7e76915f78454'
_M = 'i9lYfRmSgMG1ww=='
_D = '=MfXNxg20tWgRWivyJPzFNJrz4Ehvp4y4uh8Kui14ZlQfSK4o8bVqqF3gfeD1K7v94iQ3NLyZqgxSGr/n4oMoQn3lJsPeEPgCSzs+fS2b0+pwN//+xTgkK0dlj+c9GPr6XzStEcngJlErTVORbDXBHP+c+IGTwhSV28qafXmD1DBQX9Xf9PGy2kgaCRYHxgFydIuuLFKUGksvzoT7HdFBhqfmI75T4XR83GtOyCbTY7fW1bW6cTqeRgOvyEBGzjt2KMWvCyQovxKK1PmWRvqaxKlSWymuXm9p48784HBnYl97/oCdRVJivAUMSCIu1RW3txD5v7ioUG8feYahSDBsBOnKUJLwTcAtavFhz/5pKnZT+s+jI5Mq4nnW+ngnkC0ic0TBKYv4qK7W0lXjmYlhn8pfrjcPkmdVgCp2t4GJv0HEa4z8P8X5XotVdLv6SHoSqCeUZmLUNXC6zbHQ2ZKETTd9gmMz1yANDZMnjtpgX3h0jj6B1/FapDXcmSUUiqIABT9em1LzURDm3IMfQbLIxspCp3cuS9YwAwfhLHpkfYlJo3Rl1hZ/gwvY6MW7qbvfUTfXl/dJtYzkmt5YcD+qh+ESJRVrGOunXODS2r7Qa9psNZQK+uegZL1ABAdRzCTRjUeurqfxhsW1kU/YFBekUCYlinD8b76orgjdN+wAmM7hyP1eMbCD8HbT9YXzww1E6rP3nxhZCAy7Pf8H9M7Wgeg1+hMpt50sIF/J4nXwHmrwNGdJqV/4AGaGPVAg0ygyBSYJ7sv51+c7M9Y1PuvQUhAvkJ5OQZ/AaRnd1ZhV5qmrWUmiQx54M93pGBWREziDeNJowpGeF94jsAKR3Y1GmRkUGQhYMtPBxqrJb2YjRUVEQqnub+aDEND1zyPx90jSP2HDrgDk59We65yFDea/CH1Aip07bB1a+H+FEBBVLN0QAalUXN/fFoi6q9wgQscB1GWZKI1vxe7UrZUB9jBreLQrNnk3nc1VJRd7ToEaY+CIDKcAYHlMM+JqjssL2eKwVXUCYgw9tzKm1ON1dq2pomVTyzkVqXxqfy9y3//aCTfsxGuBqOoVtEaY0X6pBAvXIWyNIKFMwR6f4j2UdtLaVcWGyB7ehMnJwOiYZgx+IJS9X5rvKOe9IM3peJDa5x9LHvQRKmR5DvgKEAj4DCUZbAI/ebV0oP5fX7qooHLymVnNURLdfj58PKQhERp572ujIyyZ2uqIrxbjNybtnerz1AMSUd9h8zka91LxsQ5LW0cHTkbsY/NXuod+rFGsu+uaOTiHevn4WmDZjaAZT21v/hp+asTtdD2Wa5Zdc8dDrLnvHdVsYoxx5D+hxAEOWhm3+QooaheP6S1tD2kyzm1jqZT0/d3jqnYYcIB6/FfRoFWzzyAYHWHo0KS4slsv+kBqyxsxCYMnI8n1UyVQmlpBeJx/C2gj9udRHePy0annnudOxbY5UR8F1FTq5vd4bSCfmWY3gjgRK7SSIcb+xOcUtCJySD48ORlgWuH+Tkd3lt8gDIApzQMJamblmbBaAezJIp0Tm5H9VBvrI5mXRc9Ek3WcTWIrqKowe0aIxZ2VLPryB91+m3tKUhMT/0KvfscDAdpFM+9xrQNqR1Dh6MR1hX5S3x4FhQViZSjVypeooF7Rv1uKzZ7UrQMQyIfJMaJr9O3amOWgbWFRUUXMgEIxNmHtZlfxeJRiONPyAYPp1ra9RHVDJw4EtKvSMcjwrvRG/QVwa/3uHEQvexIFXEtOXNQ0yAdtty22kN43X9IURnNRFOPE1JKRdebw4s9iay6QgTl0UYmB/k8EWq9mzhTEiyBIB/W0Fy03sJarfPSPcj1VZ53'

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
