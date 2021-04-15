from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
queue.append((0, 0))
dist[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == 0 and graph[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

print(dist[n - 1][m - 1])