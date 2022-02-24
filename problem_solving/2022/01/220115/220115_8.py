h, n = map(int, input().split())

d = [[0] * 31 for _ in range(31)]

if h > n:
    h, n = n, h

d[h][h] = 1
for i in range(h, n + 1):
    for j in range(h, n + 1):
        if j < i:
            d[i][j] += d[i - 1][j] + d[i][j - 1]
        elif j == i:
            d[i][j] += d[i][j - 1]

print(d[n][n])