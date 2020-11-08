## a**2 = x mod p
##a**2 = 18

p = 29
ints = [14, 6, 11] 


for i in range (1, p):
    #print (pow(i,2,29))
    for a in ints:
        if pow(i,2,29) == a:
            print(i)
           


