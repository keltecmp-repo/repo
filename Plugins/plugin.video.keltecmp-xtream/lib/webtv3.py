# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 890128 ^ 651289
_lx1_1 = len("354fda")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-677544)
_lx3_3 = 818147 * 0
_lx4_4 = 897063 ^ 962736
_K = '5250887ff1cbf204234d15e8d5f1a6566c0de999b8b0a11b313920e76b04c9c7'
_M = 'Td1Slv8j335cpk7AB/WiDaDNU+EonE05sFshksS33tdEghbbv2aOKVKmRcxT8a5d/5BXtyOdQT7kDiPFk7yK3ELXFNuwN98pX/YX'
_D = '=YxXJfmp7xeOo2udk7+ztrVEtZlF9k/8u6eRvSnT6hSxNEYeu7gyxrKiGgvS42mF33TVeiV9lqJdnqQVUfABzcBQSbkV0Iwn79O0UbqSt8ceLcKH7Adj9fKmMFSlp3VeGLL1coqdvjQaZ1PO5QLjXEKBs5kCx84yOxRpl2/6mlm9o8XDSGzIgOZ1j00I+lrulhuuvzXzQz+hAAe1K+Ul7DRMorYOxzOhkEXRyk4+idiuOGRMWIE9FQI6HI0b1Q2EW+v5Bi0XBCwWxfisgmj/+slFWB4Prn050Gggk8rMNkTXf8E+t7Ylp4tVaFN1bg0szIoP/dmf9tVTf+oTupuvobkP0HlNCvgBTrBXqz00Ie2wvrsIxT95b7Vy4uSvFSW/bnE8y6RP/tImBs6gbXurDKYchTlccyA0ecBkEy+J9o1eNEU4zxXk6KL+YRhoR47r/050wg34zLp2fZKquQL+xO+9wzpzRS3XGNygW27wokodeMdPKtuB8oXSskV2d4n4gizfyImVkuAO+pzJC1Qnb94Qx16LjMPEIyFjCwgY4gfWLL7vu2JJQT0dNs2WlOIP8wkJ7tjDun6vK590LaOSFO6l5e60O7DHow9le+02vO8WE7amf4U+rpBRYABtPN/nedLXY1gA3utzQDqZAtqdB96R0mLlm8Rn7cV8u+PPbXlljX8Zh6x6kgdIiS4WfrYlgFkMe85G3Gh4qG+zH8d+K6Pi2FuPA1/SfD4nNXAce1iYKAa7OuTouR9aubtQ7HtAAgAFXoW6ExYQ5vUK1oHOhOHcwFyIZCensTD4cuJXP5BqitZY8id/a+TCQpekWfDR5GeSha0I/cqyE5P+WUMQ7KbqPtsDSznIiTwTvjLG/zbEqbTJT9+tOb51i98igAQ5m9SNHiAL1r3mL8SCW63+PoqHd58l3EpPZlZ695aWkqIISiQR0uTvxLf1T2hFylDhdoN6Xe2KRC4KJUDJSHsMgWo/rJTXG7SWr4nUlPn5BdjrwDsXNDSum9UKUo/nKUNmIFep6YTJR5Fw67Xl3AypxXvtXBUgK91nW5QQpnivZml0A4pdRmpTn6VbO5dKvrhPc9npW/5+e+JdZ2uSxwfDCnUwqqQRvns5QLnsjh2FC2e7a02HzL+Oo12kAjAO8RzYRzoZF7BRta6yrLCJ3x/QB1QB+LWxHZvuP6sJadi1f/V+D9pAY5udprHSyN1zjhp/Ykx6HCO+6xJfxOcvLLGCN9+imk6IHNtSymGLYQtczROf5Ebyah157Km1xwEvT9e3JHisPBZqKv3s6YRksbnvt888EBqZN5cSZnfoH10vsxrZzfapfjg+G5EMJPpBFJYQgae3o20B+KJR0ZQSxCkBvwxinNFr4JpzjGVYMFJBu77J4sINURKD/RSy2nWR+1dn9jBifWTTkIN/KKCdwZDkrzDmupL5VBxiSD1904FkLI1BwYNUimcs3smCYwoYC1gopIHLDkDAI6CggbLq83R6+tkLkVHSzKl3q+6V3Jjpgg2u5nT2oNILsu9pYTMsPPnFLu6LsDzQw/BqJpinOoT5MS5dcndzzBVWMjzz0RW+adfqqRzgsh8i8sMhmpUqNPxspaHMfYY4WdkXNjn0mIpdNiTbwa2BHH189ih5VENUZ51YUUxy9GevENXX8Cp/a6foOnc2M0ZxVrlBM553ecugBZO0V0IsqjB2Za5CcbGnZYyFUaKGJ+EGFXQ5fgsXTij5XUhTT6rW8NPA1nF8EKT4cM6+LXvrJFNlP55TPbBBcOiu+JIQha5IvOELwg/SPBMwtC/CAjFyqh4yg8HmTW5GDS+GrjzlDZLd9Mj4amMQhT9W'

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