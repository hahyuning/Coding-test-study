n, m, k = map(int, input().split())

ans = 0
while True:
    if n <= 1 or m == 0 or n + m < k + 3:
        break

    ans += 1
    n -= 2
    m -= 1

print(ans)