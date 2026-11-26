# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 351363 ^ 846932
_lx1_1 = len("899453")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-898543)
_lx3_3 = 533942 * 0
_lx4_4 = 663395 ^ 157407
_K = 'f423dc140755577c76395faa3d86d269488d5fbce591fbcd210165984e845761'
_M = 'vu+HKyIz3rpMkQ=='
_D = 'u8usXlKvneuTrXBEy9W726xUfc03ZFn8f2etNzerNWOtY729V4qulwUeLedJm3RCMTGK5qf5LuFWxrppNqogUVvN771vQpgGHpiTdLvwSp9FrMPMz7sZ/nOB0WgGz1SThegxbv3nj8Zgj++j8uZQKw7ti3EZBKeSCQnyXIfEYdAwxUSmh7oYLqCwQOl0x1klZ6hoSGBxnBoSXOL/ZFWrB/E+LygnyC2q82b8+pZOcT6SlhnE9TGHiAfI72VVHZq7a+wedKveYkTRzP7IiiM6VjT6fnsaX6vWd8a9zzPiNL8/b0krA96SQISuhUNVGys415Pe2WpoHSJ6dmJV+ssXhZTfc2PUdFHwqexvjkISU1JycMKqjfUF4+InrTVMIHR3k5Dg05cEzqLXXitA2EkoUUDvsYiKO4SJNtvKGSiB6G6HkrkISsMgG7ojgxzUMsDRIMQZMQXM2K+70hVMrmkkCBlxojimYdUzMCoBL7tsIwuI7x/QXdPi5upsEgB2dLoaHR4LCM2crVnMt7lFwjlOy50DFe38pQ06K26tO4kPh9Kkdk7w1p725NX50mu9q4Nrf408g4JONsdanLAk3vmf8kPofZMoahpCjp81A7kZn1hSyOMK5ys60aZJRMpofK4Fcse1Min5e2efUF+SfYPUbya49ucxO+EWckZjo3Lqbh5cOjGakNaDPSrHN7zrGCwjzKrzw2Yii1AoW3qshF7MBguWil2zB+nk6nDFn+0PD48N8tR7tZOjV8kPWZ8hzpVim1X/D74EZjZ2RdTFfVORsCLbS6xqWu1dgDqLbfiZKXM9YhSgd7f6udz/tMf5qfMIYAWKiCuSvzrjoAptA05hygfbQ89wsYbU0NcxbhMpG11XBjIkgaC1tSkPtQD99tdTWPAD5fhUoewqGnJ/pP33TwUaDDHlE8V2epbhI3/I7mULATNDT/KJiotXpzIp+HN6cx92E8wI0+wGWOSvesc2R/XAPH/TASY4N+Hdbbl/wdb0Tb8WW++066QUgF9ngW09zgnk/HMtfgOHPEbT202CvJyOYKsLE6U9poVvz1hMZJIiFqD5/A+8lEFbOi6PHgKAQMMWANusrH4NCvFG5Y87Xs42dCO0IrA6ZKQyosmBiAJapgOYievOb5u19BYxN8xUAtkLUfIwZ66keg49VhXfzgKOT2r6UH4phxpANE053CjPOyqcabJCFIw0YXoRY+prAmnqP8AiMzY896vzcRCVrKpu7eThm67VxE1lkUaMdX4kWx35TPUUbubiNlTRQy5uLhU6AAzaGHEoxMldLCS9vtu0+DBQySGoQhvZi89+DehSCYe2+qXktF5FAzRMnh7CGiCndPiNqjDkr+ADfnCtpbt0DGUsB9EbicPS0RtFmN2PHybZOLvp7Re6HaekoKZlnzY1EZ7MmefTU4h4PJ0UQJoan5UED/d7xQNgXpR8+lAfXZXFuNmvXUvVneGQ0wHdVthkidh3zyh5A/qW4WBbBof2Njj64AG3gdA7T/JmsJchSSABVKppNhUaZJ64vYXdRVN/w9dFmVrBCzwUlBOCf9fSor0BIwlV5dV396aMuMxP85H6bJADN/mmmD3x7ZF3GBjysFdwQR/0wyV0VE+DddMRMmw8c9yZYnncs1BKeEFNB3wF5+T+yQROHZLbcRTKHzOluraQFlbHFuMC0AlasJSnWcY7c3OBw5zQ+Z2RjIxWQfCgUCs95bMD2KJXe37FeeCqjMo9vOhoVN6xFoHXjywVwXki9pB2VOlErfh/dFBuWMbLMk6SVKBZT9puCsQhuX7MlGpUBqLGxPzRnIh22ngwvK7TFyYiqYXOsuIT5P0vyu2M'

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
