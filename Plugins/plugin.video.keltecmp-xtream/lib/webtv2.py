# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 473367 ^ 282748
_lx1_1 = len("8f89c4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-895370)
_lx3_3 = 495502 * 0
_lx4_4 = 210546 ^ 246563
_K = '1d53aa4f22b91622d5e9c29bb5f84ebf26de0044abedabfbb636b264b23dd3fc'
_M = 'MVZkDNNXUnMEFw=='
_D = 'R0Xz1REh3cPHRNwM8YQVZQHFnCEg8+J1VhKW6CIs22JfkAgDjiJYjoZ5LM9IsWcFyRacIFty95NsDk/y8RTJLyCtAt6J2sL5CUipoClt7SBU2KTJz3NZVBN45v62WMrgRCi29xQAOe/jOZWr/Z3qsV1sjwWOWUrX1DOqZbVfWM9mS57c5sGc88cVzU6cFewmiMMlMJp2C4jM78I+3+Pd1GtmFgc+QmOjdhZLfEMRwmZrarRRGaxzF+dUOcpMGYhGD9aK+iVPfSgyXcfE3wlWE0FiQnq7Ef2nU5/a7IGqJVbVU70ioJ/b5Er5Yqu+gY3WK+D6cMIuzGFNNyMeOAO3a7ms+nJqUMIdzpFtpE7uLCPFRqGZ7Tg0ihlJUxdg+GkwEwWEQkG8r6lSyTTE4822+5sEJLSaLMlbGKFcJ5y6nrypAHMdzQUL6hg8H7hWjTU3D8DSjCkQtAnIDWvqkFoq5t2bm+NWAtXbJK/p6S/OJCJ/UKO4SktEK4/fFiXEKqv+ckRj41pyLbp81Rkl47gBQz9pEFDWc8Qu1h0AtVjjCLE2mdQwHbVpaPBQSGH0VOKwDJuW11jaXNV6COAcmv4JaJSP1GjcleBa1/+Gmu+v2GfywFbG+7S/ROb1Rb5mg5wVStIWkj+KLdptMyLkKq13HZu7JBOXsLqCchi1InbZ7TLevPO+/v/bpJdCli3SDVYk/9LPtvDma/S/lNQO3KWSBnr90c1l9frG5jXD2BA2MLK3zZqsucRxUscwZsuWklIwGTt1MLs4AQYX2+IisdJupFWEc3Adq6rfgoBL9XalP0vcOYXlZsUpahL4nq+6qsPfkeOAerFBSbZsbTddC0fXqOgI3UKPdDytoc2VSNhCso3mF/3ro6LeyvDiaGA10w1N7QR7Z43+VGuPM13Y6YehfBAssjK34UzZ2x+0H3eDP+CZachjEI7Ub7bsaWZjroO9cgCO0Al9iAyKBXUzgez2YJyWp9NJLLIBHWw4xdLf+wMO0BJ/IVwo3sHxJXahfaFLyTX5pruRv0nDQU0EtxI/Hyil5LOYADHyTTeyeg1rrC5oGJxRIkL5uNkVLiOtaoDmRqbqsA93SeozZX5MqeqnXJUTQQm3z+1C9Qd47i3aC8qSVXVwiv+5jo0FHLBhiTqOVqbvfMZp14UX60wAXarzUgFARORWByHKvk0SLPimBy9B/aqVycunu7LoizUl0VjhplirDfb+xnP+kyLm/Rg6UBOULnjGUuewInbibDDJy14pCraH9iEu9KY6Z28VDlfM2aqbQNNUKnN4d5GgeQ/KRF0TQDseZ3gxzxAxwQ//m4aTw1GkIA9x31kXjd8SgpsjN676ePGGsd2CE3SxJlr3p6tiAf0s/HEIbfWxbkA8MmiIabySIZF/AzVlJ1NGpcNPEK3cvYvM/MHaYtrKf+iVgp0+DQVSQkRKuUSamDIEpHq3m4CK6yz8Dcs/6t/wxYQc7rWw7sbqAblhOBq73L4kPuQQ9x+UTn9XgC5+V0HWoA2BPjQldnwzlCBq3WySaBq0Ht9UXD46XgjNYUAnBvcfPPsVT4SIpzDQ710xMBGJHcMc+7/OCUHR3OhfJqgg0CQZqzvOKmydPTai/YKBETr9nunHpE6BftrqQuk7ANFBhbJ7o/7yLwt3tGso/MhhcMq32/0cJfBa/WENLhcP59BZyADpyNZoLqPq4Lg7ZdPZ4tz0y4BQYwHBjG5P5uELIZUyn7x+6kmWHb74fc5HM0AIKoMirfMWdw7AtCMcerhwzK6azTBi/tWxZnekRyE1PPmuFEsIWL2eIRRBHWOzyH+Gqpv7RM1WEuUX'

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
