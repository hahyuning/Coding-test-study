n = int(input())
# d[i][j] : i 자리의 이친수의 개수, 마지막 수는 j
# d[i][0] = d[i - 1][0] + d[i - 1][1]
# d[i][1] = d[i - 1][0]
d = [[0] * 2 for _ in range(n + 1)]
d[1][1] = 1

for i in range(2, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1]
    d[i][1] = d[i - 1][0]

print(sum(d[n]))