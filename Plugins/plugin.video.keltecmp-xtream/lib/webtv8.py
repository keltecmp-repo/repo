# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 217961 ^ 982789
_lx1_1 = len("15e07d")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-756288)
_lx3_3 = 508302 * 0
_lx4_4 = 982527 ^ 713482
_K = 'ece4eb5fd7d3e80993fe8460961f1f16fc011a191c69948833ef353b6927700a'
_M = 'CAhMVGWJoMPeMs+zWKkgN0jiysywTYHXb91nZnebcQRZHUdRNNLwz9Ayw+kDrXYyTrDEyb0f1Ik73mFkdpx0BQ0aRlVm1fWT3D6X'
_D = 'g/G//jdcX3y5ge+9m9ckzjQk6cKSz76l1ItY9LJ6lUaeqxDNFaxRcrX4x2XplvxjjDzPkj1ZBTDPho+82+lh6BTNgZZC6C/oAePhqtCr4yWzX0HOPaw/a6HEoYwC5ZKL73VfuoeAw7g5lthfB04fkHOHHldhXnHVprikSOzL/V22MPwejsyvH//vFdM9o6sxQ9Kl6WOWDPL4ojx9FgYRpMrD6mbf1q97VIW06WAImmcE26M8Sr8Isye6A9Do9M7MRfx0GSMrmBxcRxdtTjH5e5GH4DU3DRvd1fA7bxqotzDN9/d+tPr9PqLYnbsT/c7TZFeM0Tsxkrg9MJegWzWy0QeA7NHcArQH9cecBEo/B2scasSyHnGHP0dLNqm9eEc3BGUr5z7cw7X1tgAenMZiVknJR09f/lMlMdZD6CHDevWQqx3BrbxpNA47Q745Pn8Ue6Kz3qfKTJFx92nzw4+YidflPKsFmWkisoa/g7zDYsCCdbHLkojc8TdWx95qOwdyfG31phKxU4j6mhPw4NEENLSY84ZEVCszDL7qjJjZkVtu7PNPxq/i7O1RDLBzOXLHkditqk/C1fIatP6PU/qqDvFybV24/XCXoZ0j3gOfcTryEIjKX6zjQHG0PubSJxc5ah6ccweI9VGWAYFDmB7PkDuEnOFaYSv7DYzZYSK7kkBlXW0ApNObdINJL/8drjdXv7Xwiz93LVsvpkvv0M3Yoq+nAnOiSJENS2UQQArG3knqMkOVfmP6K8mzfZq+o+EsSdsIkKyl1/oBj65vWrat4oPNwaGBSZuisadSY8zLVcfZB6im8fsdm2j4lNlZyGX4P04grlUucvDDEIEo9DQbuhB9DqVlBV6XCFQsxljmDbu2U9hvvBNQahlB5fFGe09kiZnDeAjVhNW8BsNnWl1ZTI6P4DdKV7LbLsu/RfWAtBsegmUSiaYwuH6EcD45FgDUKk3A2Jx69eUi3S47XMx/tH/88KKqZ/CTYmUSMotsJwHiD9Vp1d/pDLISEqo8jTM2HXjkwZ9/G3cCSd2XNdP6LQS/jg95FcyolnBhNhZ/NB7JNrsNkHzl79QkhVhx5McrHufXzV0nzRaGtRUkmGNLO1qIChehi976gndIsJY0DuDOiAB9P+KxgKrRL/cdXsCDAbJsJ48c5iNsbWb4VdvbhtlfiBN38kLtkLxd4Oycj/swLYN9Yw40NGc30fvMg8Re3Fxrp8MBqiJMsSf3oESQB01q2BFy9Kg0OYgsNf2nRew72A1VUHqYHj01MDtNaWNFIRfYqbNZU07kCzjsz4Uy4fXXpPkj0/0MOj5iCU+Ivthzt5iv7wIqgzEhNyRNeLf7uTv8WH6OIpqnAjVZPC83Oizdu8G0D2VH0cGXhNaP2hfRwzbpm1F4WYTZ0EjYgh0/c7eNnvaRHl3qjPmuNXKHxDaN2HHCHNsKSsUXhSkoIOcF8BK0ExO33mw4wTAxAQaISg0RcjtQCajY/waFFSxNn3Gkg0T+sqkn6NbTwxsaUbyyvfUEKTM3xbugAOMyaYUytCRrPFqdwnqdt1PSD1QAz9/BthvDtWOq+gyrAterBSGoLRB+TmG8kAjw6uVxnjivBkVK3QaiogJ9GRjcnBsKJv4y/LIAkaj8W6L+372wae40/sZYK1F2R8KFSe5zEM0S+jOyTni84oi0mRXYpEW9cYJ8SM35455/UoWBV/7WEV7dHclUOvowXCzQHEXKmFiXmykM9fa708pdcTX7hSIqMaKi9jidzgCWl525YqJo+0oKIcaHO3vnhgMwFviO0pxVoZs/ASb/2UaC+91zZ12L2suFe9qrE+WhdRhuPcAfw5h7'

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