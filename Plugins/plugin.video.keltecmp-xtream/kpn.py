# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 181979 ^ 128906
_lx1_1 = len("131bea")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-624580)
_lx3_3 = 927544 * 0
_lx4_4 = 175702 ^ 448554
_M = '6DoqwOBqAxVcMhIGp5WeW7jN2A7Np6h9TZf25i1kYYf+ZSDLvT4OA1I1TgfyxMhZuZ7cDJrxrn9DxKTkKmNq06lsfMjtOV4DADAR'
_D = '=QJGGCi3kUQPGssnWWRFQovrAqzIZyALQYJ1LYiTgMRDeg1xuThaAOksxBn3O3cYHNe+q1Rol20ZDfLfE7Iz5gnylKI7sVnjbF+tZ77w3z67K/UNkAKhQpYDmjkOoo0nMciVLrgGlWd6pPubZEyp1b6u8Cc0HM17qPKNFVtbr0xfLTpWZObLGaVkbvbtDBhiOuHZLIeUA8KfBMxiAbbjxKXr08i9g+wSJcIDuqAxkVvPyH1Oo+2uL8SfSIXTu4yIQujbPWrPYHjex50q0XI+Oj1Zdg7x6u0dHVHBg2EXUpm8hXPFpMC0Er+7dk785lF+Lj9anJDLR1pSCdV0+aUjtow4Rexl+DIkmslMpIdptfo1XAmlVnHwXOIpQWG4MLOEZ6u2fdnUy65Q/O7SNw8un8D2nFt3iJ5e/rcC1PzNsWxZY5tw2VP+uLMVIPIbLYm/UryrKc2W+EA85jTjoQ4dy7+SSoEPVBFpSHtvjWe4rZHiimI3khCDmsga6vUmW9IElih+7lxv1SbjNrUpJsZWZwwyCENfWSuRWyYdWPLBi/KOk1Dm1XVlre/yeOx7WcM2y/Cns6sCZx4QEcv8yEzitWe31miDtzGyi2N/+BH0FXrq5vFRZghHdsqlHJcCCuPptDi4PE1r2t0HDyeNBlAvwi3WalTK1g8zFq8NfUajrG/C8rV8kLROcWtxp3XuOu7s1h5ge3S3QnUpS0+kIOMCNAAPKnx62kB0wOoYXd7Ve+1XorTJQj1plyPz/z0PbvSvPL/bZgaPMZVYxXUVKYmNAgHhvsPZViEiIeIIrCmQHRr9Xs+cKk3g6X84O2xS5mqvk03g7giOezCDFmbwvapMpR2PBD8JiZCVDNK4Va3spt1wQsNh+n4nETk5rrA1lt8NhrS+AjgLSi4nyjENITCgm4qngvbLx7OPxOZdcdthbZiReb4jKz246L/IV8ii5FzQ6Fuk3+hMITum/SHuDkz9uscbV7G+lg4kv7oUWEPCQVw/Kjp0dlcImh6bTRWNSTe5skEGnq3Ckird8MstJNh+JZ6bg5fbsn9ct30TOiUvWEM91ZJy9nh0ZBD1sw14zJKMaQZReZM1AfbWaK+YSjL7CtS+AHhCaBFSryURXoKYpuys7hGLoXD9C+Uon8+nx6CAVPycW/NpsmIhOKEHhCFCFImKx3mqMebg2KE54BRYXNsM3GIppJybCs2rCKGN+5dSHkSJtPf7wOWSR99ivzIIObHd4r3TIrDmdKM9XumFdL8Md5mCMyz5JO59yPcZ8M7AdxYI1gyikEvb9CxG0Srby2iriVN55hbMND0ETYAU/iIthDyT6L3ElwiFjkaVKsFN9Inmd7Z1HVleOyVlfTg76YFc83CY/oRVr0FtQbiKhvJ+RJb/QwRox1UN/xF8B49cVA6Ubs6Qnf6YiHx0+dZaDhZVn/whj2Pa3zZUlPL7+T/bpohgi888rER2MvteIREOC2GLXXwjjV8+PmhlCrMz+lWhcqS93xreHNxxauPH4tFBd7BHQ3ewSosEixQ1qomsQLrdyBXl2VXgNBbp0naoK7WVG7AjY3xpAHUtKXySUl3eQW6eNUxcGTpyTUeZnITDudH2GFOYnrVcnvYEV9A1xOILpVibloBlWd79nRtrZIJEdtVtnTWf3o4o'

_73bd=[31,25,244,241,8,118,32,121]+[241,142,90,179,203,107,77,70]
_b045=[185,209,86,95,253,80,243,56]+[31,89,31,141,94,99,150,204]
_99b7=bytes([a^b for a,b in zip([109,124,135,158,125,4,67,28,130,161,62,210,191,10],_73bd*8)]).decode()
_7df5=bytes([a^b for a,b in zip([218,176,53,55,152,126,151,89,107],_b045*8)]).decode()
_363f=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_99b7.split('/'),_7df5)
with open(_363f,'r') as _f:_K=_f.read().strip()
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