from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
check = [[-1] * m for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            q.append((i, j))
            check[i][j] = 0

while q:
    x, y = q.popleft()
    if a[x][y] in [3, 4, 5]:
        print("TAK")
        print(check[x][y])
        sys.exit(0)

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == -1 and a[nx][ny] != 1:
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1

print("NIE")