# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 300990 ^ 969068
_lx1_1 = len("f1b814")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-806128)
_lx3_3 = 669320 * 0
_lx4_4 = 917587 ^ 947600
_K = '8c94b3a26c7adb640804d2c176774725bf05f12358b7c3afc82bc4c3243c64d8'
_M = 'vQ8eGmTfhk+p/yWDTESgtsETrzv3lDBBWn9gCOQP5WGyAVRcN97TCqWoetAZF6S3kEP9OKTEMBMOem8NtADjYLZQAFsziIIB9v58'
_D = '==g5CFe3OsB+HVjaUD490boawjxf41iHw0dJD1VJXlj8ezuxQdJJNouH35Hm93vaPDD2DohPeF5XfFg6Kxx+cMwGbl0653kiHwofLqky+xm/d5s6Q0cAMlsrHeMoekK8fh0qe1mSPh+SiMlNqK8HL3pc+ecUfKGCnuDGZ0MsKnGeCwnhwP0UxW8zVzMYY1Y1NxF6f61fckdAWP7I+YQ6IkaJmwdraFa7x8I0jSgnSHVlvu/xE2TT4sEh9cH6AI7pHyCI1c5oHj4uFfjfAHRoXd9YNehoKCVQd09mSVjYBd+E89gWEqVv4MreRxST+B1++IYTy63zcZJrlrCAA/teGSlVW440jyLstLQUJQx1qA1tJattxqxQOssXp6tjPu3REQoeMVW+VXS8FOCGfo1PM3oMH5/QS5nFL3UhXwcD3lkF5+0uZy3UTUOEnkwcjz8WAlyXO1GuNEmhKBgJbK3Z8Mb7PKgHGpq8jyacF4IMIKg0vOvRCnWNVvn2zuRva68UQompAvGVTp3Rmml4dHZeyahsDqGYU6O6QqPzpKuqUAwTxEi0APZlUFW3J//vAJN5hfxoGwwTPehXsL5pgSglxkR2igLo7y9E0LFMVJFkPu7A0YEAZKKScJKN8wqoaYbf5wkjXb9WzQ7M/zGh1biR9tvq2VGkmKmLuSosoFb4YdJLy8mK2VsJgiJ/tPGkT+RfCQIogOasEL+GKDeN8ZqLXBP0JNcE6HhsY7rQnPMv3KUwtIWDJCRn8uh1+rediqE3k+6885I3BTW3ZIiB1jX5Sp0VHWp+eTV/sUZxbfnWPfLAD8BPLdTdlZ2pcFVeUyK8QbSPmfO37VlzY2RbQuuMsED4PG9CnjFG2HP58RDvtGziHwKty4aFrAP4B9r1Img6F3ytjTzXdoAZUp5+NN+bcQwQ+vrrZidGjUwCn93KOJSdqb2ZAu7NYZ7rLmVs7K/x8X/OuaZGx04xeBQSKpYrFWz8u02WdLi8iXr+ee2HmF1elXa5u83Qb/0rGaw7b/gMMOiWFzMJQ7Jt2gVuLQ0JdPbgZv9MCYAXuMv1atIcqLW1lfDMVUYFGJPcg0am6i2a/LjzBKFZ0ZaL0DXzC9zVtoa91iq5LnSXSJMknyA3myBUTObg6fgSqmHxh1yhnAOHHBU8RVlo/mgM0Vg7CXTeYIT5q6e1kLx5d+G8goB8qENyWfPyLdPD7yR+XN8CCoHvDUfRlnCP1CXvSqr7ilkdBZUcm1X6w0ZWXA9vLKHxvDkcbJLzvgcxGXXgCQnRJSRd9QcNi64Bv5bznE2gcVBbDqXggwC9OFZkV0zBhJdfne70SYriRBRO0eQ904crc+XphH78bGhF/C5Ik1CVodN7LW6CgUWc3WcheDnvCmyAKlELO5Saz5Anbkp1mwQCUD6wHIJDo2LBBlkQHDIXAATgdO2vhlhjUR1cfcaY7Gh9e+gm+OKoZHgqsv3KufW4qh5ogHBCewZB3mzTbo+HWiRCIqNE+y0SVVJi7V8uPhacMvkbFvwJ/I/S6HmwK/1SJuFhpU1lT/hdXKuHOy/R2rP8pWzofkXkV1y4CSkBZeZXQAuKwD02e8f++VtUC3GMA86fl1W7XkJMFbALxs1m6AmLJMl0q7DrS4GcsOPWwvBGwZyv29Sj4Ljw'

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