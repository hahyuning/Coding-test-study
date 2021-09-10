n = int(input())
board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            board[i][j] = 1

for j in range(101):
    i = 0
    while i + 1 < 101:
        if board[i + 1][j] == 0:
            i += 1
            continue

        board[i + 1][j] += board[i][j]
        i += 1

ans = 0
for i in range(101):
    for j in range(101):
        if board[i][j] > 0:
            w = 0
            h = board[i][j]
            while j + w < 101 and board[i][j + w] != 0:
                h = min(h, board[i][j + w])
                s = h * (w + 1)
                ans = max(ans, s)
                w += 1

print(ans)

# ------------------------------------------------------------

a = [[0] * 100 for _ in range(100)]
s = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            a[i][j] = 1

for i in range(1, 100):
    for j in range(1, 100):
        if a[i][j] == 1:
            s[i][j] = s[i][j - 1] + a[i][j]

ans = 0
for i in range(1, 100):
    for j in range(1, 100):
        if a[i][j] == 0:
            continue
        height = 0
        width = s[i][j]
        for k in range(i, 0, -1):
            if s[k][j] == 0:
                break

            height += 1
            width = min(width, s[k][j])

            ans = max(ans, height * width)

print(ans)
