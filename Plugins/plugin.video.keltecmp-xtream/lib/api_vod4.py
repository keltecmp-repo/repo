# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 843718 ^ 441990
_lx1_1 = len("871bd8")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-995143)
_lx3_3 = 963167 * 0
_lx4_4 = 420083 ^ 702831
_K = '7881b3cbbfdcafcf6140b282b0fcfeb26619ef23f30556cb0c46e52203b5ddb8'
_M = 'G2O3WL20HKJVPw=='
_D = '==gEcna2xhncZZbLugUUeHR3yaUSGXmtdHisTIX0Q9/CGAv2idKEvQncpmVAjpdvtuG/BayqxEdFsa4s+X3qUZSR/Cy3duzVUAHKcy6q8SLWJgZVfSoOT2NQgOUtg7dnloD0wRsmeUftWL7p0klD8XL/7aYb19u+jd9sBY2A2CqluVRRAZSR4YKAGv1K0qqYFAyJoxeIOK57iqCziJNlP5rNBI0Ptq6nFf6pg61pfYc3mYHgBn7swCYhJDEa2u5GRm7fAfjol/pcvhPSwfdCXIl/ekWcz/+nwCJJ4MOj5RiNHrXoTE3I6jA2l6CVAngUuHPRkZIhqpNsjqPAsLqWGex/F4GJn4QSmIQqrLZ7tsI1PYVeyck7HaPlcgQlYsmd4qwfxmeyCE/JhClUmNLQFTuujEaPgvuD2vqyx/e5+TxaikfztVwixFHPLfwzU0aeQntNu2mjwRPV9GPHEvrBqoeNcSYxY6dZcH+Q6SuX7+qzGdYGmti3jZSONFjLoGFT2fs9NfKU2jn9HrNmTTtqPjhhrp8T3oKyfXUEQxHlQoqiccmgozyvQYM/36NP4Pw4jRWLuVS9RQTVXgU5G5E0ercc21yXMNsCkrJkLt0jxi6I5oPfBxHEnjIAw5HcfyWG66HHnV0f2eKg+Kdy24uBD5qLyxvwedlL18Vg/HMuKCEH3mWUYTyswuLshv4O0Jo6xtW5TF+oOhgUoivUqOayaT0fEWYeHbdtDR+1bUk/D+/25QBMTklMOTLAIspOugIqVQFkFmDCqZEkAu6k8/Mq0rtp1chx4LaVT9qbg9nK6TdVXk7nSTCCHQVOnJ60heG5dGabTFkMPqgh0TkRC+NXGo/aG2QrDFkK7GhP4lrWS+NkMdKx7BrCPcAWSw/47NHBM9qUoPmvXxEXoaf9BmGKdNKBvuF0aQDfZMYioU4Vg0TwnswjogiDUc96injyoWca9Prgc7plNmwPAdxW1vUsP4XGHPxnLsKb+JyoKYRvD7zfcChIk9XhL7F32u6VsMYcWQONgyCkgca6/IayLL5nqxUh4+A/rAUHj+FG6FWKxVushCUApt7C3pQ9hsPGOuvLGG2d58ubvepJsk2CFG7fHUZLJbtDPnDeO+U9HEXQEZTqJiKaZQDEGEbGIDpmvQJd6e0c1lIbzvaj12YVAjOpLXXq2QuMZKrswC4gKKyMGlfoxvKzFz6yRpnwN/nQ0/COPyOmvGEWEwCZ+vhm1z9nBBE4NKPIQq9pS5UiTtaKHULKqL9W+ixdHNLTp+CJ6TtOsJht+y6tMrYynMNGpqkjoDh0VJjPzJifmVjvRQweHu0IBC4KTOBsY7x167c63XTOqs8t8T9T2p7+v/rnWkN6f+qgPuy2dg+kRpw7XgIouPtoNrogNbGrbjQeIggh+7D/QkMu5jB5kC1nER2nFreAJGjAzKHJlPqFCT/9wLoFukFNVj2Mmaz1dMh4Kzc6rHW3y15sz2lv1Lmu1xIx3D2Z1KJZk0Aw2BEfA+2juLl0E5MuEnOXyabL6jA0Pmg54ywwxrj7XTGJtA4IpDPFM5pmA3jpTF2QJDjDAOAOaVg/sUKd5HdTBrpxyf1lPWetoC3wztmt4IleqSRDElVXe3wAeqAbqfMW19VGcsCW46etI+mO9L6FYzTJtcK+w0RSDrxSv3Tb/L3eV0P8+eUrr4r61bEa7A1Uc6RH7XjQQPF/yk5XhtmwpWYQLjvKXaUDtdnkRdq5Ceg49CDanN9rTrtVdCsjJBIzK+P3yHXxmKuzY3wZ7180mvtQ5RMOtAW72FtiB8WHbatpg1QWhIh1LRZI1Rn7UY/vqFNgcoZH'

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
