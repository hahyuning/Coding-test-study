from collections import deque
from itertools import permutations

def rotation(a):
    b = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            b[j][4 - i] = a[i][j]
    return b

def check(i, j):
    dist = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((0, i, j))
    dist[0][i][j] = 0

    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                if dist[nx][ny][nz] == -1 and board[nx][ny][nz] == 1:
                    dist[nx][ny][nz] = dist[x][y][z] + 1
                    q.append((nx, ny, nz))

    if i == 0 and j == 0:
        return dist[4][4][4]
    elif i == 0:
        return dist[4][4][0]
    elif j == 0:
        return dist[4][0][4]
    else:
        return dist[4][0][0]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
init_board = []
for _ in range(5):
    tmp = [list(map(int, input().split())) for _ in range(5)]
    init_board.append(tmp)

p = permutations(init_board)
ans = -1
for board in p:
    board = list(board)
    for i in [0, 4]:
        for j in [0, 4]:
            if board[0][i][j] == 1:
                for _ in range(4):
                    board[1] = rotation(board[1])
                    for _ in range(4):
                        board[2] = rotation(board[2])
                        for _ in range(4):
                            board[3] = rotation(board[3])
                            for _ in range(4):
                                board[4] = rotation(board[4])

                                if i == 0 and j == 0 and board[4][4][4] == 0:
                                    continue
                                elif i == 0 and j == 4 and board[4][4][0] == 0:
                                    continue
                                elif j == 0 and i == 4 and board[4][0][4] == 0:
                                    continue
                                elif i == 4 and j == 4 and board[4][0][0] == 0:
                                    continue

                                res = check(i, j)
                                if res != -1:
                                    if ans == -1 or res < ans:
                                        ans = res
print(ans)

