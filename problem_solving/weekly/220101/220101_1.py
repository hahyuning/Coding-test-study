# 주어진 정사각형이 모두 비어있는지 체크
def check(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != 0:
                return False
    return True

def fill_tile(x, y, size):
    global tile_num
    tile_num += 1

    nxt_size = size // 2
    # 0 0
    # 0 1
    if check(x, y, nxt_size):
        board[x + nxt_size - 1][y + nxt_size - 1] = tile_num
    # 0 0
    # 1 0
    if check(x, y + nxt_size, nxt_size):
        board[x + nxt_size - 1][y + nxt_size] = tile_num
    # 0 1
    # 0 0
    if check(x + nxt_size, y, nxt_size):
        board[x + nxt_size][y + nxt_size - 1] = tile_num
    # 1 0
    # 0 0
    if check(x + nxt_size, y + nxt_size, nxt_size):
        board[x + nxt_size][y + nxt_size] = tile_num

    if size == 2:
        return

    fill_tile(x, y, nxt_size)
    fill_tile(x + nxt_size, y, nxt_size)
    fill_tile(x, y + nxt_size, nxt_size)
    fill_tile(x + nxt_size, y + nxt_size, nxt_size)

k = int(input())
n = 2 ** k
x, y = map(int, input().split())
x, y = x - 1, n - y

board = [[0] * n for _ in range(n)]
board[y][x] = -1

tile_num = 0
fill_tile(0, 0, n)

for row in board:
    print(*row)