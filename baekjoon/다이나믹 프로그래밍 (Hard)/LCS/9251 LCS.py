a = input()
b = input()

n = len(a)
m = len(b)

a = " " + a
b = " " + b

# d[i][j]: a가 i까지 b가 j까지 있을 때 LCS의 길이
# a[i] == b[j] -> d[i][j] = d[i - 1][j - 1] + 1
# a[i] != b[j] -> d[i][j] = max(d[i][j - 1], d[i - 1][j])
d = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i] == b[j]:
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i][j - 1], d[i - 1][j])

print(d[n][m])