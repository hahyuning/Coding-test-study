from collections import deque

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(x, y):
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    while q:
        sx, sy = q.popleft()
        for i in range(8):
            nx, ny = sx + dx[i], sy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                if maps[nx][ny] == 1:
                    return dist[sx][sy] + 1

                dist[nx][ny] = dist[sx][sy] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

res = -1
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            d = bfs(i, j)
            if res == -1 or res < d:
                res = d
print(res)
