
#3 * d ≡ 1 mod 13
# 1 = 3d % 13

for d in range(0,13):
    if ( 3 * d ) % 13 == 1:
        print (d)
        break

