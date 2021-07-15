n, m, k = map(int, input().split())
if k != 0:
    k -= 1
    kx = k // m
    ky = k % m

    d1 = [[0] * (ky + 1) for _ in range(kx + 1)]
    d2 = [[0] * (m - ky) for _ in range(n - kx)]
    for j in range(ky + 1):
        d1[0][j] = 1
    for i in range(kx + 1):
        d1[i][0] = 1

    for j in range(m - ky):
        d2[0][j] = 1
    for i in range(n - kx):
        d2[i][0] = 1

    for i in range(1, kx + 1):
        for j in range(1, ky + 1):
            d1[i][j] = d1[i - 1][j] + d1[i][j - 1]

    for i in range(1, n - kx):
        for j in range(1, m - ky):
            d2[i][j] = d2[i - 1][j] + d2[i][j - 1]

    print(d1[-1][-1] * d2[-1][-1])
else:
    d = [[0] * m for _ in range(n)]
    for j in range(m):
        d[0][j] = 1
    for i in range(n):
        d[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
    print(d[-1][-1])
