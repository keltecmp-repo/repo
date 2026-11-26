# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 513161 ^ 144431
_lx1_1 = len("541d7f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-589383)
_lx3_3 = 528507 * 0
_lx4_4 = 630551 ^ 118551
_K = 'f9992b8c8122da1e47fcbeaba99d60acdb5408b0345cf52a9c74c1e017319973'
_M = 'X0Tgyzq80qYyqw=='
_D = '=kPodUpM4DJZ0xTKuRpcvkKtpIAWHHQl7NGpAK5T+irfvO3ngfIqYMO70eaaAGlW6KD9q97HBASZZpo+x/ShjIheMIQwYynvoviInVQq9N+oaSm9aphgql/Lzml9BKMBGUTSTB2H6waI6Fb6Uh5BXKwu8gxIUNctq9kO0bb7ryxPq3qcaNhHkGbkueIsbFx1yhl0Tieyc+seOHy7GOAiUVoYFH6onrYRG/NOC9b5SRDJI3J8svoQvSWglcEb18PnyjtF9cIahaR3WMrn15UgwAb7Rt9jFFGR+U/GCXHnsoMiJUAuFrZQ95ndFW7v7tAKe9OS6LSmizwLC2L0Ce4jmh8Q3KVVpscOycx2XBhp5ygmjlloR0NOarIEWUNOSR5cxLUIebcM0O/D7lL38L/iPYYcuaivlsQ49VyGjUTmqjEvtWQGrtMe3V7Bto+hHHs11pFiSObZvhgUJpWt9SyHEAhQQ+laiOX87l3TR/JGw/B8OzQxKnXZU09zXipK2jxv9gyqxX+qSYwLzT+cOBVugYaY8F2LkPcYL7ibBLSngcRs9Zu/1Ax/RyZc3QyTIePwuaR1GgS2wyKVmvdr8fmbWyEjgij+bWE0NDv5YzT12FoW7lHlqLl4Wlrel5OvSFG2UkzZbUlgGZe4SDEbjQ8nlD/k25qYQ0F4IF9ayJZFRowQjdAytOBmL2Gr9vnEgL+Qcd1eSL/xY5OE0u1A+Ef8B67ocFX2N0PcKb2zkZO+Zz8RUirgiKkcEQOKHnOSYAJVw3NpYBGtyLWzb/rAsHOb2lCvvwbkCZebZvc8itcpwojKO1DAK/7oBMTwUg3tcMpdJsZ9XOZA/eJsqmr2Unypym160nf0j0ntteEyJGUBrCSm959F313NgimGsNF0k8V1A5uxGfhOlxQwKYvNrnlcGf2JvGOQLjAPLGzpyZJ+oevyr7zHI8lXHG5L1HgbR8cGVvzs3bEtIoT4SB1Cf5D3bivRBT02H8ETrttMFZDXXrGWuzEHlUFTs0VJcs4LY1XkekHETsmePMe7L/0HgrEVvgg7S389+8rjN3ZOfjtnJrjV/mQkEbqQMhJebUo3j86vi+00ZcftT2kq7Q2U7S+8CdCYGwQiCvHmwQNFOHLXZR1q2MG72VXUJqd/FiSIH+wAXnrNUzaAe0IZ1HauC5qbbtSG98kepSfoa3Qa+eP6wTsN8hFKFSu26X/1Qt5Ykgrf3O43PSP75fxY5s+2jKzubfNAXHQ0HpfvjE5SAE5hO5J3i4Q5YS+u2INe/jUphaVYKGDCXkflBRomqx0ebTp8Xho9njUhx5wvFTLRrACOP0rqxKNE0TCUNHIOgHCbqQoXhoq37QmD1jYRrB7aeTu4e0sa0yk9+iVNzMKk+68tX55NEkeqs2/050K8+LmbWNnAHlrqyWAJEz9MUNW5HBebiG+aCMZ37FsmR1dMAGPt/Fof2jJKu8d4USAu0/3V9hAFS8zMLDHGWdyRmowjxT+WwM4tUZ/MXfi9rHhAc8I9JcJstXBtZj6/DSVkf5VpIP0gU7fXPyF1Ys1kJwMSY4hH4PLtQDy8gCqh4nQWfk0VxbMkC7L4PZ9NibnEuNKAkYsMs6vihlGNJeK5VyMDkhrRiNvsiR4o3uoCQR0Ldpn9spDahIe6ImOf5Krf5UFK/I0Y7TFviGniMNFvUrmYgAGJPXNIgh1WcHSkn2S/nqz30/x0GxnaspdKFcChKUlPXLt6LYRL0l6pSI8u9gwUCsne5IkeI6VRbzSEI8XNWvubusno4EiKz0AV4feiweq9UB8fUJFwpxggyLLdEbVOI62ibrtSqpYtDZBvJe22cMd7IKf9PeWF'

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
