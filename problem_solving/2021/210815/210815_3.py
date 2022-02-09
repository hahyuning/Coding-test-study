n, k = map(int, input().split())
# d[n][k] : 0부터 n 까지의 정수 중 k개를 더해서 그 합이 n이 되는 경우의 수
# d[n][k] = d[n - 1][k] + d[n][k - 1]
d = [[0] * (k + 1) for _ in range(n + 1)]
d[0][0] = 1


for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i == 1:
            d[i][j] = j
            continue

        d[i][j] = (d[i - 1][j] + d[i][j - 1]) % 1000000000

print(d[n][k])