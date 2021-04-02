n = int(input())
# d[i][j] : 길이가 i인 오르막 수의 개수, 마지막 수는 j
# d[i][j] = d[i - 1][k], 0 <= k <= j

d = [[0] * 10 for _ in range(1001)]
for i in range(10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            d[i][j] += d[i - 1][k]
        d[i][j] %= 10007

print(sum(d[n]) % 10007)