from collections import deque
import sys
input = sys.stdin.readline

n, m, h, w, k = map(int, input().split())
wall = dict()
for _ in range(k):
    x, y = map(int, input().split())
    wall[x - 1, y - 1] = True
sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
ex, ey = map(int, input().split())
ex, ey = ex - 1, ey - 1

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
            if k == 0:
                for j in range(w):
                    if (nx, ny + j) in wall:
                        check = False
                        d[nx][ny + j] = -2
                        break
            elif k == 1:
                for j in range(w):
                    if (nx + h - 1, ny + j) in wall:
                        check = False
                        d[nx + h - 1][ny + j] = -2
                        break
            elif k == 2:
                for i in range(h):
                    if (nx + i, ny) in wall:
                        check = False
                        d[nx + i][ny] = -2
                        break
            else:
                for i in range(h):
                    if (nx + i, ny + w - 1) in wall:
                        check = False
                        d[nx + i][ny + w - 1] = -2
                        break
            if check:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

print(d[ex][ey])