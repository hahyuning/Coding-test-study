from collections import deque
n = int(input())
a = [input() for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            if a[nx][ny] == "0":
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
            else:
                q.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]

print(dist[n - 1][n - 1])