results = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]


for x in range(100,1000):
    for p in range (100,1000):
        for i in range (0,100):
            if pow(x, i, p) == results[0]:
                if pow(x,i+1,p)==results[1]:
                    if pow(x,i+2,p)==results[2]:
                        print(x)
                        print (p)
                        break
                    


    
            