# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 764462 ^ 929928
_lx1_1 = len("0e642a")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-408865)
_lx3_3 = 599236 * 0
_lx4_4 = 775710 ^ 854253
_K = 'eb60a09fa190e6aee38bafb754f8b902da29a2a50ca979af85ad118f231aadf2'
_M = '3r107ftZ62RyDjq7NBKXAejTEKvnoq5W2IKMJmljauiTsHa8qAC9Nn4LOexoEpIGvYJA++ryr1PYgItyM2I27Znmcrn8UbpoK1g2'
_D = 'z+AsjQywIvbdCrRIFcYKa+t4QoO/AEZtZpdZdSYOMFsi1VraDgaL10vJWGM4gKUPTPsefGNcqSdfUBdYh9pwc3/P3A0dAepmR6NgZ22v/g5x9kzV2g5ib21oiNpDXJWBVls8fWkknHzDBnJ35vDiFfaFOmNqL9+SeTosAkNIDv8AnQHMBqkN2hCLnky4zmH0m0xSfZqi2W28ie+jnTPkOf2LtcVr2cHs58qGGcuMPdfFFUTn55O2snnCFGkb2LnGnLVCcOgw5yzPRw2RVd0pjIbYi5Bl1v14hD3ZrTtHhgoTKMc+sNIFNJ5/uoPYdv8xjn8D09+f8rTiUHBeBf9ZNb+qme/aFax9aH8uTbphaXenj76asfx1IE6qr3BIhyo3GB/l+bgRPCN6TXqKS//MpYKu4Op4S2UoG8ZzrFFweOtX0t8ON9gRPRpDKiccmTHYo23Ha3cv528RzuNjJUz78QS0gXT51QNoY9DOzGoeLXkaGJqOjzRNhsyhHIQkNkCs0AWLRkPRz4BlhTOd0kC6orpVKpmlkah3IUOdBPTTmSKfL6UCud67qjsl2le7h/IXr+j9Os2SzlpmZZxrAgfosvxAY2eTcN3Wv0FA4Yk9L0PAsLDiA/wunv8zC37K9bu6ux+SPR7WIMOZ5NUEzsJMUAUBV+Ndk6C8wKzuXniQrO/DtdYv/89B79NsWCiibXd9Qld7tKB79K5aOqHU1ZIf96HnT948nQawl2szMrN6PzO6xfINcVGb7/myWEZzbPgNkd3d3rY4G2GXMZrtl6kQPF1UtnHA32LeCZvxV7HvPiudCJvnH4KIGtPdFC2dzDmZmlI5nNycZkDJmIiV6I7dvVvE20fzylurBtqTAqDVZAboLUiVJvkmAqlt0ElcXvcyhYSggiAMgk/6KGpZ1giSUk9GbnmSfCxFqVegkoUgFED9ZYLVBw/kcwWMCQp3n8M6VZEDpWWWe28/VnL8b+Rw3J6U95chPCv+5mb7Hoie0aVvvi2YjPHPBQYLSeYQd0/GAr/y4DfhdLWNMg9O+e2eNfUBhsIEL3QhNRG+ieU4WxVO0epTzC5dg5eL0RxD23PDPdbshfFhytOkLYe/HxZS5TiPIkH4fVA8GfUM/h0YPx4z/oVhXc+32J1obA5t3MoTOE4t5X5TmMOQDrWmku/9GTGkbvMhhQoC5KMWsn87Q+Sgmfqk9s7JqXR3OA2bei3xviSiWHLeKnFcWM3FiFLHkJYT8VYJ7fFsYP3VXh0zwkWBqlxHH0dGL4dH3JhRQqtx9G9FoSy8dRoqk7EJIBTqX85jl2m4InfOnBmnYcjQqcO3SOzljwJZLUEgyx/UYiQz62AsAg0o5yv8tHbY3ziGHOmUqpKIEeve/jDIlA1BEgSEISH9M12kEhhr9rKSwP8ZxwVXiZqtX0zjeV0twQIHRira3yPz4IKU29hPJc5xl4cKAYGSqhX3EUDF4O8nTsW+cDb4ct/QrxpJVLwAPTpg3HAWwGLdJVdhPee/ZjTkSX5H0sZFuhVX1rFVWqaxeCgLEKvlJZ+E4BxBKv4MUdNh4D2AT3QPR+PJwSa3vbJeW/saRGV5arhb5xq8277nvWbNSotwFGlI0tbOvZZXnmAfldldU9IB9c3uz3ZCe4R6m5IbITQvgHI6'

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