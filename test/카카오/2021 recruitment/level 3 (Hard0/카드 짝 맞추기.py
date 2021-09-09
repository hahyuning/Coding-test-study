from itertools import permutations
from collections import defaultdict, deque
from copy import deepcopy

def find_block(x, y, x1, y1, x2, y2):
    d1 = abs(x1 - x) + abs(y1 - y)
    d2 = abs(x2 - x) + abs(y2 - y)
    if d1 < d2:
        return x1, y1
    else:
        return x2, y2

def bfs(board, sx, sy, x1, y1, x2, y2):
    q = deque()
    q.append((sx, sy, -1))
    dist = [[-1] * 4 for _ in range(4)]
    dist[sx][sy] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, dir = q.popleft()
        for k in range(4):
            if k == dir:
                continue

            l = 1
            while True:
                nx, ny = x + dx[k] * l, y + dy[k] * l
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    if dist[nx - dx[k]][ny - dy[k]] == -1:
                        dist[nx - dx[k]][ny - dy[k]] = dist[x][y] + 1
                        q.append((nx - dx[k], ny - dy[k], k))
                    break
                if board[nx][ny] > 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny, k))
                    break
                l += 1

    return dist[x1][y1], dist[x2][y2]

def bfs2(board, x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1, -1))
    dist = [[-1] * 4 for _ in range(4)]
    dist[x1][y1] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, dir = q.popleft()
        for k in range(4):
            l = 1
            while True:
                nx, ny = x + dx[k] * l, y + dy[k] * l
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    if dist[nx - dx[k]][ny - dy[k]] == -1 or dist[x][y] + 1 < dist[nx - dx[k]][ny - dy[k]]:
                        dist[nx - dx[k]][ny - dy[k]] = dist[x][y] + 1
                        q.append((nx - dx[k], ny - dy[k], k))
                    break

                if board[nx][ny] > 0:
                    if dist[nx][ny] == -1 or dist[x][y] + 1 < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny, k))
                    break
                l += 1

    for row in dist:
        print(row)
    return dist[x2][y2]

def solution(board, r, c):
    num = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                num[board[i][j]] += [i, j]

    p = list(permutations(num.keys()))
    ans = -1
    for order in p:
        a = deepcopy(board)
        print(order)
        order = list(order)
        sx, sy = r, c
        tmp = 0
        for k in order:
            x1, y1, x2, y2 = num[k]

            d1, d2 = bfs(a, sx, sy, x1, y1, x2, y2)
            tmp += min(d1, d2) + 1
            print(d1, d2)
            print(tmp)

            if d1 < d2:
                d = bfs2(a, x1, y1, x2, y2)
                sx, sy = x2, y2
            else:
                d = bfs2(a, x2, y2, x1, y1)
                sx, sy = x1, y1

            a[x1][y1] = 0
            a[x2][y2] = 0
            tmp += d
            print(tmp)
            print("------------------------------")
        if ans == -1 or tmp < ans:
            ans = tmp
        print(tmp)
    print(ans)
    return

solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)