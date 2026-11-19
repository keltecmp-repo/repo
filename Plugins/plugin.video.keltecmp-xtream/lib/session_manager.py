# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 302587 ^ 738069
_lx1_1 = len("b91b7f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-889086)
_lx3_3 = 422001 * 0
_lx4_4 = 795878 ^ 425043
_K = 'b27afe965e2689eba1ddd9b85a746ee47538e42d85414a771f1f913fea521132'
_M = 'kh37tR7Z2x4M4kdTPj8oPCeKhPhhR37/cf6Om2JsR+HCF+GhH4DSGwLuHFRvaCA+INqPq2EWfqso+9mXMz8RtMQbtKZNhIofA+Ie'
_D = '==AzMTBba1ccMxEKyKEdRqCiGMfN6th+nCFuAPiO1HQmnPXFx7pQTprw8c3bSrgaXUxoN2ZdiBFZfsJylRND+xOgZKgWQohLdBA3Qn75Qn7Q6XgEhJtYR21EjsHOl7YdVpqBiSsA7+/vIPbd4ZM+IXJP/ds/pcn92lp87oQzunLhbM+memL1tWuUninCe1w03dwBhUt1BqlSQ5+btNrnEYWfAe3bRoQk67cuIeTnc1U7O2CbrNjSxdjgo8CKg9fjBu5geJCZ0pF/ozbEtfgZS6BKq5A93mcCqRs7yKXUmOYHHxllTDgCHnJjfVcn7TzuxfhUySAiOdkAWYpnaaFhgr8Df5ViodUxRdtQKaGH5N5a9tF4W4rNx1jdD+82AVxcg/FAvYn0mTAaF9mmQ1ehCm+ox5koyTrlloVlvId22Q0SVpl4tqTXPR1MHrd0F0ol2vaDmAWgq0rey9l10JKKPSBhjKMxcZFQiFXs0YKVqkiTg0/pNEg4jPgeEDnJkT6PsWPfRasGEP59nABhh5oToJ3peA5Y4uadV3UMHNsUOln/QFm90g6gvhW/FBQ8OofSuvq5ziLTgZSYigiyyUp+K4pLNqjqE4iPePbKWEMWJEr1GJxRHnyCNlB7fEqrj/H0DvPiT0KcBzCHk3++7uLr8Cb7OdZ1OK7NdyvHuhK0ZpRL+Q570skXgDWbH2rGDGqQhEwIy4USVVxul553u0AfpRKVwv994I3Z8h0F3s6Lom/ye9svyr1zdyDLeYMmbcISLsPRPclsA84Ft1D6+0rRLhscdE9+Cc4gaX2bCir5Yrds19+v1XBDFrTea7VJKU3olx7DLtfN+k7Ey57AL8RqQI87yIJSqYVrDoJMAq4Rfkr0uL4KT4Q90LRAeGhLz/7jaeDeqIW+58hCn5DR6QJbdhIJnX8FqGdMks7/gzJ1q7YHr1cmsO1r9KWbg+Nx6psQvaz64OdU4Jby7bEU9nH9wXbIWEBKcRtw9IxQlWX39nJPl2hvwZGrgdD5qvOlkMKu1U6nLFVSGhNq5Nn3XbMPBJSPpS/pI47BNsaALliFB5fI6k3sGwqX4YEPMrT4eXKTvZtraPooCBtF4U3MMYg/YK3hiuZyLsq7H/K0nHy1wvjO/EccmVuboUK1P6qnnMgKfg+FjntL3vT53NNGH5np4YyE5DHHhCJYb9KnpW6E9UilDD4jsqaZZbMSByBl0E6VePM5AHpkOcyOnVA9UEO3foK7Gg8811OIReOfPJNyLrnY4jmDRRoRsYnYPMf3pucZZ4RfuJqoE7utruW5+xy0TX1HOEjPTX8BZ5voifvSWoUXzlJtcHDGP9qhj1pFK3z621lbDllPdH1Cgw12fxYR+m9pwbEzRQEO+YZZFDA3aofX/E18ZRXuitDg4Vhj2sunhSawsW3bLrYYFYILZsjP5HS3H8oSulmqRBh7FB5giAL9ShtcUn1i8dYevNj1RFKKiGNJV1dsRya+WZMVdKYVinwreci/8JMKzD8eWh0fUL27AQyAHjfi0YaNR9ccDLSgJbAKMnSjZicHR+ASIQlKA/A8+lyFfku82idyFJZGFl8L8Idb7R5Z4wRZAmZ+oEzafBGv+HW0IyTHKwz9SN33JgtUU06lzaSkwqc4eMtu4PcDYKBdQem33qCW/v+oHSVTjc1Y2pRCcG2DIn7OQ/5mNf274taM5vnmP50fMqLxqW89Y4Smtw6D1LclRPyS0MisDzAuUnJq1kzMtwZbvAT7Gn08apgPy4MGkL3H+V+E5eciB+RV6Mnnzz8FtQbKY0g0B5m7AfRhogiTp4G/ggyVK1S2yErcIh7sPii0KvRqhc4FjVQ1KfEPgH+JR77yEeopInZpjQhuQFuEmgC5'

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