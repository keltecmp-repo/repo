# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 256867 ^ 617341
_lx1_1 = len("601df5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-866588)
_lx3_3 = 650936 * 0
_lx4_4 = 642020 ^ 203245
_K = '576f3662ae69d7f0b0bc9b33efe6c432c8fb2cd94693f19eb4f19f9eb34fb215'
_M = 'hfkdOYU7QlKeQGTY9RrFlT4ipcDcW02pkCSdBq7GpruFu0s+1SBbR8FBOIWmGZCZYn7wzdkLT6+Scc5RqJz7vYW3HG/QcA0Rwk1m'
_D = '==w+toefZYJKuTchgT6yzKnGUpPwqeH4zyGtW0bsERaQTfFHk9AedOHJp5fNFT9S7CV8LSvi8BLc4m30Qx1+R14y+LPcvPHT2HRUsHib8gzs/WzRzswr6X5ERiTnu8vkibmEnwce6wM1qaQHKmkM0syvUGH7B/6ydA60EleDbpNX0q6YwuLpEaavgPZQtItwAewHMGFK7begXdUWT5ss2zauXNa173dQBwDq+KdRkTRRgt0cziTZO+ikoxD0/q68x+lQqxB4jNCUpM7mFyyIg5/7Ylpcv0rjp9bsUw0dW31EkF/Z8l+7o+bhS084y3dT/yA70T/XJCvFehPq51m6u4pp4NMYNZhjilt7QGo4gap7L7dbQ8x9t6PVBSLFSJGf2244yUbMdJaAenR/C53z4z7v8R01EbeC8jN5B3ITY0TqgnUtEFOFDHn8nf3nEAJSfuLHQMOeaMMiMciklZBeP+32+maP8/kdDsWuFnMHgSvhi89A0mX0dP5vDjdISwDXHdhT4GbAYcxCHIfJTgGM68J55ezwBbob+CvISC5ONIMnveUIJJahtNBNQkbJGcgGT60bv2fKwsUqUzrOJ4Kqz7lMh+SUKppCKco5ACkJPWVA8jzAbBKX924lzCKRMyTznaF+uVg5sijdEdFpiUPmZzuier30e9MAAulMH+j1NXyopdjWEXqtA7HplGL8Fp0xbYDLUozanL4Uk7IKt7Narq2SXP9fXEUkcV5lf5xwtktgxT3+mGpds01eViWcLa4LwHG9RT6OZG2MndFgnX41T0WCkyOaWbFHg6X8yhpSBybaEkxovbsw8P6WUET3a43qZcwwkLS+tpMg9IMQN3uQMrkClZniR276lbS7QybneHk03NAVHifZKfvsV4cQXxZym0rd57umgG7QANkswj+1S7iTNxgq4oGFHU2cyC0Uy22x8RyHmGen6JZRwhsooBAAuVcdNV+hT+e+tXGJfLNyMo+WJsczF49dr2ml5kanJCvEApWjbGCeft12Vggng1SC0zHwCPT6GXtHC0+ame1q0nIoJ3T2ZkwD7tOWRuOZ7nwHRI0NU+b3r0VTblZ3PWq8BZbOpXE+F2KoSgSd5SGgezNCoj5XFbki5zjKVFRTTCrnPIh7Ukldsz953Yk8Dmc+vkUauLh6GQTCOQNHQ9acQYazOMr1NLx1bDdJ4zrurNcW51L9OSka+48JVrZxVzRc7+OTM9BClhmECn0E2msStJ6c4w1bphev10/sl/uXpI8/oACc/Zx7/WLqI3h9Iki66e+hbMvI4zWXZl+5wclAkDjPMs3unll8FdKBkHyxn1e5BPRynvsKf0Nf2iJblSAqZIaPgoQVWjZ66ilI3S5YnzL9XaI9DfP8xN+E8DLHmGymoxm3MeerUL/Le/QpNNfKaJeLKhBV8M2FIQxKHGVHlnL1dOpcJWUdQiU8FxhRg7nPbo0GCAGGqH5HI35byzvyfcdxo5ZktST5CCSPjKudQg2kP4KqfdY+f+iNP9a7xPN9GC3ppdQsJmxzcVhqJrRUpIGTvvnrR20NiNpeH72Fche+q7uA9e0gpFx01fEnc2Vetfe1gWdhx3DxcNoEkVgd/o9AEq11LK4f8xtnaO/eKMH60odET4fUg2F7O6RUvWFCU3fCBXqqdOquyrdI5hz5QZWO+pnm6UisZUHCWgvJSHjbf9TmYxrCxe6p/lF+8mrx5sM4ggv5x0M4vKR9lLqTbdlg6fBC8BKymTL/jkvbR/TkwnfLdctKCupCFl7Oc7+Bpc3S4uqpcp5WS8WpPfVWHGT1Hw6/9m9GaCLuE/7XK2NS6kAg2t2LCBcNswFY7zczuriSn9lAb7KE9YtBoXJvbD6D'

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