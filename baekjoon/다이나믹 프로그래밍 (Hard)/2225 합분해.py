n, k = map(int, input().split())
# d[k][n] : 0부터 n까지의 정수 k개를 더해서 그 합이 n이 되는 경우의 수
# d[k][n] = sum(d[k - 1][n - l]), 1 <= l <= n
d = [[0] * (n + 1) for _ in range(k + 1)]
d[0][0] = 1

for i in range(1, k + 1):
    for j in range(0, n + 1):
        for l in range(0, j + 1):
            d[i][j] += d[i - 1][j - l]

        d[i][j] %= 1000000000
print(d[k][n])
