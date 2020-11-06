p = 28151
g = 2

## g^x mod p
found = False

while found == False:
    for n in range(2,p):
        if pow(g,n,p) == 1:
            break
        if n == p-2:
            print (g)
            found = True
    g=g+1