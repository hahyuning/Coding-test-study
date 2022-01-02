# n 번째 칸을 채우는 함수 (row major order)
def sudominoku(n):
    # 종료 조건: 모든 칸을 다 탐색한 경우
    if n == 81:
        for row in board:
            print("".join(map(str, row)))
        return True

    x = n // 9
    y = n % 9

    # 이미 숫자가 들어있는 경우는 다음 함수 호출
    if board[x][y] != 0:
        return sudominoku(n + 1)
    else:
        for k in range(2):
            nx, ny = x + dx[k], y + dy[k]
            # 범위 검사와 도미노를 놓을 수 있는지 체크
            if 0 <= nx < 9 and 0 <= ny < 9 and board[nx][ny] == 0:
                for i in range(1, 10):
                    for j in range(1, 10):
                        if i != j and domino[i][j] == False:
                            if not check_horizontal[x][i] and not check_vertical[y][i] and not check_square[3 * (x // 3) + (y // 3)][i] \
                                    and not check_horizontal[nx][j] and not check_vertical[ny][j] and not check_square[3 * (nx // 3) + (ny // 3)][j]:
                                check(x, y, i, True)
                                check(nx, ny, j, True)
                                domino[i][j] = domino[j][i] = True
                                board[x][y] = i
                                board[nx][ny] = j
                                if sudominoku(n + 1):
                                    return True
                                check(x, y, i, False)
                                check(nx, ny, j, False)
                                domino[i][j] = domino[j][i] = False
                                board[x][y] = 0
                                board[nx][ny] = 0

    return False

def check(x, y, num, tf):
    check_horizontal[x][num] = tf
    check_vertical[y][num] = tf
    check_square[(x // 3) * 3 + (y // 3)][num] = tf
# ---------------------------------------------------------------
dx = [0, 1]
dy = [1, 0]

cnt = 1
while True:
    board = [[0] * 9 for _ in range(9)]
    check_horizontal = [[False] * 10 for _ in range(9)] # 가로 검사
    check_vertical = [[False] * 10 for _ in range(9)] # 세로 검사
    check_square = [[False] * 10 for _ in range(9)] # 칸 검사
    domino = [[False] * 10 for _ in range(10)] # 도미노 검사

    m = int(input())
    if m == 0:
        break

    for i in range(m):
        a, a_loc, b, b_loc = input().split()
        a = int(a)
        b = int(b)

        # 좌표 변환
        ax, ay = ord(a_loc[0]) - ord("A"), ord(a_loc[1]) - ord("1")
        bx, by = ord(b_loc[0]) - ord("A"), ord(b_loc[1]) - ord("1")

        # 도미노 놓기
        board[ax][ay] = a
        board[bx][by] = b

        domino[a][b] = True
        domino[b][a] = True

        check(ax, ay, a, True)
        check(bx, by, b, True)

    number = input().split()
    for i in range(1, 10):
        tmp = number[i - 1]
        x, y = ord(tmp[0]) - ord("A"), ord(tmp[1]) - ord("1")
        board[x][y] = i
        check(x, y, i, True)

    print("Puzzle " + str(cnt))
    sudominoku(0)
    cnt += 1
