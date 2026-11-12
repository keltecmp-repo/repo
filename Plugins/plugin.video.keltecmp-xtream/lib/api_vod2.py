# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 921187 ^ 861303
_lx1_1 = len("8f9718")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-577250)
_lx3_3 = 762703 * 0
_lx4_4 = 947823 ^ 178877
_K = '8809ecfbdd14318c893d930ae7b3c1dcf5235b807de357628ade841cb71a1faa'
_M = 'murON1diR9HpUnS4XlMl5DAPxg8v1rDxrNihbd41MHOQ4dAxRiQUheVWKLxdCnexNFmeD37QtqT+26Rn1TIweJnu0DcddBqE4VQr'
_D = 'ZIXDY2kyKEbhtovsuD1IoRX4slDlwhfjx6J4ZKiou+97Xb/FzjkicIH1b8iFH8EodPMqCcarI4HyqOcfQREzJ17pYG0ggsSksyODL2puHpMj75UCX+uF1fgrDEq2tqnfXgMBgyntWNw83rM7iL/EF6IduhayIBBZHO2xAaryIWnlbJSExMAyiG0nLWOJkjc4QgT10dlaNb+BzhlyTi4UEsVTfbMERZ/0y96Mojfe/G+MaZdtFNVXVmQQUIpJ6uh1jpvDCjijWfrn74JIgmJmRMG4EOptwJOjsLs2pdIWuMjQJx4OzP5yALKhqrsyJCV9xO0xeegiuZKyZ1/maNpIzB+DEgvfSHCinrmr4gML9dxlnzfzFeCqat8R8GVwEA+5uUbB+3p6cB2HZB2xwA5Zquhs0bofqOJo2ABg6uOJaE27LbN+ek8+favG9n4F1hzMxC4RNyT1H5JNLgxQm9ioI5KimDys4MUXrjcwBBE7ojHyqViieoPTiDxyh0r6W4ACmgW9MxmJKlLvIOD5oXAkd/t8h2q8QuTz4VqwSZlr/0GXw1UHXtHNL6eyP/iJcmg0ps3CEvQX6woMO/wM3czLMLk9AhD1H4Bqht7amlGqslszqoUWkSabXBzCSnxPaHh/niwzOEQmvZMorfjg4VW8xVcJsDZtslsSPPqtd+Q2xoJZlQf3W1Va84R229kYHyzAOrmLGxpQdStS4NgjRUR09rZJTH5PFDH/RKFz61cuZvcS8d+IjU7+Ed1tV0B46d16/auwEWeoA0w7wgrBzRn2u56XbZnwqGScFsMoZSZmppF6ehoii2wEGoOrEr/KX/s2nv9B42oUAafH1dfMEilZpcGeEQrw6Z31eYcZj/1PfYK0jMAokOiW4AX1R6ekv/8qWBjx9YYYt0qtnXpDlJJQu3WbP0z4JvZYt6aKA2pKbsCbymtl535jpvBCB8lzUgveAMjoCPnjbi7PTd/XSvT8reN0lYbql/6eh9QxZ1NrRUCy9+jbVvk7nmJyPu30CKUNEterTiMLvgRmx8CegTv5vcNBBYqs6l08qB/EixOGrzVGJC+hODgTJef7gk2K0i8yTIk8me90D3s5ljYie9bhY6tO+kj2/s559KfjkLI2Ix/AF/Gt3pSc7m4hxMdXqxx+Dzllui1VKpvH6oVogzgTObRA+dUXLBWCuhKXqPsNIULSAQjPX/DwGzdOWY0jkFWcdRaW/7CprjPFCwHPEusMwkOcobxCBLZsXIfXEJEsV6lzYGrQex5X4NPvF6CO3Yv/CyAkhp9gYktkwSNAxohwy55in34JN5OtixVmB9CGzsNC5eF3Z+BmORUPpOw0enbjjsvUZqsAHrmuk6L0u9asi/xEZxbJqV44VqW/PVYGCz0FiPEaG8tuytKRQ+9p25r5TtybzBfFJG9iXSdw2LGem9xKxvNqJTxp5uwP00J8kSU6xDGrs9VwsGBkY26oBHxMFRR/V2GU4jFfRnjc3ZNl53TJF7VgItgTR5JyR7nWVuyMJmPjCYuIHyfgxQdK7bG4ItGIcN9p3ynyDrvhesUn0Ldx0fZz7+v7/V1/VeIxRkzfNX9An5+MGucklP0Cd8DdugWMXM/x0LxbuyuBw/Jkuy4FyOkQ58Aq+Iq6vWNWvUIBjPCXJJx8NjngZqb6R1lT8pnpOEabn5RmI3DoGDuuU/RTl4rp1WHC5/vluMR5oT+oP+mezfRqPqNHzhzoOm8GNAHwXns9TyxmqHuLYupg38AryjXiPDPbid3sbo4Xvl/xc2W3h+k2yCVikdNK2LWbSqM62yjDiw5+6IV0sZR8QBqFgZU/OeVkHfK+b9C1a+l2ISqmAh66'

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