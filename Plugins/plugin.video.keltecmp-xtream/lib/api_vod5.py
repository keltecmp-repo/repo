# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 138830 ^ 455038
_lx1_1 = len("b67bef")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-562760)
_lx3_3 = 201735 * 0
_lx4_4 = 822199 ^ 978146
_K = '8bb2c4360859d9d9e4d4cf8546eaea838521c0f2d94ada2d81d9dcce43735463'
_M = 'inIqWE07v6Ly/A=='
_D = '==Qg4l9eSKYvSoadFdnAAvi7yZkT6/O24xJDOPhQGCPd9O1ZW6JgOqO7fGLtpG+jru6oU8zvuIVNjXds5VA7Gx6/ZvjB0TSe3z1HIajObOfZ5v7uajoK/VhQee4fh1sps+o7IZANQG/EIYxFE/q5OeI/ngKINSShdsfvljZluYIHM3wblgWEaL1J16INRo7Kg60TtMEj0yssuYBF6zWwTj+TIlc15+Zc+VhPtwzQAfj3Dgh4h/PfOQKP4NRmWAI2HeJJPah8OU91jdm2OFMjG3s/gO4cdjDHSICA6/BRNTZD6BBmgr31El5vt5e6o1I44pcMJ2FcXdhuIJHQuB3cNgS13HaeIfl6cQD98LxjJnCc/eL+FVbskOjx/mcC0lXNyyzIgQD1I3D58cs9pKkGdZUWgNeq0JWyayqFxJ5VWH71Hkw+jeUgj6XVIQfaKzBOg1bt7C7yDyhyMlKtTqQj5kZMCZrW4LvQ23fqUv8hlOEllhnJyUsUdLaxXnC1gprKt3j89FVwCs84BwDjL5ZGoaxq63tXXcnkUpqsztqn8+7fh+j6WSjJSz0QUjBcxjYqX5pjxCetqLqI8YiFwtBS4a83ye6d3FVfqxsMmvbpmY4eHkLeFbRGqIStVV1BjmQIgNZoFDxnV59mIu8Xi+VpLV9zGNJ+NxEhx+raXq0tiQ2Tz1c63yof6oBSgPvnmamIkIMAzC1i+PSd9WFpWbpRqmnl8pZKOgnACywDQHEw8YzF3KLkmi9/FW/5vj7oQa3vCRkta/LRILwiBlx1mpXqJCn+HpodP1FwWa4nqySP5UUqiQ8i4/TZ/7m2W7aubJGpHXzZcsbKOCUvMV4KQhbQ5hPjaIhr0NfXChXmxy4ou0Fb7dt5U2mNdw5B3wqZeZKULriFsaNGgTJ+hz8eup74Eu3ObREvoB5XnZinVgzID8xsRW/JDhuswMELH69h6JSyPu8QM+vhOoQA3tYEmGjQSo2fEwTzgnVFelSoBtKjqzE6+qVgUxCCkdpOr3k5cI0AjlSwB+4FfDXvbxPOlOVcqHi+N/iGpywHMdcBR41btKAaOlPUl6l2LkuLecBOnq7hKUL4HxFtOaw8mPgD1/Eh2ZFrcei+mEjCB/VKUWAaWFrzXutUBCbjmJwyBXK/B4k2hKSjVD+9gc9iEhz1Q9/4Mnjf1L9LDkqhs2DG7RD9rzk9dMlZIfjTLlgDHEso7dTTCGMeyPDf3lcWs0YL5Ukq2Mgl+EVbpc+BVtxXVIXmU7oog1Nze5WEWNgY8++Kj7EtvduiKhXusqD1Eh/Gi6XmkdThZq6j0PGR3tIItEyGYn/YAk+WAoxkM6k/6BQF4ON6lg3z00iQERwP4GaZdtWzgSOYyQ4rgAxruSiT4OkY3qCwmZ8m97rHi+Dm3t+A+U/R5xOqTUrclLSKJw5RxWzyxVX7tyTWFCYWo0mXMw+cMM/RcqK+1z8MMfa3nSbIaL0WCO9lln9PfhEYxvqP0o0rAfUw0icFGP6cEXQEeVwKsyB8ILl7TFx1DfwIjCLbtgQEYQLvWuC9ng5NDxolcJzgLKZityT9wrHW52vbbkpMXOtBzciTLzZMZaiFVDnNH0MOS1K5qTiuDJCJvBba0IfY3lZLFM/y0mGVQp0isjoyyApTDj5PxSgttn1j4tid8mTrRXZsw2fG1k9bMG0ATXeg8HRPdStFt3bdhRmj6Ilbk9Gg8O1l45xMXlHBIY7/rdeRGhiUXRd5WlxIRUP+J2L+udP5zODtep7QlAqA0lxf4AOtkQnofkgUpnS5ylNkg+LRhTSbw30yAS5Uk2OFhX8ZsCb8Ex+NfUHLSskZrf6yloPD7BfV'

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
