n, m = map(int, input().split())

ans = m - n + 1
check = [False] * (m - n + 1)

i = 2
while i ** 2 <= m:
    k = i ** 2

    if n % k == 0:
        j = n // k
    else:
        j = n // k + 1

    while k * j <= m:
        if not check[k * j - n]:
            check[k * j - n] = True
            ans -= 1
        j += 1
    i += 1

print(ans)