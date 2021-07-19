from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, -1, -1, 0, 1, 1]

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
q = deque()
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == ".":
            a[i][j] = 0
            visited[i][j] = 0
            q.append((i, j))
        else:
            a[i][j] = int(a[i][j])

ans = -1
while q:
    x, y = q.popleft()
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] > 0:
                a[nx][ny] -= 1
                if a[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    ans = max(ans, visited[nx][ny])
                    q.append((nx, ny))
print(ans)