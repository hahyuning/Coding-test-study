from collections import Counter

primes = [True] * (40001)
primes[1] = False
for i in range(2, 40001):
    if primes[i]:
        for j in range(2 * i, 40001, i):
            primes[j] = False

def change(x):
    if x == 1:
        return [x]

    y = x
    ans = []
    for i in range(2, 40001):
        if primes[i]:
            while y % i == 0:
                ans.append(i)
                y //= i
        if i > y:
            break
    if y != 1:
        ans.append(y)
    return ans

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

aa = []
bb = []
for x in a:
    aa += change(x)
for x in b:
    bb += change(x)

aaa = Counter(aa)
bbb = Counter(bb)
ans = 1
for x in aaa:
    if x in bbb:
        ans *= x ** (min(aaa[x], bbb[x]))

if ans >= 1000000000:
    ans = str(ans)
    print(ans[-9:])
else:
    print(ans)