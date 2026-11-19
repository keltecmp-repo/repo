# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 762809 ^ 803535
_lx1_1 = len("c0d299")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-490283)
_lx3_3 = 138206 * 0
_lx4_4 = 636887 ^ 162404
_M = '24d/uJ7rBOq13dR0/rx69DU4VG9Dxo2FECxdD2iho++DjTj0xu5FvrfdinKs7CqgM2lZaB/A3IURKAtdP/bzuordOqnH7UW56orc'
_D = '==AGL73yJwI23fgYrPuJkxHqB7UabkYR7yBlfQwwkKDn/MiQbEZvNMAFUMOVsCMbF9Rgv+1y0F5eiGuSrnJnqzu+PhdCHgqU/cboWUpUqoL1fcT24UoxbXoI466zXgiWtz4FoKqrhjNOQatP9iyTCrsugEtxK5S/q1kTHS/6xBWdWHNlKDBpyYt6aTK/vn6QQXGlCpj07T5BDnoXKVRMx/8MBnPII2OZKr9PrrgjMPNRn3wz8Us6VoxbBrVPisKi46LywYY9NW2eLHTJRAoNu5NnoG/A1VUsM6OPYwxigsarCuf7xFAlL54qhr8iwTjrtSwIWJpXgj5JIZ3/R6qVq4rmLBFZr6b+QYP3XGXEZxspL7LleBz9HeNy+M52D+myXpz2a+aGYQYGVWfm41dYZgpQ6IUxvH1ZsB++iCCbXFPmIkGJDO83xs+doWABKfmRJyArE5qzjY5LGtmY34wGhmLEZ6WZ/qL6HPdyAfGaRQD2LGzk+mCIRVZ38/Z1WPao0LuHZgT8DrUV4B0TT+2rUFH7k8DoBKMGQR+et61/Do9xFSjPAM0xBLJqDmmtNNBQMC1ba/9X1A6HkQY/mpJSNOnF8xSTG/qvdbrsN3+iwFNHVgCR/Bfi+Z7lmOHdYME7nVtLH9wouOWka6yjmkscx36/WcE1IBgjT843kZPYZOiQKAlzoi03nWHNweKRbifaqV0S6nCU0tf/7E+pIHnWTDfmA/1zjVFT7SM+7cFQrHpSC777lG/BXUWrAFmgQNeUrpSga8riyGvJ+AE1VJnmJDRViaKylpRT8lCjs8rz5S2G6UeouIjVbnOEzCXjTFWhj85JikzgVxt0RZZVyZPAsxbBqvVyLwvwwkZNi3W8nKaWbIDLtUV6aBnGnc+7QHgiTlYZ21rlLe39gBeGdHNucioxsgv2ZfLERQhY0MPeBz+M9fcTKsu/5X+5YwnTv8sWUUe+/0ZrMMOh7qSVcFbyz/eZnVnwjFKPWQSNFZu7HGMncoW5cEQtvu2zp2tPiijYJrTJbYsQQK++JCrtY2MSboeKD1N8yX27zREoEPrOipaIJmaWhDfdZIovwdez58ODrDg67WpvFBBh8G1SSV7FD0RHMbkOOYi4BX47YBSgRPFz0Hzm87BuDXv72VwnOCYPz3frrrXGys2z+br59O0WgX2XSxR5RAwDacBNZWRg05YO/FL2PgixuZHtus6M0F5r8aDZ5YTS5Bu65O8yjJzsumwJcCrfUcqKM443yBl9tQUTX05Jwl509Do5/kpYt8rEgkHOsJDvtFeV5clAwJxfIFGCiJMGkYAOcel6JXwvPRBmxxGVglggW+kChciF81Ey1mffUhVMymkEjv2anemOXl9Q5nHcSW5pwnN75VByCg8zA8oExh0JB4nLqYetTcKSjpbmASnn8+v4+1+xdbxl2Sgt40ueZ9sV29v2ao0aR/SlzItLvisaKnZD+3HPNJJ4cAoxjsFlUI1DOQ4St+QJ2NVqhBkFtrhpz9Q5D5GPCFYBPyOU+PqUnBSQ4KzF5fweHSg4tRf/yYEoZNNB25f4gb16naw0mrmLvQuSo8UHxrIjcaljO4IIMEV5eXBhaIOtNX+yVk63KwLQGrwOiMYSOg9cxByAyjA1xtLjHRm58vwysLbzyCwr'

_032d=[22,225,163,231,72,87,35,124]+[108,67,121,164,168,196,8,39]
_d0f3=[71,84,160,11,79,27,213,191]+[129,16,18,12,18,42,111,22]
_c324=bytes([a^b for a,b in zip([100,132,208,136,61,37,64,25,31,108,29,197,220,165],_032d*8)]).decode()
_a71f=bytes([a^b for a,b in zip([36,53,195,99,42,53,177,222,245],_d0f3*8)]).decode()
_cd99=_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),*_c324.split('/'),_a71f)
with open(_cd99,'r') as _f:_K=_f.read().strip()
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