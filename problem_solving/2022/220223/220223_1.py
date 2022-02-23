n, c, w = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(1, 10001):
    tmp = 0
    for x in a:
        cost = 0
        m, d = divmod(x, i)
        if d == 0:
            cost += (m - 1) * c
        else:
            cost += m * c

        if m * w * i - cost > 0:
            tmp += m * w * i - cost

    ans = max(ans, tmp)

print(ans)