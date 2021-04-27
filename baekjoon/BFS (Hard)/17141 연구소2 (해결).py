from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(candi):
    d = [[-1] * n for _ in range(n)]
    q = deque()
    for i in range(m):
        q.append((candi[i][0], candi[i][1]))
        d[candi[i][0]][candi[i][1]] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == -1 and a[nx][ny] != 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

    tmp = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 1:
                # 바이러스가 퍼지지 않은 칸이 있는 경우는 종료
                if d[i][j] == -1:
                    return
                tmp = max(tmp, d[i][j])

    global ans
    if ans == -1 or ans > tmp:
        ans = tmp

# -------------------------------------------------------------------
n, m = map(int, input().split())
# 0: 빈 칸, 1: 벽, 2: 바이러스를 놓을 수 있는 칸
a = [list(map(int, input().split())) for _ in range(n)]

candidate = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            candidate.append((i, j))
            a[i][j] = 0

ans = -1
candi_combi = combinations(candidate, m)
for candi in candi_combi:
    for i in range(m):
        a[candi[i][0]][candi[i][1]] = 2
    bfs(candi)
    for i in range(m):
        a[candi[i][0]][candi[i][1]] = 0

print(ans)