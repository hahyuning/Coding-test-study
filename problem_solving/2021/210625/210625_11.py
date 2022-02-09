from collections import deque
import sys
sys.setrecursionlimit(10 ** 5)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    check[x][y] = True
    a[x][y] = cnt

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and not check[nx][ny] and a[nx][ny] == 1:
            check[nx][ny] = True
            dfs(nx, ny, cnt)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and not check[i][j]:
            cnt += 1
            dfs(i, j, cnt)

ans = -1
for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            check = [[-1] * n for _ in range(n)]
            q = deque()
            q.append((i, j))
            check[i][j] = 0

            ch = False
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == -1:
                        if a[nx][ny] != 0 and a[nx][ny] != a[i][j]:
                            if ans == -1 or check[x][y] < ans:
                                ans = check[x][y]
                                ch = True
                                break
                        elif a[nx][ny] == 0:
                            check[nx][ny] = check[x][y] + 1
                            q.append((nx, ny))
                if ch:
                    break
print(ans)