# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 181378 ^ 682113
_lx1_1 = len("dcf467")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-359372)
_lx3_3 = 222796 * 0
_lx4_4 = 659938 ^ 878156
_K = '1af88c086274ad9508992cb0062e2217a64cd2761e1726fdf7775a03d6d09c64'
_M = 'x2D4iO3HwJ+4iTKdWmBrnIBPcl5pHdgmD5wujQyz8aHVY/varpyVz+Hdbc5cNzibgExyUD0c2iQMnnDeD7P2oYEwrN//z8HJ4d88'
_D = 'iyhxcfRaHBsSzR3ozllqeegNqPgRYbXBiGT5JjLQ4O3C82JY4PWlAwvCUrXL72qh1jGJkBEPVIUxhfm/Zzf65X0CMWjG6ukvkzlSBt+9CTa0WG0Dm4rdpBQsTB0sXgRUho19Ewm1KniGRtG/xNPODV4Xbq1xE0e+yQzXc3Xg3RyLDWCO//lWgV2FfwFgJimjNaVoE+0MNOGcmLbIxLh1k3HY/vdkKs4mUlsoiy3Az0dQrNKVmMm7SE7BqlhtW3CEnAwOXDYBVHOqiq3AsqVaR/bhwlbTfzIhipUo+9wKPxLFstsBiyq6MKjv4XCcq3JCYLzRtEhvW6jX6C4RRr93NiFymt+tp2bEIhlyWKSNlzOrdmfScZ6i7j8CKZdB3bz58ArnHPOTINvaPQetShvC/bMo05Qb5g3EKVfXyf8TXF0K54R4Gkd1osIgle83qMGu6TVwuJTxHtC0Aae2ePQdbrC3WjIaw10OpUmJekfJ/xh362qadWrJuMvU2HryvlDkFcQorxcR/wp8ke1HN1DLCAVilZhzLuHg7NHH2Hx5WK+MOpfJG1vCbYg7kzE6l4i81o+zTR0vK3UEcpOcid8g8prhXSPh1UxdnWyPHDZfbja83KfpUBIZ69/T+NCHyK0Gb/FJV9f4sqv6qc4ZxXfxqkPAXFoc8qQgqRKI9msw69pWAQKGzJrBytEmCvXg2aXzQ3JNxa4eM9jiYfy2jyku/YgY65xjKoBEEZbyyOTPZb1V8E6pDL0JtEIxIS0Ehdw+k0R0oECDe0Ak2EQHMjUvP+NunmU8TYaSfoEFcnCcWNrcqK5BhgRBSFE6q+GjmNhZO+FlYbnUY1Tzmvxqf2wEO7DOwuqBJFMzeEvvCQeNF2xpVbSsIfYBAQDwU0fFO54zeWxrOV7PonsVVAZ1GehAkIJLZQ2FQcoT1rL/+Iz/xJ2Nv6HyY6RXzmPHaDQZ04emGPOTPf/UUZM9ss4YjHsa2t0HGplu4VwFhNh4XS2LqXFWZWjTPlcT/olJty+TFDfRMZoTeoOb3pkImff+qbO5N/Iq3BK/5dnbNJi+AM1gKS60hlsVST4Gzb7D2q/wvc4VkliEBkSAlJCbvH/Ci9r1aID/6chqflkZPcedQpc94EF7N9rnUn9QE8lkFOeLw118vPysHJdhi0fex6qU1xMhYzuxbn7L2nreeMFYnYZLI+clCRGIcCUjPjhxlne1+XAi2XD6/mc5UdWCOb+m8Ayi0aG7gdZK4YAc6yUHlKLI/zpwk7KVCEaOaqdLQTl3Cb1nMNOTbkU35ZsGjA6okzKX+rGijsYgM9LgJ9bJcHBcPVyA3PIVURA9K6sFlonRunlheA/F+eAx3Sy8VThbsZuXYM4cv1HoW9KXGPfqno/0Kk0u2ogZpjhNrvzpeSQCVa4mewHsRNFwmF9uZKqCMNd5x/hBeZ8DeJRF2B3K2i/5PSv6DvJ5w7brBx5rAopeOieBo/td5K686g1T/RPdBT/uexCcmf4n1dt8v1U4cCgn3NwRVYuEUEq72qK6sxVFe5f1XUsCSWYTmb+zoX2B0zVfYaJRznIwI2hzaOdwTT+8V4SueUup9GTLdkF2DCgKoKPXJfrg2Fiwasx8hHXb0TNBD4mdIhibh4kY5wWDc7vrrhHxiBxxAAjj+mRHGZMBZVuRlgUp7tqqOq0HD1e0gXs0zFIhgurBkyduwV9mx3PGlX/ckAYOjoQkwvpPYWVMHRUKcFAwnINNzJ8E0bi1bCoGnlfAe5Q3EgYjAyQnPu/Aibi55tfv2DL12PP7msCDJC5725k2FfjegtudBoV1kF57j+5yl6OibQnY8rpVMiLsaDj8'

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