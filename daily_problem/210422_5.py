from collections import deque

n, m, k = map(int, input().split())
a = [input() for _ in range(n)]
sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1

q = deque()
q.append((sx, sy))
dist = [[-1] * m for _ in range(n)]
dist[sx][sy] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        j = 0
        nx, ny = x + dx[i], y + dy[i]
        while j < k and (0 <= nx < n and 0 <= ny < m):
            if a[nx][ny] == "#":
                break

            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

            # 시간초과 때문에 추가
            elif dist[nx][ny] <= dist[x][y]:
                break

            nx += dx[i]
            ny += dy[i]
            j += 1

print(dist[ex][ey])


