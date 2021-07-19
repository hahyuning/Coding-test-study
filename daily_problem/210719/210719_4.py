from itertools import combinations
import sys
input = sys.stdin.readline

def dfs(x, y):
    global cnt, zero
    cnt += 1

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
            if board[nx][ny] == 0:
                zero += 1
            elif board[nx][ny] == 2:
                check[nx][ny] = True
                dfs(nx, ny)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
c = list(combinations([i for i in range(n * m)], 2))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
for x in c:
    a, b, c, d = x[0] // m, x[0] % m, x[1] // m, x[1] % m
    if board[a][b] != 0 or board[c][d] != 0:
        continue

    board[a][b] = 1
    board[c][d] = 1

    tmp = 0
    check = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and not check[i][j]:
                cnt = 0
                zero = 0
                check[i][j] = True
                dfs(i, j)
                if zero == 0:
                    tmp += cnt
    board[a][b] = 0
    board[c][d] = 0

print(ans)
