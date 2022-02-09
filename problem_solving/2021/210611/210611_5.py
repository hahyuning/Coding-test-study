from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
h, w, sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
d = [[-1] * m for _ in range(n)]
q.append((sx, sy))
d[sx][sy] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        check = True
        if 0 <= nx < n - h + 1 and 0 <= ny < m - w + 1 and d[nx][ny] == -1:
            for i in range(h):
                if a[nx + i][ny + w - 1] == 1:
                    check = False
                    d[nx + i][ny + w - 1] = -2
                    break
                if a[nx + i][ny] == 1:
                    check = False
                    d[nx + i][ny] = -2
                    break
            else:
                for j in range(w):
                    if a[nx + h - 1][ny + j] == 1:
                        check = False
                        d[nx + h - 1][ny + j] = -2
                        break
                    if a[nx][ny + j] == 1:
                        check = False
                        d[nx][ny + j] = -2
                        break
            if check:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

print(d[ex][ey])
