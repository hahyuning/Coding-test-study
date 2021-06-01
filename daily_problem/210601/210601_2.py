def solution(rows, columns, queries):
    board = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = i * columns + j + 1

    for row in board:
        print(row)
    answer = []
    for q in queries:
        x1, y1, x2, y2 = q
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        tmp = []
        for j in range(y1, y2 + 1):
            tmp.append(board[x1][j])
        for i in range(x1 + 1, x2 + 1):
            tmp.append(board[i][y2])
        for j in range(y2 - 1, y1 - 1, -1):
            tmp.append(board[x2][j])
        for i in range(x2 - 1, x1, -1):
            tmp.append(board[i][y1])
        tmp = [tmp[-1]] + tmp[:-1]
        answer.append(min(tmp))

        k = 0
        for j in range(y1, y2 + 1):
            board[x1][j] = tmp[k]
            k += 1
        for i in range(x1 + 1, x2 + 1):
            board[i][y2] = tmp[k]
            k += 1
        for j in range(y2 - 1, y1 - 1, -1):
            board[x2][j] = tmp[k]
            k += 1
        for i in range(x2 - 1, x1, -1):
            board[i][y1] = tmp[k]
            k += 1
    return answer

solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])