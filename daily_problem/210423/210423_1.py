n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            continue

        # 아래로 이동
        if i + a[i][j] < n:
            d[i + a[i][j]][j] += d[i][j]

        # 오른쪽으로 이동
        if j + a[i][j] < n:
            d[i][j + a[i][j]] += d[i][j]


print(d[n - 1][n - 1])
