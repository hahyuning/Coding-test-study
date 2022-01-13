from copy import deepcopy

def rotate(a):
    res = deepcopy(a)
    for i in range(n):
        res[i][i] = a[n // 2][i]
        res[i][n // 2] = a[i][i]
        res[i][n - i - 1] = a[i][n // 2]
        res[n // 2][n - i - 1] = a[i][n - i - 1]

    return res

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    if d < 0:
        d += 360
    d //= 45

    a = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(d):
        a = rotate(a)

    for row in a:
        print(*row)
