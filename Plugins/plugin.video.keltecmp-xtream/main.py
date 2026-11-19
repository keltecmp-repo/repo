# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 342167 ^ 973294
_lx1_1 = len("5f7ba8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-454481)
_lx3_3 = 433522 * 0
_lx4_4 = 445134 ^ 228344
_M = 'mXD7PDDZO/gxfpFRwrCzAv04MKDb1rq1eepOreXRj5ieY6hoacw6uD5yyArG6+NX+G0wqtaEub577hOssdHUk8xh/2JvnW7qOHjO'
_D = '==gLKieh+zqV7H+SvBseyHfMXobNcRSyCubTH366NXuc8pQHVb06/HK5dChwXiUSFLR8R3HY8AOn+ELq83QiOqVIYAgHWirh/vdOMpI+gvbGx8nrzAjNIdVdZ0bQzV5b0a0rxQBlsNCzc6T8MMjwKRXJn68jaRdvku3p4cBqkdP5OQ4wSXpbjRPDYP3BrwxkOxpmiwtk6g0fuNrJZh08ZJzYrtHkIMu+ZWadEAX+hGKBFecPilpI75Z8jqEviHT3FaBQhV85VYJA0QSmyGo2YxOdGGXzOjtTVTahJlZ0a8hj22MqPqkW6m2nrOI2M0Bd9qQ4AYFvZVhJaSPpSJq1FDL/BYGPTkruWrwxKjNdhydTkOmNuZQGbeMkRvTkdKv/xJTRw68NJRTLA36xU3fEEwxee5+MM0wi22iA69o+LpHtaMrO5K7Tt+ZzO4BEDs9mlhU8Nk8uSR6LOmZkGnAp9CRfUS0i47Eq5PJkQpS6ZSimSnBddKU4HMa2poRO38kYlJeH0Ws+OI2p9gJDO6nluKxChYoeOFTzmMGY1u8RMdLqAwSBlCVkLES5HSJXshJfQZIslBeSENJU/GiKcvSjkERyhGyTwise0Zca1plqeLgRO17zPXx4bu6nYgO37ZchNdYdFd/o0iDusA8ck0ez0F8Ipf32MtRuDApI3q+uTDjY7dZ+yvb7r3rWIrRwuvZtNHC2ZEhWXcCXvUBD/eJR4PJtNCUPc0Ukx9mvbvVDM4oksNi6BVE/Q4gcE2p3pr+wRqLuB88fEZ4Wturix6uOHSiqTPJ7Lfy9nGQckYVshuOFEzNHhME5J4oUrQqzEh64FHYADLogiWzzabt1In/YoBKcRuOkQIA/WtUNkZKQwwlDdo2PsJAdLQJvZjX6wbV1lk41TQaqmhduWT05sMOhqPAgHfeGUY/IFyFxahINRzBLGnm+1awRRGs/1Wh40BLF3IlL6T4IUX6pGUoniXQBJp9x2qrmOZb8m5EGpih8olSqFWMVBIK8ldj9u3tTJXBmSJJMy5a7sWyJFqfzH4krhm8KDXcoTuuXn9uRmM27JbGIxDTCC0pFOGS9r05ujPXURVBR49ys9KrgzydxIetUfdVR+wrukdTVWsJ2ggQLMdeGGCcKGQpKltnqJePVNNPeWVg9PwiQXrrijLjA7GNYp9yHiWYKi9pZJeJ938KSHFuO3ZqhaiOSmS+yzIZFTw3eCXSmIYyuCVxcZowUlSiwzSFi/QJMZ9im+KBRnT7zVpi+h36AZtg+ZqXOXJrjIPC3vfqDA9Vb6Q3DqOzesVgkBOadtjRsHLDgKpB6Mel4Qeoxb0Lx+t8gONao05GxAwg6zWvMrR0eoweCBXrPmMl1XqsDfogbjb7D5Q0ts4/FI3cDTer2byAygZ2XtrqN8L7U0BBYh5KnRmt248l3cPqMmfSE6gTiFmtWm3hlX8TgyBCsgPd3CY3JG8ZaC9qlCf+0eZM2/bWNbZng0unC747fLsDnHN6hYo9JnSpu/wZutOcoz7cVxPcBPFkKQRPDEv3TPh24mmzAWSfjg8Iezzi6ZnfvdQbs0Qe3K+QEzXu7bW7jfVXWQDh6eMurEpyKKeKXH3U7XS7kibL6V1+5oHvwUM3MM0uwAx2dWbXCLeSF1ThlJUByk4qn+MexojZN9uiLUf0U'

_38a5=[139,26,77,107,42,73,223,117]+[227,212,190,91,169,136,39,130]
_06c7=[169,177,47,104,246,192,78,177]+[252,251,124,122,187,239,245,154]
_1ea4=bytes([a^b for a,b in zip([249,127,62,4,95,59,188,16,144,251,218,58,221,233],_38a5*8)]).decode()
_860c=bytes([a^b for a,b in zip([218,212,91,28,159,174,41,194,210,153,21,20],_06c7*8)]).decode()
_c3e7=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_1ea4.split('/'),_860c)
with open(_c3e7,'r') as _f:_K=_f.read().strip()
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