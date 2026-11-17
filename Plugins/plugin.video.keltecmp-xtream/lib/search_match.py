# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 349493 ^ 815794
_lx1_1 = len("5e72de")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-681193)
_lx3_3 = 331065 * 0
_lx4_4 = 555250 ^ 841613
_K = '566079e8f86f4f498df2893ec400bd67521d5c8837d9789224feee1b3a6b3c5e'
_M = 'YDgWcLhlCdB7SMIeewWKH9hFOVILJNBxM6H/A7H5AdNlN0F+6ztN0nYfzBZ+A9pO30RlBlpy1ncyoKwAvqIGgmA3EXjiakbXdRjI'
_D = '=MuT1UEPLQvZe5vCIC/pXc0DTK1OFPWzBCmBb4RBVgp46qZONsxkjIie7tFiRIYRt1/mQpmyFm5jY3BoZ+i8KEApbpnIj0cYxSB1PQlSumB6F0ohWwK9haDq6SP/wDjrjW6erK7Bh7qmwyivuppr0cu427VSc4V1uRPJ/wgomFy0LLwEOxvbYwVKv4S793szqJ6nq5VJnjimCNAuhvN9Ola56QbYIJwYJhnLCUhJdug2+EmcxciP7W2PLA8ajJ1AIxzlzT5dzP5NvNDZgRyKdqCr4+oxUiuMb2V8MCejqzGdLzV6yHkjzmiGm+IvJCASnYT0qLQKh/+x4gw283zz1F4WvCE6W/6p8NlItYEwBK3pOWB1d0YtFGr3gNTFaQAk5Z08CqiqnheM2GwzzM09deS1pKwkwxxzPXQkT+e4MKT9eszR89QlH0yNW9hGS71JCYl5afuOPz4wsObx41+2fpiYfvpQ9piw/gSGD/S+ULBmz/1bes365VS78a1MPfUPj9OrWm/WsqSjxlYirtSY8VcfXq6hsqx2KypUrccRif87UBLeCm38RPeIAJ9P0HB4tq6LGh4PKexOu88a8y9w0E8OjnHXR2LKce314PZ0TXbvOt0LL+i86v9kWqT8JgfjRM/lhuvNbLiCVsotYEajefBRanwdFxEwdilmvi4AcJUNdOu8sK9n3r4y3iLpaJNRcmmJdHkwu4J1YNUe03W+iZRiCg58pGTCf2liwBfIdsrejNEdXyFj6cF4mLT3ICHLh6jqAI10a/qlMCMqdQYucdo4/Z4EdgXuyeDaU4AhngOwf6ilTisncKESy4er8N5FXyspZwN8RBNgmYqVewpotSJdqtaRK/UgtWQ8ZMWhX5mo/cqomXv9k4gImajMHJje0+tC5Z0uMgZvwrqbliVu/WTKyiC/5FLExek3E8FeZX7AXnXW78ivVxOSpI+3+V3pcY3oxhwCCNm+zMFjhpA8gZuC8l4fmspQFQUqrkWyhLYmsU6XlWLqBAafinD1J007tg4OoVqGAB/cGsXmg27b2WFLZIGC8yOiyjhjreTQC3rcubPNNkFXAhRHwFtfGaIKswZqTATD7jXAuznNHKe3z/O1spLsNAEMbZ69LjX8R/Vg/wWivQBYZ05hknMYuj7y1AmRnT1vOXVf1TvzijMeCeu81tWIkpKWWByUqymRqrXh4n3aU2S63CN5uV0evKwr+KM989eVKWRvFbgSeSQAHmMUa0ET6s73d0g5U8TWfodS0+jGEGH93XFgdqpq9P3sP87eEvwvU1No9a1M9HGj2SACgUTQQqFPvey+PqCNFFa64eP1IzGSXRZh007YvE2yhSjvbiL7UwSDx8Rp90RQ7j7bJu4j0UeZqVtHVmWpWp8Iaeoi09qz+9XEHq+co1reiNmCAQUMoN+qmDYSWXnBFpUydf1yM6ksULOFqkkRjMSeXxTW6kedf/t8C96jInzPga8473ZDOyBD7bAXTMXzLcvHMAgzfmcjywk5PtJce4Dn2Eu/NqknCJOa2fFNjbYJMsgPBYbaKNUSIwkX7p/F7O4HboA7j4qAFTXUkARSnx0bQrv686GAG/Amk3LVTCURJR7BMLm+2auM+YBVyDy4YmNcA0aLj6SGL1ikqDfTs0jP4qW/OG1teHAWEGd5xw3DgEI8pEydorQyLj6J1sZku3hY4m1M3yiL1SfpVvE8CcsRV4rt68nyE20UU/tAJnLo0hF6qRCNyzNbPetI1yVf6gtKW/GTa90cpGMRU/cKkzctWySzHwAbrj6fZWKEejpyMU0TqvtWZ93WoyOGf2UIllo0uhMjwzZq1/M+zTwYfCLXO3SR7Pd9QTt/9tOabvAsM8LDLS3r'

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