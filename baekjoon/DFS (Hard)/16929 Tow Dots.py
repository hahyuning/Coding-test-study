# 같은 색깔로 사이클을 만들 수 있는지 확인하는 문제

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, sx, sy, color):
    # 가려는 곳이 이미 갔던 곳이면 사이클이 발생한 것이므로 True 리턴
    if check[x][y] == True:
        return True

    check[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 왔던 곳으로 다시 가는 경우 continue
            if (nx, ny) == (sx, sy):
                continue

            # 색깔이 같은 경우 dfs 수행
            if board[nx][ny] == color:
                if dfs(nx, ny, x, y, color):
                    return True
    return False

# --------------------------------------------------------
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
# 이미 확인 했는지 여부 기록
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