def dfs(num):
    global ans

    if len(num) == k:
        num = int(num)
        if add[num]:
            while num % m == 0:
                num //= m
            if mul[num]:
                ans += 1
        return

    for i in range(10):
        if not check[i]:
            check[i] = True
            dfs(num + str(i))
            check[i] = False


prime = [True] * (10 ** 6)
prime[0] = prime[1] = False
for i in range(2, 10 ** 6):
    if prime[i]:
        for j in range(2 * i, 10 ** 6, i):
            prime[j] = False


k, m = map(int, input().split())
add = [False] * (10 ** k)
for i in range(2, 10 ** k):
    if prime[i]:
        for j in range(i, 10 ** k):
            if not prime[j] or i == j:
                continue
            if i + j >= 10 ** k:
                break

            add[i + j] = True

mul = [False] * (10 ** k)
for i in range(2, 10 ** k):
    if prime[i]:
        for j in range(2, 10 ** k):
            if not prime[j]:
                continue
            if i * j >= 10 ** k:
                break

            mul[i * j] = True

check = [False] * 10
ans = 0
for i in range(1, 10):
    check[i] = True
    dfs(str(i))
    check[i] = False
print(ans)