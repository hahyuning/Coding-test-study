import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
maps = [input().rstrip() for _ in range(n)]
d = [[[0, 0, 0] for _ in range(m + 1)] for _ in range(n + 1)]
if maps[0][0] == "J":
    d[1][1][0] = 1
elif maps[0][0] == "O":
    d[1][1][1] = 1
else:
    d[1][1][2] = 1

for i in range(2, n + 1):
    d[i][1] = d[i - 1][1][::]
    if maps[i - 1][0] == "J":
        d[i][1][0] += 1
    elif maps[i - 1][0] == "O":
        d[i][1][1] += 1
    else:
        d[i][1][2] += 1

for j in range(2, m + 1):
    d[1][j] = d[1][j - 1][::]
    if maps[0][j - 1] == "J":
        d[1][j][0] += 1
    elif maps[0][j - 1] == "O":
        d[1][j][1] += 1
    else:
        d[1][j][2] += 1

for i in range(2, n + 1):
    for j in range(2, m + 1):
        for l in range(3):
            d[i][j][l] = d[i - 1][j][l] + d[i][j - 1][l] - d[i - 1][j - 1][l]
        if maps[i - 1][j - 1] == "J":
            d[i][j][0] += 1
        elif maps[i - 1][j - 1] == "O":
            d[i][j][1] += 1
        else:
            d[i][j][2] += 1

for _ in range(k):
    a, b, c, dd = map(int, input().split())
    ans = [0, 0, 0]
    for i in range(3):
        ans[i] = d[c][dd][i] - d[c][b - 1][i] - d[a - 1][dd][i] + d[a - 1][b - 1][i]
    print(*ans)