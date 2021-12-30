n = int(input())
primes = [True] * (n + 1)
primes[1] = False
for i in range(2, n + 1):
    if primes[i]:
        for j in range(2 * i, n + 1, i):
            primes[j] = False

for i in range(2, n + 1):
    if primes[i]:
        now = i
        check = dict()
        flg = True
        while now ** 2 >= 10:
            if now ** 2 in check:
                flg = False
                break

            tmp = 0
            for x in str(now):
                tmp += int(x) ** 2
            now = tmp
            check[now] = True

        if flg and now ** 2 == 1:
            print(i)