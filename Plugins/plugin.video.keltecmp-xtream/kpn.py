# -*- coding: utf-8 -*-
# KelTec MediaPlay — Fenix Format
# Gerado em: 2026-11-11
# Camadas: 5

_lx0_0 = 945827 ^ 667079
_lx1_1 = len("4d6573")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-925524)
_lx3_3 = 347737 * 0
_lx4_4 = 979436 ^ 694131
# _K: carregamento protegido
_M = 'OlzML6vbB7/sFSWbr1WjvGfYgOMu4gFZMxjE4DMnazNuV8V5/IcGv+EWJpyqV6LvZojWtSzhVFs2SJPjYC5tMm8CkX/zhQG94xkt'
_D = 'FRQcEOBJY/jxqS6e6cP5kWdfvyugdVTuS639KGuG8UHIVXmAjikO6NiFl0Q+ivDpez9TZx0MzACl17+7rc+uHgp1TITrpBW5s5FAVDMc8H9Y4oQV3g4ixpxqEu3qW39UY3gL5J1bydpB3NLPlHdbzl/f3XzzK8banef8BjqTdr3mOTRUO87Z4OBpp5DKXEJkgToW4RR7ovPufe6RK83R2LA62Vd6Lj4KA+q3eGm5f+KHmevqFa+HwQFNgq/dOAq4+Y7rjRrDQd7W0SkXEu7a9gJiu6eGN5+IQqxOt3Zt5p1Z/9cCQziGomPxZy/+7Gea4pTY/PoLYw6UgeVzp2H9aVf/tmhiiR0v4kOxUmu1ud/Ngirmf6ClHIP6zU7/urNKI8CFbFj9j51wfylG+7JCUgT3+0eY+vNpJSC67+QUFrMTAgSdC0tiegMi0ci2kiST1w9J+zd5fEhKhOKrR9Ad/92OSjThrT3XHtgsHwM/nNOfSCdBeQToCaaJA5WCSthSOYKq7LzfoxRCENmlT3+cOMi0m9ENySGMSGro1Y4ceEFRy0iTIGyK4Trkjp8v6q8NvablibBfTCjdRM5Ty6hcK/8+vWzlrpF8p9UEgMoZ5+TkzT0yvj4vy3o+JLqMFlf1mw8JRaZf8tzIwMEwJM2pJIhzvfs68HeyQhvxwMZYvjiD3NDRY7Xy2WyriO0fyRxrA1poGxf7Esbw8rgvpK7/C7BSHx4N7L/EiNVvzdsd1EbQZ1xnLSVS4tVuWxknu5A4RsV3emrTB2qZ/JmftFWHpclsJq53FdzfHlQKd3wPNSbqPbjicbsTcmuLhGXaPX/zk4Tj/7aY17P22jJF+t59q63NS0RkKOSzmT63M4QdWpn040dDxlKjc3f0bE7rghuGxwJiyU6acixP/8mjgnQ+zfC1eXnpmcRb8LsBqmUL+m/Ruwj1cTPW22MncV5rflxKXTbojL02vDtvJPq1LawYi/pp25nn3QaPj68OMo2DFNfQVeQKoUAxs7xVSREsByN29TGsmKYHeugG443g7vVR7R1rA0/1krw1QjGWEPmQ5dl47xrw/LBuuaLiGinPezKF7X/vnMIvgRfAMvboI3BtXx3zK6rsXx61smOkhwh0Gj19c6kIeS7D5fFZ0LRr5+ZyMzuI8bGUrIQVUf1aaMaynB457df/jDJYN/4yDY945+WwN8oYeF0dqsiEh+C7V/d9QBLRaIrx7YWq9iTTcom/qP/Tk3CE34MgSkSmWWMNejTQ8qFvZ7j1uUCjv2Bbm31A/AP2p6TtbeMPIEmlatxMiMMwNUtLRtD0vDckAvJHLYxWJ0Ywf5v+MRCyhECn2oGuY+pD/dTcY69yidPAib3YLg+FMKzgD6iojg5KmR44nBqx+ncTmWbqGE5O0yGCMxjs+5WyAgIFDACLqYksd/E9O29wRYoHTtNjjvcaRdgK/bTy8lGwX+iNw/A4BRmrzdiBuAvWBTbbEdBdnRaXzWK1t971vBXaIE6q75tMIoMj1YKbf/4+CV68ob7EE/7fTc0+KxUOZHUGFjU6Up08weiMbBMaA5TxdwitK/lzVMp5CQVw/6eSf49onntIJgqkNaQMgR/3s9FaJmGPxpuNzuuf4sDG/QO7SpZ0QIvNMlU+9JHO'

_41f2=[96,128,236,209,142,242,68,179]+[180,53,176,234,150,222,22,66]
_d54c=[104,66,145,198,231,150,118,164]+[43,241,127,57,50,56,233,211]
_9064=bytes([a^b for a,b in zip([18,229,159,190,251,128,39,214,199,26,212,139,226,191],_41f2*8)]).decode()
_a011=bytes([a^b for a,b in zip([11,35,242,174,130,184,18,197,95],_d54c*8)]).decode()
_67ca=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_9064.split('/'),_a011)
with open(_67ca,'r') as _f:_K=_f.read().strip()
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