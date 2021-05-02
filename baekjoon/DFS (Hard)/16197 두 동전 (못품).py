def dfs(x1, y1, x2, y2, cnt):
    global ans
    if cnt > 10:
        return 11

    check1 = check2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        check1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        check2 = True

    if check1 ^ check2:
        ans = min(ans, cnt)
        return
    if check1 and check2:
        return

    for i in range(4):
        nx1 = x1 + dx[i]
        nx2 = x2 + dx[i]
        ny1 = y1 + dy[i]
        ny2 = y2 + dy[i]

        if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == 1:
            nx1 = x1
            ny1 = y1
        if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == 1:
            nx2 = x2
            ny2 = y2
        dfs(nx1, ny1, nx2, ny2, cnt + 1)

n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
coins = []
for i in range(n):
    a = list(input())
    for j in range(m):
        if a[j] == "#":
            board[i][j] = 1
        elif a[j] == "o":
            coins.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 11
dfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)
if ans == 11:
    print(-1)
else:
    print(ans)
#------------------------------------------------------------------------------

def dfs(x1, y1, x2, y2, cnt):
    if cnt > 10:
        return -1

    check1 = check2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        check1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        check2 = True

    if check1 ^ check2:
        return cnt
    if check1 and check2:
        return -1

    ans = -1
    for i in range(4):
        nx1 = x1 + dx[i]
        nx2 = x2 + dx[i]
        ny1 = y1 + dy[i]
        ny2 = y2 + dy[i]

        if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == 1:
            nx1 = x1
            ny1 = y1
        if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == 1:
            nx2 = x2
            ny2 = y2

        tmp = dfs(nx1, ny1, nx2, ny2, cnt + 1)
        if tmp == -1:
            continue
        if ans == -1 or tmp < ans:
            ans = tmp
    return ans

n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
coins = []
# 코인 위치 따로 기록
for i in range(n):
    a = list(input())
    for j in range(m):
        if a[j] == "#":
            board[i][j] = 1
        elif a[j] == "o":
            coins.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(dfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0))