r1, c1, r2, c2 = map(int, input().split())
n = max(abs(r1), abs(c1), abs(r2), abs(c2))

r2 += n
r1 += n
c2 += n
c1 += n
b = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

n = 2 * n + 1
x, y = n // 2 - 1, n // 2

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

cnt = -1
now = 0
dir = -1
now_cnt = 1
max_val = 0
while now <= n ** 2:
    for _ in range(now_cnt):
        now += 1
        if now > n ** 2:
            break

        x, y = x + dx[dir], y + dy[dir]
        if r1 <= x <= r2 and c1 <= y <= c2:
            b[x - r1][y - c1] = now
            max_val = max(max_val, now)

    dir = (dir + 1) % 4
    cnt += 1
    if cnt == 2:
        now_cnt += 1
        cnt = 0

max_len = len(str(max_val))
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(b[i][j]).rjust(max_len), end=" ")
    print()