n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

# d[i][j]: (0, 0) ~ (i, j) 까지의 합
d = [[0] * m for _ in range(n)]
d[0][0] = a[0][0]
for i in range(1, n):
    d[i][0] = d[i - 1][0] + a[i][0]
for j in range(1, m):
    d[0][j] = d[0][j - 1] + a[0][j]

for i in range(1, n):
    for j in range(1, m):
        d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + a[i][j]

for _ in range(k):
    a, b, c, dd = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    dd -= 1
    if a == 0 and b == 0:
        print(d[c][dd])
    elif a == 0:
        print(d[c][dd] - d[c][b - 1])
    elif b == 0:
        print(d[c][dd] - d[a - 1][dd])
    else:
        print(d[c][dd] - d[a - 1][dd] - d[c][b - 1] + d[a - 1][b - 1])
