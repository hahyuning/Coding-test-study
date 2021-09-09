n, m = map(int, input().split())

a = [[0] * m for _ in range(n)]
x = 0
y = 0
a[x][y] = n * m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

k = 0
ans = 0
for i in range(n * m - 1, 0, -1):
    nx = x + dx[k]
    ny = y + dy[k]

    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
        a[nx][ny] = i
        x = nx
        y = ny
    else:
        k = (k + 1) % 4
        nx = x + dx[k]
        ny = y + dy[k]
        ans += 1

        a[nx][ny] = i
        x = nx
        y = ny

print(ans)