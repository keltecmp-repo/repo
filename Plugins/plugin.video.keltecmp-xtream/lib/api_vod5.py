# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 459843 ^ 139004
_lx1_1 = len("44abcb")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-442924)
_lx3_3 = 482849 * 0
_lx4_4 = 103361 ^ 254794
_K = 'bcd01761b0db196267ed7be0b5c3d5532ed8812c64575fe6d2134e270af6130f'
_M = 'ofp8NHhVDVmxxukxrMhjgz4eE7+/dbmsqSZKuQWyHHrl9Sg0fgdcA7iX4TKqnWKNNBsT7bEn7/6uJBrvWOAUe7aseWB8AgZY6Jfg'
_D = '14uAGGoFdlVKXwpgbeisH4TDoH9cBhnBCSBPTUtfh5KwvGdcFwwBkdEWTqe2nyrmx8UXiv6/3fpSBEtXGYB8kAIBF/4izgDrgqk40EPf0fxjSiJAhMI849VuhfuWqcJ8qXk/aYLJdJCn8NhLMU2EdV1VGnT1XaIFG7arbyF7uBMlnVP7387VWFvNcxmhQA8jrzPOEJWoZjfp+Oog2+2NBiDZGlqtn5SVphSNFMmMcv0JSnNfJow7Tw6Nr5pkI/KnfDsDlP6mRl7Hs137qRKPJpzyqRq9/skYi+kaFGdpKrcHhOyktJKBYxP5uzDwlCzUoVhoOxDJeP6C4Stz7VBg/rVPju9sVdJLkjHdKokrL+pxSmGW2GCm9Lq01Lvtyg1Lu+h3JUrliAEWSJxfKGbLjlH9MDzzuADCHWCfvD1NLWowp/7FSCDOyRW3GHlqBDyPKJ8zAEvVubM0kYd8AQGyStxGUnRoMFODaV/psxG2HcgWlIeeR+ebMTXWI/XtMNRqPd/e4fylEtS9U3B8YoC2pfQNBHhHgHx7Pg29yyoR/2bU/4yoi+V8+bgBEq42sn7/DGfqsfi5r7adv2Grq100WSST+yn1g1EmICOKq7T87QL0MHLjn0QeYqAC+Ooifyjqih92WLL9VrsAJC391Px1dZg35kZS433lhG3AvCuszBP2jsS1E2kvA4pCpSMWLI3WdUb6UdDJoxFkWtUDc6Vx+PY7iC3X659bKafgC0P7pHvWOH5NYsZGIGc9rm0P01nVb5+b18djkNW1uX5IUXYMX8yZOrr4tVegK2kRnvQ/+3itFksgIghiP2uHXHYtPItTWYZWyrC87563YKxj7igA0ByuWLarWFFBEVV67NfZKyNNpGUgHZpxDqsR1Zlmih3iNDSXgLCPYV9WO4Akf4+M1YMgaBqqGwPfPrxv+NcznJdIJILwGdpFtIW4EWwQmHqOTdyj7OsvrZXAX+YbY5Dj3gfLaoRlO1y1d4Uuylf6B9UbsjXHxx0qQFhmAKpOCJ332uzqtn2vSfAj7VXj1EqM9iU6rhjbCAjQu6zuOzjlsGvhgVyQQ0KqkdsvG6l6LHzM4qYSdOghjpJTzgqpe6Fgo/m1imqzwue4zjwbC2jlxWS0j5zcaihNPJ9JuzY79O+9a1qqLJGip+HT5LnfChh5NWdVUy8LcJlp2F7luaZXCgwDXHmhKsS1vttqGTlwBDH7c/2bS5o10DctokjvljS+Te4ITAlz5AlAfzflU2GbyjKZrPQCBftnawK3K+R7LI6vTdOFN5VhtW7WrxsDMc93vNQT0xzGbJyztNrEiKZvKhqK4dxHYiWxMp5Uk+W+RiGLORBdD9OvkOdm/D5yqnFk/s6gcE/CuIAlGN6bnIWp2nkjTWMbXa4+vQy9NordOgFq/1AUoJCjR8znvVS8l0ywazCp3gJpmrN5652clWk/8kbDXEj7W3wSUqNECEWiNhNUtMSriVMhbS7AEU2a0oEbxZFIsruXkDDBPS3VH0DVAiPar3HT9gWCtLiuYeiLG6tclyDkJ4xnbUjM3nDgCVBarNqHEXMQQxkrHCUQiR1QCTHtcYlCnDYHBZ2lu+g6gy87q59Rb4vY3Z8NY2mzBtZBuw+m9QTfPjhPom8TEQ2CQ/wzDJJQoD6x/+fJZRVvbSLx5Vdx6A5WIhR/i63YxqTQ0CNT35A2kSHVjCCoIB78tw25lIl51lSIVsiCnKST9M35mqVhbNtfV6Rkq+hiqDTdwPsorygSimr2ceizbB9P/3VVoQdwWqqqEZLix6Gxy73INMtiYUXe/C7CpCFQrHXGXAC0/dNyjt+WFxovmsUg/XRDkOetQ4dhV9Af'

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