# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 624989 ^ 625447
_lx1_1 = len("c8c0f2")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-958911)
_lx3_3 = 120284 * 0
_lx4_4 = 239249 ^ 565050
_K = 'e3c94c479744c8915b76deab13cdda603bdc6c26522611248d4a967261a14613'
_M = 'FI5lRnUl3z/TVQ=='
_D = '0sNq6amEe9WSKJOOO8HVPjHuweiWlzwCMkrTvVUH+ibeJci1k2EaJi+zJ5wZjKjqtAMry4N6BENNU3iD3ddS6Y6kOOCepudmSBhMjWQejrE3i2E/e1TtIlGLPRZEbs9pBgaqTJ8SWz6a20VKb08nTAg1+cGVMax4JCRWnqjIPDhze2dW2n2cezo7dXSH4sJZvdaOpzYCuG8mkMI7uWqNNwNzwl1IebgedKCHlzJSNlc9UWbWzbsNrc8OB539jLgtnX+ccMMomdaUf0k2lSH/Hx1AyQ8gKfWmKZxZWiGZFUWr8QhGo9RiXxEC+y5oWWCp6Z77NpLmtYdH1J8VM1CbIAF6+PLiWoKeq0xC6FsXL7pEAx7dcNlG7f/InCK5zLTRI3BCSlSWvwZsAanxObBCgDMFDCsb+KwzMn1/3Wi/E1GutM9dnzQyXbxO3SrQWm6noOgMgMiasdISXJo0erzkQUvBsTx0FcpsmacC218CsYcQeQO9kMmPPD1aKuw8Cgcd34ZJhi+hMYhID8DDJowTJ5iQZioywZG+EBAQMoZDz7nJY3cOwNOAI77ajDf6le0MU1CoUJCyx+zi6y0ipoEVLqfzvw3i+j7Ps+JqBIrH/1WJS/zdzuU09b7EG/9uFp4NslKrgOvm+VZMEKZG/sr/RaeaH04R7+5w5m5DttpaeCX8Yy+k5vg1PO++3nXUmtiLBh9j56DKnxC+2ARgQlTS5b3AmdbViZwFTGo0n+0Y1Zbh6te6ENIJJTWjCE4QKdyQQbOmW4O/Uy38p0M5Syl9I5jQ8+onhnJ8XapNrw00eSwSQJZob5s0+zwcSjwZVno0zMyR4RO9ytaRzkgHCikf+6enMD4t4cjI7H6JNw04L1VkYCB0W9dLHiF7GICpJYg8r+eHka9w+8Lh787fu+phQmFIP4ADdm7wosbL0fRc80NqCNMMZQWjfQ67rGg8mHBr8uwN4vWVFbqxSTRTGK3Y5D1W/bZNMqOXEW2L7fG0ZW0QU7l+0VcwoA/zsF109rnCSu63+Nhm/nXrsEGXPkXkFLlZKf2NnKsqaq7sCRvJqNL53Lh/p+4efNPHhn8MJ7XjHFc4QiXN4JTjRJ/zuCuoh55Ws73r78CdBlezbkptkiDlakwtK/EAuT2hYB2c3NwSWevw57NqYwwWQ44C0laHh+MFfhSB8Rv8XMwn0Nx78maiKhNZJuLA0ucsgJMlSFmGZmrpg+zLiFXq4ko8pV5xPA6d+SEgUbB1S79R3arOdUck1ENseegUCY62zrsjM/DZFsrtrVGQJtABsybxoDeiUPhrdxlkNFT/Ayd0nX3wy0O69ggeH7AEwiN61kMV2N+Lbr7aObGvZ0UPBAYw57opnFl+srz+uBanQJlkGzExo+LZ6qWZc/DbHS79Ud0DimWkhpvq4tnAlElj5CHu+5Ohqh0LsaxtbXDVL93XW41CxRQnoOg1pbxSaT4AE+tK3THN+GFhTEtvZkvZ9RM4Au7YsyWeOI1/BeaZHtp4zDroLE5WDP0Q4jlh9374UJuW7OfsHQQNUcgl55vpeC0aYwMOll2Cb+68yxObZ8t7pPFgz/Agrih2xMpfRA/R2blb7DRvhZYUaGLaSRzSt3vUmgmlIGp/3Oi+wQzQcCcrdsZgS3LIVUUxm5dMBC635+0TdCdwpsHgOTeGbeJQaZwBZZMk6Wngn7Iry9H7pmLRE0bYHpOdzUH3HUXwxUSwBtUSVnM0v97ygCKdNPn+zwY506ibPJxwz9MJoOoGCixardX1ZXLuC1pQw5d4gcJx7NQmMeluUFf+MTmNQ1phw8+EZmB7OfLuj/BcgdT+ny7ab3TancGsFSxg'

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
