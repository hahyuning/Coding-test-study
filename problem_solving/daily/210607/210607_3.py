import math

def gcd(a, b):
    if b == 0:
        return a

    if a < b:
        a, b = b, a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

g, l = map(int, input().split())
a = l // g
for i in range(int(math.sqrt(a)), 0, -1):
    if a % i == 0:
        x = i * g
        y = (a // i) * g
        if gcd(x, y) == g and lcm(x, y) == l:
            print(x, y)
            break