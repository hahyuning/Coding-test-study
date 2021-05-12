# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 맵의 크기, 주사위 시작 위치, 명령어 개수
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
#      1
#   4  2  3
#      6
#      5
dice = [0] * 7

move = list(map(int, input().split()))
for k in move:
    k -= 1
    # 주사위가 범위를 벗어나면 무시
    nx, ny = x + dx[k], y + dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 동쪽으로 이동하는 경우: 1 -> 3 -> 6 -> 4
    if k == 0:
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    # 서쪽으로 이동하는 경우: 1 -> 4 -> 6 -> 3
    elif k == 1:
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    # 북쪽으로 이동하는 경우: 1 -> 5 -> 6 -> 2
    elif k == 2:
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    # 남쪽으로 이동하는 경우: 1 -> 2 -> 6 -> 5
    else:
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp

    # 현재 좌표 갱신
    x, y = nx, ny
    # board 쓰여있는 수가 0인 경우, 주사위 아랫면의 숫자 복사
    if board[x][y] == 0:
        board[x][y] = dice[6]
    # board에 숫자가 쓰여있는 경우, board의 수를 주사위로 복사
    else:
        dice[6] = board[x][y]
        board[x][y] = 0

    print(dice[1])
