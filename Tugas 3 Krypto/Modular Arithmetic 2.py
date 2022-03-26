def ex_gcd(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        (gcd, u, v) = ex_gcd(b % a, a)
        return (gcd, v - (b// a) * u, u)
a = 26513
b = 32321
print(ex_gcd(a,b))