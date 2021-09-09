n = int(input())
# d[i][j] : 길이가 i인 계단 수의 개수, 마지막 수는 j
# d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1], 1 <= j <= 8
# d[i][j] = d[i - 1][j + 1], j = 0
# d[i][j] = d[i - 1][j - 1], j = 9
# ans = sum(d[i])
d = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][j + 1]
        elif j == 9:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
        d[i][j] %= 1000000000

print(sum(d[n]) % 1000000000)