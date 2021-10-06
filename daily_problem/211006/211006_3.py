import sys

m, n = map(int, input().split())
k, l = map(int, input().split())
a = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = dict()
for i in range(1, k + 1):
    y, x, d = input().split()
    x = n - int(x)
    y = int(y) - 1
    a[x][y] = i
    if d == "N":
        dir[i] = 0
    elif d == "E":
        dir[i] = 1
    elif d == "S":
        dir[i] = 2
    else:
        dir[i] = 3

for _ in range(l):
    num, op, rep = input().split()
    num = int(num)
    rep = int(rep)
    if op == "L":
        dir[num] = (dir[num] + (4 - rep % 4)) % 4
    elif op == "R":
        dir[num] = (dir[num] + rep) % 4
    else:
        x, y = -1, -1
        for i in range(n):
            for j in range(m):
                if a[i][j] == num:
                    x, y = i, j
        d = dir[num]

        for _ in range(rep):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                print("Robot {} crashes into the wall".format(num))
                sys.exit(0)
            if a[nx][ny] != 0:
                print("Robot {} crashes into robot {}".format(num, a[nx][ny]))
                sys.exit(0)
            a[x][y] = 0
            a[nx][ny] = num
            x, y = nx, ny
print("OK")