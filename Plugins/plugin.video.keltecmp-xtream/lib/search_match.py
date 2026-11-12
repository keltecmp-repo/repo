# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 969309 ^ 947348
_lx1_1 = len("6f3c49")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-569227)
_lx3_3 = 434943 * 0
_lx4_4 = 719096 ^ 284878
_K = 'c3a0f47e82c1bd9e9b6e97692b8647ba6766c619bf3deb37207a387ff8927284'
_M = 'FVJiDiKsehVhB1+MhRJT+OCRW8ikxaFnlzUd3XimXcgHCCYMJKh4RzlXVt7RGQOquJRazaaUrWLNY0qPe/cLxwEGIF1z/X9AY1FV'
_D = 'ib/I8aS+0hYUVTB3zLRTZ92ldua1Aqq6ITN67ANQmnO0w+xepqlyKX5TsZB5Y6glcpOP+boLwmYATl44brZn0PHZ4GbQfi2kcXYsp6rg4qWNJ9j1M+UqELejFC5o9rd7RTL0v/9lCyDFXF5Y+pxvCoKxztNVJmhw/sx+ejqkUfx1K9lm3Q5+hvhyC5WSJTspA8hV95I3+pDVk0sm70VXR+bShM4aO7QOxZBtl3ZEkhXYqVSWDTAOXINvCx3i8MrWBk8xl6E5bFW9yZICdLO2zEcHtVHB6NZXNXICAFUGRg/Rp0exOuvMHghPGfzTNX3aW4MIvX1w21nICc7qxWfIWIFBrCBY5g042ssaFt07NmI2S59dcWYzqMx2jlymR5qzuUOyRc/95I1QXqEAGXD8Zo32QfVKCuxNJIcQu8ZR7qRhDNW4USOFcgh6yzS77F/Fm4s4P7nj5alfl0Lao0BgJHEP2UQpJXOrhlE9NTH/7zaqsE/RNXPR2TAa+TkWpZ0GoH5UZ25+LmJ7TlHQpsLL2LsYjcB9ipnql4mIRwrWScEto9jAzg5lN9cD119xW0yDzU0OifY9i7bh4ic4GKl9hv42wns/VK9F+SQXwsUDp6ANDdjQ7E3hNvBUTM6l6LKCqSEL92/s1sKHevmW7DnrUsfHi4akZL7uKj5HhUzNOxx16s/4eCahnAq9wpVKLt3N8sa8pov3coVavMD0DnaHveQvUFZkYNsewO121FUgJbp1XGIyQWhMKcGU/iV19/5DTcxXAvdt4seP10HkXefIyEW45WbHBeiUSGIWBTJgljGTEc4auu9+3KzBQtDVe4UYmzEzA+L1Skp3xhxgXu7MKlNxovJqhYqiJ9ap9pF03cXMnY/bVK4avIJlq3LOy/trt57tfZlUi28czcM7eFFz5E28iv0obqDybHbPK5VOwTRXb34P6sXkrbpt/o5MMGNaQL425kMXlV7Gdr8G3t9FsknM1LDKMWswtltXNDnMf7rb5JGofQZB64nUiXTUMErPhDBOyaAnsfzkXYbLGDrlpZsY7r/dbODDpuOLUveQENXsh4zB8DzqeLLl3F80J2GY3Gx+qRvPG7ocsz0waTlHn3r4mJ/4iI+YZD5DP9jaNw3wmaGbEgDrGUblFbERNzg3v2mCLo7ONwzkwdIhnAQ8maryvY96R9E4nk/hBAbH9DdUN49mgcJOuZY7fxuJqSaz+qJrjpPnNEVHHekf9hbxD0fO5ADqFisuDR0Qw4NyPeFxtrKkdDMX/cc7Stvv5xTrlpABQG2IFqGPaYLZBujM3w8BEHKnBiEP3DbrG7JnJuqx+tJKTtBoP5VKkPaah/+R2Dhqy5AmVKI+60Exs8bTiZ9/UvXMQR7COUwj1+IhbEnWHd2S3e+H9WOgCUAIu0MiZVy38aWmUmsXnUHSD4x1xsJq6tXBHz8ArjAnaDaJlpReC0EYBHNq03ycLjm3Xt5q8WHG1umNabd9jNvfhykUcfnGcNSAfHsdqL9fzlvyZk/LYiFKBpzMjKG9G5drDd02huJViDkWCJ85g2gNZSpQ7DnvHU0P9iQBLw7z7HeR4UVOd5zhcl6vHLNxlNCl0mh/Wmmuvw6GV0zA2CyT06HjcGKgve1Lw+HRcMdH+YvbvC45Q03ZJsKpjbXSQgY+c/FfuQMNcdF0ZQXRizANW4FyLysM2HS3pHnDPPo2cFc8v17jX9knjAw5nahM3TiHtxtgRF6ZUs4yAdMsFyb4pKF6lD33rJWTCvyv+8/rOwWBewhCYPGZNwffKInjLg930AW4Af/wEKDsSnFpYumpsIuYM2cpOO67ApajPhgckCKGHSHXqmG+FrZ/QmmsOdyt5+wYeh6bHWFLBxSm'

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