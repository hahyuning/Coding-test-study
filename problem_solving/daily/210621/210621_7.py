import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    check[i][j] = True

    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny] and a[nx][ny] == "#":
            dfs(nx, ny)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [input().rstrip() for _ in range(n)]
    check = [[False] * m for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == "#" and not check[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)