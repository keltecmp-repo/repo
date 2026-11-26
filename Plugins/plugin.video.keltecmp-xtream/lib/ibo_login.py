# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 506265 ^ 482352
_lx1_1 = len("878ece")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-382185)
_lx3_3 = 903943 * 0
_lx4_4 = 213449 ^ 581894
_K = '6625735dcb91860038104c5b28709ade336051cfb527624525d41d8a07fda275'
_M = 'x0+OJOq1ar/iFg=='
_D = '==wC9YzdZjJez66f3G+BS3f7UF5EHcdeWWND5PVNc7f+55N7H9cn89Hsx1vOktGxJKjMNKxrhAodRu6Cfw8CRjl7bzepoZT4GC0WmtwAX11yBZtQvprUtswq1eUHUcAARV+d71nlRXD2zqVN8Ccoe4GZIxRoxt463ghfykCxwY3YxLSoHF6xEObXOsKQLtrgWBhs0HUxhF5sbJnb3sPe6RdStcJ3U+UfnBWIBUXz9kzx/iTDrEG67vAbukpjVdhvO6BV9SbdCnjSkjTX+9hw74w5BZuK8zweDAphzeivw1cOG0eK/dkLHy2bR6J02ltXXBt6Ld4/y1lw2iLOwPhb0JZYyvsEgakPllKt1oPTZLNa2yYQDBZGjnq05XKnwuEMqUu+lDit3ACGYQCrepYe+WaNjW77xaD2vqHMJFWTXkZzn2Yp0+w/IHSKYVUhwy/8Ze1c5Zs+S+52E9yEOdDX69eAGKm1+HRdZYj29DBt2BRmTQ1qHVl8WB1lC+lYwqlMs3m0gpGiitV5V6jnpUM7BWi1/SpSfaIq9M38W+28gm/ABPhD77qAIOZZKScjjaTmloDfdOnk4QWw/302mP3i1Vex6vvcLFR+1aDoAAZfepzXtLa3C3EH+8dP+eUsnw2H/baTyuAJ3f2+3ywowVRcovEjQHy/a5gTt3FA3zdeXboN3Jwy9un72F8cSY6jWrlgCjbYndD27AK/UyuqRds2vRq35aslDyQZwy/P+DUt1a6j0qeGOcJSs4zG7Q3zfyXeOP9OHoxJU1rSEfMP2pArF/h9bjfBteEGSqp/n+LUiPKbE04AO2kMy+X4gMBZMev/KVJVi53W0mTOP6Nu8YpW8lTuwdrUYdDJT0hAxUhpDhRXHxFl0YvBxWdFm6IBrFx78ezBLro2PG671jThfcB7MWOlpWufxFNrGgCO+VN7AnYdUSijVTwWldRiAQjioCljXGhc88WunyiXfaxLGvR+LAmNddx+0XtkuyAC5Pjizb9/fpcBb82UuMInSJ+5bToWaoNv+KbhFwnNbttnQ/yTqDKBJy2nbavVYcVpSW7q4yZcFE688EDYOKolzuInsVx9cQy8TLov9X8l+whoFULzr23c4Y3MsCXO4mqNHFZYpFL4nFHDWoEkmzLek2bNvoZhD1gQGMvUW5KDrTO1DE0qmgaxqi67r1OCg44M0ZfZiZ+JqrqlVtbXfXgvrXfrGkjwPgvlGCUrAMoHgVI87xlGVLKR1Si2Dyf/LliOxOZ3UcaXZ5Njf/zs4qvzYvc5lAhApo4pKmBc7Aac4AB85fPTynhqwz/XhqFzoirLDwqd0Ds62xu6e6mEkbDkoYxbE+6SmZXAUaSFxLA1M814j9u3DW4Mhl4WCOxdJSeumrrQW8t82XBnP9bbKawgW1vVQmmBPVW1nsyW1PAHYeatCtdg8J83ph2/Tlyr2mHOaMuGABLaK8yH9cTAL69heTZn2VlYC2iqI0Wo3H55KuKalUAmxGPjCQjGruwG+aQ3mqOReCSV+CQyz1z6YNJgiSK5Vc1rz7NNqwlJvIVbACmMZbiF++b0kIQodrLHN0Y3kPiCEu6SDq3UU3PrbzSY2S5hmFLUszo0gFAxCLP3lf9faOAs6XuaOd2/gIDFoXxyRleugBXwpblNKlnpCadY9CHEV0F69PuFWpDc2tTNzNlyypmmVdi6yKyJ3JcM4Tc6Y0xwdffqEzrtDO/L0rNMBIZyReenoMTu8PUHGhT1kWwuc4NAI6+4D2Fct2vmVKiaZ+2M3VAnAoCM3UmPo+YRVl42Cx6HKrC3GDVxGB7JQZLamBe21RTn7cRG+W8ITqBIptYi'

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
