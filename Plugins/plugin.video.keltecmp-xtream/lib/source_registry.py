# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 922682 ^ 596630
_lx1_1 = len("31a418")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-508929)
_lx3_3 = 568844 * 0
_lx4_4 = 969112 ^ 887039
_K = 'a24ed26fa1c7325a49cf029f3520cfa195a938a58699a0881416ffd183682d22'
_M = 'lhhBM5eeXAXFBIOr39XvgZ6lJMzoiIsjm3eUSrmqDiufQ1EnhJwaAsYJgKzW1LnTyP53zemJ3nLJIZlE4qtce8sSVCOEmx9UnAeL'
_D = '=oQ0DVMXlRfLfkuMLkTJgecmXbt78ikFejvGwpTT6Zy7eresOE61ajHBgRppgVKEJXFZWT7HkzR0tdnZCG4Lr1gAIUmLTSTq5d9H2ZeTo6yb5DEvTxzfqzJCtgtEHWO6rjKfsGNI8W0YkqNErlfKF8ldN6CBJTdJrcj1t3Hd3V5MkAu6ZndfkeNOwJXMsvmpigtA2vfU+lFmMXdJNK8TO5orVvxgeOz7JiqbbB56JdHL+RfPf/ibWKDxp1YECyTa4Bzw2LoJaEU3LRBE4c1Q5D2QkSbJ8hI9+AI8xp+MZWMC0G34/ODAwnQE95JNF6176XKyLRoWmwWr0ApUmsjzAOqjMGSotADZN32BTzr6imz0LyFDRPmJsfB2lWmjz3PKyVluWILBJVXxHUJm0h/wsQcx6qEr3ROBXNqLoG9ybGPhZkzOnWPmPY61GfHZn2//8aU6/iVWNhkZSJ1RDaqfDvqOsZUPdLDmehkId6peW36Ri0mjm2TL+THNx0LR3SG36fsYkIrUDBsKgqigAci88TggJan5S3kT2iSefFPeb/0JoajL86M91SYb1chSYQm/qiLw489FhSqDmJNEhxTTh2B2JHz+mhagPkf/GhvI5rgnn/IS4QqUQyEWPisv7sm0m6RhxZ6jHQs1vwgQkyBa7qaqzTYoE1E2sLXTitBlrx66Ge9HvQq3rMd9k22HYBf/8JIoHSH+W15J0ii7P/OviECluAe488HoT4PQG/djMKZ+wMD8qpYLnSIADsktDair+4i6DoQuxiBn7zyMV0ynG9KQAtpReucX2EHenHZRhCq8NscYWtX5ax0DDFw0yNzRG2fGQeuWrkxHN7zNHi+BCTga2enXJyFMBNjuTnFmW29KaHvUhHEnGedED5YYRWcfloMaxTmIUxCYSMjrKoc3pklp01KOdaEOmnZdWY+jshJ9ArNuGVuv/Taz8yt1fAMZgqnjTJtniwCyvxUVGlmUPVCpf5ol0l6A/eodjFIQEfCmQRNO4wlX0r1tvXCi6B4IQM2HtR6Jk8Ufja30SteTZxj3veJ+z8og1GXR8k7x/kEQu62J5gKmSxZNy3XhtgtVi4cGJBMsy6fTAnflSQf+YZFaRDpgrrxtWNRyf/0GqHIyVb1MLO+b+pb2tFnFfeM4lTFU7O0OYlvnqGGhGWhAnxNVCj85uUkJoJYnK7liwbvSLlmIu7Gqc4gmdv++c9tO1cYsQB7KAkKDLm1tYuNDY/9VP93W4N8oXWXo0RVNRE6Q/whkmclpvbnSqMrTSMH4jgC2Os5no+tRr/VY78hKBDYMxU3fZ0DbIvYeZHujgco7bU+6pAuXNtdvpmskQGLvZh8JJv1EPac0CK3mWIflQtBnNv4AcuMEVwVeKPW3Bn424+iM8r6HE7TQh8TfP6KMJXfjtQviO/iaaHaH9MFeEV6ZaaQg//MQA/fQhK9CYkA+yNjypJzqJQ8e2LnbR+wPcIfbQhaB6v9cwNXcAW63m6srbOxUZYEHQoNPbJb43+hV8hRMmT6X4GFJG1CeBH/p6RDAjvqXoIZa+YsHtie23M8QPIabt4JIFX1/W+VKeIfFGHxc4F4s5hHFCOvzpTZCIi6EmDPzQZznp7tL1oFDG+rkYr3vOP4L2w7YthFhhhgwOLqoHWrvJ7N9t+E9Mq4SAtKm52NpoRl0DO7Yfh3XFRdVrLWd3LpMO1YALMDV24q7p4AS+j7RAbqJBlx7jkt+LlzjMZJW0paAC/y+SilrYawj3DkQI9QRDPAwprTE9JuTUnRM6hcYG0T27rbNbpPGtgpDu4x7ya3yA1Dt+/SbcvlBH5tJ7MUnS0K7RqmtauyRV0VLP9t9zoBSJzVt8IjNv2oSXXE/'

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