n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def dfs(x, y, direction):
    global cnt
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    if direction == 0 or direction == 2:
        if y + 1 < n and board[x][y + 1] == 0:
            dfs(x, y + 1, 0)
    if direction == 1 or direction == 2:
        if x + 1 < n and board[x + 1][y] == 0:
            dfs(x + 1, y, 1)

    if x + 1 < n and y + 1 < n:
        if board[x + 1][y] == 0 and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)

dfs(0, 1, 0)
print(cnt)