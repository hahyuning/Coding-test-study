def rotate():
    global r, c

    res = [[0] * len(b) for _ in range(len(b[0]))]
    for i in range(len(b[0])):
        for j in range(len(b)):
            res[i][j] = b[j][len(b[0]) - i - 1]
    r, c = c, r
    return res


def match(x, y):
    global ans

    check = False
    for i in range(x, x + len(b)):
        for j in range(y, y + len(b[0])):
            if b[i - x][j - y] == 1 and board[i][j] == 1:
                check = True
                break
        if check:
            break

    if not check:
        min_x = min(x, 50)
        min_y = min(y, 50)
        max_x = max(x + r - 1, 50 + n - 1)
        max_y = max(y + c - 1, 50 + m - 1)

        s = (max_x - min_x + 1) * (max_y - min_y + 1)
        if ans == -1 or s < ans:
            ans = s


n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

r, c = map(int, input().split())
b = [list(map(int, list(input()))) for _ in range(r)]

board = [[0] * (m + 2 * 50) for _ in range(n + 2 * 50)]
for i in range(50, 50 + n):
    for j in range(50, 50 + m):
        board[i][j] = a[i - 50][j - 50]

ans = -1
for _ in range(4):
    b = rotate()
    for i in range(50 + n):
        for j in range(50 + m):
            match(i, j)

print(ans)