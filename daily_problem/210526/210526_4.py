from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1 ,1]

while True:
    l, n, m = map(int, input().split())
    if l == 0 and n == 0 and m == 0:
        break

    a = []
    for _ in range(l):
        b = [list(input()) for _ in range(n)]
        c = input()
        a.append(b)

    sh, sx, sy = 0, 0, 0
    eh, ex, ey = 0, 0, 0
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if a[i][j][k] == "S":
                    sh, sx, sy = i, j, k
                if a[i][j][k] == "E":
                    a[i][j][k] = "."
                    eh, ex, ey = i, j, k

    d = [[[-1] * m for _ in range(n)] for _ in range(l)]
    q = deque()
    q.append((sh, sx, sy))
    d[sh][sx][sy] = 0

    while q:
        h, x, y = q.popleft()
        for k in range(6):
            nh, nx, ny = h + dh[k], x + dx[k], y + dy[k]
            if 0 <= nh < l and 0 <= nx < n and 0 <= ny < m:
                if a[nh][nx][ny] == "." and d[nh][nx][ny] == -1:
                    d[nh][nx][ny] = d[h][x][y] + 1
                    q.append((nh, nx, ny))

    if d[eh][ex][ey] == -1:
        print("Trapped!")
    else:
        print("Escaped in " + str(d[eh][ex][ey]) + " minute(s).")