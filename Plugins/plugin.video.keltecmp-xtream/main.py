# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 962647 ^ 948386
_lx1_1 = len("e2e100")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-871363)
_lx3_3 = 575125 * 0
_lx4_4 = 357332 ^ 816171
_M = 'TNN6jtKxsBNE24e7ze4Puer+OdUn4xWvdiIxEl/GY/ZI0DnU2eyxE0rZieDO6Afoua480Ce6Gv1yIzMZWsYz80rXaNWD7+BFTojf'
_D = '==wC1QmLoCQvNLpFQIMDJDFJ3mbbZ3uZzKJDKHXUsmjK7mtG+rrcagna+Ere5RodBPY3alpQ0QPD707h+VKhkgq0FgrtMoiKagyUhJu1/kMqnxlJtlty8M3GTdRWGnL9epxRThaybpj6A8hKfARwUOOi6k0VsBq9dB9o31lZ1IIb+vAjnqmg/llA6lMMNpoEZ6lnExx9UTdEpg+chKhmnOyf90NvqNJhve/MVWXLWR8h6Dwl2VOudpQXzBbs2WaH5FweINWl9cYfnr3II6aUKeytaLibsZVNfJ65koSyV3KtXyggoi1kOY04RVO4Qb5j4NzI5sK956DMxRj/H6deGw3qObJ4pHLs8zHt3X1tO7ch0JDy9fuuF9PlyJvZqb32ArFF+PUx+CCEVZ4nNb+6+FxNkNy0XbpGgyA83RJ3fFlK/pRsCL/lI1WFeyeY5mVffJ9RlDdIK8BXtzm/kStQE/SZzYO/abvOOS7laNEYZRcVHg71e5OKICF4jiVx4E5FXKzCmV1heDpvSWxeyNmLipkEEH7db3tAtdJhq+QoX43O07WYxY1HFrucbCqkbf1Y5mNQ93+MJ9te4huaH4a7xnn7nIdAoS4b1yInIAcO6gXLHifuZhDAEzZSNDFOeT5m0+bLZa/i97S+g0wXxa7n93RGnw2mYnjRiF9R0B2UMWKqJE8udlggXemIjdWDrNlchT5CX5lBijEKXZZO9C99jQCCJHesyLH3fUIgfTDYLePW7pw68r3wuirMcN1p0d9LqAAkki8I2aJhsE2mtXUMehNeT7JSqpvcmjlAgIf+KjaOmlytE6knE6d2sJRJrsMbaUQfzLQRG7D3pJ8Dm4DIYrtLMXtQMOOFrCPhXt7idqwfzZP6XoWj4IWcg/ShwYz1O4kMRtpBx6isx3qw831tjAZ+Dj6cyUAbkvnBU2COkxxfVmK+hpfZQlE/RfkJsoyOAyMlmLvMvbUuJgVXQK9p2ggA5z09FVylRnlk3gU9V56oB0u1RhJss2q3lufP31W8/gHkD7cXwUWeSs0IPouOZDLhrbIT32C3ebxSgdnFjo393LjPkynRcYe3/9c/D5pNt8lqjmn91/0Om971EF+j9FYVmWCYzZt2cA9/yEaXJJFF7tqxaAPVa6UdCBi0bHJB38GNDA5G02l20WdwPuzAFjax/81oPxfl5NvlO9G48RkOdnEW7dr2qIsRGNdC2L0XmIiQcU1HUcf/A+XaQeY6mnTwP9LS2DZS/J3IidgG0CDinhzp5N2uN5/lGqlRcuKizRGWSiSk3FQbiyFEvJhgni7I3f42doO1yhBDCTWVU7e11+IwjQPT4LP87HtCPnETCUuueM8eRIImriG3rAdUN5eOnffw6Y8AHmhFqwsfoNZ4UzFmDvurnxT+nB8mIyQc0ouJ01UKgP7gzvetlxrIthpT16hJfIWNo9AU/PaIZxuTqP1nph0XV6uCG7D41VtiLKkYg8J+esPtI+u0eMMca7dmeuJ5Yiff6GOjf+DPrNspuwb5xVNNKOKLAshfAe2rxZgLX5oQdMsO8+EIw2CqBrB2YLhigCUt65xmW5ZESqotjXbX2cZQDOA3F1gk7GbghjQLkZ3VP1SVsRHxknef02dcUZxQphsDStE6Tk6aM3t6CT4wUw5ktNidaWp/rqoEvLeQcGq6a333'

_eb49=[115,208,131,196,233,197,136,186]+[35,98,248,115,156,89,181,153]
_57a0=[215,22,212,208,37,32,32,174]+[29,46,202,214,85,6,226,177]
_6112=bytes([a^b for a,b in zip([1,181,240,171,156,183,235,223,80,77,156,18,232,56],_eb49*8)]).decode()
_55e8=bytes([a^b for a,b in zip([164,115,160,164,76,78,71,221,51,76,163,184],_57a0*8)]).decode()
_bf3c=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_6112.split('/'),_55e8)
with open(_bf3c,'r') as _f:_K=_f.read().strip()
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