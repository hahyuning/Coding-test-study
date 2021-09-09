n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[0] * m for _ in range(n)] # 확산이 일어난 후 더해지는 미세먼지의 양
# 3시 -> 12시 -> 9시 -> 6시
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 공기청정기의 위치
air1 = air2 = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            air2 = i
air1 = air2 - 1

for _ in range(t):
    for i in range(n):
        for j in range(m):
            if a[i][j] <= 0:
                continue

            # 각 칸에서 확산 가능한 칸의 개수 세기
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 0:
                    cnt += 1

            # 확산
            if cnt > 0:
                val = a[i][j] // 5
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 0:
                        b[nx][ny] += val

                a[i][j] -= cnt * val

    # 동시 확산
    for i in range(n):
        for j in range(m):
            if a[i][j] != -1:
                a[i][j] += b[i][j]
                b[i][j] = 0

    # 위쪽 공기청정기 작동
    air_x = air1
    air_y = 0
    x = air_x
    y = 1

    direction = 0
    prev = 0

    while True:
        if x == air_x and y == air_y:
            break

        tmp = prev
        prev = a[x][y]
        a[x][y] = tmp

        x += dx[direction]
        y += dy[direction]

        # 범위를 벗어난다면 회전
        if x < 0 or x >= n or y < 0 or y >= m:
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    # 아래쪽 공기청정기 작동
    air_x = air2
    air_y = 0
    x = air_x
    y = 1

    direction = 0
    prev = 0

    while True:
        if x == air_x and y == air_y:
            break

        tmp = prev
        prev = a[x][y]
        a[x][y] = tmp

        x += dx[direction]
        y += dy[direction]

        # 범위를 벗어난다면 회전
        if x < 0 or x >= n or y < 0 or y >= m:
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 3) % 4
            x += dx[direction]
            y += dy[direction]


ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] >= 0:
            ans += a[i][j]
print(ans)



