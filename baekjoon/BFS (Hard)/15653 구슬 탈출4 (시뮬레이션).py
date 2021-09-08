from collections import deque
from copy import deepcopy

# 주어진 방향으로 구슬이 이동할 수 없을 때까지 이동시키는 함수
# 움직임의 여부, 구멍에 빠졌는지의 여부, 이동후의 좌표 반환
def simulate(x, y, a, k):
    # 해당 구슬이 이미 빠진 경우
    if a[x][y] == ".":
        return [False, False, x, y]

    moved = False
    while True:
        nx, ny = x + dx[k], y + dy[k]
        # 범위를 벗어난 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return [moved, False, x, y]
        # 벽에 부딪히거나 다른 구슬을 만나 이동할 수 없는 경우
        if a[nx][ny] == "#" or a[nx][ny] in "RB":
            return [moved, False, x, y]
        # 구멍을 만난 경우
        if a[nx][ny] == "O":
            a[x][y] = "."
            moved = True
            return [moved, True, x, y]
        # 빈칸인 경우
        if a[nx][ny] == ".":
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x, y = nx, ny
            moved = True

# 주어진 방향으로 어떻게 구슬이 이동하는지 구하는 함수
# 각 구슬이 빠졌는지의 여부, 각 구슬의 이동 후의 좌표 반환
def move(rx, ry, bx, by, k):
    b = deepcopy(a)
    b[rx][ry] = "R"
    b[bx][by] = "B"

    h1 = False
    h2 = False

    while True:
        rmoved, rhole, rx, ry = simulate(rx, ry, b, k)
        bmoved, bhole, bx, by = simulate(bx, by, b, k)

        # 두 구슬 모두 움직임이 없으면 break
        if not rmoved and not bmoved:
            break
        if rhole:
            h1 = True
        if bhole:
            h2 = True

    return [h1, h2, rx, ry, bx, by]


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

hx, hy = -1, -1
rx, ry, bx, by = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if a[i][j] == "O":
            hx, hy = i, j
        if a[i][j] == "R":
            rx, ry = i, j
            a[i][j] = "."
        if a[i][j] == "B":
            bx, by = i, j
            a[i][j] = "."

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

d = [[[[-1] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
q = deque()
q.append((rx, ry, bx, by))
d[rx][ry][bx][by] = 0
check = False
ans = -1

while q:
    rx, ry, bx, by = q.popleft()

    for k in range(4):
        h1, h2, nrx, nry, nbx, nby = move(rx, ry, bx, by, k)

        if h2:
            continue
        if h1:
            check = True
            ans = d[rx][ry][bx][by] + 1
            break

        if d[nrx][nry][nbx][nby] == -1:
            d[nrx][nry][nbx][nby] = d[rx][ry][bx][by] + 1
            q.append((nrx, nry, nbx, nby))

    if check:
        break
print(ans)