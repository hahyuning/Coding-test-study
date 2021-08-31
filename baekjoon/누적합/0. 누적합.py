n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + a[i - 1][j - 1]

k = int(input())
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    print(d[ex][ey] - d[sx - 1][ey] - d[ex][sy - 1] + d[sx - 1][sy - 1])