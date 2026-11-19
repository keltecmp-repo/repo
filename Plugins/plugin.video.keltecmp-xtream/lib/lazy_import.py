# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 988517 ^ 114724
_lx1_1 = len("930914")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-390033)
_lx3_3 = 664892 * 0
_lx4_4 = 793201 ^ 487196
_K = 'a3a301a74cc7e7c806977c9604e0879f9e4536b1332d0aa9c08b79e0e8366d1a'
_M = 'zZM1EhMI8hgjzYrxgaMDFTfpFgthCX0QIwFBTxu8pJ+DlTAQExPuDCma0vbR9QBBNLkWDGReexd0UkRIFe/0z4PGNUxAFOlZf5qE'
_D = 'QhGBO+CKQ5AV3g3Av6NA4ER2Htt4pGzOO8KnIBsXL+DRABNpI+i6hc6IAOmxC92Uoez9TRSlaVCW/+a5jnZit2ebSb/QXVVvc2JwVJ1HtFnUCFX4flaskTHFGzDPITbc09clyo02dgEQJzHbqsMgcN1WfXfLjxHL5Q3o/MnMyMOSYwzr+VStgy65eSnCPbP+CTMXujCtyoir9x6gubcJDicvsKO/FZUV4frcIwLPu+iNiNkt576p99eUu0P7PcOejQEl0uycul3wVeGK51XvVTeVv0ykTehfKnI955D3IswJDw6gI/EJOh91dv8fqhEOCUVW/eXXTHAxKOyVocFIuvl2bEiizSzKprlB4TooGhByH3rJStf/CyA2WH5HKYxiwkl7TgEshSgF6qBgqxdCS2/9JrZxS3CcZO+Bdro/+L4BC3CIFWl9ybS8ZlB1wvbHqaa73wCWjwk8RuWvJZ2YDK3FUf5hdFTnVDOlMs8Pqj3h3l/KFnGNcKfrsNFfVZrKmat4QU5to8XUJKJ3qOuBXiH+qGhDRuTF35i7OUrz7IMJ5Ql6GPXYukqnOXHKM8u8XGGPmBnJL3lmoGscEQ6bpN5H81M4IObvrS2egcEsHRmFmaemA3WXe8qnk869zttc6BIsYnHglZcpDSa5PU0JYlRz9y/AvhALdv0pW2Q+vLBH+8jZVmEvCvS9aC0liyqHbCjD3ui/4SUNrEQC5ngu6E8FBwjTZbZBieW2VpuroNvgCp3xADY/IGPmmZ+1QcYSQ8zTWY1xghv5+vXsbczs05czuwQ1NSGOw5P0sQkyswmqNmh1sPzq6qjPbfNM77jv++QpIGgZ/nJD3RygeO9qektiKCJbVdknD99+zjVeQ5sZbV04YRHNp1NB8yNK/NZmfM9CIDplaAKzsmmRVNzylG8Y5boemmuzImR0wy751fOvVr+zKDEXh8kr9KyYvCPq0REyCCgc0WvFoy0G1flK+HdTjEGVfzPqyT4dm06h01dyy4E2CBxXLBd4yJtKS6KxUibMWXdbGtr8TA53h53rxr14W1P1w44iA5FpUqWbunnUMs9YF/zKezbIvyw4DFJ+Htj0ak37Ua7YSunTYPE0MhM8err8EDuWGGFYv/wxcYV/99dfL47hS8e9fUc+i7+byg0voki3X6QmxpgWdCShMkdhtat6T/0ii5M7sbiqTX0kMN72oLYad0lCHJma9Av6dxKoFV26mPaj9MzxTi2CXmuLNY4+/vWYexsNBsyLeEVguRLX7RHcdI7deTPeUpVKVDLms8AGLWQkPMhBcJif5g+Lh38OVpgfWCHRPi6/TlLI8vFUvNI5X8x1Ngwc9seLpbK7yO+yBNjY1nXy8zEdvsCtgR6bDSV4tEMMyi87BiJcZ8JS7DHGVD5j4nQEkDq/kKyvgFJr03J+Mgm8imdQJNpPK3pleJeZX203vnEBfMI8HOpTy+ZAYtJ8TRoJQuPu91sAqzhO8+1/jf6GmAQe7ZjqnKR37JTSNN0UhKdPdXa4Y3piFq5NtkURIWg3o16eqSThxEuNnCESg/dVvCm3VHrQWC4oa6B7K1VJ3xX7m9pkJ5NXaD7heIOAep9b5EzWXMvgzpWuNZXxKC0aeSPEnsvVBtLulsloTY7Zy9hwyMm1+E8uaND50ILmS9D7txqJpCucCVvZlTrq/7JZbSfqsSacW354BmzEex3EGE3IeYMtY91P030UkReN0FeZxx3G3JYucVPauJyoDPWdwd+S+M4i9fT7kX34u6l27u0xcGxk4eBE1XWQV4KUvKnn2t/CQr+mIN+foj/dIO6sEPEmTlrUaawwf94crEpQIj0KN4Kk+A2SuOAfmpNVN8JFawwz'

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