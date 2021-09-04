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