# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 210592 ^ 499256
_lx1_1 = len("c69229")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-252957)
_lx3_3 = 771771 * 0
_lx4_4 = 693695 ^ 312631
_M = 'OY6ilktJOO4ockfwwYaAmBtCIrT14xDfYIxjWuQ0uH9miqnAEQwyrHd2TaObhYeVEx1z4PXvFYRh0T0Ot2XpeW3VqcAdXTeoIiQc'
_D = 'PBULMGrY8+MNGr1Gsxgjoz8B+MWnu7d1ZIbCtTRBfHfX3Zm9qP1pPhphV7CiCmU5e3w4Sask+UvKuGWn5mB3/6bolh3Zq0hdcTxqfmpVyTIkTndoIP+1gEAnJY/Ug48LXnrys2b2JkGRD5QEkImhIuTsTnEgjL0ZF10f8SJ58NojO2OetMM4UqnLI7nR4pyr2WA/A11T2x0/WxXzom8sgNnBVZInTJ6vt6kxKuRBFc7wSmcuW99sKOxjJLk4qyUp8yNkieMJfTYcRkXwMApfmyTff1ET0FhrGpFkigQCT06YQZbIBk9YF89r8EeZxHe+NmYOBtnWX3eBRYOL3Q/EjFbdqe92/+VbeoKf7DXie4ATwgWXTuVSzT9XwUb8naQU6nKaXtqRe9Xdeq7nIV4LKK3zfz5txMX4sp6gKrgVIc2ne1yFDouKRD4uSlAG/btbmufZyeBSdTGk3qLJzHBAlr6CJY8Wwrnf2/7eFNs23CAwk3ed7tnDFqrw95eCIYj8nfoOE/wwVmUZi1r95IjXdBsC8e5tvaZoyjTh+h2RRgDw4x2+BC5BLUKfKy/nukA7PrMc+L0DY0fxGQAuTQ34i5430Hdx4RdzDpzP5jVmoztqaaKPUU5Pnh/zkD8INQMatv6jhawztZXoj13Mgb/mKVsPZzx96SQQvu+J/Epo3T0qh4RqhGWqAf4Jiy5R89UzXUrNZyWPvTvwgEocBgVNo5vd0sLm9kbaFkaRtEFYL5hDSK0sNnnkcEI12m/iywZnceAG4SzW8pPYtQci4lbrZfa/xMROzHVJExOce0hyFysGuo4+DQcHwPavzVABTvinUe2e0XfnprgcwiLrOQV+yVnWg6NTPyw0++YyUzlilRa0jnaWu3iG470DFnVMPyykqDAxPuYFJdAoXhQIXhmUixL8PmuPZisw7+DcP5napou2fJ7vnGPC6RvvI4S+JGV9/3afM26AatzmDV4SjqnTFIVHUQ9GShGDBkpdlL02g8oeXZlijdeeCbCN9aUaXD5wLD8+57A9ym+2uoQtnbNbr8UUx76KKDSgP8OdVlMF5Cw9VA9UDc+S0g8a78vosU8okfvgM7SjUIMFx4+vludfCikgy7E6DxqPlhBqRYyxiXoSoMHhUDZA1yRcXyEKUHMwQWoZvuiJflBJGCCEo9aqBdLbbry19i4ZNwJH0kxq8daWwvrv5irnjrOWe0DRgTs2Gk8yzclMZcQeM9KHv53nn8dpntD98rRcLe/pJr7xkUVG7Vbq52iyprJ5eCBsC3Q9EMCG7kka+xu2CFVP2vgruB/GTm0aUSt6pEYCv6a5ZTAnUE+QygtjnmwIMtwrbPabfTdmgCdaVXeLDhwXjZ7mXgji4NG7L/oi3IjC9uDBHcUvQBnoAi4dmyKI+05I3j9pfKHv+aiXR4o4KccfsSXj3632rEBkwmS8DQTUHR9mDtmqZj0VOZNQ3bFCbM0ID2f7sBwiHPeGhhncYndc0fHyesQsFXptwUOeaaWcvAzrW7wRDZQyYt+mX8/Cvf1igDt5EIPODke3wonm+Olxh8bReSyJvfb//h1uQQayybAO8XolH3vDep81fXWZ+bbnJAJONClOJlWIZpAVExiU06faz3dAQoSt+wmnbvLBU/sZ27wgfmAE6xFR6xQzuOjg'

_42ea=[125,181,51,7,192,250,191,32]+[18,14,62,83,184,163,104,69]
_b2ad=[69,150,1,15,148,183,10,66]+[114,36,230,191,183,196,47,106]
_b9b3=bytes([a^b for a,b in zip([15,208,64,104,181,136,220,69,97,33,90,50,204,194],_42ea*8)]).decode()
_86bd=bytes([a^b for a,b in zip([54,243,117,123,253,217,109,49,92,70,143,209],_b2ad*8)]).decode()
_fb12=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_b9b3.split('/'),_86bd)
with open(_fb12,'r') as _f:_K=_f.read().strip()
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