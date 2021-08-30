import sys

# 각 섬에 번호 붙이기
def dfs(x, y, num):
    check[x][y] = True
    a[x][y] = num

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and a[nx][ny] == 1:
            dfs(nx, ny, num)

# 한 섬에서 다른 섬까지의 거리 구하기
def distance(start):
    res = dict()
    check = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == start and not check[i][j]:
                check[i][j] = True
                for k in range(4):
                    x, y = i, j
                    d = [[-1] * m for _ in range(n)]
                    nx, ny = x + dx[k], y + dy[k]
                    while 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1:
                        # 자기 자신을 만난 경우
                        if a[nx][ny] == a[i][j]:
                            break
                        d[nx][ny] = d[x][y] + 1
                        # 다른 섬을 만난 경우
                        if a[nx][ny] != 0 and d[nx][ny] > 1:
                            if a[nx][ny] in res and d[nx][ny] < res[a[nx][ny]]:
                                res[a[nx][ny]] = d[nx][ny]
                            elif a[nx][ny] not in res:
                                res[a[nx][ny]] = d[nx][ny]
                            break

                        x = nx
                        y = ny
                        nx += dx[k]
                        ny += dy[k]
    return res

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

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 섬의 개수
num = 0
check = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not check[i][j] and a[i][j] == 1:
            num += 1
            dfs(i, j, num)

# 각 섬 사이의 거리
dist = [[0] * (num + 1) for _ in range(num + 1)]
for i in range(1, num + 1):
    res = distance(i)
    for j in res:
        dist[i][j] = res[j]

# 유니온 파인드
edges = []
for i in range(1, num + 1):
    for j in range(i, num + 1):
        if i == j:
            continue
        if dist[i][j] > 1:
            edges.append((dist[i][j], i, j))
edges.sort()

parent = [i for i in range(num + 1)]
res = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += cost

for i in range(1, num):
    if find(i) != find(i + 1):
        print(-1)
        sys.exit(0)

print(res)