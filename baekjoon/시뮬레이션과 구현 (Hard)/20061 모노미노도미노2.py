def monomino(board, col, type):

    # 블럭이 아래로 이동
    max_row = -1
    for i in range(6):
        if board[i][col] == 0:
            max_row = i
        # 다른 블록을 만난 경우
        else:
            break

    if type == 2:
        max_row2 = -1
        for i in range(6):
            if board[i][col + 1] == 0:
                max_row2 = i
            # 다른 블록을 만난 경우
            else:
                break

        max_row = min(max_row, max_row2)

    board[max_row][col] = 1
    if type == 2:
        board[max_row][col + 1] = 1
    elif type == 3:
        board[max_row - 1][col] = 1

    # 삭제되는 블록 처리
    cnt = 0
    deleted_row = -1
    for i in range(6):
        flg = True
        for j in range(4):
            # 빈칸이 있는 경우
            if board[i][j] == 0:
                flg = False

        # 삭제되는 블록이 있는 경우
        if flg == True:
            deleted_row = max(deleted_row, i)
            cnt += 1
            # 블록 삭제
            for j in range(4):
                board[i][j] = 0

    # 삭제된 블록 행 수만큼 아래로 내리기
    if cnt > 0:
        for i in range(deleted_row, -1, -1):
            for j in range(4):
                board[i][j] = 0
                if i - cnt >= 0:
                    board[i][j] = board[i - cnt][j]

    # 특별한 칸 처리
    cnt2 = 0
    for i in range(2):
        flg = False
        for j in range(4):
            if board[i][j] == 1:
                flg = True

        # 블록이 있는 경우
        if flg == True:
            cnt2 += 1

    if cnt2 > 0:
        for i in range(5, -1, -1):
            for j in range(4):
                board[i][j] = 0
                if i - cnt2 >= 0:
                    board[i][j] = board[i - cnt2][j]

    return cnt

# -----------------------------------------------------------
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
        score += monomino(green, y, 1)
        score += monomino(blue, x, 1)
    elif t == 2:
        score += monomino(green, y, 2)
        score += monomino(blue, x, 3)
    else:
        score += monomino(green, y, 3)
        score += monomino(blue, x, 2)
print(score)

# 타일이 들어있는 칸의 개수 계산
ans = 0
for i in range(6):
    for j in range(4):
        if green[i][j] != 0:
            ans += 1
        if blue[i][j] != 0:
            ans += 1

print(ans)
