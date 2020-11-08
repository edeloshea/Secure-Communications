results = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

##found = False
##while found == False:
for p in range(99,1000):
    for x in range (1,1000):
        if pow(x, 1, p) == results[0]:
            if pow(x,2,p)==results[1]:
                if pow(x,3,p)==results[2]:
                     print(x)
                        ##found = True
    
            