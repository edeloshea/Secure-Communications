def ext_gcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = ext_gcd(b % a, a)
		return (gcd, y - (b//a) * x, x)

p = 26513
q = 32321

gcd, p, q = ext_gcd(p, q)
print(gcd, p, q)

define the extended gcd function (ref: https://www.techiedelight.com/extended-euclidean-algorithm-implementation/)
loop the function by dividing a into b and swapping the order - loops until A = 0
returns gcd, p and q
print the outputs