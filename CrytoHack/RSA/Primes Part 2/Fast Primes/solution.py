c = '249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28'

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from itertools import combinations
from math import gcd

keys = []
for i in range(1, 51):
    with open(f'/home/b00139077/college/Secure-Communications/CrytoHack/RSA/Primes Part 2/Ron was Wrong, Whit is Right/keys_and_messages/{i}.pem') as f:
        keys.append((i, RSA.importKey(f.read())))

for (i, k1), (j, k2) in combinations(keys, 2):
    p = gcd(k1.n, k2.n)
    if p == 1:
        continue
    q1 = k1.n//p
    q2 = k2.n//p
    pk1 = RSA.construct((k1.n, k1.e, pow(k1.e, -1, (p-1)*(q1-1)), p, q1))
    pk2 = RSA.construct((k2.n, k2.e, pow(k2.e, -1, (p-1)*(q2-1)), p, q2))
    with open(f'/home/b00139077/college/Secure-Communications/CrytoHack/RSA/Primes Part 2/Ron was Wrong, Whit is Right/keys_and_messages/{i}.ciphertext') as f:
        print(PKCS1_OAEP.new(pk1).decrypt(bytes.fromhex(f.read())))
