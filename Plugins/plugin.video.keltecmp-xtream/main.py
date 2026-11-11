# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 276407 ^ 138995
_lx1_1 = len("3aaa34")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-102962)
_lx3_3 = 301706 * 0
_lx4_4 = 332989 ^ 323961
_M = 'AZz8V0tConoFIB85pEDeYPIA0qKTDfsrSd0mvEQk3c4AnKhdRgS2KQ4nRjvzQN9g8wSHpMZarSwZgCK/QSfew1PNrQ8TBeEuXXAS'
_D = '==AkX2h5gmThZ6qEwupaCHUFpAFRwsVIPMf9x4ThYYWrAfWxjS6ZrsdAOpiVmvm1Vm+9XqQYHzGFFHgutL6hraIPVHPQzDCw8R51X9Nwe4dy5RAzQFLg8wrAWZ9Sa7fnCriusqOI6Ovob5CatnGhdb6UxfwrQng9mmmqDcJ8fzEuH2C5doXRbVa9BBlaYgiJmwC9UWCbnz2AKqrUhx5qw0WXo5xh/lb1r2uBEEefe/OzTwRXBCBHijQAsYDhP/Zccn7nM3AQ7Ai4lI44jQe7c67NT5TG0+JP71GaPiOCYpOBw45vNpkbksWBNXeZkyg1Yb1NfBd6WjEcuSStpcrsx3P9eGkhfu2Cj0tRClqa0yN2WqgfJnKY60H3rHyC09NEs6fWrUzNuYvaYef8zh+6tCOy8XYgh1ot2s9RXOruoC8Z/HsJz5vC+AhdVfno+b/a0S0h6QRi9W8jVd7AXLSMf79F9oa1w1LeiA3nExiAzCv/yDSmzw/TlkAC4DrzuvbxkMuAjEvdwR3esQ9KDWwadw7R48NmB9Y7Hw54a0SwqlEaLqbZvNRf0VGCs2HMvGDq6jGl6VtTYFmQyewtq8eKyoMSRybpj5aEa4o5Zy47537VUDlt7+Dlpej7336ZdXcD/7XEBBp/GElppXoy9F2ESo0Vf9nRhQw7mGWNG8B6OteKitdx4dpZCYbDn6LWPJoyi4fbYfefwMMNK63zb40wngBwTxicNLlZjFB1vBpTdsiquFKYBgsOnPsgxGDRBUokLqmraqleGyvxD22rWCf2wHZ9VjgmYiInI2Ez94bRr/7zfua4wiq60iKlD/JS1v7DtPfuKX9L2u0U5SoNM/imJQ+4Zx0zey0WHvQLUm3Gxvc/1zR/VNUCjJYdhm7UKBirhICmqhhD609jDnbWZ2zlcMULIM0qwOQ/4F1mRqJfTvzfCeM5xjRVdW/VEJA3X2otREnZdJoc5tHulPnWOsCIT5jNSinfE7KKwk1KlDH+QVPz4LnAdokLyBs1UUxo8iEyiydNhY8GegtxMgrBH0LX+j8yXEaFxT32x5dZMy8x/QZI47GE9jI3YmFNFXOMAQEuKSxj6lFVZVbs27+HXa2CgBYFkrai96sg8iuP4XSY8CJDXBKMwCEy+kYEf/v/XU6A2jnNUKG7CIWCmMD70P6WjUv4WePmaJuCdQgFPp+CMnwmzZpJG3TeQgCjA6B6MSe2lL8YIc6SfT9H1BzocSVSbwKBDbtTFhPvVnv94TdaSZKJEyr44YqAGGIe0FEayS8vpM3s1PSq4ncRGepgF5YDoscwkHBFdYn/fUirSJ2vVM4dKBJgpAlv3aa45dPIA7fqlEOFYfK0xaiAk1o08qH34GZPqEBTQj9faUWy9gddrQRwI+qElM382Bm5I+0E9pIpR0yQpX57NGXtPH00SCnbReEbWABucjpdazuTxjka//nzPuZw1isqQqaf6NgTUjx/azqnoTYPvnpM8jhhLiT3VPqIR7NtzOWwanJtkdfG6DlzWApjGlOGpP1XzznQZALVZRltCi7Gr5ZNaLgJB+kJpiy5pUtyTtKC1QPo940Gmi2SBeM8l2NZsJ7w/qldQnl1qOvPB5+ORsuab2USGVnCDv44cKlW9+Otz6f7ck93BE+uFzODTJnY8+Gw'

_38db=[67,192,236,113,184,152,235,204]+[86,240,233,137,162,154,44,203]
_0ae1=[146,88,145,244,153,66,214,181]+[20,93,142,39,158,94,202,15]
_fcc3=bytes([a^b for a,b in zip([49,165,159,30,205,234,136,169,37,223,141,232,214,251],_38db*8)]).decode()
_ae0b=bytes([a^b for a,b in zip([225,61,229,128,240,44,177,198,58,63,231,73],_0ae1*8)]).decode()
_07ed=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_fcc3.split('/'),_ae0b)
with open(_07ed,'r') as _f:_K=_f.read().strip()
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