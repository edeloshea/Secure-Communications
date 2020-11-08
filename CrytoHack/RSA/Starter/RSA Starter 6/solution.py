>>> from hashlib import sha256
>>> N = ...
>>> d = ...
>>> flag = b"crypto{Immut4ble_m3ssag1ng}"
>>> h = sha256(flag).hexdigest()
>>> enc = pow(int(h, 16), d, N)
>>> hex(enc)