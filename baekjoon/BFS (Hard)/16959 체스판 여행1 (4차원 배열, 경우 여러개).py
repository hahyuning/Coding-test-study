from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 나이트
dx1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy1 = [1, 2, 2, 1, -1, -2, -2, -1]

# 룩
dx2 = [0, 0, 1, -1]
dy2 = [1, -1, 0, 0]

# 비숍
dx3 = [1, 1, -1, -1]
dy3 = [1, -1, 1, -1]

d  = [[[[-1] * 3 for _ in range(n ** 2)] for _ in range(n)] for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(n):
        a[i][j] -= 1
        if a[i][j] == 0:
            for k in range(3):
                d[i][j][0][k] = 0
                q.append((i, j, 0, k))

ans = -1
while q:
    x, y, num, now = q.popleft()
    if num == n ** 2 - 1:
        print(x, y, num)
        print(d[x][y][num][now])
        if ans == -1 or d[x][y][num][now] < ans:
            ans = d[x][y][num][now]

    # 말을 바꾸는 경우
    for new in range(3):
        if now == new:
            continue

        if d[x][y][num][new] == -1:
            d[x][y][num][new] = d[x][y][num][now] + 1
            q.append((x, y, num, new))

    # 말을 이동시키는 경우
    if now == 0:
        for k in range(8):
            nx, ny = x + dx1[k], y + dy1[k]
            if 0 <= nx < n and 0 <= ny < n:
                nxt_num = num
                if a[nx][ny] == num + 1:
                    nxt_num += 1

                if d[nx][ny][nxt_num][now] == -1:
                    d[nx][ny][nxt_num][now] = d[x][y][num][now] + 1
                    q.append((nx, ny, nxt_num, now))

    elif now == 1:
        for k in range(4):
            l = 1
            while True:
                nx, ny = x + dx2[k] * l, y + dy2[k] * l
                if 0 <= nx < n and 0 <= ny < n:
                    nxt_num = num
                    if a[nx][ny] == num + 1:
                        nxt_num += 1

                    if d[nx][ny][nxt_num][now] == -1:
                        d[nx][ny][nxt_num][now] = d[x][y][num][now] + 1
                        q.append((nx, ny, nxt_num, now))
                else:
                    break
                l += 1
    else:
        for k in range(4):
            l = 1
            while True:
                nx, ny = x + dx3[k] * l, y + dy3[k] * l
                if 0 <= nx < n and 0 <= ny < n:
                    nxt_num = num
                    if a[nx][ny] == num + 1:
                        nxt_num += 1

                    if d[nx][ny][nxt_num][now] == -1:
                        d[nx][ny][nxt_num][now] = d[x][y][num][now] + 1
                        q.append((nx, ny, nxt_num, now))
                else:
                    break
                l += 1

print(ans)