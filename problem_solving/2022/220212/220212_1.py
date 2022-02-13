def delete(board):
    global score

    res = False
    max_row = -1
    for i in range(6):
        flg = True
        for j in range(4):
            if board[i][j] == 0:
                flg = False

        # 블록 삭제
        if flg:
            score += 1
            res = True
            max_row = max(max_row, i)
            for j in range(4):
                board[i][j] = 0

    # 블록 아래로 이동
    for i in range(max_row, -1, -1):
        for j in range(4):
            if board[i][j] == 1 or board[i][j] == 3:
                now = i + 1
                while now < 6 and board[now][j] == 0:
                    board[now][j], board[now - 1][j] = board[now - 1][j], 0
                    now += 1
            elif j < 3 and board[i][j] == 2 and board[i][j + 1] == 2:
                now = i + 1
                while now < 6 and board[now][j] == 0 and board[now][j + 1] == 0:
                    board[now][j], board[now][j + 1] = board[now - 1][j], board[now - 1][j + 1]
                    board[now - 1][j], board[now - 1][j + 1] = 0, 0
                    now += 1

    return res


def monomino(board, col, type):
    max_row = -1
    for i in range(6):
        if board[i][col] == 0:
            max_row = i
        else:
            break

    if type == 2:
        max_row2 = -1
        for i in range(6):
            if board[i][col + 1] == 0:
                max_row2 = i
            else:
                break
        max_row = min(max_row, max_row2)

    board[max_row][col] = type
    if type == 2:
        board[max_row][col + 1] = type
    elif type == 3:
        board[max_row - 1][col] = type

    while True:
        if not delete(board):
            break

    # 특별한 칸 처리
    cnt = 0
    for i in range(2):
        flg = False
        for j in range(4):
            if board[i][j] != 0:
                flg = True

        if flg:
            cnt += 1

    if cnt > 0:
        for i in range(5, -1, -1):
            for j in range(4):
                board[i][j] = 0
                if i - cnt >= 0:
                    board[i][j] = board[i - cnt][j]

    while True:
        if not delete(board):
            break


if __name__ == '__main__':
    n = int(input())
    green = [[0] * 4 for _ in range(6)]
    blue = [[0] * 4 for _ in range(6)]

    score = 0
    for _ in range(n):
        t, x, y = map(int, input().split())
        # t = 1 -> (x, y)
        # t = 2 -> (x, y), (x, y + 1)
        # t = 3 -> (x, y), (x + 1, y)

        if t == 1:
            monomino(green, y, 1)
            monomino(blue, x, 1)
        elif t == 2:
            monomino(green, y, 2)
            monomino(blue, x, 3)
        else:
            monomino(green, y, 3)
            monomino(blue, x, 2)

    print(score)

    ans = 0
    for i in range(6):
        for j in range(4):
            if green[i][j] != 0:
                ans += 1
            if blue[i][j] != 0:
                ans += 1
    print(ans)