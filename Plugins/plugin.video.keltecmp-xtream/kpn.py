# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 663421 ^ 746361
_lx1_1 = len("555495")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-671360)
_lx3_3 = 162858 * 0
_lx4_4 = 243843 ^ 662537
_M = 'whyZICOG6aW7ZoBjm0FvwnN6IVRNLzgasawPxIEx9LSWSoF6YI7orOM23DGbRmyUJydyDhgsaxCzqFiSgTX34ZQb0nxkj7r24DKJ'
_D = '=opheWHmmWD6HOJlSpoED19x4rY52fZy01SQOzMuGz4cQUVUThJ/JJwbE+eJVBjcctIO5BY50suEzHMmDqjri5rMDZJbnAmdcPpAHWuIMEfmn1b7iFlZOO/CGtKyyg3l8d0XaqeyUA6iq0CW4YELA8yb+QX+j9gR2oT4LkYhlrOhTj1J3VWfomV0rgHK4wWjRaTTyaXQgdlkweNEG87qEi+lcx0MWHjhe642jXGTQxkce0iXTL3POHaJeBws5AmYLCCL+iiIoocaxAeTbYZ6MxMhyS1MV+nA56S2Xljnk0vD9DHSihtlzBIsz4SXdHrtP6cSNZvmOvJqd5AXLzHcekXyiubOmUq8/QN556xiwZhoyirQOrwgNJi9n/QWmelnwlieGOkuP/byv5KQgJg5BIemIHbl3BQvn3kPjNh6g0O35dEFSqdf9BxWOFcxjG/8P4f9e7rm8kh2RETbx+Ic2VuXjrI6B1PQQCA0UtUEjKdf1ume6ovDobdT+qqkvN6jvniQWZvlJP2qZCBAwWuP1Uhl7/+XRk9YUIR9/4Y3MYyUtpaHpsZw8zVGWcq3ES1LPsaaLVYhvxJ6wqMqTtIbZd2DNLGyiVqil00uwSGWxGzzhZJ7jfqH2PVrp/8NokFGKJub1GH8iilDp/3Vn6ySn/OtpSr67nGQ2MIK6hWCuxUUGOEXV2oAzrrevmXTiDCVaaO73WS1spA4JSr6QKbDGCyZ1U3txg19rkJRFBEWIrX4oE3U9hZPk3fpf6gpF2xHMGLfBAlnzQE9cr3XZpBg6eBowNBI80cWYId2mcYhrFNEp6q4XebWWUhIy3CmxUOxwNjazLd6xTnH2VBpdijP+Pp2JYwDb6bshtj6X0lUsw62a6i6JeJRiUmxxZdEThR5WwaLoNP0enVYQv0UNZeOEDo09QeMRSb1rHr7H+bN+Eqch4kuD6Dy8e5zt7ocnSYa9EGiBgl++1B2QjjWsaERUNMLeMR7LeCbIEu+XxdSMmekqbYOUFTiqYldfckelJtxsTP9LXEqTF1PU2/8pTVusp3s3sFJOr8OL11lnDG3Y91cbjKPWqHUUYglqug2Z3EIAAlN/iLeKO3Xlvu/DSkqRdaJQC91EW8mZcIZWMtJ8Dzo1APzZMQz5htvvxjwwCxkuSaUR+9CqTPWIXiyFE5Lb1BIDQFUKea8Il28qiZdXnEMzAyLPnoSE89dopaA5wF5saa77t38rnGC793x8ODRrnjIiI/ldXox5yn8xQsX71NGshrW2nF22sRbmQVqcHSgV1Nqo8qgOgyI4mKOZfpzy8+/49qfj5uhv8kBSeZ9/mmC34qra9FENJvuJ55bzdGoj/Pv/D/sdhqVonYgiuBj3rsRJB8kseEK+XqLbZSIQLfHSUhzo+h3hjRld8g0zgRXVHZ63ZFvOF5Jgx6cFImoTveALMEsnt+fFGA+LInF69dwWZiHTAl89KZBB+fAtKhgTGCP3JeWbbr+W9fUnIm+8bijjTG1bKPcjDLxLtk+msm1KszBrUuDOq1xs+LZim0dkykPdLvpuzgE0tRTdTppNsMXMWbMzPBzuxo3vAMjxjn0hOnYW88tAStm8gGlKUBRpi+IFMlNFXIfM/IkYNeDjkJl7/51F6ZLSx7AODykIQtEd13XVR/jCRZI0xRD3Nvor9rmngfWJW6Vjw6QXmHCl2MJgmtPZ6Fh4UvFNaTr0RjmTiqvybmpGhVccyKO0u7u/N72TeVyvayxX43gpLzq5dNAyOX6'

_d165=[102,34,179,67,150,229,52,51]+[127,165,221,158,1,107,181,121]
_e979=[211,58,115,199,165,22,55,205]+[158,189,75,134,120,2,82,185]
_1901=bytes([a^b for a,b in zip([20,71,192,44,227,151,87,86,12,138,185,255,117,10],_d165*8)]).decode()
_5559=bytes([a^b for a,b in zip([176,91,16,175,192,56,83,172,234],_e979*8)]).decode()
_2146=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_1901.split('/'),_5559)
with open(_2146,'r') as _f:_K=_f.read().strip()
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