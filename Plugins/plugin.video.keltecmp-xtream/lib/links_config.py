# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 736962 ^ 326790
_lx1_1 = len("b16061")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-541055)
_lx3_3 = 688061 * 0
_lx4_4 = 359224 ^ 189715
_K = '77c52eaba53e2d05b2d51d1cab4175d5b4cee6dcc28da0774e4742675f70eb84'
_M = 'n8K9Y0kDrSQWOUnlNcPbL77QUzJK9xTaJIcTI6sgGXSQkv4qWUyhdBtqFbNhw9F8voILZUGhR9R310Eg+XUQdJHI/35aSaF3SD1F'
_D = 'nQy3wiVQOU8IQ0zCN3NZ8cnHjMMsRIDBSKQWJ4soBt/iahZJAcyhWB36luTQ6fI7j8U6xnhy5DmlLkRtx+gcfEnDKksGOpVQ3aml27gQNEENhnOIGZAn9CSKDg4+cYNmrr+1RNCpqonpRL/6ymR11O6mh0g6Ds3KkAIYuOxgeIuzRAmdZsCF5sx6OA1zIlU7+Fyzi2S1L7lt/Ho9UFAHZn1hSBM2Q2dprQqDzyrJ/Zh8wBLiOnMgivcW1V6g8VFs2zgdaRycehbxr9+926BOFxOjuelr6F6oQX8+knVrnTSVsen7/MgkbnUg3HCby4N6TfCc9qGBXQ7xClKBlYbHy5awEoM7tvJtpEnG4TgQlh49cp1wijJo1LhAYM4/yq7512SSCSEx0U2D3CLUpiVReT0jNXpLVg9Bb4P62BobDTlX8C6/CP2Pj9TynvzArFhE9cLNsd4pSgPB0L+ltPgLpIAPv5rdCKL5aMduZ3diV6hzN7si6gaXYWi0I/x0gQ2d3A2eTNTPAJkgvCotsPbhKdfF89f2iShaEvWMFcPgd1usveeno1DwTwjOrySvQyAicBAY7awhJNnqqO1T0+yvCnC+cS/2ORLBCh2adYrAwUSX1muvKCePFKRsIeT9lxAV/KEM4sz6BPm3tY17Q3iDmxHdv9zzuADwjnXwpHpu34JtznPUZkc7wo4obi55IA1soN9f0t43b0lFp6KH5nS19IuqhDWRl7jcbxcCztGJY68bShWypxYO2RMec7st2j0gndCOilhaw+UNeIDgG1G4Nv1Zu9KOPjThd5bp3+32tdSNGlZBGzwigNC5C2xnGY0rv2SIWPOe/RkLfzbGm48GjRNmmO2uS2/Gq9KNKHU5q1E7GehNQdJK6D8HqnYhLT/7ZHYU3Pb5RXKFuwQUPDZw3Lhaf8WUcrWn9Tjy7XqPnMxP3wnKqSwVkGZ+fxxfmJQwdLGbdOZIfi+SuzXsSMluluY6DrrWk56dhcxEozTal4p4CuhqTvW19eGWKZrbjOjNwk8dwXDnewkfI3wIkK8/vWxJZ+0T3ESsGLLqU6vyHLUfX0SyOZxU0l4d1M0wd9LTt1yK7SwX2Qw6wvNFmgHIMLpktwnPH1zxWxyURWQVGPRBYjq5UeueTus7gQpuQs5BdRZVAV8bD9tL5mfj7/qp6mUFPmQTHn4P0WEOwSRYKmNUnOMmq33BDXybjWFnmfmvEGdZIS2cb/JaC19Mdp+8llL5xIuG2ugNIL7s0KjoeF+ZY9zgC5QDi4uRUXXKgd28yUF6+YqBVWziCx8fzR/2dlyJtuI4tMpI5sl2tKeez9XjNKz+xy9eszFgzmNIqcYPZpSXQIh/tBH6TJM2JBaELG0z+N4BKW5aLES9XrCL56qHbmk4+ZZo+vAKoq0H6EzkxelHAOfSqsiNgArD1ZFtlPY8kszwzu9kN8+tbCIuEHNg8RIEYeJk/SfUas4dRaiZ5uzS72dXXCpysvCa9zls2jQowwcyZW6LLCWiMLNxQKpNhgMD35zt1KWz4Fn+2auOUzWgiFPMA6XGJPsCGSbZ9a7hveDj6rLBLxCdCDnOUpAVYATu4pQGh3P6On6Jdixvhg7p3m6Bf76aCT2CmZobXirt8rx2Eqexgq80gmC9jkHxlJd9t2sSSLL3fhHEnNGVOCQ1LFlgFFMb0jCqrpcuwcHJ3tUDmzKzXYf1/5tUicwXI1oYVwSnwBjPYuMyTNp3lwMye9vP1UXLd0LbeSKZRVi+RmqZygLy4QSHuIJL7WlGp1xOJSTK7AnECet6gomYL7sw6E643+3658qmmOza1GIUfRyOpLZoG4oLrB6tsRnjBGE24HtxRgk+VqEG3kwlcR488aOBhOcYdwN7'

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