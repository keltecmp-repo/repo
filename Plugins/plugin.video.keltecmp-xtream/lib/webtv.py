# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 404004 ^ 177284
_lx1_1 = len("986024")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-171388)
_lx3_3 = 813503 * 0
_lx4_4 = 740231 ^ 592691
_K = '9f17f0c1fb154dc2bf73bbf5dc82527869b25a7cac280ba333e43969be8237f4'
_M = 'km4J2HeM3L9F/t2AGbzXkXyxyLDFhiRetFbZqxbH38/CbkiCdI3R7En739EZ6tTGLLae58DRc1HrVNalRcqPncUyTdUj0YDoHq+C'
_D = '==AwBH9Yp76YUXk/my1XP2O8vzj8B+1HdeP0moG2iWuCwAYutgYTdD0z28M2Gz8yp2JnQP9WyGTWS5cWV10/2yjhmBzv/Ko2r9dhgKzE8/Capbex7NQv2VaLrBSLlTw2tp6xDt22NVj5AbSF5mbcXrAxUd3hVdluUZY5///wtwRT4WtC5c+EvIkGG1KTRovDfvuYbkI/sMyHBRkQgVQCbeis3hDJF7C4Ab0YCGUjM/7sKnKll0ZuSVmd0xO310sNZqTWbLG8B4sldbkBLJEbo3ryrsbmyDHggpH9jrx4NX7G+I/Sc+AhBND877cQ3yQCDi9XuV1Gs2I+FJjysRKzzNSmCjIh45bA2UQt2JYuwKpuwQeSvXZe+npB6ursIWzYmjK16uTHe6k+ricg5SS4PD0n6OOnKVCtEv7rNexCn6ytiTS/liPSbNKp8WzAN0100byDZXH0WY5ljgQuJ0QZUPHZKvmnBIUBlmb2BqF9/7ktLOckDFDPVHlKABR+cUbdzbBDYbp8E38Yajtsop+n/FXalNAdK8UJK+Cr9FBYSfls9+mlaouMy5CdQOJ+LD/gO4c4bLd24LnTfB+/RcGPHhxtCLFTpNclThs1s5PadEIIdbPZyAVc3/HZGWBkwfR0q+Cnm6Sjvna6CTDmr/nOIAdVesbGYuFyptI4je5LVyZTZXHTLtWm8Vrb2A8HwyUaXBGtkAXdCDQwia7EXyQmdY3omVIEePqDgE7CgYu3Kp+Y9dtklVWqHmki/RjrFFNnkCxlZx4Ff9Z1ybC0ubCxb8TnhwFNsWPwKgy2jDDAL0KR5qTnTQAV6IRPkVHdTc7YLzLXZBPfvXjsTiLYRe3+hW4bLypmBhoWIMRoPqGZdeAv9/XOY2nM9ucFzlMzk9siztsgJXcRCrvHiTtnzxalyWwFy1E2BYVCeO97JuyzdefL2dbprEdr7WjkL4JMewvZneZeWkfkuGWdPgtd8h43FZeOvweV5PhaW2UwtWIQqWp6x5opTRiY9XWyISPzNTF8Sb18sUiFsybrkatgA9L/k720Yo1CPxH5l8d9sJTEdsMdepi+goDEPG+kDZke66oOZ+qKP4WqvTjkWJRPyUlygad1PSn7SLc2duI4JpI/c2nEcniCNDX/8hjFbbRVATI+RCgVnR2PZ5elGwR6r7EnA5pbm4XCv1qoZP1mviETl1t/7NJCvxly2m3QmeBMWbAITJgBe6CxGx3+AYnpzngc09J1bsdbP0bqhP7ffUuZI8dYnqZYvmfDhk1zOnhjEJYMzwux8lG/5BuX1oSo7Mp13TsFFx6FttFK9X2TNjvgs1tVobM8lDr+lgquEfa/OBm0nQA0JPxi8UiPNZF5mk5+tWl1um/53cNmqZVUvjLGvrCQptjUimmkDKwDV3lDErQeffDNjQsh4+HHlf9Yqk4VbJ1yQr4TLA5ph8QbtIIVO61vp3/BbrpLa+iKm3R3wt0w91On20pqzhrB3nTKqjggyuG4IWAZPFk3vEDcZtmqOkRvLNDJvDLAujA8TT2IVYZs8YJ7OoAn3uRQffmIPPaR3YNwQ5U+YMXc3YdBCV3wSNAOLkpI0z0BGuvPvbCd2TzvcFpW1xse9Q0SWC5Q3sGfR4dI7td9ZzMBMj8W+/TLsTMFoa2vdvcJQ6+JCzN6gZkDDIOV65w2qBpw4pkahkwESoKLdxnQVQvvTeqCvKXcQyVfWnx+4DcAD4fvGvwEYucjYh0qCCkg18QuZVA6pG93j+TkFmcT6F6HSbm8ED1IaMy/wuN4gg6r+OfD5a+WeW0ookBXat10/vZPn/anp37uIO4CdOmZEJvTxZWEC2RG1u5BO0H7'

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