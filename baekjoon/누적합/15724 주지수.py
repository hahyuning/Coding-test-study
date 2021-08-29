n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * m for _ in range(n)]
d[0][0] = a[0][0]
for i in range(1, n):
    d[i][0] = d[i - 1][0] + a[i][0]
for j in range(1, m):
    d[0][j] = d[0][j - 1] + a[0][j]
for i in range(1, n):
    for j in range(1, m):
        d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + a[i][j]

k = int(input())
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    if sx == 0 and sy == 0:
        print(d[ex][ey])
    elif sx == 0:
        print(d[ex][ey] - d[ex][sy - 1])
    elif sy == 0:
        print(d[ex][ey] - d[sx - 1][ey])
    else:
        print(d[ex][ey] - d[sx - 1][ey] - d[ex][sy - 1] + d[sx - 1][sy - 1])