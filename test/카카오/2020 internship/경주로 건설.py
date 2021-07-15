from collections import deque

def solution(board):
    n = len(board)
    dist = {(0, 0, 2): 0, (0, 0, 3): 0}
    q = deque()
    q.append((0, 0, 2))
    q.append((0, 0, 3))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while q:
        x, y, dir = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if k == dir or (k + 2) % 4 == dir:
                    if (nx, ny, k) not in dist or dist[(nx, ny, k)] > dist[(x, y, dir)] + 1:
                        dist[(nx, ny, k)] = dist[(x, y, dir)] + 1
                        q.append((nx, ny, k))
                else:
                    if (nx, ny, k) not in dist or dist[(nx, ny, k)] > dist[(x, y, dir)] + 6:
                        dist[(nx, ny, k)] = dist[(x, y, dir)] + 6
                        q.append((nx, ny, k))

    ans = -1
    for i in range(4):
        if (n - 1, n - 1, i) in dist:
            if ans == -1 or ans > dist[(n - 1, n - 1, i)]:
                ans = dist[(n - 1, n - 1, i)]

    return ans * 100

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 1], [1, 1, 0, 0]]))