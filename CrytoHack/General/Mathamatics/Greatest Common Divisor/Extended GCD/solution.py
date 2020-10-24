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