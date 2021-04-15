from collections import deque

k = int(input())
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
cost = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

dist = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 0

while q:
    x, y, c = q.popleft()
    for i in range(12):
        nx = x + dx[i]
        ny = y + dy[i]
        nc = c + cost[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            if nc <= k and dist[nx][ny][nc] == -1:
                dist[nx][ny][nc] = dist[x][y][c] + 1
                q.append((nx, ny, nc))

ans = -1
for i in range(k + 1):
    if dist[n - 1][m - 1][i] != -1:
        if ans == -1 or ans > dist[n - 1][m - 1][i]:
            ans = dist[n - 1][m - 1][i]
print(ans)