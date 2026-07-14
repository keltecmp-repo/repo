# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 728131 ^ 703475
_lx1_1 = len("02dad9")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-329306)
_lx3_3 = 411390 * 0
_lx4_4 = 643514 ^ 596022
_K = 'c42c685e38dabd290da075819068475f4245fc9db0d0450fa15fc2a567fa4447'
_M = 'pJC6Ix3XLiza0Fcn8l734DVYxKA2AEaXpJhTxLrN/omj3u1nTYEudtGAVXilD/a7YAzH92oBEpfzzVSQ6Jv73KrQvGdE1yl0hoBc'
_D = 'f1k1khhfHk3bhbXU2EpOeHBD8y4S2E729XXCLrEjO80jQ3mNQFhDrgideNOn/Ay7/sm8lzKHTCjrRv5qJNCM/cFswG++yVdPca4yUHVYCez94q4ZP8dfGEae9M40+8QnjNKNpuZ6KOLIwxWlNrJ9UWZ2It8axQV59oHOOic2hYUHOuvIfVENub9yhmVOQQENV+QKkbqUDN0U+YKDzaM0nF/eGvYJVMnrtXnWvQaxlC/ZFXTnY44MoVKnp+LdNDiM3jWV3WXTcUV9JETdgvhtSjkyv6SnC3WWy8Ka+Xlyd/vPymjl+th/+JWg1fWiJTHfU4IyTPUzzpakCCl9LIjwTHGoXRgO/DvvuEPoTGkyHXs/yER/zW7TZD8jZgEAVN1mtTcWZ9sr+iDJuxFPmO8fNcBoKTWv71hFuf6gGuiurron8Xzrr/AJzHoyeYdGDMhmaHe0ftoUe6708PVurrs3U4ifYCiLEa98G+PwgdFb7RFJ67+04bNdhCiXz6NG95hRsn9hW8cRhmeAn2/nBl/nf+HUEqeiDqmiAKABHuL47eEXbYlUl7F+lKwqrFln+GtEFQUrhnEKzm0uY4eOas3xI+74oBvtYTGUL5NXHtGWXQIQ41T30oIdQbPgzFYLF055pq83bKz4o/WL54m/sVUZA9zle1HnMmapNHOzF/Ykh/T4MlNZ0HE7j+helk/EB55JTwUyZsOVYtOu54TzsSdTVOVdLMrQFwcXSgVtJRWi6qm+7BwGbhhs+O624AAGFIcCCpG9GUKTBFvUM8ZiHdMWs+FoYqX8cBM6BO/G3YKp4G1ttsVaGcFv0Jh47sZxr0zyRGV6C1KDTe2R7X8tCuC+i9gJx0oH3waijWRldXbu/C7aA6otPbjyEPaZX43cTTXpquVzUUX1PKGfLCoi2YrDvnYPgO4nu1WkulVlVTM8LoVJX3Jv5HISmwn4AwuES2G5EioMvkf5cYVZRF2i+WUnRxiM3Q8hvZpT0Vr1VCCDqfGaQOOf4QxRXVW4+QMWPI27buCqq1jSY+NcRmnVCRIHS6aAwJ8y8UuooKgvVqPj0/rXG8kO8Cwwj6w6ADK4Ek4uJ6mcZTRORExGaN1AE3f+Ph0iDriJhOu1tcpWlcVCiXKm3k3nzCVwQIwtXHRQW08NFB59TyUJbuVC1jtOWlUXZEqjY+twNJDr7jVlcI3yWGy/wYcFV7lKMhTzbVrhtE40KV0ZjXMrAohe3GsXw7D0jYujikR6TDNU2Ice+KpP+eKUBa5YUw2GxRpzkKWMqDjx/nr/luxY1UcidTP3IBpFO5QoROyl3EXZePZ2b3MaisBtSiPlUm9d5rsj6+0lNbIdJf46t9fGkiUJrlqgS71gFMVtMJyi9LgxQ2KoRtYMKE1QC/6Uk2liX2rxR8AcXSY5C5a8FhaQinAomSXxDCSovrxddXcSvzPUhKJO+ieBCJIN10hjgLJ4H3OchHXPHaM+tj04tqt/iotFS3MPkhAaf28V9UZ5K1PX0S8l3CJKnwb1uDKF6AReUfR3ttS7QSuO3CMc7N5JsKZIjfsVAVNwgPk5GDPlZT8Aux6s5X3KFEMDb6kt7ZqGAyzEmBDN07eX4vZre6nXbClE+SkOi8DuFxsklCoyEZB90nbyhNCt0GcrY4MulLrN9jTYR4fRu09dLnlEpnX+bIX9ZDG4SD9xBf7wwG1V5sKEGoTRuLcYm2lgQ/XLJ67w6UA3B56TCY/BBZ7TkOMM5msLRMp18FYlQpYsPYOuS4JDAsk/VDLoSvziOFqf1OUybatTRrpd7APeXjAle+easxCjZ4wQoK6zA1mJnKn32EnZ8eJYkRQ5Ov0JHe2n4qZRCfNE1Iz52n6D7LM6NoSI/ySieZEPHorIN/sKWsApiM3bk61p'

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