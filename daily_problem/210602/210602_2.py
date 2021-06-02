import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
if k == 1:
    for row in board:
        print("".join(row))
elif k % 2 == 0:
    for _ in range(n):
        print("O" * m)
else:
    k //= 2
    cnt = 0
    while True:
        cnt += 1
        d = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    d[i][j] = True
                    for l in range(4):
                        nx, ny = i + dx[l], j + dy[l]
                        if 0 <= nx < n and 0 <= ny < m and not d[nx][ny]:
                            d[nx][ny] = True

        for i in range(n):
            for j in range(m):
                if d[i][j]:
                    board[i][j] = "."
                else:
                    board[i][j] = "O"

        if cnt == k:
            break

    for row in board:
        print("".join(row))
