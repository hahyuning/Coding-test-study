from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs():
    while q:
        x, y, a, b = q.popleft()
        # 버튼을 누른 횟수가 10보다 커지면 종료
        if ck[x][y][a][b] > 10:
            break

        for i in range(4):
            nx, ny, na, nb = x + dx[i], y + dy[i], a + dx[i], b + dy[i]
            # 두 동전이 모두 범위를 벗어난 경우
            if (nx <= -1 or nx >= n or ny <= -1 or ny >= m) and (na <= -1 or na >= n or nb <= -1 or nb >= m):
                continue

            # 한 동전만 벗어난 경우
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                return ck[x][y][a][b]
            # 다른 한 동전만 벗어난 경우
            if na <= -1 or na >= n or nb <= -1 or nb >= m:
                return ck[x][y][a][b]

            # 이동하려는 곳에 벽이 있는 경우 -> 이동처리 하지 않음
            if board[nx][ny] == "#":
                nx, ny = x, y
            if board[na][nb] == "#":
                na, nb = a, b

            if ck[nx][ny][na][nb] == 0:
                ck[nx][ny][na][nb] = ck[x][y][a][b] + 1
                q.append((nx, ny, na, nb))
    return -1

# -----------------------------------------------------------------------------
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 두 개의 동전 위치 기록한 후, board 에서는 빈칸 처리
coin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "o":
            coin += [i, j]
            board[i][j] = "."

# c[a][b][c][d]: 코인이 (a, b), (c, d) 위치로 올 때까지의 버튼을 누른 횟수 저장
ck = [[[[0]* m for _ in range(n)] for _ in range(m)] for _ in range(n)]
ck[coin[0]][coin[1]][coin[2]][coin[3]] = 1

q = deque()
q.append([coin[0], coin[1], coin[2], coin[3]])

print(bfs())