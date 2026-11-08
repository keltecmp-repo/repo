# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 713367 ^ 174496
_lx1_1 = len("8dcbf1")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-664219)
_lx3_3 = 117213 * 0
_lx4_4 = 614759 ^ 593132
_K = 'b8a5e8f08eded445340958ab94cdf4d5586642f1f12b711a116ac92032bbcc61'
_M = 'ktSMMPNgoSA8EJkRsuquT0ptYGEU6AivXiV9Cz3hAzyKn99suG70ez8VxxOyvfsbH2U2ZELsXPVeIHlTaOcOO9zD3z+4NfBwPhyR'
_D = '==QFKTCCtvFUimvsDJRje5Wb2q8XU3XZgI5AzHPEm6XVqWS2kYxXh9FwUbw2VytQ8w7YQAqDq1b4U9cCnwtckzoSqRbTUWvceJ8R/5P2eVhME/AAT9q3gAbfxR2YoYLgxqXVckurdGYfvjCqRNgH+UgJphKvH9HsZNG66b+RY5gNFj2w5BfnQApRS3sTRg8LjrT004cNHGl8ud2JrD1ftj4ia0OlCmaGPS3BspLn2Q1a21A02wVtda8oo5YPRMA1GQWK1xXL61dBMmb35lPFE6MxrxnKt+oKEnhxALGit3ncbPWOZqKxaLr4hJvhpWcEkUmz5FYmxPDsBqgQH1M41Iq42O3DR2/2MTHWOkIl4iy0jL+45p8AREa0dD48VD3pcY34hKak3LF85wxVnVbVSpNZ7ZjcAZT0pcQYoQ398TTlDREAytiy2EEFR/oIecCZYpnXsffSZdZ2CgvU2VyP/aq3bhKwO3aYif7xfZt8ASboB9eNqxp/lINHomI3lwhdQlFm8nXMT0ErV+Hq/KBb4ndHsy0JnEkjw/BwCDhJGZrY2jLL3Mkjons65I+RvbukBIoqPt9l10XYLtp1goq2n2k2gcdhaXr/QeVkrs1ykIHqDT6JOL86Edv1gDNw3I/FlAcdaxEsGTIFQDV3eESnzZ8YI/VUS0He74heY04iujSFqgfrkno3vrXP3ixGHWWFqKzx5pw8mt/N9MbEMGQFXQG3EKbZX8rOL/MLkObaV9elQzGg9EFOLd3BNvJWuv8bM7A2dOg66zVgPZ36N/k7zJB4IvbyxxzLfxPDjGhGH8dPf4AQM34w8whmrsPQm3F3s91yTtquVsosmCCeQJF2llHfB1hsw0+rnAlk4TWuBtxr6ez6C+cfNVN1Z3aJqVeiE7gtvrS0hx166pYO0gNNTZphw+DGBBrpwXBhPJYWeuRCEjm/Jqs9O0S1M68EivF9w3kvDi6MbfeFDvg9VVitRID+aJ3AuJJKEgTxabbw1hh7DtkucnF5xrEya6EaehkQHf/Xcu5XAmIrnc0/y78LueWK6v63lVcoFtaEZgNLvHZqQ0aqkN2W1jerIvlEGGndFzqrfkudYr3xOHl9fl61Rg9VQfBNtodbdLst9I2aKmjARLdTdcBpiY7xjnKwMO5zqJowvz1mna/rYH4FYUeflyBls3wqf/DmmBXcVKwEZ7XixNPZPUyfnClAREbpL1MwUIRwlPpi+6BpEtzpwr+pz3kG+xG6mFyjP+BnsSUtK78A/HrLUDl+9wIugS1Adi/+cgimKpHrybPGdfoyhVda6FMk9+aooMHELqX7QM21C4kOCXUzl4FPLTpN1PJrjBCkO0k+VuJfWAcPvcqMT9HfOWMfQv0eUCpCb987+2JrJQkOpqSZiRm8QPYrONCWpDwuPXs04FyBMBD7UZwnVKOIxPWckt7KbrfwpScmXR5LJX98iEWvKdTNK4KASyVX5DJ395saCIOTaRLAGFj/dK6/uAK+m+NwAg/JJJOYGbSwNHo9Fr80a31zFTeqq+idlkl2o7usziq0Xk7yO9D/3wwXujkzqyrW78Z9tRfYhpDVxiGAd9thP9FHjSb76wMWggkdE006eGmDQGyXW7PYiI+Rke90Y/CtZ46Id1NFy8P9bW3BTV60eNqgY7eW'

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