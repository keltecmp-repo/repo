# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 662759 ^ 347303
_lx1_1 = len("73e03c")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-509183)
_lx3_3 = 134104 * 0
_lx4_4 = 391315 ^ 613299
_K = 'b30495e2fe8b45b7286d50b7fb06fc666f0e8c796fd8756c6ae42c4c883ae658'
_M = 'uh/T8TmnrN+bq+AF6H7lcsYN3OGTnQhxUt18DsDX+cy1R9n9P+TylZX67gPqcbN9kArct5jKBiVTgS8NkNr7z7QUj/U3tfuWlf3q'
_D = '==QnW2KhjOYHgXCNwwW6JexkkUnX8xDhb/3WUyQRqfrsKNfAwRAPIrN5fodwlOabk4TXUoCswW+e7p7YLtDAtM0xYGKrAN4n0VKhHMLCVtu7CeCmVx6fl70Pwb4bGq6Dt/i9IHtMjj7lTU1KJ4vJ0BYYbHfR5WqfJIC/EfI1rEJuH80lYFlbhL9KpwekQQDyFvxzKvDXjz1+c4oCGz41BCrfgds63d2td5Bu6vytrHvIWDe5JmwUhRJ8g2KcawnMPrE+xEU3T5qkNO9mPzG9089lPm7GGYSfxqc8W06qnXq6RmKVa9MX95djXu13AyKXEI3SGE1rm6EruLaS/NFM+sPLU445IKZ1s64pI8oL7LiwIzVti/Vu8DO0mRBtfsI08b8ib1+5eOBi6J7ULNjkC4r17YpL5u2pi/B8ErJvNXjhV+my+sVe4d3JpWnWAkLzTcQ3NOAEGtkvaYuajabmOKfZ5+gqabrGdheq+zhESQSUzJW8B5Yh1rLkKxs0KZa+XsP0hpdfdEyhiU1gfjqqt7OTZzmB4245hVJFmQQcQiM77BDOE5PxoECgm8uD23ZCeWW1YSOkQyvh7lIbQEIvG8FnrVUp7aLHykt4JNpokFO43fUl0698mDT5AY71KPgdG+S5ZgKC3fqJim6bIuDBS4PyC1QV9scnPjlB10ceI/39PwdX4fQgHUfn8DLMj2pezNcZAWra5RHSJqxqsM9IRjA4CooAN3cbnXJco4Ja/8YhCryNfarlHR0OBnu5T8UnkpxoCBxN1HGcJRDafgCHYTB/oiJ9U4v4xDoWA4HevZCJlusbtTPFmerzZj0Ovu1/BCISFIbHqNfxSFY93laBOAfEOPA17RGg3YHwHnzlKPagVOSsndbu/FzOpuIFOc9kSOMJVMimqVBQBXcoOQ2S8GuKmznoKPfXnLQ92pgD/N8QeaAC3PtaScyTM4NJ6SKgxBOJ6A887/VZD6Bm57sqG0dPVKUabhd1MVRsmyFYjDahhSM1knQqloy7O0GuWkYt1VwReRT+hrdTpzglA0L1fyzHFihtl27uVhHMtZj8K/MPaYkxfoDeJUM/AmJKEKWPfs98XkW9a+b2CMJ13G5koClLer5ZNC7RJ5PRRE4D7T1gdaoydTr8+LsqFyKwxBz0J36xA6HZfJpAOW9ZiwxRyBtpee1ie2lB6ZfOHkHzXoryR7eW7C8JlcflrbDZt+zZ6pVYQ8j5fYtE/X1hPkBEEzq9P07ZVrj/utDfchcHHGY+DCkL6HR+kAS17OHtUAOMpgKiru1W+4Y65MpRpw6f2aNUo5OtxLJeFA/Myz7ZVSE+2l4O+8a3mIl7nnEOmdpedYebRLuAqM40w+ECPz5uYqrc7OVzcBEHx4UpHoVaeTaLQLwbwosgv4Xcg+9pBVgNcuqzBsyQs7AaSpVoj9oMbo0+ixsFMMBlSxkKaVHBwO/lilp4B88HsRER/PUGxYjTEV4H+HkJwKDbppmtvwQHeLUx9eNM/L15sysk/sUhc1CigyV2VeTygpjBzaG3djaHOqGtmqurhNoP4KJPqsVqeCEqJby3l7NPdfhcj2X1nK5dV325g9Aly0EWFmko6kZzX6CCR2cUL98+Qwv1vJ8Ip4gXcbTGcRbVdi65QtYjPJyWY6mot/l+qhoOKW3pdPYvxDceTKloIXORHY2u2BnUKdUkNGRjyLiyjItdgKMd9JfNXktbmcUluuxbPLAtnl4iusv5TJQiTL8kX8va1wEqbgZGbTsmRlG6cZakb61U1mqgjlSsogsWg7bcypLAde9DYlzOUu1YTxKaqYXjcypiO5oDcO4iwKbTqUGlVsWRv3dq77jybiZIMX7HWWin'

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