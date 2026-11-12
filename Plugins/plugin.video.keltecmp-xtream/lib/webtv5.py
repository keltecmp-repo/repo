# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 971312 ^ 362380
_lx1_1 = len("6eaac8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-132099)
_lx3_3 = 193890 * 0
_lx4_4 = 438769 ^ 483912
_K = '74d362c6b33a6623ba5f1eb7479043d027bfa352ccf13a12f93bbf3019d28c3b'
_M = 'O3V/gNCWuiWjh8GVsJrFbjj/nCcoBc+D9d68iliDK8MyKGnUwp28NPrRz8TmxJVsOPnIfClTmtjxjbeJUIAuwjJ5PNfBye1kq9bO'
_D = '==Q8IWEnWSta42Etag5IM38HhHC1vPF2qMlJ5hQ9JUi9SZ3hguICNuHjuNuydeNltqqmqrYTM+Q8QKf8RqgDj/sj4nXhA3VtjeNeCN3VA5aurZ6VLyD9Fj79EH3x+kEtQBYapVGwruRj9G0C4037QB6TgRdIKbz6vFxb6P6s6yaqnmeBSEIbAyvLN5EuvNyd0MbXfAIZ9uDC7XxSF+wK3TOghkNv7ambZf3WjNO8FsDkE1HWjsmg0cnwTXSCdVwP/4wYLChdAa/ybOcCMIQb4rAneVWTgzUz3ljt+n79jvIXbUph5Q3oZsGi4W3QQ+nTb+s6hIWsOIOSdS7pz1tyOQSaZVy8fGkZfquVhRukEBB+XfuMEkZqRqCXT7S82k69lJVZU6beznUCejqwYx7AfLZSvzl5dj+/8foQKN5lNW9ivXXNNCRFO1tz9R8Koi5bnlXkKKl0YJT/OF3D48rLxJ+OecYQFNX6qxQ0gg2OyrSHcZnelKinHWrBuI8ZJgC7kIy6urSkYG96HwtbZjamhuvSKQX7vI4xeYGeUvMeScm85Fy+agnB5lKbVmBESM7X6D0Ddh3PaUYF7shxBwjYHuimfZkW5tb8mJ/bN9oBBV12QcrK4HC06KKhzNd6LQQhWmin3FXjfvz1nEXzLJxv0kg5a5dIcu1/cS+S54bYfLc5e1ASaCvhvmKrXhA/iVwpbw5n4cRrsAKzp06djBpS3uhUsxStoHkqVo/BODmlnf1NWA/iG/XXLq90NdQaBoghO3VzsBWNpUN+MHT7DX1SOBLo9mlf0p3e2rJzugp8/4odg+JrP5Hgcq9RaXI+d9UhmYXLe0CX0yvRY1uoRcYo1BSyWdQ8mRXSTvGT2fUBlfUq1mOxS/S4qTQA9XpB948dhwOohZzOGW3iGzPqa0mhD/ZxxbUWNJppZgQIGNEgKIYEiGTrn6M+NAdTxX6EzBPTxn3voecVsbiZ01Fm59X3kdIahtr5CyEBznrwWhV761rGE00G1pBy7SuZiLEH/IAJGrI5+emDkclfjkGh13xk+QSz0Qu4KAvyoHRsuV42gYg9tNXzdeLnNvZw6enEywvdiuIPTST2iOi0Gt7qDjs5lioEYXzvT6MDnObnSDOrw/ZFiq1ELvnYh5Wu7XTMYgn5pB9w2SRy85WN4R4xDFPh8ZOdA+UW+O3QEkQ3oKnZ/toCbnca1/cUET/7MFnVEhCavQh7yTQTQrTD382BNnxfgsmgWe/nCWmotcrUEaMKMnfMNoL1TBwn1hKWzOcEzB1LzXKPQ4S7bYimugT0MqGMHKxQqdNOKo3eUpdTpJTUXzkp5mss71idotJZGFiHMzdyv6YuSYcqvEbUON2NymRTumr5Q0IshLucnJoq5uJ8BuJGyRuUHrba3+c1MSH24s9p35BIkN8/MZ8tu3TubVu7Q3NnTjfSajADXIAoMBq6x56O5EP4PXwSSoUb/rCruqVi305nFRTIu7Oe/H2Mzh7dz8MYft56d7/CXa8N6GzXw7SeJulFk+VQLqEWI71zdHC4X5ggNpfFIZbfvY/fYKs+VIbHDiiPoQXqdPJJ0tyrW6Gf9KVlXnZsHP5NyNru6ceWVss+4OwWFVEx5oGwp3anaQ4rxGVmDI/AxU2AUIzotDFsv/Kt5pDMkQBAPMUO0UgaVtxA23fFFjSC8fONuwbfcNcV/oFVBehlZHz7ygw5R9/+ktKq4K63G4W2WQlMah9l0NxO1T5BCgkhJBjowyRu8nAFbF/ueAL4HpLlyYpJNDHrsTXbL5EjBSyF28qz//6GnYF+hvut8Kxk1q6MXGv4TnSUheH5038PSOzI2xH7yFns1frfHUMPtoEs'

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