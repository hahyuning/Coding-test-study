def gcd(a, b):
    if b == 0:
        return a

    if a < b:
        a, b = b, a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))