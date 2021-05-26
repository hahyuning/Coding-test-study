n = int(input())
target = int(input())

a = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 0
cnt = 0
num = 1

tx, ty = 0, 0
sx, sy = n // 2, n //2
a[sx][sy] = 1
i = 2
while i <= n ** 2:
    for _ in range(num):
        sx += dx[dir]
        sy += dy[dir]
        a[sx][sy] = i
        if i == target:
            tx, ty = sx, sy
        i += 1
        if i > n ** 2:
            break

    dir = (dir + 1) % 4
    cnt += 1
    if cnt == 2:
        num += 1
        cnt = 0

for row in a:
    print(*row)
print(tx + 1, end=" ")
print(ty + 1)