n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
row_sum = []
col_sum = []
for row in a:
    s = row[0] + row[-1]

    for i in range(1, m - 1):
        s += 2 * row[i]
    row_sum.append(s)

for j in range(m):
    s = a[0][j] + a[-1][j]

    for i in range(1, n - 1):
        s += 2 * a[i][j]
    col_sum.append(s)

ans = -1e9
for i in range(1, n):
    s = 0
    for k in range(n):
        if k == 0 or k == i:
            s += row_sum[k]
        else:
            s += row_sum[k] * 2
    ans = max(ans, s)

for i in range(n - 1):
    s = 0
    for k in range(n):
        if k == n - 1 or k == i:
            s += row_sum[k]
        else:
            s += row_sum[k] * 2
    ans = max(ans, s)

for j in range(1, m):
    s = 0
    for k in range(m):
        if k == 0 or k == j:
            s += col_sum[k]
        else:
            s += col_sum[k] * 2
    ans = max(ans, s)

for j in range(m - 1):
    s = 0
    for k in range(m):
        if k == m - 1 or k == j:
            s += col_sum[k]
        else:
            s += col_sum[k] * 2
    ans = max(ans, s)

print(ans)