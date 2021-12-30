def end_check(now):
    prev = (1 if now == 2 else 2)

    # 대각선 검사
    if (board[0][0] == board[1][1] == board[2][2] == prev) or (board[0][2] == board[1][1] == board[2][0] == prev):
        return True
    # 가로세로 검사
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] == prev) or (board[i][0] == board[i][1] == board[i][2] == prev):
            return True

    return False


def play(now):
    if end_check(now):
        return -1

    # -1: win, 0: default, 1: lose
    res = 2
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = now
                nxt = (1 if now == 2 else 2)
                res = min(res, play(nxt))
                board[i][j] = 0

    if res == 1 or res == -1:
        return -res
    else:
        return 0


board = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

for i in range(3):
    for j in range(3):
        if board[i][j] != 0:
            cnt += 1

now = (1 if cnt % 2 == 0 else 2)

if cnt == 9:
    print("D")
else:
    res = play(now)
    if res == 1:
        print("W")
    elif res == -1:
        print("L")
    else:
        print("D")