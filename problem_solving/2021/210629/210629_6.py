def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

a = input()
b = input()

n = len(a)
m = len(b)
k = lcm(n, m)

while True:
    a += a
    if len(a) >= k:
        break
a = a[:k]

while True:
    b += b
    if len(b) >= k:
        break
b = b[:k]

if a == b:
    print(1)
else:
    print(0)

