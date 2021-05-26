from collections import deque
import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(l)]
d = [[[0] * m for _ in range(n)] for _ in range(l)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

cnt = 0
q = deque()
for k in range(l):
    for i in range(n):
        for j in range(m):
            if a[k][i][j] == 1:
                q.append((k, i, j))
            elif a[k][i][j] == -1:
                cnt += 1

if len(q) == n * m * l - cnt:
    print(0)
else:
    while q:
        h, x, y = q.popleft()
        for k in range(6):
            nx, ny, nh = x + dx[k], y + dy[k], h + dh[k]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nh < l:
                if a[nh][nx][ny] == 0 and d[nh][nx][ny] == 0:
                    a[nh][nx][ny] = 1
                    d[nh][nx][ny] = d[h][x][y] + 1
                    q.append((nh, nx, ny))

    max_day = 0
    check = False
    for k in range(l):
        for i in range(n):
            for j in range(m):
                max_day = max(max_day, d[k][i][j])
                if a[k][i][j] == 0:
                    check = True
    print(max_day if not check else -1)


