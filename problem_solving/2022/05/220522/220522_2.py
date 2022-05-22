def solution(size, i, j):
    global cnt

    cnt += 1
    nxt_size = size // 2

    Ltromino = [[i + nxt_size - 1, j + nxt_size - 1], [i + nxt_size, j + nxt_size - 1], [i + nxt_size - 1, j + nxt_size], [i + nxt_size, j + nxt_size]]
    for idx, val in enumerate([[i, j], [i + nxt_size, j], [i, j + nxt_size], [i + nxt_size, j + nxt_size]]):
        sx, sy = val
        check = False
        for nx in range(sx, sx + nxt_size):
            for ny in range(sy, sy + nxt_size):
                if board[nx][ny] != 0:
                    check = True

        if not check:
            board[Ltromino[idx][0]][Ltromino[idx][1]] = cnt

    if size == 2:
        return

    solution(nxt_size, i, j)
    solution(nxt_size, i + nxt_size, j)
    solution(nxt_size, i, j + nxt_size)
    solution(nxt_size, i + nxt_size, j + nxt_size)


k = int(input())
x, y = map(int, input().split())
x, y = 2 ** k - y, x - 1

cnt = 0
board = [[0] * 2 ** k for _ in range(2 ** k)]
board[x][y] = -1
solution(2 ** k, 0, 0)

for row in board:
    print(*row)