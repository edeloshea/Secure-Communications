#v = (2,6,3), w = (1,0,0) and u = (7,7,2), calculate 3*(2*v - w) ∙ 2*u
import numpy as np

u = np.array([7,7,2])
w = np.array([1,0,0])
v = np.array([2,6,3])

#calculate 3*(2*v - w) ∙ 2*u
flag = np.dot(3*(2*v - w), 2*u)
print (flag)