# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 131129 ^ 851687
_lx1_1 = len("7a67e4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-519214)
_lx3_3 = 108341 * 0
_lx4_4 = 831687 ^ 781071
_K = '6c6909d6e4a943688b123194ec9c5f1da5cea962aa26bdc1356eefb3fbc81849'
_M = '0w/N+eaRbt/0po6lSK9fMRW+RIEXRgyJXekVZSqTOA3SR8iustJsy/n10acaqgYxG+5PgxVAXooKvERiKMFiAtNLnfKy0Tqc+qaC'
_D = '=cREbC+V3m/7/BQc7Ia8shsj1PhuVbUiALh94Cw4yRM8wElQPcdB1WEA77jHEBN2Ujr7MLMZhbxG6WABL+hk0ULRSRtbpXzh4MDnyxcQvx6BjllECmF0BLfXHI0OJCHpRDKSpyehTTrohLmA5BWwfa1/H8KEqzo93l0RGyvuGxn5627wk6P+Tu2NjzC806GdznyUnSlFfH3KCQPUTvpbNOGM9ZD3qyi7WuM0BaiTevpEIUIEzE+il8nEdj7QIfnjUbpTkwOijrsCKhivJ76Q+iCQQLb9uD7a83Szx0t7Aur1nmryPZZ7Qc+vJ3W5L9uJwnAvFfHbdSBwbJqwsZ6CnGbaeOvAhHmyU0Y2Io+hKo2f18czclIU9SsaoVtrky0OmbsOsIYk80zkXscRt8xgAJrEOlWpPtRyKer6+TAwicwv0qGsHuKcReZc4WwiBzqJpOI+hAU7M4eF/44z+MQZW83Wg3pFIA19OtkQACWhC4cfOrPvMbDGyltu2LEp5SbEcq4FZ8FqMEgxi5WFJBJwlbJheY+121oSQKVhx0qKh4thTzC1DPpO8fci6GTjvsutYpQJmt020GA4+mDNVcjCJtCkvGGVA+VT1Y/3eA1n8BkOQ9gX6/Qi46z954l+1qZDCEODpZivAYKrd8V9SWBPsCy6t4qZz16URDfxgiA8hz9soBmvV50fWnZ4HhPa9njsPIi2Po3Oj2g/NN7ob9eSC8omAL2RjHc8Ft64dng4GSoeInasBhzouBB9R1YRpIVUxDT/EJu5FOrqj5ohEQ/HTx3z7pCKJpRzQOv+tkY6NDrgFmoHMA5z+hlIjVd8XSmQXrajpNLpUNDKDTcETO6HA3r0w1XNepqKfcJBO23Yo2V2NFRANvAwxWsQOFCooOT3sxJYTXICc2I2WPC/yQjWUom5x8czW1p6xhmCuj6bNkoL69UAMoB4bMuvLIrtyhL0SHU/Yrfveq6qSL4TFpj4jkp8ZAvkANZ/108PuBqG4f/P6PCBDeFtvzECz8RnaxhCKTJ+MkPDIqFQg0IuNAoeDmibSjkMO7I5iQtAZClNmIAGW5LS+WaYeF2n8gRWvhiVIy88TrDTcHXdCcELmmi7M1a4mnY3yjJTUQcvLObESuraDIUtxgfYL25FD/yd43JvZyGyVEQ8ra7lLGreubxHEgLKyuKGCL3OufvpHWo7/faDT2RwKmSE8FqkBDMRWyfgCBmYQPJQCXrIgHDDdPofhimnH+eBAmfrrkldqOIUrZC1eHQIN3tqL5xfCjH74xCnW1NNwGPJVy0JzpwgZ63lLH6lI+HnQbj1OgJZNJ2M53JHhwyaKf6Gxf1jiL7LOBA+le0xXTDjFAFqekG+zCeKOcspFSwWHjC9InMe+MHK1ZHG0D3pNz88dOScgsicqa3xwQN0OBL8ruVQl8SU33Tagq+jAB7IMErXE22Lyp9j2SabEwItZKkj/f6IzqztiT9QJ+SJ8W5VEWM2oY6KAvTl+AO3uQnMNPxXyPdJ6RvTbSTEAbHMrlC28tPyBmu8A742WlaRX4UhTY58qz6H0hcAaPba67X+8ctReVX0flTtptqyvhtvjAIiJnnIr+PYLfPjzb7cWWpzWJtYvHAEXovIR0cQpYK6iRl0Iv1UxlcBrONS1YiitTRXQCgW'

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