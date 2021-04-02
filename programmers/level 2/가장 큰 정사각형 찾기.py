def solution(board):
    s = 0
    for x in board:
        s += sum(x)
    if s == 0:
        return 0
    
    max_len = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                max_len = max(max_len, board[i][j])

    if max_len == 0:
        return 1
    return max_len ** 2