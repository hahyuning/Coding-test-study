import sys
input = sys.stdin.readline

n, c = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
move = input().rstrip()

sx, sy = 0, 0
b = []
for i in range(n):
    for j in range(c):
        if a[i][j] == "I":
            sx, sy = i, j
        elif a[i][j] == "R":
            b.append((i, j))

dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

cnt = 0
for m in move:
    cnt += 1
    m = int(m) - 1

    a[sx][sy] = "."
    sx, sy = sx + dx[m], sy + dy[m]
    if a[sx][sy] == "R":
        print("kraj " + str(cnt))
        sys.exit(0)
    a[sx][sy] = "I"

    tmp = dict()
    tmp_board = [["."] * c for _ in range(n)]
    for x, y in b:
        a[x][y] = "."
        min_dist = -1
        min_dir = -1
        for k in range(9):
            rx, ry = x + dx[k], y + dy[k]
            dist = abs(sx - rx) + abs(sy - ry)
            if min_dist == -1 or min_dist > dist:
                min_dir = k
                min_dist = dist

        rx, ry = x + dx[min_dir], y + dy[min_dir]
        if a[rx][ry] == "I":
            print("kraj " + str(cnt))
            sys.exit(0)

        if (rx, ry) in tmp:
            if tmp[(rx, ry)]:
                tmp[(rx, ry)] = False
                tmp_board[rx][ry] = "."
        else:
            tmp[(rx, ry)] = True
            tmp_board[rx][ry] = "R"

    for i in range(n):
        for j in range(c):
            if tmp_board[i][j] == "R":
                a[i][j] = "R"

    b = []
    if tmp.keys():
        for key in tmp.keys():
            if tmp[key]:
                b.append(key)

for row in a:
    print("".join(row))


