import copy
import sys
input = sys.stdin.readline
# 기울일 수 있는 모든 방법 만들기 (재귀 or 비트마스크) -> 4 ** 10
# 바로 전 기울인 방향으로는 다시 기울이지 않아도 됨 -> 4 * (3 ** 9)
# 바로 전 기울인 방향의 반대 방향으로는 다시 기울이지 않아도 됨 -> 4 * (2 ** 9)

# 2진법을 4진법으로 변환
def base_change(k):
    a = [0] * 10
    for i in range(10):
        a[i] = k & 3
        k >>= 2
    return a

# 기울임 유효성 체크
def valid(directions):
    for i in range(len(directions) - 1):
        # 같은 방향인 경우
        if directions[i] == directions[i + 1]:
            return False
        # 반대 방향인 경우
        if (directions[i] + 2) % 4 == directions[i + 1]:
            return False
    return True

# ---------------------------------------------------------------------
# 기울이는 시뮬레이션
# 빨간 구슬과 파란 구슬 동시 이동 처리 필요 (R -> B 무한 반복, 두 구슬이 더이상 이동하지 않으면 종료)
# 하나의 구슬은 다른 구슬이나 벽을 만날 때까지 한 칸씩 이동

# 각 기울임마다 구슬이 구멍에 뺘졌는지 확인하는 함수
def check(tmp_board, directions):
    rx, ry = 0, 0
    bx, by = 0, 0

    for i in range(n):
        for j in range(m):
            if tmp_board[i][j] == "R":
                rx, ry = i, j
            elif tmp_board[i][j] == "B":
                bx, by = i, j

    # 움직인 횟수
    cnt = 0
    for k in directions:
        cnt += 1
        # 각각의 기울임마다 구슬이 구멍에 들어갔는지 체크
        hole1 = hole2 = False
        # 각 구슬에 대해 실제 이동 처리 (움직임이 없을 때까지 반복)
        while True:
            bead1 = move(tmp_board, k, rx, ry)
            rx, ry = bead1[2], bead1[3]
            bead2 = move(tmp_board, k, bx, by)
            bx, by = bead2[2], bead2[3]

            # 두 구슬 모두 이동하지 않은 경우
            if bead1[0] == False and bead2[0] == False:
                break
            # 구슬이 구멍에 빠졌는지 체크
            if bead1[1] == True:
                hole1 = True
            if bead2[1] == True:
                hole2 = True

        # 파란 구슬이 구멍에 빠졌다면 -1 반환
        if hole2 == True:
            return -1
        # 빨간 구슬만 구멍에 빠졌다면 움직인 횟수 반환
        if hole1 == True:
            return cnt

    # 10번 동안 빨간 구슬만 구멍에 빠지지 않은 경우
    return -1

# 실제로 구슬 한개를 이동시키는 함수
# [이동여부, 구멍에 빠졌는지 여부, 이동후 좌표]
def move(tmp_board, k, x, y):
    # 이미 구슬이 구멍에 빠져서 board 에서 지워진 경우 처리
    if tmp_board[x][y] == ".":
        return [False, False, x, y]

    moved = False
    while True:
        nx, ny = x + dx[k], y + dy[k]
        # 벽이 나온 경우
        if tmp_board[nx][ny] == "#":
            return [moved, False, x, y]
        # 다른 구슬을 만난 경우
        elif tmp_board[nx][ny] == "R" or tmp_board[nx][ny] == "B":
            return [moved, False, x, y]
        # 빈칸인 경우
        elif tmp_board[nx][ny] == ".":
            # 구슬과 빈칸 자리 바꾸기
            tmp_board[nx][ny], tmp_board[x][y] = tmp_board[x][y], tmp_board[nx][ny]
            x, y = nx, ny
            moved = True
        # 구멍에 빠진 경우
        elif tmp_board[nx][ny] == "O":
            # 구슬이 없어졌기 때문에 79번 줄 필요
            tmp_board[x][y] = "."
            moved = True
            return [moved, True, x, y]

# ------------------------------------------------------------
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = ["R", "D", "L", "U"]

ans = -1
path = ""
# 경우의 수: 2의 20승
for k in range(1 << 20):
    directions = base_change(k)
    # 해당 기울임이 유효한지 체크
    if not valid(directions):
        continue

    tmp_board = copy.deepcopy(board)
    res = check(tmp_board, directions)
    if res == -1:
        continue
    if ans == -1 or ans > res:
        path = ""
        for x in directions:
            path += dir[x]
        ans = res

print(ans)
print(path[:ans])
