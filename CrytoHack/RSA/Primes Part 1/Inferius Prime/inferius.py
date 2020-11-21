#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
## ct = m**e mod n
## e = inverse d
## m = ct**d mod n

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while True:
    p = getPrime(100)
    q = getPrime(100)
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    if d != -1 and GCD(e, phi) == 1:
        break

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")
print(f"pt = {pt}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag
print (decrypted)


