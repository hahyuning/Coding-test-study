import sys

def change_direction(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    return 2

def move(x, y, nx, ny, start):
    for i in range(start, len(location[x][y])):
        h = location[x][y][i]
        location[nx][ny].append(h)
        hours[h[0]] = (nx, ny, len(location[nx][ny]) - 1)
    location[x][y] = location[x][y][:start]

n, k = map(int, input().split())
# 0: 흰색, 1: 빨간색, 2: 파란색
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

hours = [0] * k
location = [[[] for _ in range(n)] for _ in range(n)]

for i in range(k):
    a, b, c = map(int, input().split())
    location[a - 1][b - 1].append([i, c - 1])
    hours[i] = (a - 1, b - 1, len(location[a - 1][b - 1]) -1)

for ans in range(1, 1001):
    # k개의 말 순서대로 이동
    for i in range(k):
        x, y, index = hours[i]
        direction = location[x][y][index][1]
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n:
            # 이동하려는 칸이 파란색인 경우
            if board[nx][ny] == 2:
                location[x][y][index][1] = change_direction(direction)
        # 범위를 벗어난 경우
        else:
            location[x][y][index][1] = change_direction(direction)

        direction = location[x][y][index][1]
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n:
            # 이동하려는 칸이 흰색인 경우
            if board[nx][ny] == 0:
                move(x, y, nx, ny, index)
            # 이동하려는 칸이 빨간색인 경우
            elif board[nx][ny] == 1:
                location[x][y] = location[x][y][:index] + location[x][y][index:][::-1]
                move(x, y, nx, ny, index)
            # 말이 4개 이상 쌓였는지 확인
            if len(location[nx][ny]) >= 4:
                print(ans)
                sys.exit(0)

print(-1)

