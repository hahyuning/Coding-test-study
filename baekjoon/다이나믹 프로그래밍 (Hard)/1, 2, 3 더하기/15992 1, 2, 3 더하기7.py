d = [[0] * 1001 for _ in range(1001)]
d[1][1] = 1
d[2][1], d[2][2] = 1, 1
d[3][1], d[3][2], d[3][3] = 1, 2, 1

for i in range(4, 1001):
    for j in range(1, i + 1):
        d[i][j] = d[i - 1][j - 1] + d[i - 2][j - 1] + d[i - 3][j - 1]
        d[i][j] %= 1000000009

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(d[n][m])