# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 508321 ^ 567359
_lx1_1 = len("84117a")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-333409)
_lx3_3 = 260931 * 0
_lx4_4 = 155611 ^ 362342
_K = '6a9e72d763d6636eb4831970dfa7919bacffa381a083b343899e7cf6c6265489'
_M = 'uVVsKTe6AXRa2RrA+YgEWM4C5TTqNN2BcykEMCzNXT7oCyMyPedGN1HeFcD32VNal1jtNb1ihoQudAQxeMVbaOtWKjRitkZnUNoR'
_D = 'YSiuGJ1jf9jK4tqy29W+CtbA+ZDygjIdKaQv7vljjBPEZSvAYM5aHpA3ePHkCrr1ItGH+ZkeAmRQS5RA9UP2HV3FqXOzkagg0dkQoMGM9/BsJyRRIpjc6B4008RKDW/1qzQ51MCpmQLvWINBECdAnnGb+vyHxvJw03Qrbs8EqyhUFBNLohLIhFrwlPsO58pwGqPJEZ1JyIywdNNnzYpA2nVUtOtUqF/pPMYWQgDHd0nRovvtQlNDLbNQ5m2IjoHZzOgv5kyEVKGvE6B3zRNVC5ol+lcLSAsOk8i5LKCBkx+9rQNXIqEztyEe/o1VSSx+uacRW4mspznl0MbfUS6r7X5WicOgGkJZT3QysnHEp0hjDh46mXk0yPPrR5BWaePKjkmNLNKI8KCatvtaYPGu+2iM/AI5iMHfwsK+NvV5nPTjSGbCFe8PuWqJuZIrPW+dssZAENISWUTliBEvUKbZ/svk2ZO6Y0XlWI7bWMHxz5xqzgR+CAn6A4Xc+Z5eoHGpdosktF8izkPVrG6kABAR1n4wOKsjruOv/tjVIWrgf8OkbQI/qyWGRCxRaFo6l1u/kEvBsNCxZj9yaQoNLIIuxKUOicsxPtoUybCKbIiv7bCGjdbW8rKpwSao9xxZH+pwsSaL61BSqTrZ4U5oRRVD5D0WdwMgeMS+gQw+G8frgjQmTJcgIyOkikn4o+HZVy3YF5Zkqw3486lRccehv4r+iynHUmh2mCkcwmQFDinARd3siWJfbXaraAXO+Yn44TXL0RfrHGCOlDHvWEF/wgUd0f12rqeQCnaVZaBltUcmOeZWaXM5K7fokaHXBY+RW0eEjGt+mitYwU+LYwRpZeANMj8cWc7EQNImeA2PQ1y2WHs3eIN3rI/q4oo3sPeLXCNeKD0FO6CC7/c400TSxUBCCMlCWYtq7DupP6ywU9K8qHJlItLmQbuevFXsdnng/t+eRvuR4F+pDTvEE/WBPKahPufZ+jW4GS19ITUP0QZNnBJhvFMPMtmG7TvWixXamD2io8ImfZWnL46lnTSfyKLR5NAQzV/E221R3woZDhsY4OSlqRsMOPJr1EZbNgBKB7U8WD9ZMq4AGUS0aeaYdCPaObSBW88pSOyO0Rmy63ZcF2f2rrKe1l3jL+emHD0n2b1jvsnfKzglVtHxc8cLQdMJZgkfbtmtDHzfJgTClz/Z32/31vXlhH4Gxl8c86hnmBFkJXI6vBHoxQMFqsE/omSAH1u7EGHV/pimG/y0hyK5GP6hB44KcCGoWcf9wp12kt7JzS83zJNgqmwoMzbAJPNgNnaP8d4RFtarEkwC4LpNkT6lrCWH91vka1WKdUV3G/SGZTNQCK6qPPxaKjTxpAjCuGijcazBBe7xZ4XlbVVcS/ajFblHJuEw0lvU8L7SxMuk7IbLV9p+zAZuNmXyNNjqF/7gkD9MEnNe2breReaYTRrjGK4P5jwqixzNXtJ4UIvh8YXCbtvnM9xHdWirOAj94elq8l9UGnbOQ9RX3vEo/xQlbFtrkYZHb2RNeNW3Shf4ofuX+gnzgooDex9a+f70oPD9TSQoRbXtV1JB/+avNhwpgJUzUcXsmqVvAHiCuiV0EpYDtFfh72SxlkjPtpnOcamB4x9tCjHXWuHYYosfsG1cx4q1ARcVDrbJQDOt9SxNe6ngZbtAZoZmR28fTFo03yCYEz044osp0D3YU7lEmYBcARjxdtZykmKq/ru4dHRpVMRhAu7rGffVwvaE7hPCzVUcD8TS5lsw+p9h44PYBt9jmjNsLI+UGw4MoWSU26g238qEdfwnCfCqpEjotubEdbwy6PM6i1adGZqdYQISx3BFT1EUg1qMyHPAaTKv9ngyO0eDF1aL'

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