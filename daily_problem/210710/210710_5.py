from collections import deque

n, m = map(int, input().split())
hx, hy = map(int, input().split())
hx -= 1
hy -= 1
ex, ey = map(int, input().split())
ex -= 1
ey -= 1
a = [list(map(int, input().split())) for _ in range(n)]

check = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
q = deque()
q.append((hx, hy, 0))
check[hx][hy][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y, wall = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and check[nx][ny][wall] == -1:
                check[nx][ny][wall] = check[x][y][wall] + 1
                q.append((nx, ny, wall))
            elif a[nx][ny] == 1 and wall == 0 and check[nx][ny][wall + 1] == -1:
                check[nx][ny][wall + 1] = check[x][y][wall] + 1
                q.append((nx, ny, wall + 1))
ans = -1
for x in check[ex][ey]:
    if x != -1:
        if ans == -1 or x < ans:
            ans = x
print(ans)