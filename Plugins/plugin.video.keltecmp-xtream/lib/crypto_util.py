# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 864158 ^ 747657
_lx1_1 = len("f93bf5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-621225)
_lx3_3 = 134534 * 0
_lx4_4 = 700716 ^ 599438
_K = 'fee23e72193252ac8b636f81328eae4a7691c8ca91ac70ec6628d36a6b173d00'
_M = 'LVh+LhqqGcFESrfE5AHDBLnyPzLo/1G+NmXniVsbbwhnByxmSK8VykxPupDlBsIJ7KZvN739Bes2ZbPfCBo9XzQMe2lNr0+TThy5'
_D = '=83Wb4GyqnC9QIKd8WvKOdscHpNla3W9LXf35mWztB8tg9S4SYPqy/Z5+5WZ02qHcCUspSXqsPiALQsEy9zYA3Rgdb+5hui7Ud3zcwDBEjev6A4JykYVE7YLcQbhF/1Ihp1kDnQjTcw18zUm9m60hESUadrU3Qb+Kpa1YZKCEEdEdxOhxzHopGS9Ah4+ZWQVAXcQptCZ2OjK2iFFrU4bgmAmkYzyCUoU0rukPithIJ9S/bh6SBUZzqVeRXxpdqU3XoV6ax4gyWAU9JOXtYWHG225CBpscxeFiaouVA+QlfTchC6SfE+MkWn1KrXxgnbo6Z0YR+sEj45sOO2dH9dxx3G232erYpn6lwZ4EWB7AQqwv4isp8CTRG8ds6STIAxQhtsx9ITX4j+uudt542C3qrASZY9k+mZSoi0KhCHuz2RCtB1HoFs6ORJ7XMic1q7tUXwMnXUBGPj3KVZJIm+NZPer7FyJfWoLRpWGOaOYDi34GyvmPoiWsDM9qiWt9Ifi/hBZbIWPZXO9SgVQIF+e3vWTw9sZeReK09NpQo1SIjbsUU0mkCI+ONPMJfpu94t9Yc1s5e6cRipHMCErw18MpO8BtmT5hjTFXQaSATDWxB1IYWgy7/CCdVOxWLY8FytOti13gXGq6Q15F921hJF0voWH6b/xcGYxXTgOTcXJfyzNVkTD/PsTfggjYUyAuuUoORSInG3/AWca8gPBexeWdJZdrsTWcXcNcmuR7yo1HZZ0MJ8Ux3fQ/Qj4r7vyTP79gEcMiweKC2DZD+d6Z52OGV8Oogj47i1LignhkhO2YRxp9B/IQY6gppgmUJRaqCq5EsP9ct38DWdGGNfM6JGfvqtP+9J+0uoH2EdG/9fu3AqdgitFM4Ky7aOHvcMr9XC4QTFfbezNdMDgU0qL3lem9XcmIcVEPCD5zT+rp9gp7UbT7mGmTbInqZIf7F50ip0Hn/bsv2/43Zq7BCZyyEGOcSoReXqQhesKkKnYGnP7PEtc6YgC96P2Ho2TBPT0FbFyjZjVkWc5DC8MX9J89VLuJjdL49v32Up1kCY1XVW5EOu4'

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