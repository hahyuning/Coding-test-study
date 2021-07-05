from collections import deque

n, m = map(int, input().split())
dist = [[-1] * (n + 1) for _ in range(n + 1)]
kx, ky = map(int, input().split())
kx -= 1
ky -= 1
e = []
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    e.append((x, y))

q = deque()
q.append((kx, ky))
dist[kx][ky] = 0

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

while q:
    x, y = q.popleft()
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for x, y in e:
    print(dist[x][y], end=" ")