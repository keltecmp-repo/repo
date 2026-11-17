# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 934910 ^ 173159
_lx1_1 = len("eec87b")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-420615)
_lx3_3 = 981474 * 0
_lx4_4 = 657314 ^ 248182
_K = 'ce24de3897d6c0d59e66096db54349b21d3e96e1d786d3f62e605225f1dc29d7'
_M = '8kN1FdixvfopWeFpbnu65ka+I3AkSQxOl9ykrbi2j0PjEH1Mh+S64HEN7Gg5LuW3R7J8d3AcBE/GiPGtverbF+MZL02G573hdg/i'
_D = '==gvDmo915A6ZYtp+9oUB8E/UBvtuZwiqU0ZxDhCTcOgsR5hCmGWtYlLvFDYcmhi/h386JyZ4dF/8yCOPIyJ+lAMImQhAiYnsjgafCJM1eaHccYQqnpLefP/bGVpiponJmAZsbA8Aqm1R16cowHDkfDa/O5qrepRRy3qbgP6hEYtIioEfIUT9iSmbXr+b15kYcE66YsJlc5Hcx8mFFXQcNvlUAa8+Mx8NPklxAThftwvN6EYKwi5yyISAtvv9pvIwMttHIjTi5Fhq/ReT9x7zSHEh+34Tq/FXQ0KacOFDVtNAluR+qUN2bkvxvv2FzlN83AbwzLU1hXB5DZfGYzL+89d6/8SFcCM0NdIEYJBfZHC4jR9QcdN+pnHw8QSSqWNyxvOvhW+899a4eSTEApdwMIafy+vniWNoF0VCQd5po0hXSizhrjpswyxsZ1qekVxIorfDSXuOLpxlA5sYZPt4NCMBSmOY/ssgLRupIK5+5mOvlNYq48CSBH0dI//DnPsqVeXDWTFyDgwHtmSaMkVyG6C27qBW5oBKIfdqwk6d6eWAjvoIU5Q9pCaopUhcjXs9W+u8jLlo3IQgbZRavQOMdUg2aSq+WYyVG9+faP/1BEcoISmDGeKf5QVJ6LqNk0GVkiX/HQ1szs86batDdcDXnvgc+4v6FfxJ/qWcHMWDV6VrQGE3Kgc/EPfg79tFQ4HA1hOlCsBYPVEN2yIxO714bg3p3gxjpiOLXzWvgYe26u9eFc6ybkxjJX7JFyprUP5RH+8uC5wvM1mGyoygrP9ej2M3K/EvvOaf7xoVNIT1k+CT95wGwzpG7UKo1KzbPZdlk0wMnttKhvTCYaSGUlNMSjWhUXrFQrniTl0TW1AIHPyu7YxK1y4x1rkbpX38WxRGIwQJVFAgXx8NWfHGnyg4SvNJVugod/TTmWStpukBXMndv9IDf12cKis1ei9PDNJRf4ervKfirboIJmUKvbPz7AbXtsgzlCiyrw7wL4daXJwaudTWZCWeADOnEA0miRjhiPGfrQlrp3Ti8WI8YVp3XiYY3QSUv2GC+XxE06ojaoeRwITSgYPPAdEh7S32Aw/3yd7AHVfd9MZa9Rt4bQN64JVUdUxDNQ+6rTYP51K3an0WcITdprk25ynyVnGngcbU3hKklh3f8jXRsEgDTXJhaFoPZ4GmlgN159e/tVJzPPP+6tnH2jy8squMWVIFLAlPQIk5xeYqXtziLqYcYRDuZuWPNjffS0eul8pYKtzWRy1C7jiqVgNOAu/45M8/7GPZjbsym+SgDznqfJ6m//nMruA8WMM5mLs90AyvjXF+5bTbF7h77jgr9xk2NQGbccCRBUY/xoBi7hFZWrvvhzNKjVHB5BaVC3swRr3yTkcLABYO82a8wLh26W8vZ7dAc+C+7scienHcdWJbOHcbGB4T9MBh4cRnRqhPSRXjMBB772bLzQJuE/R1FTMAP9gPA95DvXDHvTLx6qhhPNeVaX8LGAIg8x93LS7zY0dVdCGk6ounOc1C+iyRUjpip5O2zVw83FO6sZcCA4s+RGtAAxPVApdTNFLu551/ct/V+jh1XJRPQkNDUPCpMeikaKcxlFxgj7xQARSDGzyPCWJFqHpOQaj0mpUDtAS4tv8fqqkEIw0tFoUTInaB7YSisOiBuzh7Qjw1Xt0V1p+KJMbC4rT10xQ3B19rFGpzkkgCGAbxcIPyIoFnuDzgMqwkoBQ3q1hvr586KEC0eoAtS5QWuHeWe8soCGR9acDT3PJMrS5g6k11OnhM6BBl73eYUL+X7fZMd4HZvukkYyPFMzYSRSzrBEArLz5cuzMR4R2cjHX7WK5Tilo'

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