dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, sx, sy, color):
    if check[x][y] == True:
        return True

    check[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) == (sx, sy):
                continue
            if board[nx][ny] == color:
                if dfs(nx, ny, x, y, color):
                    return True
    return False

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
ans = False

for i in range(n):
    for j in range(m):
        if check[i][j] == True:
            continue

        if dfs(i, j, -1, -1, board[i][j]):
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")