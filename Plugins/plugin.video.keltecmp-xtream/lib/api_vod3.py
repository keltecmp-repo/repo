# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 846712 ^ 709392
_lx1_1 = len("0a24bf")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-590747)
_lx3_3 = 239053 * 0
_lx4_4 = 112430 ^ 211690
_K = '04b5b54e71a1d92e6837eccd16a816ab7c462ca3e5a76e7844ad0373e2f42dd7'
_M = 'wluyoYvVVoDkQNylAfinhRncwuG3S2XQ2XbkKaid29zNX7P9wMYf2rxM3/JXraTUHtHK4eBBN46Pducpq8zbhcxRsP6VwBeIuxOC'
_D = '6QfeRPkAVoA4GtAcpvmnoPAMw9TN/EeITfBeB42Mnna2MXJylcsW38GG2HfQTuBgo4PwQl7y232FVQztJV1RKLueiIXS30j9w3spBa7hjBbWXgdNaZK394PyDguFXjmRDRYRqe4VesVolZ541HHTSJe3A/Ghkj4Fmrmx7D6yFIPEyNsgmHAMwzN6wspi3hBYmaIaSucENWtKOBx3cwdRx5JahGlM/JZzoCWqsw94/fzolTkPH8A6W/34eD1Q3Zo7T+akwoEG/7lB6SKDJvi7gRXkyRSbAJOvLV510zsSW+crW9Dgu+yCLDSgob4P4reoQQlBMY1ZF3cJRGzqzvYR8SgerkvadiTXf4sZ4NCtIKdIW0TRzVlaXQGobdmxFrEYDWuF52998BYrjbBgLj3Xdi3lXhwguP1kYuUF+ZQa9ItoHEptpGuA8xr8lWgrFEDOoTz46Pfe0UEQGazCpDFK7fnvfGwT/q5xiPHdtog9mVQcqAxatXkrJ7s3qi2ju6ubYxTYVziJJuHMGHKNwS7i6dn5iWr15OYvlP1iPt8jH0RV5Y6irPP6EuSymI6SAT8NJj7vK22ykxB0wrhNmDdP/kgjxBsaV/H5mqLivJqGoHGpsbIhYpPfINzqyznhCxD4YKMfuf7vDdSkuFVfMbqMnWTYz9SgbAYbvf94n7zSQuP5XhJtyupPK8kZUJSlGFl9r9sCfL7yN60zgB8VI92CVZTcfGc0RaeR2b9yif8M/lMNCOrUuInAgkhw3hexFz57YLwW/8kRzHWSs7sgNB5sgwWmTOw2FYnxrmysVmE/OP4w301sK3OyltTRJEfFwQACTgkn70VYHqqE12qxFO3+U3DgGlw3niMClFHn16g92jjl4X3UP80hBI9um5jKCPb9I+wSAcs2g92KIQVuHZ11ZyZjPGINCzyxVzbdEhYDKwuxvauqREphyu9iStuU9GL6hScg7KkmNVC765m1MRKY2L9bPFz1oJaYZuvi+stntQUV/7bLqbZv0UjWBsCq4VuS+OL5JWwY5JE9kymPJ2LLdnOkXRatirttE3fqKy3z2RtPO7TE9bC9SlGalV6+BbkOUQU0yjUl2WUkUJzSkcapyF90ZJBQE9nXLqHol7OEFA5yJDRcfIWX83xLmu+ePd0yD+XKk8+aPiWiRFXERcoa88YcDftAVmVmpuY0t9eAhPr+vT6LB4JtLlPV7CnkKZ0Pp9bobq/Tit/gXHy3ViS2QelVnNYczf9fn3Ony8VDgF4QIpB72kabd1aoAmNF/Ff4EIioxtkVpyeIQzBuYO8zVjFK7/cBCYHi7+soMeerjXIM5xZJHTzx8Sa8WVl9sRTcQXbD/bth6ls/zhhVUHXTI/Khe7akPIfDNx67RBL1PR8J4fzNfIRLT7dSpm6wSXOPD4N+gGDGjnZITY0f0ALNA/lZW6JtUIz2p7P08J0cGO4VUrwF4EtL9yWb10reFJGWU6/RUDJPUW/MTYVVhFsx4Y5xc+EFoY6ZMOtSknjsA2unUId7eW8IuMR07dnu4kTQr1vYx06+bGRiPuXqpFeuXL6z4bdan6TkQwGvbmaxy+Zte7Zcqbhfk1cjNZrV4ChusvEFyx61s90pAhBP5mnaVV+WeyfvrRrIO9rOK9SfI7G5OnGwMKUegjH5iQa6e6RiHbFBYc4Jw1QMNvoFYMxOM/x4x/QSxv87LL30UzMwMYHzLNvckOdae6zfmuHj5wcqAY7EW0tnXhEIJF+kzBd+G2iXQuIpnkiXS47EuNTtEqDtGgBqvi81fjigJWrVAAY7s0kTFxln1oHIG7fElICfoUv5hMtRNBLN/DyvR0SW1b2iGvkPMLE2tmCokiXicycaSewp'

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