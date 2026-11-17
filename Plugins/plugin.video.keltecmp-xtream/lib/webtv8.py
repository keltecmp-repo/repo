# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 281763 ^ 584240
_lx1_1 = len("c124af")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-965517)
_lx3_3 = 735666 * 0
_lx4_4 = 169044 ^ 469965
_K = '15616ae4ba7180a0da2daf34ab849e9360a249f42de6f19bfb9ca15ac446cae8'
_M = 'dn2qVo6qOzSTPtGJE7LOGb9dm8N2ex0WRKBGqv2+iINjbqAI3KV5aJ0/3NlAv5RKvVvIwXV4F0FF+xP2++vf3DU7+liPoS9jkDPS'
_D = '==gwiiHQ0pXvHtRvdYzqJacpniHlulDwQydW48ygaeDp+zaolspa/JRokML6JbJ/CgFFm9uRpSXv84jWUgX2jl6pGTo/luIsUq7FiBdK5s5WXlDBi02EbV+dt4s5wgmUuki65Z0sxzmeb52WS7IHJxjsg53DZ2d2BorKpVItGWJWcqhdfCT+tu/Hoir3+HUxw8+Fz1feoQMcpSCdmKcQWNfCppLqL1nSWbog5fg6Ae069zPF97RbTt9D6n238g5GQ2HhFcY1zOPfLEPufAbED0Vr5piYaPJLtKkxmx1G7HkbFbuEjLuQImrRdjNDEIFkA1YaDlEbih/RtsgGZsW5HasWXEQF5scq2781ogmGKQMe4ZZhsWMf90OthYKbyhvGhz3foztq9hUEu8Z5qv4z2sk+I/hyHmqzj/D7BJjai0s0rWZH1AXbqZWXfIeccbenSBxovFqbz4Bn59Lar0E4bOueQKMxFb9sYEvwwo1FUAZWYD4tevXOOeq+gEz11gIxtwCQiKT0JnvA2/dI4R2Azb5inlSi24T7Ut29L1lAnp7MP+usm40GTwiRH9n7dycpdeGG16O4tXoGj6EDHUJcsyFahjIDHJc+cdCJvB4kUCUNiC2PbW20MKzfRnuyi68qblWz8lnIYLBPY2wi+Rg2iAN3bd/1tYAhFxlhUBepq9RhtekBqHKFc5lK4GW5odxjDIqFMj3lbkAy26xj69CmN5N388hQK4YJm/JTt9919UE+JUe/zF61YIk+s8/I8UfmSAWADEcFADzcSda6bHdyRIXPpCJRVSL9sWgzYJwYhr8uf/yVK7CkyYhMc0GAbjuUguWh41gnHfC147HJuv+kj/LkoqhtYVd5Cfs+WLp6+IrjHVa6UB7n0WW4UkNgLMTmTZXGVQX7uPD37g3EV/LF4v5ygxiKAIujy1h7pPmTACzTktOvj3zL8qQke/rwPnRdFAS+2fKAsCbh2fQ507UzSsjoz7HNsyJKspznQetybPZksaooz4yal5VSKn7BxNxIrTvqOHrZbjX/Cr4uy00aD6fnNDDlElVr71NrjpyIPP7ZxXlA995fXAgDpATi1FmzX5TmULlIibAiYQne4TPOHaW05IKEMtutiHpM2q4A0iDQ1qfRxoXiJQhY4TYvAUqSSeV0KVzmL0wt7PWUf+HkSaFZtSwuOcXyzviMDT6FmN1hHN7NR1c2RcLJjZkxP1TdFKdUp/7JoI14MxqDcvMad+pGKGOvWnykKN0EDItpUrkSWwrNllvJIY3wIlDawzMVfknqaJQMLmHOAhZ4GmAwCCE8BbON1VdzaNikWEdSvh6MHSpkOLqnGPIwzleS79afvrAWfriqKQ5RKkoeDMFZnxKfpEVLKAA9EhfrcEq6xpe2BOtUMMCZO3pQIkIeSbkmlXbzPQtk1W/d6UT04cSuwN7tfEIzudmO9PnJdDEDoOIJsiDeVbdK+sHFTJkjE9PAc3ui4ELVcmNBQdVI0PAAswDMokxHdRf2/Gf2ZSV06nUecoNUTmfPSdjMTUnRiLhQ7d0SSq8eLdOqdyurbidV1QeNn3EYmdny1tWMuIiLI2WAjxNW9bJa7VplUwiuYVrL5CzhIMjpcpVAxWFzLNtyZpx6SWih3ZGwfdFexbsusDTZHJBErmJedkBVg54HtJSSmoo135WgpY4/hJN2xXTvbIM7+pbxTyub6VkR494+tUvhiIz24ImzUEUEd3mpwxgpbHAsPdL4CIANvuveJlCkm3cSISnu4GQB5NTV8UO4szbQ3qxqvNRo83vZ5SbFacsar5S22pTce7hmHWle9xfWKmzOyLngTumeg7pBX5BZzd7kmUYqUq9uCmjDrLZhQVK/'

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