def op_1(a, n, m):
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[n - i - 1][j]
    return b

def op_2(a, n, m):
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][m - j - 1]
    return b

def op_3(a, n, m):
    b = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[n - j - 1][i]
    return b

def op_4(a, n, m):
    b = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][m - i - 1]
    return b

def op_5(a, n, m):
    b = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            b[i][j + m // 2] = a[i][j]
            b[i + n // 2][j + m // 2] = a[i][j + m // 2]
            b[i + n // 2][j] = a[i + n // 2][j + m // 2]
            b[i][j] = a[i + n // 2][j]
    return b

def op_6(a, n, m):
    b = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            b[i+n//2][j] = a[i][j]
            b[i][j] = a[i][j+m//2]
            b[i][j+m//2] = a[i+n//2][j+m//2]
            b[i+n//2][j+m//2] = a[i+n//2][j]
    return b

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
op = list(map(int, input().split()))

for x in op:
    if x == 1:
        a = op_1(a, len(a), len(a[0]))
    elif x == 2:
        a = op_2(a, len(a), len(a[0]))
    elif x == 3:
        a = op_3(a, len(a), len(a[0]))
    elif x == 4:
        a = op_4(a, len(a), len(a[0]))
    elif x == 5:
        a = op_5(a, len(a), len(a[0]))
    else:
        a = op_6(a, len(a), len(a[0]))

for x in a:
    print(" ".join(map(str, x)))
