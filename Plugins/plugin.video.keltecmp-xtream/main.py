# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 706515 ^ 372800
_lx1_1 = len("db6f03")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-885891)
_lx3_3 = 925526 * 0
_lx4_4 = 810450 ^ 671073
_M = 'OyKJnNvUsiFJ02pa189aZ1mLU7Hzrl9olrfxKi8xuHU2NYnA2N28cBWEMw/fnlhvXtMFsfqjCT/G4PwtITbpezdgi8Lbi+52Eodp'
_D = '=sRwN17iqBiBe2T8jVhapHGLrET4RHADqhwqvGB3jKOZisEGwPvc/HG2bVMrae+2qMbGZsLrIym9hzCEww3qWb4I+MBtOn4ciy7wqfp0wbcZ78fb0j6DRywy+No8msaIn+EmOJW57rpfBL8t+zMkKEShUlfQhBJSyEZujfDUFMaSTlEAVcB9J3jMdWebKEeDcEgaCPulMBJnPLtwqcLgkIDLgMKeVad7JsLbC+fb/Hm7TjRUdyNOXqbwRQKPvv1KYpaRoQDelgOJ0Xx7Y6lUpS/FO29HbaVuPlfKK5FXySfEB6glcY0MP5Dhl5cFLwuXEJ+O6BY5xteJhwvGQQ+B9uG+ldVTpGZpDnlix3y4sZoVbx7m7n/IhN4JLEUpP1IFY9V6DGDaH1ISpiEF1g9HZuJ6K70Bcav0G4L+0TaX722bef/Qxshm3E+Y4MFT8cge2eA7Axh7cEtdLH9dvamotiFKUMY7TEEo2dAH9szpaiNb9Bbm41CwwDtnhysvHIIqS752MO7WfAFdVAeTnT1HJwqCkcT1sapRLZIDXXu9evWMvW6ba1L1Zi5HjwZNnoOPu7u9Sp7m6fsYaVbGbn5+MTJe7LMUSXTXkdk/6sbhj7JvhS/qaafIKQ+TCYs0GHcevdQaZ+VMfr4K5/4lSBrJtZzfFG/OB5s0J4+0C6BGnoI6L9clVRwWZprB+xvJ1qk5u/PV2lDSh98D76xY7KElhd8y2BTXgPH9NCwP7y0a4gKo/Nqm+xyMZj9/Xg5u5zS/GEN772CyWJ+Hgbbtna4PvHN9TSoL5gLUl/l2yre5khwHnFHdNERcrwsnI1u+/7ht34J7EPLVEbjScsXAXZN+ropWj5iGDduaa0WnrvQ5BN+HB/QnkaWY6Lvy26bPQvQiXPOqcUbbKMlRO2bd2zsLLto1S691JQb0nqvqyaOAiMIt0QhyIJ3BrZYBCIxyV2s+5UEhLRYaxX5OcZmzP/8Nv1MDX2b613tIeIGzql8XPJUz2b9VUoCXe3NJUWdf0Li6BrtruxUyIblNY1x2LTXTsJidyx9YLRSH0AwS92lTW0+LzZt9WpafM9nr2YO7N3SxK7exJsKCj9HqcctgVddOUDDtdHYNlD/G4KlA9kWvkFJDMh2mzteiVPZsJBIot+Ps5+i5yg1GU4JgA1vNTuhCWVqy1c40LcCNFknXhMVvecOY7ed0m40zLxhBY3ljO3g5unSbM0h9rAtJbS6c6Brp1nvNoKi665ZlY8o2Lpa2MrGeDCxndRhXko9CS46PsKw3j9B/PKl6mSoK1ur8Jt87mZwlhyp9Xb2PS/H1GnqmdyTH7FA60MQvCAmJp1w+0rFSawW1qs6f6PrKEchicnaDgkN1BN0JoTBeW5uJ7aIFwxaKHvRDQQmYTZWXRSxnh9zU7wgPsINYFAijmnfgLiCuEndYZBQJVHghMBQB5IaymuUFQPsH3zG7IbUF+xNZkVf/tJ98u4JDi5NtOHaea8nVUQFhPmVPU6W38m479sybmz5ncYHrIlmymSZt4SN8CU7/1J8n+u+BG7MA71uknmMtHcA3syxXFmAnkW9cEBrf4eWnSs917kKf1Xbc/v28SSasLMLJfGs/drRs+OyKE6EvYfJbZvDQ3KpNntSe3gmvatpEdA5mB5Y8/k02UdhqGjXsvOABJFUKoTkb8W+kua8IAdLs2ieXUc5MxvilWFmX+PjYYztKyiQ5'

_8f70=[252,148,6,47,50,36,143,91]+[111,153,138,92,252,71,171,111]
_8f64=[215,146,130,145,197,45,38,1]+[79,189,27,154,47,109,151,35]
_14b1=bytes([a^b for a,b in zip([142,241,117,64,71,86,236,62,28,182,238,61,136,38],_8f70*8)]).decode()
_fb9b=bytes([a^b for a,b in zip([164,247,246,229,172,67,65,114,97,223,114,244],_8f64*8)]).decode()
_d278=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_14b1.split('/'),_fb9b)
with open(_d278,'r') as _f:_K=_f.read().strip()
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