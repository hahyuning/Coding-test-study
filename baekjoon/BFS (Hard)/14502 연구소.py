from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global ans
    a = copy.deepcopy(maps)
    q = deque()
    print(a)

    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    a[nx][ny] = 2
                    q.append((nx, ny))

    birus = 0
    for i in a:
        birus += i.count(0)
    ans = max(ans, birus)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(cnt + 1)
                maps[i][j] = 0

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0
wall(0)
print(ans)