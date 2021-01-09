"""source of the Gram-Schmidt Code: https://github.com/pwang00/Gram-Schmidt-LLL"""

from fractions import Fraction
from copy import deepcopy
import math

class vector(object):

    int_array = []
    magnitude = 0
    
    def __init__(self, v):
        if type(v) in [list, tuple]:
            self.int_array = [int(i) if int(i) == i else i for i in v]
        elif type(v) == vector:
            self.int_array = v.get_values()
        self.magnitude = math.sqrt(sum([v_i ** 2 for v_i in self.int_array]))
        
    def get_values(self):
        return self.int_array
        
    def __mul__(self, c):
        try:
            assert type(c) in [float, int]
        except:
            raise ValueError("c must be a scalar type")
        return vector([c * i for i in self.int_array])

    def __rmul__(self, c):
        try:
            assert type(c) in [float, int]
        except:
            raise ValueError("c must be a scalar type")
        return vector([c * i for i in self.int_array])
    
    def __iter__(self):
        return iter(self.int_array)
    
    def __iadd__(self, v):
        self.int_array = [v.get_values()[i]+self.int_array[i] for i in range(len(self.int_array))]
        return vector(self.int_array)
    
    def __add__(self, v):
        return vector([v.get_values()[i]+self.int_array[i] for i in range(len(self.int_array))])

    def __sub__(self, v):
        return vector([self.int_array[i]-v.get_values()[i] for i in range(len(self.int_array))])

    def __isub__(self, v):
        self.int_array = [self.int_array[i] - v.get_values()[i] for i in range(len(self.int_array))]
        return vector(self.int_array)
    
    def dot_product(self, v):
        assert len(v.get_values()) == len(self.int_array)
        return sum([v.get_values()[i]*self.int_array[i] for i in range(len(self.int_array))])
        
    def normalize(self):
        self.int_array = [v / self.magnitude for v in self.int_array]
        return vector(self.int_array)

    def fraction_form(self, denom_limit):
        return tuple([Fraction(i).limit_denominator(denom_limit) if int(i) != i else i for i in self.int_array])

    def __repr__(self):
        return repr(tuple(self.int_array))
    
   
    

def v_to_tex(v):
    u = []
    for i in v:
        u.append(str(i))
    return "\\langle" + ', '.join(u) + "\\rangle"
def vf_to_tex(v):
    u = []
    for f in v:
        u.append(f_to_tex(f))
    return "\\langle" + ', '.join(u) + "\\rangle"

def f_to_tex(f):
    return "\\frac{"+str(f.numerator)+"}{"+str(f.denominator)+"}" if f.denominator != 1 else str(f.numerator)


def gram_schmidt_tex(*v, normalize=False, fraction=False, DENOM_LIMIT=100):

    #Check to see if argument is of type list 
    if len(v) == 1 and type(v[0]) in [list, tuple]:
        v = v[0]
    
    if any([type(v_) != vector for v_ in v]):
        raise TypeError("Argument array must all be of type 'Vector'")

    #By Gram-Schmidt, w_1 = v_1
    w_1 = v[0]
    w_n = w_1
    w_array = [deepcopy(vector(w_n))]

    print("Start by choosing $w_1 = v_1 = "+v_to_tex(w_1)+"$\\\\")
    print("Now stepping through the Gram-Schmidt process:\\\\")
    #Every vector w_1 ... w_n
    for n in range(1, len(v)):
        v_n = vector(v[n])
        w_n = vector(v_n)
        s = "$w_"+str(n+1)+" = "+v_to_tex(v_n) + " - ("
        sum_str = []
        for j in range(n):
            w_j = deepcopy(w_array[j])
            if not any(w_j):
                continue
            w_n -= v_n.dot_product(w_j) / w_j.dot_product(w_j)*w_j
            if fraction:
                sum_str += [f_to_tex(Fraction(v_n.dot_product(w_j) / w_j.dot_product(w_j)).limit_denominator(DENOM_LIMIT))+vf_to_tex(w_j.fraction_form(DENOM_LIMIT))]
            else:
                sum_str += [str(v_n.dot_product(w_j) / w_j.dot_product(w_j))+v_to_tex(w_j)]
        if fraction:
            s = s + ' + '.join(sum_str) + ") = " + vf_to_tex(w_n.fraction_form(DENOM_LIMIT)) + "$\\\\"
        else:
            s = s + ' + '.join(sum_str) + ") = " + v_to_tex(w_n) + "$\\\\"
        print(s)
        
        w_array += [w_n]

    vs = []
    if fraction == True:
        w_array = [vector(w).fraction_form(DENOM_LIMIT) for w in w_array]
        for v in w_array:
            vs +=[vf_to_tex(v)]
    else:
        vs +=[v_to_tex(v)]
    
    print("So, the basis given by the Gram-Schmidt process is $\\{" + ', '.join(vs) + "\\}$\\\\")

    if normalize == True:
        w_array = [vector(w).normalize() for w in w_array]

        vs = []
        for v in w_array:
            if fraction:
                vs +=[vf_to_tex(v.fraction_form(DENOM_LIMIT))]
            else:
                vs +=[v_to_tex(v)]
        print("Normalizing this basis gives us the basis $\\{" + ', '.join(vs) + "\\}$\\\\")
            
    return w_array

def gram_schmidt(*v, normalize=False, fraction=False, DENOM_LIMIT=100):

    #Check to see if argument is of type list 
    if len(v) == 1 and type(v[0]) in [list, tuple]:
        v = v[0]
    
    if any([type(v_) != vector for v_ in v]):
        raise TypeError("Argument array must all be of type 'Vector'")

    #By Gram-Schmidt, w_1 = v_1
    w_1 = v[0]
    w_n = w_1
    w_array = [deepcopy(vector(w_n))]
    
    #Every vector w_1 ... w_n
    for n in range(1, len(v)):
        v_n = vector(v[n])
        w_n = vector(v_n)

        for j in range(n):
            w_j = deepcopy(w_array[j])
            if not any(w_j):
                continue
            w_n -= v_n.dot_product(w_j) / w_j.dot_product(w_j)*w_j
        
        w_array += [w_n]
        
    if fraction == True:
        w_array = [vector(w).fraction_form(DENOM_LIMIT) for w in w_array]

    if normalize == True:
        w_array = [vector(w).normalize() for w in w_array]
            
    return w_array

if __name__ == "__main__":
    #v1 = (4,1,3,-1), v2 = (2,1,-3,4), v3 = (1,0,-2,7), v4 = (6, 2, 9, -5)
    v1 = vector([4,1,3,-1])
    v2 = vector([2,1,-3,4])
    v3 = vector([1,0,-2,7])
    v4 = vector([6, 2, 9, -5])
    print(gram_schmidt([v1, v2, v3, v4]))