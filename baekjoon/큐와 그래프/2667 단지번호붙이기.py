def dfs(x, y):
    global cnt
    board[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1:
                dfs(nx, ny)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)