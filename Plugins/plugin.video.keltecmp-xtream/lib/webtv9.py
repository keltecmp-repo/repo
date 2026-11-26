# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 117741 ^ 671545
_lx1_1 = len("6b5eb8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-573123)
_lx3_3 = 834342 * 0
_lx4_4 = 580189 ^ 644355
_K = '65bc62dbabc8161190f4ceb02e3389c573860129d01721ec981edc79bbcb5f2a'
_M = '/Zx2YfDKvRvhmA=='
_D = 'AFZYZMqjrXhf1aF8hpoEJ9hKuYnEUya06ySLNBuORP6wxmFlAC/Kyw4Ypf8JfrbGIAmDPLTnmmFPBuVIiK31rSobLSiY0nPlsuiSHdZmVryF4OH4GGDvV9zE4D4yMUFg3RiyV5ju9U2CUk1hHwYeNx3L/bhz52FyJOShwOjfHKbQvwauCWWFJtZzjSGbbmfpt9l04UmWwru34QJVbrBCEPQzlZugW/0g6ont7KcAsO1fv1AxDzPfwU+BDKs9MenC/GDQS2zthxeCpxjQfSCr1lMxBxUZMgUfr9tk50u6icaUGJtFXBjV1AH0/2losAaVxaWmYBlL/rU1pQpRClbfc4i/0UYPtOkR9u7fyf11AtlKgUX5yKqTEGjttyZ1wmQQCsvRNgGS6AIw1DuVEHTEOIiF9245bv7ZpxSQHYg+2wjl5VDdH9gQ3NHwj9vWr+PnCD1skC1RzWhkxTo4yL6RyFGj1fJ6WNH8jwei6jtumRi9MV28hHwNyfVuMoMRXbjQGmyuFHPCcIbZRs8DKfOn1xuVZntfwvT32G1v8oRBQs+9YfGG2HUAPr4pTPbme9lYDfRxG8pB4EqQ0WQfDm/SCLnDxe8BdZ0GxJEn0dunlL0lvTHwkDDWQVysjtFHs7xJ6izKds3438oSQ5099+Dyi5JUvt7kaHl5LsKQcCoCA4z8jf72uwGxtGF9gY4x8Qg/wxNLKAt7TH86jWU1XyoiZZQ3AdFcGw7VP+sAWkuAAToi/HZ1v54bimYY+2wVGpobP+S/dBxi/gbuLlflOHvEY3u1VWjteT9NTn48pUZQJGVT1CtLJCZ+ROo2mPLSbHJgDUuI1D5Xtz3fnXPRq4APfXQNqTu857gpBCzPVKnlXAfvojVirD2DFfpxdzZBjAuA0O3UhPx4NUtSqHsNc5uVVtMXMpHI4yEF2eFDMdisnPdvXJw6SV5EY4dVGPj1gnGcuxXrfwD4Fz0eGfGdNBFd0UflZuAfK+qUFoVc4aHBAC8FLujH102BRb8zV9NnXdkIp4Mey156ExPf1CWc0sW1JIRBfvTFBv3C99wgFOlYB0hYWCBJERRsRJ5mRlwySchdoRY1PpIfVwI6Ie20if7EKiGPnt1teP6dWRfqrg/Z79I2y2DqrSvDWkBlMH98mXT4qVWT5qzmqcLqyBIFZ5U2HRTRnIdLtX2UsOqmBtYppzb0auhNZTZlNdArd0KEwF4XGbW7AdYSpvtVjQenZb59SwQqm0g/mSIn6XAG+ZKKp3UnC5bRp5lhfaV+qYlBtQAQH91u1A1Cnec4aPnPqJrhPImtxmcxrG9SQne01u4IqhEK2p+/YQTBq3R0xLSiXQM6+OTX4DInIJCQ0jZHAo2vEXR2xNpwnezwv4sPx/odMtWLLzqGkU8ppZaJDnNY+W5unc7WoOrzt08OQ9lvj6FtEWuC2oM2vkRd0FGodDxKibry5SFyAIFCs+oeykmAtnNGcgddK6SiBVt08Bn4yIXW9PgvQJpC9HaOWX7+JqD8hJDghRcbgvLSKp3bO+NZ7lwEdaFyhArBnEiO4G7I/FhPgkM50OQngfPiyERGoPROaGojGMSQLJ4Cj2fOcg8kVskD7HC/F9EM6E5ntmcWhAad9Fn0i7DdIph+mQnhetfpqirJDKqYckEP7PMe4lOrt1JV8rLptEVnSGtoOE85xgrMjZBuuLIrH39viltdyHq8jS7y9zYcis2uECgM5FJAjbsax3MXXY2WISs8LIVjufth/kucZv/1jdJBcKS8ufOCxXn8cRjKz6aLG6sUDLsAKMNv1MG954k3NF3BXxoPtcK26fGknNwXoctSe6lMk3EQHnWZ'

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
