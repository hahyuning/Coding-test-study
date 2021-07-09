def gcd(x, y):
    if x < y:
        y, x = x, y
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return x * y // gcd(x, y)

a, b = map(int, input().split())
c, d = map(int, input().split())

g = gcd(b, d)
l = lcm(b, d)

e = a * l // b + c * l // d
f = l

if gcd(e, f) == 1:
    print(e, f)
else:
    g = gcd(e, f)
    print(e // g, f // g)