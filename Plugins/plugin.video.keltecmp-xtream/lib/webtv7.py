# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 134170 ^ 769736
_lx1_1 = len("e0ff3f")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-412174)
_lx3_3 = 221630 * 0
_lx4_4 = 201988 ^ 590240
_K = '054cb0f51de29ee0c0c6e99c8a2b339fa2e2002002b62f2f4a3e9c83abbdf7cd'
_M = 'bgLQtth1rjWn/RwK44/CcCsNGi/I/UIjgSXU2BzHg+5vRM7p2irrdKz/RQu42MZwfApOdJ74FXGNKNyKTsLSsj5GmLmJeOJ5/vgR'
_D = '==wRTm0KRetdvq+1TQkQB+OegGRr+QYSmZIU7hrb/GCsdaD5yW6SWgPNj9677qo+AR5u/O7jpPOqFACRJoSXECMEiwIjNmo8dEXXE0/GFBHzj4po6KEhgwio9RWGuUpMEs7/ZrCp3aXPGUtyKmQcbJdibL2NZWEKKluTdpa5G1oqc+H41ENF268H65Vlx5WrJBy3GR85URy5JPvxQUd9WN+9N0U943CPqHWw6DiFZk9pBAVlgTU7mqL3gkIKy9Za3Xk6G5e1fd3A9OLBK862y3TWmFekXL34iiXPIUAQmob9oF26IYHfSlWLzmtRl1mVhdP3ZnxfC8ircKUXHgbRUsHTjk6qCRbwNRdgd4rpCd/9bl9J2kEHUD9qQolFMdmUnUXTNRM4h9ZSghk+/cbxkrpp5i9BKBfaLntCEmX9r3NOhc1/y+eb9agY288sWD60KlhF/RDZHi1vQcVOMLM7U4W4E6EMV6jCZKrBSW6EdtjGmld3zwbdABwzrMDv43R46BueR1wLPpNb5rDIzsz48LzOmOfpGzohvz2TUeCzuI42idQQ2Fjmk0Zv3jJAtRHZHNBVo61WycZaFiugtz2PyKjK/99sOfccz9mcRfHMQCluZ4PNInEArttdgr3Tr7cxuRUO9dRKNXYsqc25Kjzgl7i8VDENTDd0CVqVknqhWuSm8pULiqx+uHUWGSg3KjgI4nzFKIvFtw2xDXX/K4WosWQFCCwV+uEQYmUVMw+wN42R6HSNde1NlKDX2oAP8xKPeuB4d6paeYrJ9l6aergadptwN6OwpW9X7Cya/EQbiRHMwMVQvbt6AiF4EJIsuEd8AmeTSr/s2YeZzg56G6n4yEO2KjosoQFCidAFW8KdGQzMJeC7Qgk2ZJ2tftbu2T5+e9E3U/07Du5GcDJ8bqSjGeoMSWNl9LpMzPGkBSlTOaFidWMj8Ru1S/AcFlDykKbK0ZB/wXzHbaoYEstEq++4C57vKKZjFEZEp+gMBY9r9hbpOOQvlLA7Akia6knt0UWfhrYw2Zj9juYzMgDTTujyaH7DGnuePTZ8WOXlvVjvNbCmtPoBSkMk/cbU1Nw/4Fiqe7JKTp9Oo4unDC95FoQ/1xeiBwyu0P2dEpitwJURrnKMg22X7gWVJscIzlZiabMkwBJpsPWbIveIAmJ/KhNZ5H/f9t+OsxMc8IMnJGuLh494A1CzpjXeLk5WqzWnxSsv6IbyzNi1Kq/Mk5Cv3PZKl5axP6rjRz7V2NwoZy7DgRNJAm8XRO7MRQocm6o6uAnnEmHTdELfTwv7UHuO8UiQovZ8mgpZuwDbWpX+ty2vtinOnE0CvbTnbEwdhCGa7I0pJCoSQsRpp4La30VO7s6dkM98XwPY6Pxg9nhrvo4UMMA753S9XA1kbcIDUwSNm4bRZwRBzXZqJ++l1+R+2WZ0P+9ImpHI2Z3WILmFfNrhGTQWsZ9NE9OXXZV9XKQAfW/UBifrcaeMqeROErfdV2Yzkpt2St26lE8gQ6I3Z97O/TRuJ+armTwJykwJhYsAErj2d13Lg4F2TqXV4ZZdEGBN1ERvbfBib09P40nQdGxba+GNUAeWAtzC3qNsladteCLArWXrSid/UrUskwZ/DFlx/rRFbtkUDhZKic+PZZfN2r9DblO+jxg+rbpT9B89TY+8IqPXGJA1ZHBrj/f68VZpII/7FtBw3m3Iklwt3BNadAnNsWp81iEd4HyOsZX5wQN4LhehexAIXh1Af618G1nqr74dpJaQreLut0VweKo0+WquxUnTJ5Q+0ggYVcW15euraQvYtZMbC9U3s/fpbpkEnah1CwVpUQttY9YdN6M99M6RtSUSd+k7'

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