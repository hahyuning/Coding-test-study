n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]

# 범위 중요
for i in range(1, n): # 대각선
    for j in range(0, n - i): # 대각선과 얼마나 떨어져 있는지
        if i == 1:
            d[j][j + i] = a[j][0] * a[j][1] * a[j + i][1]
            continue

        d[j][j + i] = 2 ** 32
        for k in range(j, j + i):
            d[j][j + i] = min(d[j][j + i], d[j][k] + d[k + 1][j + i] + a[j][0] * a[k][1] * a[j + i][1])

print(d[0][n - 1])