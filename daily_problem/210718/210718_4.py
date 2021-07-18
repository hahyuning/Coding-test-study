from itertools import combinations
from copy import deepcopy

n, m, g, r = map(int, input().split())
# 0: 호수, 1: 배양액 X, 2: 배양액 O
a = [list(map(int, input().split())) for _ in range(n)]
ok = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            ok.append((i, j))
g_combi = list(combinations(ok, g))
r_combi = list(combinations(ok, r))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = -1
cnt = 0
for g_candi in g_combi:
    for r_candi in r_combi:
        if set(g_candi).intersection(set(r_candi)):
            continue

        visit = [[False] * m for _ in range(n)]
        # 3: green, 4: red, 5: flower
        board = deepcopy(a)
        for x, y in g_candi:
            visit[x][y] = True
            board[x][y] = 3
        for x, y in r_candi:
            visit[x][y] = True
            board[x][y] = 4

        res = 0
        while True:

            g_tmp = set()
            r_tmp = set()
            check = False

            # green
            for i in range(n):
                for j in range(m):
                    if board[i][j] == 3:
                        for k in range(4):
                            nx, ny = i + dx[k], j + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in [1, 2] and not visit[nx][ny]:
                                visit[nx][ny] = True
                                check = True
                                g_tmp.add((nx, ny))

            # red
            for i in range(n):
                for j in range(m):
                    if board[i][j] == 4:
                        for k in range(4):
                            nx, ny = i + dx[k], j + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in [1, 2] and not visit[nx][ny]:
                                visit[nx][ny] = True
                                check = True
                                r_tmp.add((nx, ny))

            for x, y in g_tmp:
                if (x, y) in r_tmp:
                    res += 1
                    board[x][y] = 5
                else:
                    board[x][y] = 3
            for x, y in r_tmp:
                if (x, y) not in g_tmp:
                    board[x][y] = 4

            if not check:
                break

        ans = max(res, ans)
print(ans)