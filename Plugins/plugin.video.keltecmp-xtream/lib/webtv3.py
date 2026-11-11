# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 712704 ^ 415622
_lx1_1 = len("4bc3ad")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-327796)
_lx3_3 = 852486 * 0
_lx4_4 = 819504 ^ 317509
_K = '46599b907931ed6dfe4bbb187808b2f6395cc5ce2490415fdf8e76d5f930a276'
_M = '/+oTyC1zPsiFFCKRB5ybxuYlBhsjqsVL1AvryD3HX7W3thmdJXtphd4VKsZWyJHKunMBHHGtxEuFALnIbpML4raxH8l4cz/YhhQv'
_D = 'v3d7a+7Ws+6QI62dvYtRT8PvRpJOz4SmZgzujVPGXs5BGOLStnROSJ+QrKPavd53qzhlsNY1LcI/DS1odyO7sO7yfVtyMeCbGYjt7GFHegb41k3TNCQi3dSrgpOdftOA7S944/C0k5hiKbBjgaCUtjUYn1KcFDitkYrtm9gxEbs65okqroTQ75Xr4gTSb2fYK7igrlSDAe8PVsa+rU5RYS7jTqb+ghFS31/yOaJVVIJy9Lbb1pKw2WAZXUk3QIUsCw4DN2m7B/IjjwN7BHgkjvUpmmcbWiqwr/OiBGKAY/nUYYBqWuHagRuC/j5VRrnB3K5xsXJM+cNKVb/2KIt2OI9Q3e8GXD4YOopp2mg93zYzLvfqzWSPLsFcESnjc2xLAprVSYZWlO+vo6j+/sQIoHUiRpv4IgLc9fQqLlk/+gy8mHdEDou568KYU2tHddqSlAMr2XteZbP4Oe0aeWdwg6ko0i66KRZQ54F8MYGM0lPB2ti8wJhYrO9shdpFrL7bpk6cdNZPAGwtyFzWujvklrgkBmdyZeYTdAEZ7wF0HtmzIP1EfDOMzSBeOS6Q2SZx3eMZZZw8MaICm03OgdmdL3kcuaXa1FYF9RBezy3EjvuefoCYldFFq59B7Bm2vttdg1B2bh3hK2samqgWe3j/kKr3aCpj/sdsbp4BhnMe24Jm5/ghZ9VeujoolnOfLO+jYlUtAN9f903hO0UMJhYNsZIm9bYO2HMbCsEPVYvpP/9LOP1aejLQSnydt1gnWHTKIEbOBQkkzGyfSBoGFqZK5VatzlWZeYqKRvDeduLR2GwNqXJW62pTXP1CRZbIMmD7YlBAqvBnfukGKjy0vzHrqN9QW5eM7HddPQ90S3GiSsLNmD8hmw38APCncYoxTXTASu7ap/yHAUmS1s2dSN41m879guM6gcYUkDlvNowYiQ/GfCdprL+DItoHXATExxLN6lBN+LiSkT3qR9WeZ3kgS3CO7B3XgGU5szVipicqQV3eUPQa/ZpmxbvygHYzYgJ0BNU5eIsostUPYoVcuswkgpKW2jdsnfNtprowAKAIlH7vkLXNCKqT4IDahxxz62Dee8H72C3wQgdjaa8mXsJvBnyAGi0a50aSxsDmv/TR6ZzZZdrCgnLecLKYCXw0ZBqu95fe3XGHqsqzuK2aao8h4K6KSFXWeizEz4hQv/c5bdtWmdzXAwlydFMbK69r4ozUp1Wqt/zMzWp8jQJJ+cUlGXbDxcT8oKRLFC1lTbpDxArfWsu16D+fI1P8ONzc/ejsDOcC7Sj9cOOx/Gjzv89K9nA/5YMVXbu30/fm9Zrvrp4McY3Cob595aMEPA6CD7ylgfEwTWzu0uzIvKIvuToix8N3VHWcCp9HAVm/ticgbaWj/auMGgPrFNOvD333t/6Uv8VPNOHOuYHcCTlfr+6MRyil5BciLi6tHnLjlOCrrAuwiy0mbgXfnTkjPtzBpmHkAVlbIARMeIj14cIJHTSMEEkxeKpt6H8zsiKgp9OTCvWfQtgGVxKqiY6JIoJOGnO/Hp+/ukPsmOQlRyqetlcxo5amhFm6omm2l8J21LE89EiNXl0vqosMmhunXiRvDOVg+HzCLhRIEWsfuRcqKadyZnGyuqdl2WrMpgMc6Lp16/CbB1uQ7KcTTy5G/vl49vO+rDuChIPAgtI8A1b2iBoFYDvUIuHg8brRS2RNvBp9X8Ao73Hp'

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