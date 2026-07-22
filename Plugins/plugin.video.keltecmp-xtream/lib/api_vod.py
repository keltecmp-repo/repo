# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 290937 ^ 276874
_lx1_1 = len("545e09")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-938032)
_lx3_3 = 522292 * 0
_lx4_4 = 996746 ^ 793015
_K = '64c5c6c598bf38dacd9dbd1c374ffa8a4c0f5c3a60050783e0c3e214b54ce788'
_M = 'Uyg7AcngVWakb01bfZ87E63LGoTzn0v5lLcECMgB+3gXKCwVnKFaaqw5TlkozTlDrs5H1K/ITv7DtAQJn1CrfkFyeEmdpg5qrz8R'
_D = 'cBP95BO+/6np48VEQxxGmO7j1yXMLNlYIbpedhlKddK9PscTb0mYEuzWrSnkgxRGWvAQWcJpWXeK/ZPz814SZ6aBMSCcQb9vOX2Q9cbOnIYhVEN9mdlTs3AlKQWm8aZO04d0JPUP5cHJtPfafYqAMA1UwsQzhkEf1zh3wmvUGLkFHfbsaTYgDcpoM+uJYl34YQjAG4fqKV4SQrcApG/whb0/MJn+kQ1abDNlmtaU9M1KhEcBAYoQBLa6TeT6vXiEVCC4QyqD4Y1zvh5awi4KdJOqL41CA/LwoJcA5lTaMl2RZjK3fGpr8Jn+1tOr/LQwjYAqa7GxClbp5KhWhohKTF2hzVDoeBBuDmZATJvjd+lRgRyvPaEDLJdN+CZvcQjSMmvRh0wx1tAUK5uILBVp/jqioEYhYkytCkMWKLBQ7gyan16Gshg/9kCgLSsduW6GlKaQu4kJ7kZwFyNnucWVgDiDNWoDUqfql96I1EpTVhEBQyduAoSbWqeR8MNzXVqBeAjJNjz8H85WgITUObNKDSrvYZF12ov0fx1UnlpVhv1HE4VC2RKG/tQ7OawLohUvoKkq7N0O9LGSZObf9w8bxfhy+vuBIXYp37VDlDo0zh+iMG9l5Ejp5ilOF1hyAI5aHtdNHp8+jtGfZ6Ix/l3ZVGXxTLtXCJROFZKV39ywZOpWJqYDAgM1EvylT/Nya8Ph3ySZn0hmVq0T/I4pwaOE5umLw5TnFBN11oZrz8NWLpMoqVESE60sUlmG+UH9OszIkcZNJ3uWO3iGwo1YNrx/2y+Ik0IlJu9lQqzrBbGT0x07lLPVIEPBkl08s5AdzYFoiu9HEnQNmscOuAP9ugg4pR0mCoCbj6EfCbcXYHB0NKp8/OverXMhw16shFcOo2c1bYaVDISA5Y295ZvouEE2jL8Pab2VqAFQdXqluQns250AgWOylLnmBzVigSunFbnnRLVOH+Eo7BVBLkl4ejEkcB2f//hqATxneZDwUcidAf1/gMOOiFrG9bcOKf0RZTPgRalQObAeze+AVeGR3R4TMUjz1ExiqmsShresqxueh9/M0KHgjLHhmhfbleTmQoWihjG/4seQjDUU9YGEdfFgzNy+QrKUXd4UthVnwdsAQlEVjUG9056Sknj/JV/Ni/3j+6emSmx1cOM8qlIdX0mV/FEqG1ASrlmLeLvKX0ATOltLvm6N+2nV4jvfzcYqODG64s9uEqDXf04FzcwdbD+cSH2HSSL0IoTByhy7ZWKuiL0YodlS40pfMop7HPmvSjnYxYbKQVEqQVfVy1K6cY/gUUVtYZpauf6pQ47ArCwMp5HdSDGm3dKQGNCWM2Hrz1O1mnOnkVFnsAdxv21yVIvlZsxFkqQtU8FpcqrVUAYdXUnHCjZKTxrrwq5ARYhoJApPexEACeTDN3rvNzYpAYEdF8rEJB78Pfm+paTSL1dCv8mRqDajr+Whu7Pc8oVvCGSsbEEQnDZywXo5yZ18IS4ZgcaeJ3JRQQGwUbeWJ96RlSnCIV5n/6/ObWxAKsE1Yb/tm/RkzeTMhE7JmhOQF+a7gB5bmxZypHZnDMwmD4aCD7S+k6xCrK2zp9S7xzrFj9rlRXkmqsYoVz11njiReESL9qrlAWQyCupOweGPfIhG04la'

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