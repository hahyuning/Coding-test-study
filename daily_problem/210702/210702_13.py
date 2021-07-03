import sys
input = sys.stdin.readline

def dfs(x, y, d):
    global ans
    if x == ex and y == ey:
        if d == k:
            ans += 1
        return

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and a[nx][ny] != "T":
            check[nx][ny] = True
            dfs(nx, ny, d + 1)
            check[nx][ny] = False

n, m, k = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
sx, sy = n - 1, 0
ex, ey = 0, m - 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check = [[False] * m for _ in range(n)]
check[sx][sy] = True
ans = 0
dfs(sx, sy, 1)
print(ans)