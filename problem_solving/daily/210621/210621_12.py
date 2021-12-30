import sys
input = sys.stdin.readline

def dfs(x, y):
    if y == m - 1:
        return True

    for k in range(3):
        nx, ny = x + dx[k], y + 1
        if 0 <= nx < n and not check[nx][ny] and a[nx][ny] == ".":
            check[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False

n, m = map(int, input().split())
a = [input() for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [-1, 0, 1]
ans = 0

for i in range(n):
    if a[i][0] == ".":
        if dfs(i, 0):
            ans += 1
print(ans)