# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 497553 ^ 437533
_lx1_1 = len("a18948")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-641116)
_lx3_3 = 965196 * 0
_lx4_4 = 544490 ^ 554179
_K = '297364b188d004b0e17a06dd0c4cd605463a8960b8461f504b61d671238b585a'
_M = '/L1iqzHwICysA5roq0R2swuOuGv+t7z+kX3HuGEByofnuDCpdqVibqQHlL+pQnToXI+6PKK06q/AKJbkZgLL17O4Y/gm/2Zor1TE'
_D = 'f6QclOQUb+S1cUXV9QHYJKorBEpqhjqlbiwjqqFenf+SCGcleV66ANBMWJmi89WZ6SPiqDNepfRAuGQVCYvUDvzq3psaneSfcoKxBLkZl+Bj/AE+qsnWq9uMUqrePD5YbKAcQM8f93ahqm9jg9aPp2q9useEM4whz7vZtmOmKn4H24HoL2f1uY2kjusyz7NxbA06OM7ieS/WEO8dm/CsAWV6/bj3taaYRi2q0zroHnvCAnEx672oYpc4T0bBRJRHq/RPmgfyYFJh2hlneWfqC2ewVpM++dmboWzyKuMnds6jWzdZodQGXHKsPx8QL/sTZ7A8UUqRen/kerX282PQSmk9AP/D35T8Mhndg8p7hDyxItOXhTxkdVVJnLS2dbnNaLcyR01OoijFwE6m5EjR9fFCn9yuVvqrm7eHmursfn6MqWtKXXDmRUAsGOHOc2Tf/gtfHTy6Q/73zKwzaotPoBttDdmPMU5Dwa2v3d8VcHZgHndDS91flZwQhckJuhx9ynteR09ozeuPuIW1uglinxa9sxY+bEPfuHbGSvr1W6ZrYm7buhlc7c1NwVWNiXGIs9l0rKdtONuxt1zv6kJEFyIiunIYgQKioLl/VARU9kzvhqemUvHF6pxAp82TCwhW/DIO1Xix4PrRR4FFuJTsk1i1puFLgnUx7qIvTZ+CJy8UBfLrzJFitGf4w5pvJgViuLIAL0AubCMe07DwM+iDc61eWKDUIhUvr0Sgo/zYMew7osNu1AT+rf34h+9mcgYZxQ0dqOXdBfPJghsmMKAC8am9O2g8qtqYXEUKnyS6ATSv9w5VjAybOhEO7UwvGRVYm+YHDJ3eVM7zgl57By1s+YQzDualODQ8sUSaMnadtd5VgacSuSUGk2gN3Q45SnanGVQj2dVaYNTzDaECXPvMeCIoadPqDlpjih6+JXGSdl76M69//rHnAJ5cKiddN9T7WnOU9dVtiolKQ8/7/KRzQ1rR6K1fGTfHo85/D837K9nPYFUEBExMT0a/MtrtQafEYihT/Ud+KDgL3jHfRiAGzKwNs5MD2XUmLanES9TI7Sya62PshFW4VA46YIOjgznEcBNwFwENmsysosnmP0+wZkDGiXNpo5sRi30mxqjurr2JexYyM/FgVUxK9XmVKvju4FDo9u3FwpSaXe7tZo07lQkV6Hhj9q96aFEFPeMGpGwblz/Nlp8i4nEPaNPDugs6G4n2Vu20z7piogdtiLjGS6rGvMbpXlkx8b4YmhezoKxbiLna7LZSXurPS3RW8Kim4E9Si84s38Rka7DEcgTyspLA5LZcg0ouPad9vIk/nHgANN21uQ39Hp8TJ8CPry8PboGSURr2+I6NNXOsJPU7st2sSYtyrDbMJhZ3lLBfLYZFBv8+NavzWHxCi+bKHPeT0nItoX5d50fSv4kjOVEKtAHjQIP4pDmKgzLXmYr59Iq6y+0VlvgqY7LqUBcDInPqU74mJPmwNkW+YvfDl89JnAQV7MgA8ssxwgXA8Ac4ZU8QpSS2cnFvSmO6pw1UW4wO9AiUqBd81LewzoewE8xzptIefsdY8SabG0RoGtW4oZoR8rA1sF5c0LDVp4S5GI/bLg17AG+X4F1HkdorJyqsRIlIllUOwuoBEXmfvW3oSyUy/5FZgyKA/HRkWvhlnQvDyJiF2NtD8VHF6aOFRH4d2FXbVjjruN7vb1fLb9ERfhDshYhbYDT/IkZFAEaocRMcALFahcCBhN7Cv2ssmvWYHqwr86dKvTbYUqOcRXTGyyNt3fJhP0zvTA9Gktd2JzhwBhsZfFueSyan7caOgXEQfhx2JsV/Bw0y71RXXsT8VeleZ0nzz+shGa5NlJ07AVNtCFGY0G4ncZ0+'

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