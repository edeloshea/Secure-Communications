p = 991
g = 209
## g * d mod 991 = 1
## g^x mod p

for d in range(p):
    if (g*d) % p == 1:
        print (d)
        break