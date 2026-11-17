# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 373802 ^ 291545
_lx1_1 = len("80f65d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-541967)
_lx3_3 = 473544 * 0
_lx4_4 = 706282 ^ 676769
_K = '4630f04bbdaf3a898093f5d71ca182a266bc917f2a2b96b3c22ac39d4c101e84'
_M = 'BHgtm3YA+jnot8vm2O7Bdz7Ee6CHW6RK96sSXQ8pKqZWeW/WdUi6ZLThwbWK4sYia5Evo9Vboh35+xUMXyYtoFklb4l2Fu5g67LI'
_D = 'lP2LOvWdkl1NInkIsOKIBFMUEHg6o6Zc8vdBiuwLUUNSi47GgxuSLYPU9CXohh+w1SMPFSOl6kBLs9z2y351Hi6AtusEYDLrmaTTTRRi0GZsvsJWraSmIRa5Ox3dnZQU/TMHpImGM/GK0rluo0npOcgQjz3UuJ6i0kggDVegYAxu+K+cDbD8SxyeFN1z52dzP72YbSMAtND64jFISErG7gRq+LXx8Q0HoreC46C+32C1kyIbp6L/Fs/0FReyDn0HqWFdbsbhIllsrT7JwkfzbywhRfnU7UOSD4CYNbLSYdVC4G5NUVwhLQb+bJV1c2m677EHqMLZIydirpRghmLnC88Tv7tgl+FQ2sLGXTxsL6W5xq9lyed4tfaKpcXv/slkW0mFJM/Sbzm1XojsujF7QYLqJ0h6hueL0ySF11m2cnQTcMMk2y64RyCEW6qmFJYUpniTxJSi/Ec5VMt8YC9G5zMCnOveoWPydGNsv8MP669FXFooZnyIAxpIR/2rxb7xgL1DOptjNiHqjHZu6xa83me3JWK4zKUoM4X0uRnSydigy6NMiqx4jvkMTZS6WvItLA7YoIvI4+iR5fa9wiSgVYH8Do9tf1soNGV/AERpjcs6puaIKsofaZuUnWd1mvPG3sxv5w1GHijan1KNjVhi5J8wgwQRSKG+L/7Xe0Bh2cTTYgHWzrEi+30djjL1kMLGvczBq7vZYKYERI8jFMECpiWgSPniJh30bRT+mP7KjHto0coijp66n/5dfqOaepo3VBdXDcCifPxH6GFQ76U+YftOOSON0Do+NVB1jGW/Nbo5TjfGdcf8DAmze+4loNOTDvb2iLdQVRuqxrpSg9AZSr/A+DTK7asxHMcpqKXxq1Zp9dDJMfcH5xXv5nKbijodHxWTS/q/F8xbC/hG6xIanYPcyQilSxb7n4XUoU871m+uxOvNd0wKCFHXyBuxegHafP5jVCjB+jYAMmzpBhaqFcnuiG6WfQjV7CyMRHXXLC357jPnqjfdVtorv/7vvhJwzCNbQyvC6mllVsHwo1qDmzQQp0rJUredgodakZhwPcEYNbP3WzVaoyeEDzkxTEtSDZBBW7poNbtloFxIsasHIEUh9Ea+lNvCosVz5B0EcsXRmEn+vAN//nHALFBoLAEggBqMHCZfVqBo7JWF/OEIVT511AhS5vDG2K3TUoe5i3QES6BfbNzF1OLS1J3kT2PTzPtdhuFC33AMosNXEuFe87tDI5kB8Qh1FVJoNGOpLsYeAo2rFYHU/8R6phG/sDzfyJTygBWlx1VM1garysuXh/rao0BhvLCuKp1gM09IWd8+bJSc0fyZSFgNNt0QefK/DEziTl5z/SI30c5l7WHX+Ph7XzVESFNgw/1rDPYblMJ6+25sBC7O8Y50ndLr2CORRAgkuA3HEc79gE/r16dGYKD9wI6eIXFX0Uf92mFqXuN4tA8DmFt3P6ua9fXfUPgZ3VWIGz38iaBZLsLSzHCpBiBnn5SontBTYz2wj+sIAa9dmY27i4f+ZC4w45MQB+HDD7aJNLekeSEQC0l8LGrvuRneR/4uDIvwlatwPSdZYrAikbhmaN8we3AmKKZBd7OgDGauy6BQ0Buafv3/JjVSn3V972HYv/AWUZu44+QBu9omBUewzc+N8Ee4Gcfh/SGsxNn6xpBoLV/bpCi8dC7QOzOJKJiSPXHQOq7TW1CJxK0HNV9kqqTPEnmJEDcaCYbwZ2YEhm/Zs8Fzd9DFw9S/UV54P2gCTSdpGE+9p6xBFVJtkOstTZEA3IN5i0mI5E+B5+vAx524zy6IcfUYcsdsoi+RqFkKZraHqJhIoFSbS0qLC6m8ZqW0'

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