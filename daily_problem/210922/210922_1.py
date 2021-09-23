n, m = map(int, input().split())
a = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

d = [[[10000] * 3 for _ in range(m)] for _ in range(n)]
for j in range(m):
    for k in range(3):
        d[0][j][k] = a[0][j]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            d[i][j][0] = min(d[i - 1][j + 1][1], d[i - 1][j + 1][2]) + a[i][j]
            d[i][j][1] = min(d[i - 1][j][0], d[i - 1][j][2]) + a[i][j]
        elif j == m - 1:
            d[i][j][1] = min(d[i - 1][j][0], d[i - 1][j][2]) + a[i][j]
            d[i][j][2] = min(d[i - 1][j - 1][0], d[i - 1][j - 1][1]) + a[i][j]
        else:
            d[i][j][0] = min(d[i - 1][j + 1][1], d[i - 1][j + 1][2]) + a[i][j]
            d[i][j][1] = min(d[i - 1][j][0], d[i - 1][j][2]) + a[i][j]
            d[i][j][2] = min(d[i - 1][j - 1][0], d[i - 1][j - 1][1]) + a[i][j]

ans = 10000
for j in range(m):
    ans = min(ans, min(d[n - 1][j]))
print(ans)
