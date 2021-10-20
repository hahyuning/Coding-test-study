from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board):
    for i in range(6):
        for j in range(6):
            if board[i][j] != 0:
                cnt = 0
                color = board[i][j]
                deleted = [[False] * 6 for _ in range(6)]
                visited = [[False] * 6 for _ in range(6)]
                deleted[i][j] = True
                visited[i][j] = True
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    cnt += 1
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < 6 and 0 <= ny < 6 and board[nx][ny] == color and not visited[nx][ny]:
                            visited[nx][ny] = True
                            deleted[nx][ny] = True
                            q.append((nx, ny))

                if cnt >= 3:
                    for i in range(6):
                        for j in range(6):
                            if deleted[i][j]:
                                board[i][j] = 0
                    return True
    return False

def move(board):
    for j in range(6):
        tmp = []
        for i in range(5, -1, -1):
            if board[i][j] != 0:
                tmp.append(board[i][j])

        while len(tmp) < 6:
            tmp.append(0)

        for i in range(6):
            board[i][j] = tmp[5 - i]

def solution(macaron):
    board = [[0] * 6 for _ in range(6)]
    for col, color in macaron:
        col -= 1
        i = 0
        for row in range(5, -1, -1):
            if board[row][col] == 0:
                i = row
                break
        board[i][col] = color

        while True:
            if not bfs(board):
                break

            move(board)

    ans = []
    for row in board:
        ans.append("".join(map(str, row)))

    return ans

solution([[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]])
