import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global tmp, check
    check[x][y] = True
    tmp += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1 and check[nx][ny] == False:
                dfs(nx, ny)

n, m, k = map(int, input().split())
a = [[0] * m for _ in range(n)]
for _ in range(k):
    sx, sy = map(int, input().split())
    a[sx - 1][sy - 1] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

check = [[False] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if check[i][j] == False and a[i][j] == 1:
            tmp = 0
            dfs(i, j)
            ans = max(ans, tmp)

print(ans)