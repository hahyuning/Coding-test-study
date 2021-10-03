n = int(input())
w = [0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))

d = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        d[i][j] = d[i - 1][j]

        if j - w[i] > 0:
            d[i][j] = max(d[i][j], d[i - 1][j - w[i]] + v[i])

print(max(d[n]))