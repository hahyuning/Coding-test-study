n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = -1
for k in range(3):
    # d[i][j]: i 번째 집을 j 번째 색깔로 칠했을 때의 비용의 최솟값
    d = [[1000 * 1000 + 1] * 3 for _ in range(n)]

    d[0][k] = a[0][k]
    for i in range(1, n):
        if i == n - 1:
            for j in range(3):
                if j != k:
                    d[i][j] = min(d[i - 1][(j + 1) % 3], d[i - 1][(j + 2) % 3]) + a[i][j]
            continue

        d[i][0] = min(d[i - 1][1], d[i - 1][2]) + a[i][0]
        d[i][1] = min(d[i - 1][2], d[i - 1][0]) + a[i][1]
        d[i][2] = min(d[i - 1][1], d[i - 1][0]) + a[i][2]

    for i in range(3):
        if d[n - 1][i] != 0:
            if ans == -1 or d[n - 1][i] < ans:
                ans = d[n - 1][i]
print(ans)