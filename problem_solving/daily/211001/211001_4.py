def check(flowers):
    cost = 0
    visited = [[False] * n for _ in range(n)]
    for f in flowers:
        x = f // n
        y = f % n

        if x == 0 or y == 0 or x == n - 1 or y == n - 1:
            return 10000

        for i in range(5):
            nx, ny = x + dx[i], y + dy[i]
            if visited[nx][ny]:
                return 10000

            visited[nx][ny] = True
            cost += a[nx][ny]

    return cost

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
flower = [[False] * n for _ in range(n)]
ans = 10000

for i in range(n ** 2 - 2):
    for j in range(i + 1, n ** 2 - 1):
        for k in range(j + 1, n ** 2):
            cost = check([i, j, k])
            ans = min(cost, ans)
print(ans)