from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    a = [input() for _ in range(n)]
    fire = [[False] * m for _ in range(n)]
    time = [[0] * m for _ in range(n)]

    q = deque()
    sx, sy = 0, 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == "@":
                sx, sy = i, j
            if a[i][j] == "*":
                q.append((i, j, 0))
                fire[i][j] = True

    if sx == 0 or sy == 0:
        print(1)
    else:
        q.append((sx, sy, 1))
        time[sx][sy] = 1

        ex, ey = -1, -1
        while q:
            x, y, f = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
                        if not fire[nx][ny] and a[nx][ny] == "." and time[nx][ny] == 0 and f == 1:
                            time[nx][ny] = time[x][y] + 1
                            ex, ey = nx, ny
                            break
                    if not fire[nx][ny] and a[nx][ny] != "#" and f == 0:
                        fire[nx][ny] = True
                        q.append((nx, ny, 0))
                    if not fire[nx][ny] and time[nx][ny] == 0 and a[nx][ny] == "." and f == 1:
                        time[nx][ny] = time[x][y] + 1
                        q.append((nx, ny, 1))
            if ex != -1:
                break

        if ex == -1:
            print("IMPOSSIBLE")
        else:
            print(time[ex][ey])