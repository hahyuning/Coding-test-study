a = input()
b = input()
c = input()

n = len(a)
m = len(b)
l = len(c)

a = " " + a
b = " " + b
c = " " + c

d = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, l + 1):
            if a[i] == b[j] == c[k]:
                d[i][j][k] = d[i - 1][j - 1][k - 1] + 1
            else:
                d[i][j][k] = max(d[i - 1][j][k], d[i][j - 1][k], d[i][j][k - 1])

print(d[n][m][l])