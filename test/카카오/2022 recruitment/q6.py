def solution(board, skill):
    n = len(board)
    m = len(board[0])
    ans = 0

    for type, sx, sy, ex, ey, deg in skill:
        if type == 1:
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    board[i][j] -= deg
        else:
            for i in range(sx, ex + 1):
                for j in range(sy, ey + 1):
                    board[i][j] += deg

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                ans += 1

    return ans