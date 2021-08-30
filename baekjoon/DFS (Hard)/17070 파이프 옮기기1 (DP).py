def dfs(x, y, direction):
    global cnt
    # 목적지에 도착한 경우
    if x == n - 1 and y == n - 1:
        cnt += 1
        return

    # 파이프가 가로 또는 대각선에서 가로로 가는 경우
    if direction == 0 or direction == 2:
        if y + 1 < n and board[x][y + 1] == 0:
            dfs(x, y + 1, 0)
    # 파이프가 세로 또는 대각선에서 세로로 가는 경우
    if direction == 1 or direction == 2:
        if x + 1 < n and board[x + 1][y] == 0:
            dfs(x + 1, y, 1)

    # 파이프가 대각선 방향으로 가는 경우
    if x + 1 < n and y + 1 < n:
        if board[x + 1][y] == 0 and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)

# -----------------------------------------------------------------
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dfs(0, 1, 0)
print(cnt)