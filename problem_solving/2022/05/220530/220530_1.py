def dfs(x, y, res):
    global max_val, min_val

    if x == n - 1 and y == n - 1:
        max_val = max(max_val, eval(res))
        min_val = min(min_val, eval(res))
        return

    for k in range(2):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if board[x][y].isdigit():
                if board[nx][ny] in ["+", "-", "*"]:
                    dfs(nx, ny, res + board[nx][ny])
            else:
                if board[nx][ny].isdigit():
                    dfs(nx, ny, "(" + res + board[nx][ny] + ")")
            visited[nx][ny] = False

n = int(input())
board = [input().split() for _ in range(n)]

max_val = -(5 ** 20)
min_val = 5 ** 20

dx = [1, 0]
dy = [0, 1]
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

dfs(0, 0, board[0][0])
print(max_val, min_val)