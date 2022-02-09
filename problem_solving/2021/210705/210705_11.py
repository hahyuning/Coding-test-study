n, m, k = map(int, input().split())
# d[i][j]: a가 i개, z가 j개 있을 때 만들 수 있는 단어의 개수
d = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = d[i - 1][j] + d[i][j - 1]

if d[n][m] < k:
    print(-1)
else:
    ans = ""
    while True:
        if n == 0 or m == 0:
            ans += "a" * n
            ans += "z" * m
            break

        tmp = d[n - 1][m]
        if k <= tmp:
            ans += "a"
            n -= 1
        else:
            ans += "z"
            m -= 1
            k -= tmp
    print(ans)