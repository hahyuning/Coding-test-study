from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
check = [[False] * m for _ in range(n)]

q = deque()
for i in range(m):
    if a[0][i] == 0:
        q.append((0, i))
        check[0][i] = True

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and a[nx][ny] == 0:
            if nx == n - 1:
                print("YES")
                sys.exit(0)
            q.append((nx, ny))
            check[nx][ny] = True
print("NO")