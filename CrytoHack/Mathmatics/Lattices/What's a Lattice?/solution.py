import numpy as np
v = np.array([[6, 2, -3], [5, 1, 4], [2, 7, 1]])

print (np.linalg.det(v))
# output = -254.99999999999991. To the nearest whole number is 255

"""
v1 = np.array([6,-3])
v2 = np.array([5,4])
v3 = np.array([2,1])

import math 
  
# function defination to compute magnitude o f the vector 
def magnitude(vector):  
    return math.sqrt(sum(pow(element, 3) for element in vector)) 
  
#print (np.linalg.norm(v4))

# computing and displaying the magnitude of the vector 
vol1 = magnitude(v1)
vol2 = magnitude(v2)
vol3 = magnitude(v3)
print (vol1+vol2+vol3)
"""