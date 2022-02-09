from collections import deque

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs1(x, y):
    q = deque()
    q.append((x, y))
    d = [[-1] * m for _ in range(n)]
    d[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] == -1 and a[nx][ny] == 0:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
    return d[n - 1][m - 1]

def bfs2(x, y):
    q = deque()
    q.append((x, y))
    d = [[-1] * m for _ in range(n)]
    d[x][y] = 0

    check = False
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1:
                if a[nx][ny] == 0:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
                elif a[nx][ny] == 2:
                    d[nx][ny] = d[x][y] + 1
                    check = True
                    break
        if check:
            break

    return d[sx][sy]

n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            sx, sy = i, j

res1 = bfs1(0, 0)
res2 = bfs2(0, 0)

if res1 == -1:
    res1 = t + 1

if res2 == -1:
    res2 = t + 1
else:
    res2 += abs(sx - n + 1) + abs(sy - m + 1)

if res1 > t and res2 > t:
    print("Fail")
elif res1 > t and res2 <= t:
    print(res2)
elif res2 > t and res1 <= t:
    print(res1)
elif res1 <= t and res2 <= t:
    print(min(res1, res2))