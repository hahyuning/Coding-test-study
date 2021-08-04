import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
weight = [[0] * m for _ in range(n)]

q = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if a[i][j] == "S":
            heapq.heappush(q, (0, i, j))
            dist[i][j] = 0
        if a[i][j] == "g":
            weight[i][j] = 2500
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == ".":
                    weight[nx][ny] = 1

while q:
    cost, x, y = heapq.heappop(q)
    if a[x][y] == "F":
        print(dist[x][y] // 2500, dist[x][y] % 2500)
        break

    if dist[x][y] != -1 and dist[x][y] < cost:
        continue

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            nxt_cost = cost + weight[nx][ny]
            if nxt_cost < dist[nx][ny] or dist[nx][ny] == -1:
                dist[nx][ny] = nxt_cost
                heapq.heappush(q, (nxt_cost, nx, ny))
