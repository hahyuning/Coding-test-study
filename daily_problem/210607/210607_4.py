def gcd(a, b):
    if b == 0:
        return a

    if a < b:
        a, b = b, a
    return gcd(b, a % b)

n, m = map(int, input().split())
print(m - gcd(n, m))