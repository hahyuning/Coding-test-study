while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    a = [list(map(int, input().split())) for _ in range(n)]
    d = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        d[i][0] = a[i][0]
        ans = max(ans, d[i][0])
    for j in range(m):
        d[0][j] = a[0][j]
        ans = max(ans, d[0][j])

    for i in range(1, n):
        for j in range(1, m):
            if a[i][j] == 1:
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
            ans = max(ans, d[i][j])
    print(ans)