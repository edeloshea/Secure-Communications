#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

# get factors using factor db
p = 752708788837165590355094155871
q = 986369682585281993933185289261

## ct = m**e mod n
## e = inverse d
## m = ct**d mod n
## 1 = d*e mod (p-1)*(q-1)

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print (decrypted)


