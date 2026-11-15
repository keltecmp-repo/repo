# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 162623 ^ 728762
_lx1_1 = len("ed921e")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-277669)
_lx3_3 = 727945 * 0
_lx4_4 = 570994 ^ 832432
_K = 'ffc98fe6da42644399d63586e3ca6ac52c3dd28bccac2c901fb2a5c0f959b7bd'
_M = 'ezEnWSioPQuyb7H5FqlPZNQiAeLRPuUrgHv7CbeoQ146KncdYahtVO1iu/hAqBo41HhV4YhisX/XeKkN4qQTDz8tcx1l+TwB7jm5'
_D = '==wTLjs8MjEkQDWMRNQtF/8z9QQEvtaMUxhEcW1FEM+JdN3bcUQpV3eBzv2tHNzX4BbT6UN2bs9vQ4PE79p6/FEphVdITlfTAQzrsaw+x6w+z6p9AXK0RHPu0WBEz08gKretPMFPhL3rgX3JziMFQNTsxrI3VIafHQHyOMcT2LzFyBZKjX2KqaYNTif+lwQQ7Fkk9ikdmCB1cPKAa0x0HM52Iq2i4fD5WzZdy1QlZXdMlaHxaJWTLjtTdJX7Qc0OgWsE+H0ZdCsgEL79EGbb4AeGZOnEIKljHqrkhZPZgXFDTq0CUBmenit6fPT65OU3qXsuV8CLAltp7/d6sextFChoOdP37o8WojYtq8WzMCAoyDgmf1Fqr3ICWVA3GgvZFVvn0gsdp1dDUQ52REV3R20TM+KJLuqNhNGlrtCw5zUxsfo1iMyLF6w0h6cNn4+qdjD+Dcic6Ss/1F/D1Y5BbGdQr4dXI1s4pGRX1QYtZ+ut9zQgumNBZ+0Mmt1208sZaxuaKlY5hXXOVaGt/303qqz4CmICSlQnbSjcL49XO8rIFZBXeHBjCM35mvPvXxxB7/C3HppjJcvjppL9fwNqplfF2seTRJfzXjhBHtKXoZr7coAUHdfI5OLu4IIMqVbKoV8b0jv0GdQZgMANxHcm1KaaqUmVxNj3MYZj4+nrFIL2nVqGPGqPJKaY0tw2Xb4vtQhyiiDhTU1TFPp70/Q9MK1sPtNfqAkAKyBsjVSoskwCini6m1pwuRtKpWkXvXcisOqtM+zopFjHhonzhTdj1hxLRQXVkE0jyYxjPtN1OmnGBOWINpzE9K1hTS9S/nfwYFIWOZyipS9a9DhOwR2syjNo3X9twOHyhs937MggxO21jbNNzJcn1kYBJ2UkK3JkccVQDona1dj53Yg4pcbB+x/oZxQnr/gZfhi/u6vo0iZj0QGR0aCJFXBwOzJWSCwa0pLjkegj/wOdyJdgZWT3N+ZSZabfiGvs9JdyysqF5yTWLq2Jao6lLLcsyp2lQo3VUV2myyWSZ+mha3PCe2V0nIjNhEUvf3TpC6HhC655jEjn33sTMPl5rfgQPjaOFYJnbfd8suoawcocl74LFpxbr8IPiF0B7NoHZdzoo6b91WyhtS/dQVAtkwGniVqkJOrwdC7G91ColdZ1KxmOCaVNgDFvC05HBZisoiFHXpRRx2CMI5c9Kl3CLg4YqgAxoOC9ri+DY58bLQpwLr5McR/c7xiTQ67pnE5LvxVFYxUwFOujb9NeB9AOt+BTFyuvg27NMtdBntNufjJ+5YYA0jxm2fVtUhAm3uWSnjVEemILmEc5mTuqaB8aW1IVmb/Q+Gcnw9MACRPkmvJCyoshaMqEJCg/m7h3eWhtF4oK0g0OVInRLaoxNAfdTvgLELvHR9C44JaEtcd7Z2VBLoha7usUxbEobVlAWCWugdrIZ/qhU8Bqu/ToYAGUjbQ/mjx6fW9dPD9r9Sx9uz0DEDVq1raPgv4+JDUkqS3zEZ+I0NTvx4SsE65/nX9+mlU189pZhUiuSpeXoAjP8S5jfZ3ZrKQLXybEOK7BUa1uYJCkccptr4XQL+EzJpMV17BKx0cgJg0QUmf8YtNOoi3KToP3A/ENv2loIWz92/fgPUGbVTQtUd8iUGsuXHhnuceDMuvI1tkRvsS3fIMYinPKVPl735kya7U1mK9wHDMJZeHd6HBH7yLDKfOBYXyYzDK7n0s+G67+STwON7Ga6kkKKInpqxyYZGBijjedj3J+CrTVca/mFEQCdl2Cr26SQDHRnpW4Md0vx0jm0bHYKZup4VjVQz+oZf9BJri0CpV1qvmK9zQO0iuDkzoEa20MijURGw8TsSEQ'

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