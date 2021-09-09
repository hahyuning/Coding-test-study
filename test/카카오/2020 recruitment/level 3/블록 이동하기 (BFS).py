from collections import deque

def get_next(now, board):
    now = list(now)
    x1, y1, x2, y2 = now[0][0], now[0][1], now[1][0], now[1][1]
    nxt = []

    # 단순 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        nx1, ny1, nx2, ny2 = x1 + dx[k], y1 + dy[k], x2 + dx[k], y2 + dy[k]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            nxt.append({(nx1, ny1), (nx2, ny2)})

    # 회전
    # 1. 로봇이 가로로 놓인 경우
    if x1 == x2:
        for k in [-1, 1]:
            if board[x1 + k][y1] == 0 and board[x2 + k][y2] == 0:
                nxt.append({(x1, y1), (x1 + k, y1)})
                nxt.append({(x2, y2), (x2 + k, y2)})
    # 2. 로봇이 세로로 놓인 경우
    else:
        for k in [-1, 1]:
            if board[x1][y1 + k] == 0 and board[x2][y2 + k] == 0:
                nxt.append({(x1, y1), (x1, y1 + k)})
                nxt.append({(x2, y2), (x2, y2 + k)})

    return nxt

def solution(board):
    n = len(board)

    # 범위 처리를 쉽게 하기 위해 겉에 벽두기
    for i in range(n):
        board[i] = [1] + board[i] + [1]
    board.insert(0, [1] * (n + 2))
    board.append([1] * (n + 2))

    # 두 좌표가 바뀌는 경우도 하나로 처리하기 위해 set 사용
    now = {(1, 1), (1, 2)}
    q = deque()
    visited = []
    q.append((now, 0))

    ans = 0
    while q:
        now, dist = q.popleft()
        if (n, n) in now:
            ans = dist
            break

        for nxt in get_next(now, board):
            if nxt not in visited:
                visited.append(nxt)
                q.append((nxt, dist + 1))
    return ans