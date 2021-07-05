from collections import deque

def rotate(d):
    if d == 0 or d == 1:
        return [2, 3]
    elif d == 2 or d == 3:
        return [0, 1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
sx, sy, sd = sx - 1, sy - 1, sd - 1
ex, ey, ed = ex - 1, ey - 1, ed - 1
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

check = dict()
check[(sx, sy, sd)] = 0
q = deque()
q.append((sx, sy, sd))

while q:
    x, y, d = q.popleft()
    # 회전
    r = rotate(d)
    for nd in r:
        if (x, y, nd) not in check and a[x][y] == 0:
            check[(x, y, nd)] = check[(x, y, d)] + 1
            q.append((x, y, nd))
    # 전진
    for i in range(1, 4):
        nx, ny = x + i * dx[d], y + i * dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if a[nx][ny] == 1:
            break
        if (nx, ny, d) not in check and a[nx][ny] == 0:
            check[(nx, ny, d)] = check[(x, y, d)] + 1
            q.append((nx, ny, d))

print(check[(ex, ey, ed)])