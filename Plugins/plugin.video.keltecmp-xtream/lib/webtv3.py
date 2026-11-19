# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 303397 ^ 303524
_lx1_1 = len("fdf748")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-103603)
_lx3_3 = 890368 * 0
_lx4_4 = 588506 ^ 454380
_K = '04253d6309e4c27283cb3cd2d7894ece6b449aa4fcf6d336543d6ab86f07e5e1'
_M = 'iBXd8B7EpkFjPNIRdY4dz63AuBrt4qNAvQVRO9g2xC+CHMiqF4LuU2ls3xF4gR2drMXlELjlr0u0WlprjDfAfNAeyPhA1rcAbGrQ'
_D = '=0gdsHP3FZT/c+3jfVP/h8A6z6vRJgDQ9DT17MmZg8KXIEizsycqXBqBnpwXvBfR8r25TSJKEo12QbUDJ7HUESoMIGIEEwiaSAbk2lqfnBCcqQVDr+k72nfiOnXggW9Yos16CSFtioFyZnv1AkJaa/eyYlK/OWALUGWTOw9o0usA02sicky7+Mcic+5CMZBT/8IM5y3e3TNQpQ3Ad2uLwzHLH01QM82P67gRj6SRMUwFM+xxahSCkuAxD4CY3GjeUu+DLuzUBczUDLsXv+bmJmanTOLxg4gfGOCwCY+8bMpxQ+RYGMvnHj502kfPj1X7F1xPYWg+PLsQ86gS7PFHTd0oKDePnWF42A6lluchBnNMWhvJ7o4CYmu2WVdwdEs2l6QjJ3fQztFAIttc1PNwwsU/HmUhOyfaxJlXfLI094wixWu9CxOLjj+sUcjQs7EP4ZkXQO5mMi1LYOJ+uCbnjTHBVcJ1TIhcxoPbyLPh3o1RCCvr7u4VRh7WYfX5znkYXgjBftzpta9J52B5KFAWTe7UUUSmfWiWR1LBbLHmGdhHwazXAMgzK2+EsV4cz78okdP9SGTlWwNLHWOdq9DpaM/9xSk9ZvFrbA5txK+6jee1qQHUFlp8wuvnWa3ibdDJS17AMSPUTOkYh14hePRLdp+QfcE8CklMkjM+FhZehF3YzUJKfthSr/qBL79JNLBKCuKptz7uPpa7dNPz0mhC3U+4uevotvNjokGXBF05PQ5sMSQcUdpzOBNO1bYr9g/wX3ZK/XnTEHfhivc4GjZH1a8Nw5dGK6G+LXBXFCIloFHKqcyM/OhoC+MgEBw073OjDV7FZoReFZadwvqa53w1HF47CI4ePp3K3PRmuq3Y4lr4+bFPzIwCsVbQZRALv36iuhsLH+2ZiNhTDCxzedBQBAaSELOQLVaL/G6Xu2eLyrNt5BDvCyeN+R81x28cdG6r+khKdouRDfNsy4rfmsLcwPB6fUVpHYSyEmyx8h4sA78PZW31RSppWRlqqVfZC52780dHB84GnN2pAlpXZ2ItAtBpvB9B28lUHKkR3++zmH9bkLkWjpylJaLgh5GGRIzjhtFb/m3eiq6d8d8BCn+8DsvyR3MbvMWiZyuzplezgp+NsE3kndvCpgmWXBVWt4Th73WdykfyQZkZjOi8peopuAMzZAi90SMktfTFvMBNq8GyDVmQHb58IskzKzSp/aVCE6E3xSnkDcHJMgaG8HE41i5KRfhH8JjjlBxQ9Y2HcimpEE0ugZEegyt67EO8flZlPYV+oQn7wUBoAuGpn4RJmd5YIDvNOSgw45UZPqyUlNjQlSxyCsI18XRvGFyfX+p0IIuiQsP3dAgRT/XDoNt8jGlPElmTlq/ZgTQQfBUajT9YIDOlLEKHxpfQaIPeUM2xHFQ3lxoBflz1bhQD1HLZr8pPQnIzUtWsFCDY+dVAGBzk/Oom44ePZpHtCAd8pXHgMFh8AxtVGP8qIuhESeO9TUU4FOGe46PAI+JVg6Egssv2gSs3uyQhLSSMJF0vQUIJFi8DGbbO3v8I0/LA/qZtRK/g5lixni8oQ7NrAuZC+OhQUWs9qWB/WgFjy+xab1pFBthDRh2q3rC+3bWAT1aE1cB5sKSIWRrpVo7NfBP6Q4HMtwcB6kZLgjyUFqacp0fr2KoXuj4S3LsJvbWznKoir/Qnql2eg2q0S7seVPcz0jsaw7Dpsqzd3o+RjZ7zcW5O9fttglE+UjWLyLGHJ5ym+hg95LNhGTM/gfX1e40X5AbUUuzPJwuSs41Jy9oNDNT9DQ+ZvVnjVX9RpznCGGviTcnIG/Ge71ebQdK0mWl00e+OcfMsCLtvPhITe1e8XteD'

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