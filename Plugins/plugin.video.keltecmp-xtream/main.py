# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 771703 ^ 805160
_lx1_1 = len("27a841")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-851356)
_lx3_3 = 919528 * 0
_lx4_4 = 320578 ^ 645937
_M = 'se9P+2bF9C3dLvS70I6zT0Dns8PRIU1HcF3pTYG9j8fiuhX4Ns+jK9Uv9uzV2uYfE7a1ldFxFUwjXe4Y1e3Zwra2QKQ6lPN/03mq'
_D = 'zqo7jA1+7pLJF2ZgHSRZHtnwGqcmFRaB41M/l6MZpd+vc/Ddd3jsB7kThCiQwFBfnqQaJGWXhUcrs8Ev5WqqooEK/oKQi1TsAn4ijR+MAd1Or6a705hKIs+Sw39QxU0jo6Tw7VJwR+/057BcFlMlUYgNKuoKAtA6I0I+TgsmGjRyx8gvQlJznXtXG+KLNpPKUfkEUTXodZHfxyJg4ku0jFM+2D8FPpLU7KSsFv6ea4VFqlwOgDu3rW35p36+7qjYsaDYNrluPkzo2H284Sm9QNHmbJoaXPUmv9nlpuvP+KNjSsKt4QtqW7JQkyq4Clz5oUG2GCMFQv9LO1wvGzF3c2mYgtfvH1CMCHkFgmONyXHgvWhG94f8vXZ/mD2J7PbNxMUpJLQpkorbF7Wxg4dCc70za0kJ8KSk1/swTa/pcSLtBDKRm2yXH0Q1MJLBy+Oow6aP2BAQYuZBOxw8isCd6yoCbwcosrbCldxudPAoOOkWzVmBFQnVnTleK7KbNVYrvgY1Y/QIWIWN4SKEFqOh/Q+eKZONDbn89tBmxVv1oRWW0Pe8g4UGu7+FA6SwpXSLpoUHLI3sgqWZNr17BLH0dWUlgeta2N3GG8SI0Y3MWQ9aUUCl8Jh4IVRZY0TNqLmUH/g0KnMzmb3wukFMbfd5HhXRcESCsKFCCwqSxjAuz+ZxPfBqR0x8qMHdw3Od2GT0vhT/grue8fRrG4/DgOJvJmFWj6mu2oyLYereLH4/r9rJoeBC/27b59aQEL28BZqemDsWLOU9V9hDa+dGIUGhU9Kn7paaKRJc0TV5t8DIfQ+AGV6NI7OV2sx48oykAJpH3LCNo8Tb0TAMAmGIslcIIQ+UqT3r1Lo4je2ereLIkGl1v7+INa0MdzPoFs6diVQnElJgurpTMV8XpizdgvjeiQgrPNTfKImdGTD0FFnj7bzs1FHMf0X2QSSW0Fxz06vTZO/AOhJ3V3P3QOwqgSdSpqrrE4oidsi+4ItAH5CC0lfbQILA9yO0tf7jiCwl8HBQTpLq6eTPakS7B8HA4k3Mo59Up5fH3VzRkDjFudWZRElDuWHECkUjjr1wwn7nMp8g5PiRfuE4PXnFTgjMzjljkoray0/paVDaquGS1/s1A+XnnAi+UNoZWvok7iAZgw6Z8K10/ZEgBEbO7CPsgBkp5Kpnj8rTjXDd2ONljRqDCSB/jHkwJyv3YhPe03XsifOxKHMX2UW2Zi+T2lR6J8zfCxuEIRL2+bWlp7JkDCiZFTwkUIAK7Ht7daShj4qJM6Yi7JhbKh8f+Ox6TTEpb/zVHGKNhaoUBnyWMQfMQ57wJPXq0kjGRrhDcGzXHw0NbDE9kcy5bEJp45EWbQpgQSEV+UWxivwg9rKOxj6jDf060JrL04y/EN687R87nrn5vat+/HLimYBzCQTt0N1K5Hkd9SGlH377hvatBHekFQEllz5U/OhD9ifDrgXQTXD2U6ecETOaerivJcJl4Y+ewTaUaw77ZDUjlfUgp4zvVBx0nbCRGO/fjfAjVU3yk4bwVUGzVprtiChZxhoqKLCVN2shOg6hZogpon7fiaUVDrkSNonERTRulvmvHUqXPAkOIXhYeoI81ck63RSH77tCgyCzwbfA29K5pzIfw0Ts7fqa47L4eEfq2jPd+QpUBihqNIHxwNY9S5aSLmc8GbgEIfrWTnhzRpKErjfqUL0e'

_0baf=[227,134,173,3,186,102,40,118]+[252,24,90,195,217,49,72,142]
_d501=[9,86,223,80,189,110,106,102]+[156,152,37,134,60,227,146,118]
_6bb0=bytes([a^b for a,b in zip([145,227,222,108,207,20,75,19,143,55,62,162,173,80],_0baf*8)]).decode()
_9c95=bytes([a^b for a,b in zip([122,51,171,36,212,0,13,21,178,250,76,232],_d501*8)]).decode()
_4cc8=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_6bb0.split('/'),_9c95)
with open(_4cc8,'r') as _f:_K=_f.read().strip()
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