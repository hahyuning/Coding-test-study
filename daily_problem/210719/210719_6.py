from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]
sx, sy, ex, ey = -1, -1, -1, -1
for i in range(n):
    for j in range(n):
        if a[i][j] == "#":
            if sx == - 1 and sy == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

ans = -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(4):
    ssx, ssy = sx + dx[i], sy + dy[i]
    if 0 <= ssx < n and 0 <= ssy < n and a[ssx][ssy] != "*":
        q = deque()
        q.append((sx, sy, i))
        check = dict()
        check[(sx, sy, i)] = 0

        while q:
            x, y, d = q.popleft()
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny, d) not in check and a[nx][ny] != "*":
                check[(nx, ny, d)] = check[(x, y, d)]
                q.appendleft((nx, ny, d))
            if a[x][y] == "!":
                for nd in [(d + 3) % 4, (d + 1) % 4]:
                    nx, ny = x + dx[nd], y + dy[nd]
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny, nd) not in check and a[nx][ny] != "*":
                        check[(nx, ny, nd)] = check[(x, y, d)] + 1
                        q.append((nx, ny, nd))

        for j in range(4):
            if (ex, ey, j) in check:
                if ans == -1 or check[(ex, ey, j)] < ans:
                    ans = check[(ex, ey, j)]
print(ans)