# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 662029 ^ 635868
_lx1_1 = len("fc1e10")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-855157)
_lx3_3 = 419200 * 0
_lx4_4 = 197690 ^ 969294
_K = '460debc6390fa0a3441eb30bfaf9d1d88d30331512c6ea0d4e66137132b623f4'
_M = 'dALibkY5wjtasv1Jej2LkRo9ZXvhOTFhMmsZgk4JCM00R/BsBi2UegKz8El6P4rHST4ycLBuNjJmaBnQS1RTmzJKoW9TKsd1BeH0'
_D = 'HHOCHgv0r3KMH/8aMyqWovSuKxiYD2kicAbe//8v8aizakUI5Mr/o2BWO7s3y5PsxntN4gBkvQp4o/BAwL1LWT3uivSNn+7NwPiJSN2F72lgymmX/LFcO0bYILu5/IxyYRU3iYaEvJdNU2C2YhzQcQw1d+AM35fJQbUvF/2bvi25u16JuxG+emChva+OpctDqJmlHTthsHvSyR2mywc2TDgdrYTVR3f8SeaBnxEii+88GbIf1NhLJHnw/R4wcMYE80wRZse64hAN5Pczqre3STbPGtgBAcRHTxUh+qzLhMJD2fkO2EGfaZNwAo9m4UM2lHljihIs+pddhMidXb35Tm+3emtZZ7Y4MorB8K1mwS81QRqvEXSOTLQCTtQA1cU8tGuGlW2HYNOu/Tc98y1tQJFDwfJdbXMdu6wPU7kd2RdnAM3rZCGGTzFYn2C+epE4L9PpH3B+EemfUAD5YyxDcEMANSDKQQ3FSMfdq/mUzQZTwo+FxooQ806cJrPALaFOXWha45WVM6kv1A8/htyCWBRb2TCcozXLUqyVi2V7wW5mPX7Q1dL4zi1Qh7nRDIG01oCkqoBeBvTHK+JBsQ/UAvj2v8hD9pTNvF7kwsbPioyg2QuFUYtHH+jjXM3GFRCojYSgTVfV0F4hLeEgot/fDLvsW1pvanIogjqsjCGanG5ecTbk2S3I6OGyDjRO40NCRpvgphPlnpcnfeVi7jfyfxPxFIcVFXI7XLpDv38v4u+kxTUB8n6XcwuAHE8gqy3p/xuF0rKTrmVtqZeAg11PjigLT8OKlrSDyCdVpRzRJ+yfq1TtlrXna6djZL0wjxQ4QJxsAvkx9/lZNYADxYArSVfn00jsLVz4byeAMng8DEquEy8pSZONbgs8pcW4Xa1Krz3a++MNxWivaGSMfj2zkH2mhBR5XJOzyyH4jdkauSRWsURUzoYdXpmp6frsoKtb+bAOy8kbV/4QQsH8Ef+g2+YGNfGSHVtMZOMWCcCgSbsiSqrsuMjQAPQR48UFmp5ZBE3z66idRQ2hzJJ6ltUF/+gNnexVdF3sKZHtAv91+Rs5NBdAknXGHE7Y9Efxg4nPNL8dwyEIvCclEhpF39htVNITP250VjyvnNsihtDgz47grQLV/9lrNbJ2Mw83+1ulPEfjhuh1R4JuOwXlzeN4PHZPLUusyr3wYMovBT9s+LWY6lgue65wapZsnMFHbThdFXu3L14DKOgN2pj80mj3AzXmngRbDQY6TVAxdI5rzkr47PGqRfDAoaZphvL4X3KRM1SzkRFMTEzACKXD5uqHGF2jn2Z5t7TTpfCqwRBdU7Sa1E3lbAl5S87JeP7SFFMrF2JH/wwPjUmjkTkHCAOyrSIJdW2WQ2Mp2kagzcFgyj4ZnmQCQvzPw5bP4Bk5P4B1aeDV005+kQ6mFvN4H9PDXiFvZ+AVxxdypINbERDAwXVjK22MogKS2gzxuQKMBe9LAY+wAlcVGtskryFzS7V3pnukU3Xypuv9bXaO+0UL3cIeuDH+Qpy+3vJryqc9dUueEM4Y36a9fled1kmUnbbyc67uvj48VjWCwzVWUxJrISKZ0MBwvlw1qNRePvLCW5UIzgi8CHkMFmaILajY4f1+nYvj4BPtyOfNSM6YwV+PAbxZ1L/mE6aVpw+TlMtFS07XiGMHG2YMsivsScV9Pm1BLDZmcfCHmeOPQ/jy+bMscLfrLARBtx38Tt4vWH+9C/TGcqAoXDxedLn+3LS+IkDT4JV+fgX6Cj3wGXBcQtwd9Yf5TMu8iN41ghhXA+RtfJ0el65IJE8Cy9bU2bSXxkCMk0R1cNr8vHxADXbcEGLnqAZR3uiE73nbtGNcETDd'

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