from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [input() for _ in range(n)]
d = [[0] * m for _ in range(n)]

q = deque()
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == "J":
            sx, sy = i, j
        if a[i][j] == "F":
            q.append((i, j, 0))
            d[i][j] = -1

if sx == 0 or sy == 0:
    print(1)
else:
    q.append((sx, sy, 1))
    d[sx][sy] = 1

    ex, ey = -1, -1
    while q:
        x, y, f = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
                    if a[nx][ny] == "." and d[nx][ny] == 0 and f == 1:
                        d[nx][ny] = d[x][y] + 1
                        ex, ey = nx, ny
                        break
                if d[nx][ny] == 0 and a[nx][ny] != "#" and f == 0:
                    d[nx][ny] = -1
                    q.append((nx, ny, 0))
                if d[nx][ny] == 0 and a[nx][ny] == "." and f == 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny, 1))
        if ex != -1:
            break

    if ex == -1:
        print("IMPOSSIBLE")
    else:
        print(d[ex][ey])