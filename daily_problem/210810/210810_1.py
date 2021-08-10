n = int(input())
m = int(input())

x, y = n // 2, n // 2
a = [[0] * n for _ in range(n)]
a[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
now = 1
dir = 0
now_cnt = 1
mx, my = 0, 0
while now <= n ** 2:
    for _ in range(now_cnt):
        now += 1
        if now > n ** 2:
            break

        x, y = x + dx[dir], y + dy[dir]
        a[x][y] = now
        if now == m:
            mx, my = x, y

    dir = (dir + 1) % 4
    cnt += 1
    if cnt == 2:
        now_cnt += 1
        cnt = 0

for row in a:
    print(*row)

if m == 1:
    print(n // 2 + 1, n // 2 + 1)
else:
    print(mx + 1, my + 1)