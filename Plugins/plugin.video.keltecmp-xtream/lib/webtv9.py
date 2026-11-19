# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 614731 ^ 770113
_lx1_1 = len("6ceccb")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-726758)
_lx3_3 = 360139 * 0
_lx4_4 = 516875 ^ 848033
_K = 'cfa736f4da56eb5deec9ae891b4947c898a209ed3ef478fee4743968f5ccd1ab'
_M = 'lzmGPxbGwpfoDGI0gA5Y6seDJcLLHlmZKpzQPFHRakjJb4IyEonK1uMOYWSDXQrqxYZ4ys0RWs95ydQ/BN8+S5xs0jVBhcfd4QA5'
_D = 'SBdRcYWRqLzp0IB9qnIjrKnTTNKNkFasLH2g+8UjPTVw4xQNluDbzUlKBYPJjDWbTh7PHc8YjfuHIbO8EoOhd8Q0D81nzCQwk2F6xU4vYEECMRZa6oMuoWL23qRd8g2LxTQPBHr1srhG+xTQeAhyh/OpPv3z4H+HC2mLOHm4/3avhMv3zoLupBPoEg6o+EEhvFMJusRTDyPthzxPUbwewO3DhakGX8DkCIkmtPX6SViWM/9XMwi4wUfCOo+gPRFOWpLLyTav3FH1tbK1cxgIUXiZmgT63KhidnIEbcd1mT7K5mKrrOVJ+mNgV+tplQRxUv7Y65lJXPaeHcM6dPRfd0cHG/G5wnjf2X+XdVibEenQKN8Z5DHzSdTO4y3ubePIS4SILxH+/kpyCwKWksXHly4JaYrmUL6Aw7CRxEchVCiLnyQGx/AafFvxxmEh1dIxBxEZb8UTqPmVFEMftXDNv1jUSweAr11kC1Etd5Viea8ruRT9JX0mbp9t11+F90Ix3OxAgg3gWQMa8WyNtsvYm4pvVe8jXHPlrdKZlx5H/8tgkv3lfhL6kRxgrKQk/d4K5zcqv3nt7ns2tTx5os7yZ+U3TFDN+93+7N5Aitp5EH781OSSF1LrqUYeNZdzHW9U07RAl9qGfnkkiHq3vI5RJleMOS5SQn6UOzAQLOJue//CwhMaAaMxFT0h2oxeqf99J1b/NZUcBGkXmBz33iiq+gcOHlTwtIJr3r0kLAftyDh106mp4RhO19EjBh5GMOFwrTYVM5rWxLFZcE56P3ceX74Dorkpkxj6BPBWap6oL1oHtzmVN3Rmzy4Tpalp7lzu1dox3CnxNjh5jvXx+Ll4Qot1AdlSbBU4XfFEBh8SDDjScczenizo9h/AFekyhOaHDmyarWn3bf7FoMc0DNhUqQydeOYYCKht5qEZoVffvHbk8pjZ7z54b1zdE+TFAvRH+EVKr3o6tnzzjB3j9rmdIRLK1sm3BRHerU3XqpeRP/muBX1/7UD2L4+WC+5teRO1lO/yRXTOvpSqbr3MAEgzk+LZc3MC6RCzdhHTunj0a4EWg74MZSFg12mg/Bgg9ByuGA8H6qn5G3bQtRpEABEyNCbfrTGLzymIxhl+sXIo/bvehkOOsGA/Qt1tx1GyUfltaZYkgZQM670T84CFO09OUdpL6R7mkh51n4J1+6Z//XFa7jSF1JureFp8SvwEqVLWX6oiYTp1KbqHwH8XsSVHuBqde7RWAAYD4WMKcH3nQB7F8Gu7FKtERADIobSj5p4cv2dgB5vZlVCqoDCyvyvE6Q0P5za+VlASX5acpMvDQ92LnKALdDAHB60759LGgaZskiJOmFbjrPk44RvLlygxg1I2cpjUmvuQwMK/7iiqERqOybYyrAOqy00cj/5+pjTA27VrVdy4jeXGIpUZB9nF3YziIz2pPI+8TxgJpNphJgh+Wwoh/cfDuxGtSkFp6BpknQxkJkxwHhPOszIwQxA0T9M2rgPgLB4Jh20rPdTJ6ck94V57w1pn8+ElEtlEdWpdJX6eC6YvLRDVgHSyRBUbgXWgTpAmwx0FVt0E/jqb0frwHgPhmHQW05sIGbsdYxb7hYTXiI7TgQXrfNLVSRX+2MN9qIEOp5vMyICbMMJB7vCqIAWCuJVy43UIfD0lCO1CPvHsvyJYF1PxzndMZ5QK5ne6u6fQ6/MLvKJF3y5bX+WempNVOZIHW+kK1fGGnuDWTspHaCpRmJPcjWlTxCnFW68WvCVpTaP0grDFHIRMQeh05FL2GG5Umq7X7ye9YS+noKyujutgOV8jCo/FH+cVhQEH5hfgZudAkGFPK1PvSxgx47mBLeqEXUvxSSyY3ysn'

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