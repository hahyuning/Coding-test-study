from collections import deque

def bfs():
    while q:
        x, y, a, b = q.popleft()
        if ck[x][y][a][b] > 10:
            break
        for i in range(4):
            nx, ny, na, nb = x + dx[i], y + dy[i], a + dx[i], b + dy[i]
            if (nx <= -1 or nx >= n or ny <= -1 or ny >= m) and (na <= -1 or na >= n or nb <= -1 or nb >= m):
                continue
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                return ck[x][y][a][b]
            if na <= -1 or na >= n or nb <= -1 or nb >= m:
                return ck[x][y][a][b]

            if board[nx][ny] == "#":
                nx, ny = x, y
            if board[na][nb] == "#":
                na, nb = a, b
            if ck[nx][ny][na][nb] == 0:
                ck[nx][ny][na][nb] = ck[x][y][a][b] + 1
                q.append((nx, ny, na, nb))
    return -1

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
coin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "o":
            coin += [i, j]
            board[i][j] = "."

ck = [[[[0]*(m) for _ in range(n)] for _ in range(m)] for _ in range(n)]
ck[coin[0]][coin[1]][coin[2]][coin[3]] = 1
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

q = deque()
q.append([coin[0], coin[1], coin[2], coin[3]])

print(bfs())