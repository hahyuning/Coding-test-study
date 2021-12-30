def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())
l = gcd(n, m)
print(l)
print((n * m) // l)
