n, k = map(int, input().split())
primes = [True] * (n + 1)
primes[1] = False
cnt = 0
for i in range(2, n + 1):
    if primes[i]:
        for j in range(i, n + 1, i):
            if primes[j]:
                primes[j] = False
                cnt += 1

            if cnt == k:
                print(j)
                break
    if cnt == k:
        break