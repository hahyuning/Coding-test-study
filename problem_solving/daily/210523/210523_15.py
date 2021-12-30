n = int(input())
k = int(input())

d = [[0] * 1001 for _ in range(1001)]

for i in range(n + 1):
    d[i][1] = i
    d[i][0] = 1

for i in range(2, n + 1):
    for j in range(2, k + 1):
        if i == n:
            d[i][j] = (d[i - 3][j - 1] + d[i - 1][j]) % 1000000003
        else:
            d[i][j] = (d[i - 1][j] + d[i - 2][j - 1]) % 1000000003

print(d[n][k])