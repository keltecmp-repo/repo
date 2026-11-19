# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 988908 ^ 490519
_lx1_1 = len("e2598b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-831602)
_lx3_3 = 562094 * 0
_lx4_4 = 701827 ^ 746398
_K = '9e4ea8a88bf6b4d28c04470b46dab8280974e388cf8ecd0dc626141e31a633f4'
_M = 'KissLp+qX4EfjRfyXqJyUQHyPJ0pzZVSRwx2eA5p/3Vsczsrk+sL2hWIH6da93dRA/lqyinLnlVHW3AoDW79Jz13aXqV7FveQ4sc'
_D = '==AQ6W/4ybamq+8nMmjvHzM5F9nepZYig2BsVC2RxCp1eYuaP6kZ7+Jktlc6FK31EPf8ZWgjJcKdrwtZL0oOTVe4lqq4609ozzqRX4g4+qZwOEJHxGe629fllBkqTggumd5jxYpnIri3rd66FJx79IJoOxOslVKBitL889Rvrv+EDFQBTxsMO46NIvT9XNaD+dY/lW3HCtS0KP2bgB7d1j3c3Zz87gN5PDctI3xVM8HmUkD6kEdrd8foX8WOL5o211iU0D4R5jpWkzb3R89tRTPs6YMArOcrs+BTErYymFlAn5BkSf/DMC0L2qWZFxI//w9JUKEg4wGl/S/8G9ZVmwH/3Enk3tHHK2A4Ju4h2J7eBcmbRqsv+S5/fO7rXEHth79ZMCnZ65vz/2mB7pGIwnczDi4sVODoYhlscpAPT87RVp1dRt9z7O8elvnG1rsru2kWLVTG9MVJty1rUtbH6y64+yhwN5BsZbz2OlNx2DHl4dqwc5CLjBPNbJZVBvgUb0PRhOli28zV6OMPVSRxGADQ3I3pYixqbu0/l8WHG4ACRysKf3jJE+MU8ZRg6sjXNoiJ4BldSIeK/yw5CQRnzT9+gJ9B3rbq1Bz7jXEaZA8v7lWJ7Z1+h/KTB3KTwslD+3K49whZzIFHhbpXUDd811LOBFAxtQNO6R4Oh9Dk/H/JE6o7hE9KKwtWSgnWQkmPvFqyslDiClfGQ0kAlrJyH2PTMz47+qGYX2ZQ2ykfBX0MrsqC9jF+zMgajio5RCTmjWv+JKK2EGUCXGkyxa69d1utZSqLJo1mVphQ7wFjyKzaxavKFQwyJ39Bsvtp4gxbByVV9RjaWNzvXZ631L0/hFTyfmwUnyPHiuMViik0LlJxsAwKd+ob/tx98IX4kaChHkFnnIYC8NBdObWbXc5JkSHYTWX1gzpVoBiciR9c2shLPa+08Ou/wc5+u330GOnZ3WuYUwwck6iUoZySAtUSBHtS97nX70amRwgW094QQvGU6X4PA7LWRdtFAl/3hut5EMhMyBQv0Z5mFieYRu4lDyqWALf8OoM4Ei9VxB93SrUJxI9YcSwU3SEfgcIBeUHuaTLO232NxBSbS310a8SYIK+KXY1B7CaMow1U2CS13fFdorrsWJ0a+NhBu0HxZUTCgJPVtjguJr5DXT/bkx/C/qs7kGe4QydtxsKCEvbvQmp0Z4avWpYE6DgzyZ0N3qjlVTPaPfemB704api9d5mC8pJVccCj5yLtIWDFdNRVtRRyxNLM/YD0nqPAbav6PpneIHvX2DfV6WgMkwj0EY2zT92c+4uhcIpDhwUlaLHsRZiBbkYNQBPQJHQL0jMMNvmbs3RlD139zBWa6AIAFQ4TwDntfH/eisVFnntGPSAYXOVAD6+GZmGmlaR6jeXZOrmNnn1HXGpJjvbmS3Jn7SZHcWuNrJiUTPG3ClIxlunz9ELmW+9wgn2cSbUdjwfFKpzwLn/pnR8WXEOJW0rJknxN24YScRsIfu/ZcHj3sqv0VHmXiko7eVjina52ubCGMA5iOCw7I2CMPGXqP3A5FTtSRADplJuWia+N4FUEzsqB1eLHOxtssMxehO/likQLElHC7LwE7JUSBUpSQA7AWu9Do/aq1A402/VUYP0G2iRByjTe2Ahs2CGpk0qkMR3jpxv0WjW2ZZPSb5ddLoqi73wFlk+S9lBjTWoBbDHcnHQWlYE3qBjful7p9cINKyfYgR02wXAgrMQCkgGbG/EHcLlaRuZreKJP+o/wY2oamyCc+2XqzhRH34yRZW52ntzGVw36mRR7AoY1PESKJ0DrGoHajnc4YW/vXAUkey4KwGZ63UOAMcj5Kz+F3XqBd981'

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