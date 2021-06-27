from collections import deque
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
a = [input() for _ in range(n)]

key_num = dict()
key_loc = dict()

# 처음 위치에서 열쇠까지의 거리
cnt = 0
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] == "S":
            sx, sy = i, j
            key_num[(i, j)] = 0
            key_loc[0] = (i, j)
        if a[i][j] == "K":
            cnt += 1
            key_num[(i, j)] = cnt
            key_loc[cnt] = (i, j)

q = deque()
q.append((sx, sy))
d = [[-1] * n for _ in range(n)]
d[sx][sy] = 0
key_dist = dict()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1 and a[nx][ny] != "1":
            d[nx][ny] = d[x][y] + 1
            q.append((nx, ny))
            if a[nx][ny] == "K":
                key_dist[key_num[(nx, ny)]] = d[nx][ny]

d = [[0] * (m + 1) for _ in range(m + 1)]
# 각 열쇠 사이의 거리
for i in range(1, m + 1):
    x, y = key_loc[i]
    q = deque()
    q.append((x, y))
    dist = [[-1] * n for _ in range(n)]
    dist[x][y] = 0

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            nx, ny = xx + dx[k], yy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and a[nx][ny] != "1":
                dist[nx][ny] = dist[xx][yy] + 1
                q.append((nx, ny))
                if a[nx][ny] == "K":
                    d[i][key_num[(nx, ny)]] = dist[nx][ny]

edges = []
for i, x in key_dist.items():
    edges.append((x, 0, i))
for i in range(1, m + 1):
    for j in range(i, m + 1):
        if i == j:
            continue
        if d[i][j] > 0:
            edges.append((d[i][j], i, j))
edges.sort()

parent = [i for i in range(m + 1)]
res = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += cost

for i in range(m):
    if find(i) != find(i + 1):
        print(-1)
        sys.exit(0)

print(res)