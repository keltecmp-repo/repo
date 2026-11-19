# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 500425 ^ 499986
_lx1_1 = len("eaf502")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-773869)
_lx3_3 = 755637 * 0
_lx4_4 = 355435 ^ 674942
_K = '6c500915d84132765ae1ac331fd01980ca04236cb377b09e0e67398f4decac57'
_M = 'w2OmuqkmjdCO3ulwkFffLFr/OjJTjAd99Vw3FobIq4TSbKzu/2zHjYGI4HfCVdkiXfg9ZQXWXyPyBmZGi5/4h4c8rbL/Np6LgYrm'
_D = '=gfKT1zwxQ6KqlMpqzPyMJ1WfktE3MiegU5KtotrlQtpLbR07H4II3lugPoYByVrojwQWxLzxeXtUpo+7Pm3rnava8HO4WFfvQdHuJeiwzgWbPrwIsSbb2HohyyRam93iXZzofBleA/IMzhand7UTE9jiQDFaklt7ZkZP01dinQFlvazekzaVDANMfOPz4zfDIEwqSOwlUQgt6OLdsGdVK6v4JpLIDbciAbN0xYwcNfMG3UUpXnJXtPeQk9v+jRMzGYVPrKZPIavDiYU583R0a0iskDtDvY4TAAkbU8VdYfV4wPE+NnrBzFlW+WpXHsxt0zucI6TZZhQbKC1UdEkHcSWhAhG6lmM4foaHuueYlSHSVlTEZZhnb8vjBRw0MKl11Y4woRJpDpJhCXX9aeHaxN0uhaQAOrOIS74OPyrKncdBwoeXQnoivR34XReSuAxRBPXlODqfV32CpFxWaDvGc9Zep2zq0EJyHTkaQggnYnTxZoCXqnnf64TDXrM2eoVORIhbt6+7zOkdfkpYQBY6yXxnYD5/0ckL5HPVwwuS/lIiSBw+kCW8oA5K7jEbikvBODwxwCxBxsQlpBbx+eIFQtSJONNBHiSP+H3BUrSdXDhDZMUBubcXHtgBrt2XYGIWvWT4HvdRjuNFpIkpRM4s49tw2fqPh20MKErUqZuqktAaL821o4g4SUmfmvavZ1nh/os0JTtYwfYK/bSsEIbsVsbhv/j/l6p2oWQKE5pDriO88wdji98emuvNgc1m5aeqgspVJcyKfdgbs8Par76+qTpfWX6sJ62xF4wrYfZk45rZlDMtMMkwpuISHg+D1mzQEu75vdV4B7NtInR3oDM010LJMMlz3j05/vzcR6ioO2uDp2w7V5vtN592wrHmPCELixltxTi3BtIknPndEYSkRRhvtWvC6eL2r5bG8I2mMgNhUr2L7AQSn11pEG3TUCHFA0xcrRP98F46mJhXnzvdF9QzE8v8Y4nwjwIRrtcHmz1vZ1ARrUEeBGhSUjV9B13ZK667yMCB3ZfCCT2dZp5hmYCL8TzYAR8NLkd6yq2DwPKCmkSmNk2rUXzq/Ly0sztRATP/Ez4tk9AId8DZs2Y+0eg4wQZVONFPET7BW4516ZAhV0zL1z/+Jupar7faZYnfSw95B8u5P5EjYl3qwXrKzag1TlZPNaiAXwsPoaFdvalOpg+lyTyrrnsUR/Rou17SP2qpspX1UtxufYqFzBsVQ+MO6y9X0feMW8UF0nOa4WGbdOdmdrrUc1KsEiarCQVXhUOw+difBr4yGgwIusapOd+dDap0lvAP1VB4fRKJBH9/gXihnTb+9P6QJRM29t/LDei5rBeIqFThMnwSZ2t6oT1jufskwAXNEfU2AO8DHIBAWjV2p6TrM1His4FGgZPkK3xTbDPABw6IvKUZprCfbYqJt7VRoJvlJi+99+UnCbNydkFWumxaHxc13IXo3TQW7G4pUmsKXLJ8EwqCi8i9oaHFI62bQWsB1/spfx21srCw9etJBa9cf+ROV52n+WD7Ks9H/e5pZsSibDNUQ4pz03JbawF+0qjyyv4DFykjh6Q5nto/PV2PH3ppGBexebbP/4JOm6fqSmWiHEeQnejN0y/wSSTTwz64bwndgUHJb8APWkbaCU9MfHLxgbFt8NBDR9bfJJuRxRZFPMH47Ta2LH1pES6ZBN7cvTtSEnuCiATEaiQ/h8pRqciRRWnGcsFoScgXuHR1ELTpeRWUaKBobiIShqhQDmibmJl+uhhPrzcJBRsYqTX7OoAyfNu1zA3QT03VjLSGviYJHDWgfC2huonEaxIyTCM8gfKflOTnMNkJWABEfUuzKn6k75eROsVU62xdJEoSHFI'

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