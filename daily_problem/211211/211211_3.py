def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return x * y // gcd(x, y)

primes = [True] * 1000001
for i in range(2, 1000001):
    if primes[i]:
        for j in range(2 * i, 1000001, i):
            primes[j] = False

n = int(input())
a = list(map(int, input().split()))
ans = 1
for x in a:
    if primes[x]:
        ans = lcm(ans, x)

print(ans if ans != 1 else -1)