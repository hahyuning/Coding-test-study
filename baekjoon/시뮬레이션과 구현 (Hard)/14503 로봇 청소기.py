r, c = map(int, input().split())
x, y, direction = map(int, input().split())
# 0: 빈칸, 1: 벽, 2: 청소
a = [list(map(int, input().split())) for _ in range(r)]

# 북동남서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    # 1. 현재 위치를 청소한다.
    if a[x][y] == 0:
        a[x][y] = 2

    # 2-4.네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    if a[x - 1][y] != 0 and a[x][y + 1] != 0 and a[x + 1][y] != 0 and a[x][y - 1] != 0:
        if a[x - dx[direction]][y - dy[direction]] == 1:
            break
        # 2-3.네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        else:
            x -= dx[direction]
            y -= dy[direction]

    # 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    # 2-2. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    else:
        # 왼쪽 방향 구하기
        direction = (direction + 3) % 4
        if a[x + dx[direction]][y + dy[direction]] == 0:
            x += dx[direction]
            y += dy[direction]

answer = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == 2:
            answer += 1
print(answer)