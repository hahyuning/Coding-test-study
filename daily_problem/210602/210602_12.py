from collections import deque
import sys

def bfs(i, j):
    q = deque()
    q.append((i, j))
    dist[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != 0 and not dist[nx][ny]:
                    q.append((nx, ny))
                    dist[nx][ny] = True

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
while True:
    island = 0
    dist = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0 and not dist[i][j]:
                island += 1
                bfs(i, j)

    if island >= 2:
        print(cnt)
        sys.exit(0)
    if island == 0:
        print(0)
        break

    cnt += 1
    b = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] != 0:
                w = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                        w += 1
                b[i][j] = w
    for i in range(n):
        for j in range(m):
            a[i][j] = max(0, a[i][j] - b[i][j])
