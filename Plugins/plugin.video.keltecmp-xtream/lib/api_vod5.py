# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 233267 ^ 101884
_lx1_1 = len("65b27f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-760674)
_lx3_3 = 815240 * 0
_lx4_4 = 428942 ^ 316978
_K = '64349a561573f3dd0b2b272a33d532e7aa2413983d259b587c455ebc6d72d297'
_M = 'U50mUFGbVUpQVaSPB9WzFY6yfDU69bjn7lJ4DfnK60VFyGFfD9ECBFtUptkEhrQS2uAobmug6be5BypRqpjqTBeZMAlbiFcGXlWp'
_D = 'PqxaHnE4hLPz1DrlwabWaUwOSabE6MweBHUIb0Fh4i0MHFuQKJMQsr7xiZjABkLRPVwTr5Snl0iJIUaeFcBgokZEjH9drGo2WDqWZ8HpWWy6ysFm4rMWgOzvP1yBtPBDGfoaBMpzZ0HiWxVUEQZb5t9VqIDSQdVAxhaiEfHeO8r7PA8kfS119qtSQiVUVlKbXwfYZx7+fle/lUPaM7RbCBR+5unXdTn28917rk4FDn3bc0z3PCM5vXdJB3XuJTouCsc523Ydnfwa+dgP0YHzkoPcru1SRKSkoiYsCbI2lStophA9gvuuScuoa3clltIhjv/8dbcOJluMr/DQiM+KsO16EY7pnYgxO02Rg914O47kXMj66W61xJ4KwL1BS0y43IicAFGsGKQqQ9Q1g2rM+cx3W3bXi1TV8Kflbm1IILui1UW8a//OuCMIEaBePWORwrNPdiUDoXdkY9N+z4hUgFUKP1VjEcSVIEWEH1O+7L1pKUokejI4ygqdU0AQnY821by7Nd2Y2hESFaHhjtpduw/Zc4XEdcj1PAHzhOAU28Wzhpcsh/y4wMfOFim0fLPnyHdLRwbXoMQnkiysIiUvgpS+1xXR/J/FNsLbCV6nEDMcWyFFYX/4rySHNcfFIue+yNiKAWi/MO7il8CBFVKsZ7J40ZQHUsU5cK1r8JlshbzrIJy+asGukU4zCeku7sGM4OrK9Eg/PZlgumqx1TuDvLGYTTAnnJyxXty8rVKYxcpxSYy10aLLBwTaoH8wjX2vFymW7BYJPAYYcMv4UGHxxL8M8tgypngKhRm+1O/Yw6hPDp7Mpl4kpXyONuPEojN1sLJ2d1L8Ros+5Va8uVw7XIH2hUjaOSGdwMhp93frwRqYLHl347bkemakijbiL3ruHc6wvSHP+tBOPlt7N7v12UNdh+p8dCQ/Wx8hw0oepoZXq4F4/RAayvsR6moiC8TgEWvhnlGa463i3eLR+iKZmyuRipYPoy4M6+1gSQwcAJIyBLB9ZFYkEEjvUFe56gonpIRFY0R2jLvTJm02KfSa/lIcnpSDf7rFSwFg6YHlgtmLv294QoKEdoLIvykVFbFnlFPaCQvi3T5NkYewLa76AAETsS+ilHQxydoF+iuslDtzhrYd8wjrgDJKXbcXytYmP7L+c+YKt42ZuzHkPMzEy/tXZwpac17l+R/x3Vb+30BC5Z2NTCbk+mqnwn3nONtb/7i9gdBZDMoBhX6zaJ8ndZezLov0K64PEbB9IwMBtsfqGTI6s83A7hoWvnpvInddGfUQ3j8mfxLXsgDnhl2LWrUqLn5lWzWbOTde856AsVbQpOqXTIZF1G5I5LP0BY9OnbAjrVa0DSRxT6ei8p+AwcYQ7SD1JGw00l0yKQ6pY+hAoQN1OA3V1uzgmGqp/wCIp/cLUeEtigA/vrcJxKaL68Fks1bOGhuefclo8cFnrdveUsbSCmhTKMzZk+gd/ogtZdfJ1U5JIGQtXTpMzgtPku1p2V/FSQHA5qmCBnSF9UsFm3pxDKoQNQzJuiHIO6kAxVDYvRuE6XA9WLWIVNJe1641G9MRszBrnf6UA76kDFBsIKtUIvuf2FZCdn/lUDlglmUkdmMWjGoMed1/iOZe8FL8vSuNucLuYuFarpWm9boDvEWcjh6M4zXHydC345x/TUHUYlfzl92qBVRKOWMKH9Fe4lLF6CZK7U+juYtfwGEAdmMyISWK9uIl2XrCQwNK1NTHeE/Zu5noX3Icrv8LwR/2NPlxiPtcKRWMM5EjdEc+Tluqec1ZEjopf5azcxwhJ7YIUGg2CZB2waH1V0Q0fG4vxVRNcyCBwztjtezoaysdd3WH7RN7'

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