from collections import deque

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

q = deque()
d = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            q.append((i, j))
            d[i][j] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1:
            if a[nx][ny] == 1:
                d[nx][ny] = d[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            d[i][j] = 0
for row in d:
    print(*row)
