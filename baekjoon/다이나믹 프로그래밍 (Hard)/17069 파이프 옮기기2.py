n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# d[i][j][k]: (i, j)에 방향이 k로 도달하는 경우의 수
# k = 0 가로, k = 1 세로, k = 2 대각선
d = [[[0] * 3 for _ in range(n)] for _ in range(n)]
d[0][1][0] = 1

for j in range(2, n):
    if a[0][j] == 0:
        d[0][j][0] = 1
    else:
        break

for i in range(1, n):
    for j in range(2, n):
        # 대각선 방향으로 가는 경우
        if a[i][j] == 0 and a[i][j - 1] == 0 and a[i - 1][j] == 0:
            d[i][j][2] = d[i - 1][j - 1][0] + d[i - 1][j - 1][1] + d[i - 1][j - 1][2]
        # 가로 방향으로 가는 경우
        if a[i][j] == 0 and a[i][j - 1] == 0:
            d[i][j][0] = d[i][j - 1][0] + d[i][j - 1][2]
        # 세로 방향으로 가는 경우
        if a[i][j] == 0 and a[i - 1][j] == 0:
            d[i][j][1] = d[i - 1][j][1] + d[i - 1][j][2]

print(sum(d[-1][-1]))