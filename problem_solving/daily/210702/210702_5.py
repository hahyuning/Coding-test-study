while True:
    s = input()
    if s == "end":
        break

    board = [[""] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j] = s[3 * i + j]

    # 1. 말 개수 확인
    cnt1 = 0
    cnt2 = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                cnt1 += 1
            elif board[i][j] == "O":
                cnt2 += 1
    if cnt1 < cnt2 or cnt1 - cnt2 >= 2:
        print("invalid")
        continue

    # 2. 게임 즉시 종료 확인
    ch1 = False
    ch2 = False
    for i in range(3):
        if board[i][0] == "X" and board[i][0] == board[i][1] == board[i][2]:
            ch1 = True
        if board[i][0] == "O" and board[i][0] == board[i][1] == board[i][2]:
            ch2 = True
    for j in range(3):
        if board[0][j] == "X" and board[0][j] == board[1][j] == board[2][j]:
            ch1 = True
        if board[0][j] == "O" and board[0][j] == board[1][j] == board[2][j]:
            ch2 = True
    if board[0][0] == "X" and board[0][0] == board[1][1] == board[2][2]:
        ch1 = True
    if board[0][2] == "X" and board[0][2] == board[1][1] == board[2][0]:
        ch1 = True
    if board[0][0] == "O" and board[0][0] == board[1][1] == board[2][2]:
        ch2 = True
    if board[0][2] == "O" and board[0][2] == board[1][1] == board[2][0]:
        ch2 = True

    if ch1 and ch2:
        print("invalid")
    elif ch2 and cnt1 > cnt2:
        print("invalid")
    elif ch1 and cnt1 == cnt2:
        print("invalid")
    elif not ch1 and not ch2 and cnt1 + cnt2 < 9:
        print("invalid")
    else:
        print("valid")
