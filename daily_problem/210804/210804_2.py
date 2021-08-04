import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(0, 3 * m, 3):
        a[i][j // 3] = (x[j] + x[j + 1] + x[j + 2]) / 3

t = int(input())
for i in range(n):
    for j in range(m):
        if a[i][j] >= t:
            a[i][j] = 1
        else:
            a[i][j] = 0

cnt = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and not visited[i][j]:
            cnt += 1
            dfs(i, j)
print(cnt)