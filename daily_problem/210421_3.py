from collections import deque

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0))
dist[0][0] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == "1" and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

print(dist[n - 1][m - 1])