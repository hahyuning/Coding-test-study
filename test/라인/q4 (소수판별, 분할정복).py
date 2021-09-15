primes = [True] * 1000001
for i in range(2, 1000001):
    if primes[i]:
        for j in range(2 * i, 1000001, i):
            primes[j] = False

def recursion(ans, a):
    if len(a) == 1:
        ans += a

    m = len(a)
    p = 0
    for i in range(2, m + 1):
        if primes[i] and m % i == 0:
            p = i
            break

    for i in range(p):
        recursion(ans, [a[j * p + i] for j in range(m // p)])

def solution(n):
    ans = []
    recursion(ans, [i for i in range(1, n + 1)])
    return ans