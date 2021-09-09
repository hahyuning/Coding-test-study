from itertools import permutations
from collections import defaultdict, deque
from copy import deepcopy

def bfs2(board, x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1))
    dist = [[-1] * 4 for _ in range(4)]
    dist[x1][y1] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for k in range(4):
            l = 1
            while True:
                nx, ny = x + dx[k] * l, y + dy[k] * l
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    if dist[nx - dx[k]][ny - dy[k]] == -1 or dist[x][y] + 1 < dist[nx - dx[k]][ny - dy[k]]:
                        dist[nx - dx[k]][ny - dy[k]] = dist[x][y] + 1
                        q.append((nx - dx[k], ny - dy[k]))
                    break
                if dist[nx][ny] == -1 or dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                if board[nx][ny] > 0:
                    if dist[nx][ny] == -1 or dist[x][y] + 1 < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
                    break
                l += 1
    return dist[x2][y2]

def solution(board, r, c):
    num = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                num[board[i][j]] += [i, j]

    numbers = list(num.keys()) * 2
    p = list(permutations(numbers))
    ans = -1
    for order in p:

        a = deepcopy(board)
        order = list(order)
        sx, sy = r, c
        tmp = 0
        for k in order:
            pass

        if ans == -1 or tmp < ans:
            ans = tmp
    return ans

solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)