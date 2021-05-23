n, m = map(int, input().split())
a = [input() for _ in range(n)]
d = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][1] = int(a[i - 1][0])
for j in range(1, m + 1):
    d[1][j] = int(a[0][j - 1])

for i in range(2, n + 1):
    for j in range(2, m + 1):
        if a[i - 1][j - 1] == "1":
            if a[i - 1][j - 2] == "1" and a[i - 2][j - 1] == "1" and a[i - 2][j - 2] == "1":
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
            else:
                d[i][j] = 1

l = 0
for i in range(n + 1):
    for j in range(m + 1):
        l = max(l, d[i][j])
print(l ** 2)
