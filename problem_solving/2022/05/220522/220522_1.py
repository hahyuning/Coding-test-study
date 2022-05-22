def solution(n, i, j, dir):
    global cnt

    if n == 1:
        cnt += 1
        if i <= x < i + 2 and j <= y < j + 2:
            for a in range(i, i + 2):
                for b in range(j, j + 2):
                    if a != x or b != y:
                        board[a][b] = cnt
        else:
            if dir == 0:
                board[i][j] = board[i + 1][j] = board[i][j + 1] = cnt
            elif dir == 1:
                board[i][j] = board[i][j + 1] = board[i + 1][j + 1] = cnt
            elif dir == 2:
                board[i][j] = board[i + 1][j] = board[i + 1][j + 1] = cnt
            else:
                board[i + 1][j] = board[i][j + 1] = board[i + 1][j + 1] = cnt

        return

    solution(n - 1, i, j, 0)
    solution(n - 1, i, j + 2 ** (n - 1), 1)
    solution(n - 1, i + 2 ** (n - 1), j, 2)
    solution(n - 1, i + 2 ** (n - 1), j + 2 ** (n - 1), 3)


k = int(input())
x, y = map(int, input().split())
x, y = 2 ** k - y, x - 1

cnt = 0
board = [[-1] * 2 ** k for _ in range(2 ** k)]
solution(k, 0, 0)

cnt += 1
for i in range(2 ** k):
    for j in range(2 ** k):
        if board[i][j] == -1:
            if i != x or j != y:
                board[i][j] = cnt

for row in board:
    print(*row)