n = int(input())
# d[i][j]: i번째 타일에서 두 사람의 거리가 j일때 안전하게 빠져나가는 경우의 수
# d[i][j] = d[i - 1][j] * 2 + d[i - 1][j - 1] + d[i - 1][j + 1]
d = [[0] * (n + 1) for _ in range(n + 1)]
d[2][1] = 2

for i in range(3, n + 1):
    for j in range(1, i):
        d[i][j] = (d[i - 1][j] * 2 + d[i - 1][j - 1] + d[i - 1][j + 1]) % 10007

ans = 0
for i in range(1, n):
    ans += d[n][i]
print(ans % 10007)