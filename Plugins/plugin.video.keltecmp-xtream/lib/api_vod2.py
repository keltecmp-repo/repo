# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 757577 ^ 992414
_lx1_1 = len("4a9c0e")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-295233)
_lx3_3 = 236454 * 0
_lx4_4 = 563861 ^ 189045
_K = '76484e61bec0876eba01f9ce1b7aacd1afd31ad59b6d88bed59591ef8516f62f'
_M = 'EqiGqd+GhXyilWZkqANSFlGkax0b3H/S8yUJixjc5OYLuoTq29PWPajCajf/BFcVUa9qQUvVLdTxIwyITdzjsQq5h+CL0tU4/MFk'
_D = '==Qd2fu+Z/pi48xqhBcZdOUqq25UzILymwt3yHLXbJUj1IzaWXPJBUgzz27tWHUt2dDzucHqLlri8qisZ5vZVat5cvWSSPoh0An+161Ap9d2cKzaDfFct49pYiEZd/YB2r5IWD0zFcyWdXJyHhdRh6pRbu5itL+0da5Jc5ViSCouvdSozhhCZe+Sq1IDSvt5JcokSJ9YqI6YSOkcbzPcnkUazFmZvGkB+hTJMAtLAiHAq+WqP5obSD7r8pev2SmWo6Y9xTobJWjeJel+e4rFSlMt5dY5I5TkkoeXx+RXA52aySCFhhArMND1KUpzGNNx3173f+7CPST0xDvhOaUO3fMATCQ+nJlfpCLKeQ/UhqLspJRpzpGkqy/Smf/Tgjvu5jqZomoRwJx3XShgij2XDlrvlYatGPC+Uf05zbc4CGojQ0ZUDPxa9sUpgh9AxDdijE+G8Lz50Dmv3+BKqqNKhFW7XWJrlF41b8cSJCVjNfVanQJGVsNjmMwDEBvxYc9hKboNSLOr31kRwbYMEsTv408YLpIgF+pc/R+AvS8txIfeHUg5ZkthMAhDVFR8oyEiJDSLeWZ65a3walxenkV/3Ntbzc6mhom1GqtzesM5cohCdqXMp3RXjLvB5CWcOVtmeEsxjorHJZmflw0Ii9rldzqP04RxpC1rzF95MjAKG7XimHQiEXyCGgxV9UGTT34C+SIWRc/mAYheb0YIHj8+1FplXgCFnLmSmAccmffILrnyFtPw8jL7GqomN1qULDIXxsOdKsHrRNiQOlrTuhfTo5VaOE3zecIBNTCeO5OwoMN5VlKqN7tUT550x6l5jHXv1+U3Bzh6wDt7GLAz8ij4sfHg4fss02C58QjIZTNUxZGFTk8Rt3dZKMZMYV/1tEY6beIGo9bxDOyjAr9Hg3qWBHCZ+o/1fnLFm9Fwp5APaPkrMXgPr99zvLOrQ/PofdLjxv8e3ABACi+ypqCsLXcGXkjL3P9WvKjrxEdYDVw6lD6OUFBlgVlai+wf8sm4QtRv7OxAJUlS6XgsC2v7WiYsMzGInTSZH4pCd3fiemN3R4BlKr7wED/a5A9BOUOEEk5dOrRrg6Ok0MjsbGqo5R5W2zlIQMQAMqvlUAoNo/ZjdFscQZYhK3LWCBbnOzw0JpvBKxJ9rh/Lp3t6utK5onh+g2xs53Z4TQLSIkc7ufZ76gP/nh8SU1YceCfHdtohUZqD7+OVzet7eF/khBisevoNCX5yi1z4f3l7MXJglocaU0YOkCwFXejDtpPz1wqF4GkkE9DY/6K8PPX3pxy7mWqE0zTxj0CONQ1KMPzqwJLsYlQH61x4fm7fblcFAtVicnzVPg7+kron7caq9kkAHB/jz5dIKDa5qVATXwcfORPiwv1uDd6e8vUwIWtp6W40ojIAV9O9aGey2IoS1frHR/G36U7yStM40Wa8sh1f7Moc72tVS+8TD3Ela2PWlCPuh7jiIegmqae683VrUpgO7Vf41CSWuNEuQBG7lmFJf4BuDoFNaLRj9EFd9MPum3gfZoJRDtvqBm5vREEgdYDd4V7C1KGjWRF1d/OZf2fw1Ij0WWLhu3CtbxTj71236AFTXHYxveTscwPGuMwIPu5dD55ofNn1teNu3FXXFyBsrMnKprWigxvz'

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