# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 605103 ^ 900114
_lx1_1 = len("817ef0")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-265436)
_lx3_3 = 957894 * 0
_lx4_4 = 875246 ^ 614797
_K = '17e771955a5e66ee3086ac7c22662bf01eaf52c9aa1ed1f63749525944bd18cb'
_M = '+QkOQcg1VuUAWlUiEkJ5HkWC6/GRD78DGCXNExJi2b37D10ZzyJZu1gMCytCRXoSHdO+ppVT61dGJpMVFTDY4/gLWxvKcwbqCVYO'
_D = '==gSF624lTH871IG9kYZTdBvLAO0MuRKYyLPAP1xuqYzBaIA+1vyJBEu+7bDCZPSQwsaSj9FQtK02T5r7wRXms5yNtSCPaAQ3LVaCor1P5yAJSHOa64FxptFdfr9zmk/WXcZ68WCDEu12KrY9QDjvxQtajIZmHoap/Lj9h0EajUpl2mzcxR2dsbS/DEdCWY9E5IpHfVs9UwCs68Ye2KwRO0YAWV60q0ZKx/Tv0HLVNvqxth6HJxNV+QWVZUuOPWSudMSznd1sO9mp7U1BUZAu/CP3lqHJ9IYozAdq58ft9I7l8IXh+HtRzDoDrB9wJOxA8LetNL8Ij53u70AE8x8JdGOEG37jQpvJB27GVd8niFMkXtGKGI7t7tRsxb7pzGFnEPCrwMakG/7y1UDR9H2NeaqE8GbpXU/kHdYXGESh35jQVqjgo9hcYwN4n2fJTOp0Du/HsmOE9PsstgT9yuy3JDBjimz+UZpd3boXPsu3Wav+N82b6LKqLlE6pshmPy+Py/66Y/3wmdrcl3W266FszArxwuVzdG/WYE70LEFNiXl3X1VAqP265qxzD6IRlKJnxvNsZ+OB0zIPKhoaCCoVoNNT55M0a3buclr12kOic/NcdBWD+ZdaSgM9IqY/+Id3BfFCwth8eD3n77RcMs2F5c03DZtkKjdNkAJQ+SaOHOiOQBjeynWrTt77ZzYQ10aMN1RZgX2t20X+RrNB8RQapQRq50Ftu9R3LLMN5oM+NUdTX57dKM49DE8yhjFZcsBbo7rJcR/nIYZNZ1CU65LjMh3BWfQxyI7j8ahT0s8fZEa5Ln3IHkheG7m57sINOgIWb/GmnvWpJ9kTf1g1MhK/rXw6uE8clhYVPneEfsk4tZkJL1eUohRAy32/HR6N9++3uvbnfsBl6r9oTc2lELY8dN49spff7YoTv4Q0sm5+LmY5mbGa4ooaSB8I7KpyQtA/4ZYb7I6YkKFPIKm0D3yLl3tWhA6b9tTUpB0iAhrGmDK5KzmAGQ2Uk9iFO0ecHp4t6oLqcks4iGSLAfNH4kg0bZuyVUbZBBI6ehifaqiCVjMeQNp1jWJEDhMbf7cQ/Pcc+dT2cAUYEKjiv95z/4jbXUm0SR1Hcth+OuQ7ANBSz1KlCwXbhtjXrGvN9PuCAfTfcQbu4XLXa/T9fiQrqkZawaR7c2wKVYNgaRq7yldxo+dQn0nvdXTUyWkt1hkW0i8q2tFdO/8Fl+9TmUIzqtCKyGoCPMaAEN5EcrOcEvgVXOBeL2XVX+VybuymKCw27gS3FkbR41zPidXepl28Q7MfsxiNJ+91yKeZVvmx8RvVGaxFJldUBmvTOWCsFqLB20cpcSpjgL7ktkVEAW0JyCIxuJuWMNSWYKBX+VYra3K8TdxP/46LGYTd+7tzLPdK6XZOv5GjhZVeNgjhS20fKN6qWDMKjRy/y9DmTkBepwBTrprLbalXU9ouD0obXT4aljgpTiQCbkbVkzsYoZr5WcfEa70B3DXgUDH7fMVgm5jWFcyzk+EGjQcz9A8CwhANjb1LvVw7o4QqTHBs9l86/WZ5Jr34efQZj/3Fyx3rSM446xNNvSdkAf0GmQtzBDtLAo/F5JyNW23NCAC63QjeyC8FAVKFmX4FffEbRnzBZ3rsQZBpU5E'

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