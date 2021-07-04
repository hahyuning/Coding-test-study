def pull(x, y, d):
    global score
    board[x][y] = False
    cnt = domino[x][y]
    nx, ny = x + dx[d], y + dy[d]
    for _ in range(cnt - 1):
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return

        if board[nx][ny]:
            board[nx][ny] = False
            score += 1
            pull(nx, ny, d)
        nx += dx[d]
        ny += dy[d]

n, m, r = map(int, input().split())
domino = [list(map(int, input().split())) for _ in range(n)]
striker = []
defender = []

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(r):
    x, y, d = input().split()
    if d == "E":
        d = 0
    elif d == "W":
        d = 1
    elif d == "S":
        d = 2
    else:
        d = 3
    striker.append((int(x) - 1, int(y) - 1, d))
    x, y = map(int, input().split())
    defender.append((x - 1, y - 1))

board = [[True] * m for _ in range(n)]
ans = 0
for i in range(r):
    x, y, d = striker[i]
    score = 1
    pull(x, y, d)
    ans += score

    x, y = defender[i]
    board[x][y] = True

# 공격수의 점수 출력
# 게임판의 상태 출력 (넘어진 것은 F 넘어지지 않은 것은 S)
print(ans)
for i in range(n):
    for j in range(m):
        if board[i][j]:
            print("S", end=" ")
        else:
            print("F", end=" ")
    print()
