n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# d[i][j] : i번째 집을 j번째 색으로 칠했을 때의 비용의 최솟값
# d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
# d[i][1] = min(d[i - 1][2], d[i - 1][0]) + a[i][1]
# d[i][2] = min(d[i - 1][1], d[i - 1][0]) + a[i][2]
d = [[0] * 3 for _ in range(n)]

for i in range(3):
    d[0][i] = a[0][i]

for i in range(1, n):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
    d[i][1] = min(d[i - 1][2], d[i - 1][0]) + a[i][1]
    d[i][2] = min(d[i - 1][1], d[i - 1][0]) + a[i][2]

print(min(d[n - 1][0], d[n - 1][1], d[n - 1][2]))