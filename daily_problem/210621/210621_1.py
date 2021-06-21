from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
check = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wolf = 0
sheep = 0

for i in range(n):
    for j in range(m):
        if a[i][j] != "#" and not check[i][j]:
            wcnt = 0
            scnt = 0
            if a[i][j] == "o":
                scnt += 1
            elif a[i][j] == "v":
                wcnt += 1

            q = deque()
            check[i][j] = True
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and a[nx][ny] != "#":
                        if a[nx][ny] == "o":
                            scnt += 1
                        elif a[nx][ny] == "v":
                            wcnt += 1
                        check[nx][ny] = True
                        q.append((nx, ny))
            if wcnt < scnt:
                sheep += scnt
            else:
                wolf += wcnt

print(sheep, wolf)