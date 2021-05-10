import sys
sys.setrecursionlimit(10 ** 5)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt

    board[x][y] = 1
    cnt += 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            dfs(nx, ny)


n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(n - d, n - b):
        for j in range(a, c):
            board[i][j] = 1

size = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt = 0
            dfs(i, j)
            size.append(cnt)

size.sort()
print(len(size))
print(" ".join(map(str, size)))