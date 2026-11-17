# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 508141 ^ 291489
_lx1_1 = len("78ffef")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-763362)
_lx3_3 = 784304 * 0
_lx4_4 = 949300 ^ 233428
_K = '8f344b0c466c950085c02baafa34af8cff27dbc8ee491db44b0523d81173bc9a'
_M = 'bTx2Pdwp3OPQN1sD6Nl9VSHj4Z41GkDL8++wqNsDp9hvOCI60SPMu4k3WV7piiwDIeazn2FAHsijteao2QuviWZsdD2LcM7t0mNQ'
_D = 'VH02nOTyQ6/sUzO4EpAe3SChcy2l+0G6Cktze3GLE6jr6XQGvQWQdLBATtuNrYR3TKsSKNEm5NZ35tt48o2Ymnx26X91FcS+nrNrbHB8/6ERdF3a8yulLcxYlMx8jowCgAWOAJ119FZfomB0DGS2B4W1+yN+IfXEb7QDw9hb3Pdn6ZNWWpJrXQuAzWy4mxMhQMYtECYbyZoIRecUfKwYGSH2tlAvDMfgipYeOOCTjGZ6ZFP7mIPuiRTr1wyC3uW9FPpUoERACfPV/VY3P7Z4u4R51SQqhTj+2AG0r+rNLjJdkXiOmlALHJZ+oSfxiO/JXn/NeXO0PjCVhkjnqbunMtoyMElSRTiUxcwHtssdMEaM0uE/7ahk58m6FPnlGCZpRDj79weft8bvOZtzMSK6XDocrb7GpkFBbtRQfjyTH4xfLDer/U+wxOj8Pf9B/f/AUPE0r7XDM3q7tAMTP53E7uP4S6UFfJYzi1xv7xUmeelpmQy6dEWR6EPsXk1656dwyJpzIRBhcRqcVxaVKo0LNerNwXNIlBrwq6KgzCNyOQYi2lWkTztlLvb0fIeJ0EXnboK0ICFynEq7s2bo3Bryt8oK81tDK5uVJln2r6dABoOJ9DGVR0znFvPcyphMOacXPBN6DibTvKBKvkHl55+VWSeQ7I4Z5WBLSTa2N7NaLVKDzrzr5D7MQKcY95rhUdnZzbFr29406p7nEfhxnl/diddjhsS0SD+X+GEpW5zRpi4CQ38HOxxR+zzyhwT3F+PeR+mY8AkT8pT8y6MlQEsvAvNIkcrtoGirXTNF6VY46gsZi1hmNbhmgyIbL1lAL8d0X6b+LtYFHDEgOScDJmnwhxG2wabbgzoJ68tuQgaNopHzwaHmrpB0rn0u6alX84o2WWOXIMFm7LSVK/9KfBe4HYlMO8f83WP+L2hecOzUkEIS6PNYOwWkvMJzmfAUsALINcS+NcigSE6pT3ATpHfDsFSfban/MqX+EtIvQDgKa+3E/MpnJs1LogWomBVG8H4m98aEsoYabLGRIrFWjK9UvqtVwBgyxiXOdOoHw2H25XLMjHSsjEuTDsXn7pM7alFK+c/It3WtZJ0f/VIw/wObz3TdlKhqPdBgXkBEYdIkVIkHZ8Bldku06YWl4p+KS9wyxHhtcydf+EVSew9vnmuR5yV1IGivBrOh+F4SAxnBq3Qso09ute26Mt593lIcTlFUEEeDy+Q0CFDV0kO79gBRuhHFNVcyRG6ct3NbnwpERd9OvmZWixjENgHJFhwNlUBsvtfOqKvVBpZiwWFG1qjesklTaQNsuYFJLOcSsvGh0valds4iVJZ/jprHnZqp2gyTxjRDradsXEzslHKUgQj8n2yZWKOrVqsvfx2+8uh6UdrLv2uZcPGdw3S2JDtNzVKCOuO3RssKyDPorKaoBRUENfUgMH/+0CIZGvEmDdftKUVosOWP9eo+LwkB49S6qkuR2VQV+S2yt/taWjAEnrp5tnLrud4ieoGOY9b/dUJdYOzOPNMOMGLXV6ZyCPsHqEzuBAv+7CZTH4sW/lZ+/EHgnbHY7sJjmEQZeI8Zt7ac888MQjz3XU+CGBFBD1dMytsr4jArwEp7ZXugIizdIEvHLy1gYR+t9CAUY5raSFIbY7tvB7Irg8UG8WCPfRjUbWlQMGFCYNEi8OudUWCm/PhvYwLuOBYbqJKyr9C7Wq5o4xj8ZWBe9+BEnX48TejxcOtC55oCJCT41zmmQSJCBB84f9ZivLKdqOSVtK9sv3H1m8v3odQS0cczzbcQSSAO0jlmjCnibyuO2J1eaYWTR64IsgMbwsAI01c3FPnu9Tum1PM3b4bmgGgmELbL'

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