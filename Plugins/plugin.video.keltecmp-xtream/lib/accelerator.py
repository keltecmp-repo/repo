# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 451709 ^ 533738
_lx1_1 = len("e4d333")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-467980)
_lx3_3 = 343402 * 0
_lx4_4 = 842005 ^ 441088
_K = '693c2dd9a483a1f1cbc89065f290a788899316eafe5c21634db593709cbb2f8e'
_M = 'j5q3sRqcqeZQo06fDANd0nyr6bNLwUaEhXVF1bE4MRTSnKf6HcCvtA+lQstcVF7cdajt50+THdLYJUbe5WM2E9ae8a1LwKvhCaFE'
_D = '=EwNel+Z+3poPWydO/yoJZnxlRCF8An7iPSOuOWNDL732u+TBvzseTTmEDNqoDKzTBQReeLZLT8A1sN+12oVZcpZ9QTvfTKkwK2jgr1IV5H7/l37xiHDyfaViQPJDAW9P/pHG60zOqrHfnZHcYyhylpEUn4Mghep+o0B7jcrjdcnFyOogxwxTxVbJrb2FzM1T+2NenLPwFmr9ptRXCdsTKQ84a5H0ZOG5OcsqzDwkmwKZwPmVkLn4WTd2+rTDYaeAlJdDRyvCLqzoQu9XcqwksnUyYVNhWXx5uGoN5I5gJu2shC+75UsWckrJk+6crBDD0zw5qXP63fkRmSXJyHeJEgfPsGgQxEcRcQtvSkku2mmqAoufaNj/cUQodsZRI9bUtOIO7KuM0Rkk0koyHEyxwQP9jhsQJAtizLxfyXBhfonUW+rdGXdsFRH8EUh2bcQ9S+g9iwfiN5T7RmI7ytXORRzIQrYmKR1G6RWecojyZ7INDoZM0cnq9jodnr+X7X2ktTGnsYsB1KoXNxhCqpelIQdi/g0KEmVwz3FBSHA1SOrP98p6flaiYzCkYrQFlJ5013u8Qht92ETElYkyAx0vhwppHzxKqLzjNPZVAaxwJ13Cgrf1rCzWAhdLnFuso5/fQXW0aZD3hihlBlxqS1HZu/j/B4vmMOO/3G+MdSWa52ZdliS59+v8HSKIX7i9yxpKMN7yftGtVFUvU+xnG1SCScwqxXohGHG2f07rCKA3szNlUmy7GlP0ysUTFIYUxRZiy2MRvqQySysZjQcus9wBPxpNd8kJl0Mxi7t1P6yPFThL7lC1vO0bPHOcmpW/Rc2Eh65d3/lEqFNNolBntpijL47v5bZjLbaAIZQtZYQWKUs+NfnVaCPNgonuwbqLHp+54KrnvPZVuU5qZTJxM0c6vQfRLhn2NdfMMMXbB8vTHBff81OGmH4kgOFsnNDmTJuPOW5nS1Ee6LNPl+1XkKXMT43kbECccfIFeIUDiNk3AI4tBRgdl0rbR+ijfFGJBt6o47dwIaN0zzovaBDB6G1lYe47+/MoYcTHDueKw3ETeUvGq1Ujt2cPs1Y/U//orIcdUyA+jHbFjylE6ePtEye64vfj8R2SwtXMxdXRPoTNp+bfm2VtykNxyfXS68wH7hlpm/Wtap3LL8Au4mrENjGJm7T9g+tZnPMWJ7Roz42/O/7SVacOfhEQBT7pV0HzZv156+D97qnaTK1SYE/6KvqEsKaZMeMNIjnhH4HV9t/iEr/yHvQJGFBMN2oE1UUtsQzEMN+/8SDZTLDgZRoaJK1w77VKOa4t8RtlaB2Azv5VeujPghpGWCEYL0oyZxdkUs9hQUi3AxzerSc1qwg6kvEm2eODAzzkUxp0f+EyL4xJsLJ2OIVQFWGa4udGzaL0K+zyw0DDHqDaFtnbze6rUScdOG8G40hyijPSClASNgab+IO6VjE3J5aA0CRGspGoHirgFDdFXIRf1exbvrMD7poSc3pwU5DWbKHjecpUYa0+cFciRiYVhZpu4UJfgl+4kXvnND/MBmGolUbLI2cqzXPr/wjFBVe2QG+pI0F2/bKvu3GTUi/Ygk+5WbIZV0f908Q9FktjZy3giWxtS1Aw+Gj5d5RDpqaPLL3tQaq2ooYcmguybiHqDOMf/jsenayDg30rQv/XohmDYX/QVSi4jcac85UbTQgQZ0IyIZlaNghULuqx4+rWAcgBXa72mafTuhljhb25w9QtwtJSBgbjuy9OPn4nbqx1GKjlR222p0rI4TW2snkJEFzcYBjA+FLvRJWqOP28SO+cpS3oajr0Bnj7F0MgBIDtS6OG2eXI4C8WEc7qnD6DcJKy8j5Sky04JFj'

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