from itertools import combinations

primes = [True] * 10000
primes[0] = False
primes[1] = False
for i in range(2, 10000):
    if primes[i]:
        for j in range(2 * i, 10000, i):
            primes[j] = False

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
c = combinations(a, m)
ans = set()
for x in c:
    s = sum(x)
    if primes[s]:
        ans.add(s)

if ans:
    ans = sorted(ans)
    print(*ans)
else:
    print(-1)
