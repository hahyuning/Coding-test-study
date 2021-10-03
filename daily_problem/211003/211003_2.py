t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    # d[i][j]: i 번째 수를 고를 때, 1 부터 j 까지의 숫자 중에서 선택하는 경우의 수
    # d[i][j] = d[i - 1][j // 2] + d[i][j - 1] (j 번째 숫자를 선택하는 경우 + 선택하지 않는 경우)
    d = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        d[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = d[i - 1][j // 2] + d[i][j - 1]

    print(d[n][m])