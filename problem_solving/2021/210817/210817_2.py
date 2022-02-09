n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * (m + 1) for _ in range(n + 1)]

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1][j - 1] == 0:
            d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1

        ans = max(ans, d[i][j])

print(ans)

