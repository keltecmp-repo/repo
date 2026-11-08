# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 818612 ^ 396478
_lx1_1 = len("f5e61f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-428684)
_lx3_3 = 309153 * 0
_lx4_4 = 536736 ^ 976021
_M = 'IKkrDd99qAKwTtJZ/4byJS3vIHPtYf/Qs2kUSZRnDk9y6CAEh2ijGr1M2wutgPR2Kr1zIO5jqta3bRAYmzBaGyO7dALRP6VAuBmM'
_D = 'HwM8qPD90EKdjZlBzhxgT9q0sOfhzdpZ2MVFaDEBJ4+ZUyhCrnNq2cDMlCuLamlVfFIEyUt/zXiwikfvB793PdLLI4D79J/XFsuM0npjFU/Z0PUC7IjQTRNgopVuQICmn/h+MfDzHdIfoTxqUpF/N+G297SRetN/v12HVCaNGqm/0Rz+8JoOc7KXVirS+bK5wSRfQz26MXZnfZi3j3O2Xb3wl8kunrmNmZ/4kq+NRz3nBRcUFt2OHMjbQa+h0Nvc47oRmuGmTjHD72Dbpe0E/PW258OuDyu+6wORvMXZyfQZk0+q6zlfbaHgWgbVw7K50+HAoV9faqAYefeW4KagBQC4NHDnFpJurhVFYsd6AuN16sogoA0a9TzaflAL+bsnRM9ozwnP5xf9TJ14vOePTqVoBGRlfr2/HMFzOtrlS4t9nkFNuhD2DGZjIxMXqpd3jlOxPLbq1H9iyjBssI3zex51reny7FQB9FJc52HfrEaf2sIly4O+xW7nGU/IioBQwPQHGbKbO4qbFPtveq5jTcmyLSRDerufCv/HwjylLtyAx0cCmbsQko/gmacyzieV9l+eu1+lZf3Db5sgkFtWojORm2JQT5MVvn22rbswdwAwK/3sGWOgfOxhMCSQIMLq2lAXgY37CO3WMhTHqxvMF3l4w+lKIXEvYmClM/ni3Yrn24l3F/Q9p/M07citL2LtUqfqqdyo92Kw7LnpgHi3nqeLOK5zOusMN+uYdWPCgwSa/oVRzWlDGsCerFKSsSatkL9dgXSemqXXbZr8BHOpMRX6sBR0hvI75/8phLgqv/xi5rNBSGW7zjT7HCrLacLf8JhPD7H4M1m/n6dmEjtemJ7lW6hP57nVdngrXyST1vVJVtrO3hpVmToiaAwJVUdYcvmpLJJAiiuzRjoppyu/pJwX+vnEkTMjZb6oPHWZLw5xpcEoAz1uf+IkdESfXAKFPjRLjtXQReEXUM93vnoJcdC1zPiXwPZC6JPo1Gmdd2yupRp4WXrMaMoAIykCuUSjaP2xvhTo4rAtHWsRCtZIGkewlYriH7YrUsR2FRYg+pGQiCfiJIo+kvgfbwb3O8hqhzPCeOgPNjYq9xDo77tExDc/2rLofpmstQOKqrrKUNQ7yMc0lYMVXu5X32nctFFtmLWJkyED0HMcqDM2TarkbmwIz3h3Hb+3UrgSMlMRAjxNxfouDuzH7UL84QYWHz1fqbRzxDqTu8B8MpiZD35LlXIgkgXF4/LHStc6OYboXHwvXFRz1zNOJ4L9Whm/0WrxSSRWySJ/lMCYBgZW50m1m/8JDuVZX5RNlLgkmmAJI2qpgu8uRRZ2nQmXzHVhH3b3z0dv3G73reX0uqLm8M0cye+jP8FpaTYXByZVQ1sQZTQL6BxeYiMNzKSwZdh5uEceR7mEiO4DUQghXVvVNZaN3MZfOstrmbOzo+nGyNY+gguwjouKddS7qPk56Q9L6zy7BksTQD+eIPszCLWsl8x6RA+AiHChfoL5BgnYDgRflaGj9tO1I20nXgkSU0rXUUX/rNYSinFTafIhlRIdjsSI0o7t4vaJGD4/qQb9A1FnRkJkqWdV1YC7bu9LHcWT0DHRUMe7VgKh8w6SBBWL7yag+2caKBhWkkvCM2AO7YkOgR4yxnEt'

_9a75=[137,107,210,172,129,150,129,189]+[118,101,58,41,57,204,82,181]
_31ed=[205,86,25,108,200,51,232,63]+[182,177,35,20,37,222,65,27]
_fe57=bytes([a^b for a,b in zip([251,14,161,195,244,228,226,216,5,74,94,72,77,173],_9a75*8)]).decode()
_1443=bytes([a^b for a,b in zip([190,51,109,24,161,93,143,76,152,211,74,122],_31ed*8)]).decode()
_c864=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_fe57.split('/'),_1443)
with open(_c864,'r') as _f:_K=_f.read().strip()
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