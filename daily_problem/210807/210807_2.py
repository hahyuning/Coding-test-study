from itertools import combinations
from copy import deepcopy
from collections import deque

n, m, g, r = map(int, input().split())
# 0: 호수, 1: 배양액 X, 2: 배양액 O
a = [list(map(int, input().split())) for _ in range(n)]
ok = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            ok.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
# 배양액을 놓을 전체 후보
for candi_all in list(combinations(ok, g + r)):
    for g_candi in list(combinations(candi_all, g)):
        # 3: green, 4: red, 5: flower
        board = deepcopy(a)

        green = deque()
        red = deque()
        for x, y in candi_all:
            if (x, y) in g_candi:
                green.append((x, y))
            else:
                red.append((x, y))

        res = 0
        while green:

            g_tmp = set()
            r_tmp = set()
            # green
            while green:
                x, y = green.popleft()
                board[x][y] = 3
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in [1, 2]:
                        g_tmp.add((nx, ny))
            # red
            while red:
                x, y = red.popleft()
                board[x][y] = 4
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in [1, 2]:
                        r_tmp.add((nx, ny))

            flower = g_tmp.intersection(r_tmp)
            g_tmp = g_tmp.difference(flower)
            r_tmp = r_tmp.difference(flower)

            for x, y in flower:
                res += 1
                board[x][y] = 5
            for x, y in g_tmp:
                board[x][y] = 3
            for x, y in r_tmp:
                board[x][y] = 4

        cnt = max(res, cnt)
print(cnt)