# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 337095 ^ 142637
_lx1_1 = len("0f35a8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-223395)
_lx3_3 = 279708 * 0
_lx4_4 = 564619 ^ 819535
_K = '55f8d10c444bdb47ce94251e05851af2ddf5b5b0cd635cb0583b3d31f7a78e09'
_M = 'VZeSMoK15NAGMgwwh7egkVyZx8UbqUS8EjFvfYUbVU1F3dw2j/LhjgxkAGWBsPGUWp2cwRr4EOBCbD1yhxJcHhXe2Tfd97aJXWMG'
_D = '==QJvrvhXNRgSz0jOpNbV4LwaCmJucSd3C4ybX3IkEXbDI6RVqAAZuc1A2x4d8+MlJrghxMAZOB+lMzMErkPTcxGoP4mXayHLVh7bJN7jqRhbJN9JVL4jRXojBZajAwZSMT46JzfpTtlN21quFzAzdWxJ0QkUCC3jmA2DXHGRT7YI/LglqM1z/yaBHxsDgvJeDNXYllR+VTF/2w/dyXDiOn8bPvyVZjI4UdNeUpUghX1FnpRYR/DgfrPFhRTfgyo2XX29QL+XWe4Zs440bD1XFa9mdes7oihVU3PKmqbTqEZzUrQ+7/h3zLEPDPqauu1e9E/ZqJ8Q0NQ6AxWK2mGOd9j5D9J/HOwOFNtBBccX/nJTa156FezkMhq1VryBI28jml6gXXMc84mZLHXMQUyDuB1NqjfVTlH2EYrayDoGajWVNBUZV9wYoGDqXoP+c0lhlhEqIOgwc05tnZ74PHGrTxx7tEWRzQBuf27TCVBsos+7OfCYepNAwBkEumPQlXzgxVb/g0oZD+CwzoA1KMKlINoqtjxJwpVMUs4iyqhYzSkYBeXVWqVlQelQInMNy21q+vp1YzRv6MvpuCPI+L5njSy1f5cf42NX21toF/Cqbf0OfiFR0azGgkUnNgfFu8n9UmaOcMByb3E/2Md/PvvR88UiR6bpUFTwpYR4E9RKU2gyCtvIZcXnxTIIuVy5oIFsLAs6sTmzO1iKbICggd+LyyAYfvm1cEj0eDku99ir2wm36tWQj1t7l20gpt+Je9SHS0AvHYxYQwxvZOXCd0v88ex12sDW7mNu2WPbwxJieIW6PkmsOyBp9No8keNDG7vOClxvqBCMbnYbGzg6pNMP6/nbMtbqnSvg8ccCDO//1+1nfSYwh66t+MScVtQn4uqVDGhu0jeaGN6d9VqKsKsGnGHKox9vSfv0DJYds29XLccwU3tG4a4lTxkesjHZ7UQ+H/GUgDBn79RI+aeUFTnMMO+Yye5j3yys9BCTU39GEadFHW1D9QIqL6tifPP3hwqsP/xYbhQNggMnWkJmOFLIVeBIDuLbauPTj1YcUnhRbw2jKRJqCTHkhv2A2mXPXm6lZUx1do8xXSL/gZSYZJMcVu0PH5bMxibUcCWPYCwxBPnSx1PdaGcZy++oXqZ/0CRQgubwuH1hQ5e+HUva7TwcEcQgkSRp7w/0Azc3Lk+KJA8rQ5wgFhMYRKXq3KsFv6a3ZBQc7WLkDKXL1KS4yIbpUaWbEGnz33VopQiijNk2v08aDVBUoPYkz5KC4xxYYpHWoLQQcz2uEBjdCKvdF8qOPO5qTvKnY9+Ug6IjNOxeyhnWoxRNx6jjZ8tas7ZrjhGTMTxng3bZQT8UvP4Ld2iy3xEY78ko1NQHD3vReLF82C8b0jEGVPyBEqaPWQJbk4c6hOalaEyuV94HeZ9jr58XnEiPQnjtUpCktmfzw+Cwp4Jh+Sf668ZuEpPogeKMQE4PDKWZiPPajdsxTCIMt/4pdSO6wKC3idU3e+z+CQfUkpNizmQBzFj58dL80F2uen4GQV6MgeUFwMCIAq59PViSX2cIo0H5YPF1AzZBTFfKHrq5YHfb1UAegipA95crowTH2Jr3ybXn/2mW7Hvynx6Ch45MdLr5is9ri5Z/34M9oKhUrUUnxRU4pjzOPeM0ErjVmtKOTCDNswVjOUZ7IVnkxp4J9OTI9Majs/eFYUM77JadrMc5glpepNS3XmwPZHf9FAN2UvXm4ZGAWZGU9zECxo3gKSqpJgjHGFKowp3IHZ5FK+cMH7bbzs7BqF4qQGYj9D7J94dIvjJqcl+q5dcNEGXjKXAYU2AghSSF+8DyVWi7kGM42qGEcEdDUS5EYW+0f1LP0EGXKB1O3Ny'

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