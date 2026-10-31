# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 213750 ^ 629239
_lx1_1 = len("cd3bc0")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-733009)
_lx3_3 = 927168 * 0
_lx4_4 = 236301 ^ 273577
_K = '03f4081f250315ae457cd776d49c0caacc853f18a2060f39be562a19cecc77ef'
_M = '5SRdQTpPKsZezE1hwGLtjq0/3J1kmFowOpzz0jfa9ofpbgpONF5llAabQGyUMriCoGOJyGXLCG0+maaDNdb+0O5lUR5rXmWRAp0U'
_D = 'eeS4ZPvgmxzLZgITTfEbDKTpK4CMSkNXeq9ejXTBu0zyQrq5Y9BHbhC6FkWrslHtVoYTKz1hYbBV55cMS+qR9dofY3Ay6ax6bZIaZwobiimAF9EHr59qSqkCqQ1twRGKjuPNFu+bd4DN8Vz7b1CwC0iA6ECSBf8bsajxm3ZQQzQ+YKmMJucX08Ba7PGYDXVjPlDeiqhk3U714MkZqT/utaqD0GRNdCScJUBK1d1YSi9vOh4cLtLycOAxEwbMLQMXwuVs56g2ef36dZLKwsCZCfag00GdV77Y1FPCB0Fv2otK/Llb8g9EtTlJ8h6LPqdMUTEUCrclB3NiEGZVAsL2gnfj8JSPbzTOVwi3JINYGcEbzG5RpCTFzn4HQSA0mHpOg1OwoDqAzo7+tXsCrPP4pJyrKrBKehgxa6OK7IFDu2GY23dHtbSY0+A95yOa1+Om5/5XXJtM6mYoYi0Fgq6e587jzJnwMEWH/u6Z8Eng+7lymjut+bAQV+OqOojfW86uKK0NpYuiTmzwwYJ4+HwzUW/N7PYihmcwFOAznTRjNFRnvz4b+yse3wrWUNp0ibSQbsOB5tEQ1lg1g+op1KSqjDrscLqKXDFjMzDSs7pH2mk8g5mcQwnDW8Du1a2289ONEDV8407ZmvBqSCjoWQN+LgiU26kQUNqGxw2C6CKqv+8oUeacBxUxjlCNt0VmgEOvfdoEDnzkLplS9XE4cxmjToHtnn456uyUxTgTFm2NyTAexMeo7/tLcRpvvklFZzu5v5CrqE8YbXYnzOHtpH1YX+eS9SIZszC2ciSL7y4eH2puo8JLh+JmqnNNucHQMFvrb3z7X9947ak+aauwQAkiRK8aPlE9MKAIaiRFF/bdZCHr/l0+ksO56pIzNgolohkvNY64R3R+jXX8fGyMrlDg6dVcwN9TuRbWDy28oabWbieKmCqFzixMivDuhQTIPXKCXX25y2RoBIY3176IhL5ljNWly4hg3gNHXrKL+7Aqlijr31C3nfYirkRkDUa8OMvWz1uFwBFLTdA1xFX9wfBh9HTnfTWbz3nLBxgrnY7m4IP1vqAS94dWYDf3ANtF+LnmXfsdj40e8DpjWMpJVKT6hWE4Z9sZoEiYEMgnDOYbOFeNMQPIaKmD/tPTnyQMcYiAsa/uSSGlNMBpAebZ23mBtSav5DG4ZP8h8+g0YrUMuvM13RCBXx3Vfm8j6uZOcu8ErlCtN5KJZC4qDJITp0L277DeDTg9ZBJUIaAJZqPZWu9PWXjEVNDCU7pIMPBNamSh7rqGPzs26YS8BraCq0fSsC7BvQJSCXYgngmB05wgptFXJ6SCd4/uZiwSNI1J4sDvcH6khP4aZ9nL6p/SvE80tqZuX/cr5SxExpa8Zo8/cROaDIW8XhSl3QYDqMTxl43xg3l0j7FhZcoY4ijOCaVZTXX+q8Av6NCq+9UvRDpAovHqcgqTAAtmH40aP+jN0GLc8LW1wS9J8BBwl284bh4w8RkiP24NgrvyW1pEi8qtDXCRYWA7g+oNWCR56LsEkR48iSu9QZUTmOOUznku0o69wMm1l+Bci2CZymcMQA6tLiDMd+jgt14hI/c7YvLT0mGb4ykkDRUyIQGORPy+qcTvWepWmj8TdWmOERpFXwyZFN/LeKPLeKwJ'

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