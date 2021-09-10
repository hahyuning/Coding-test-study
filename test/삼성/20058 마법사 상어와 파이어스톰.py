from collections import deque
from copy import deepcopy

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 부분 격자 회전
def rotate(b):
    res = [[0] * len(b) for _ in range(len(b))]
    for i in range(len(b)):
        for j in range(len(b)):
            res[i][j] = b[len(b) - j - 1][i]
    return res

# 부분 격자로 나누고 회전시킨 후 결과 저장
def divide_and_rotate(sx, sy, size):
    b = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            b[i][j] = a[sx + i][sy + j]

    b = rotate(b)
    for i in range(size):
        for j in range(size):
            a[sx + i][sy + j] = b[i][j]


n, q = map(int, input().split())
m = 2 ** n
a = [list(map(int, input().split())) for _ in range(m)]
l = list(map(int, input().split()))

for i in range(q):

    if l[i] > 0:
        size = 2 ** l[i]

        for sx in range(0, m, size):
            for sy in range(0, m, size):
                divide_and_rotate(sx, sy, size)

    # bfs 로 주변 얼음의 개수 세기
    b = deepcopy(a)
    for i in range(m):
        for j in range(m):
            if b[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < m and 0 <= ny < m:
                        if b[nx][ny] > 0:
                            cnt += 1

                if cnt < 3 and a[i][j] > 0:
                    a[i][j] -= 1

ans = sum(sum(row) for row in a)
print(ans)

# 가장 큰 얼음 조각 찾기
check = [[False] * m for _ in range(m)]
ans = 0
for i in range(m):
    for j in range(m):
        if a[i][j] > 0 and not check[i][j]:
            q = deque()
            q.append((i, j))
            check[i][j] = True
            cnt = 0

            while q:
                x, y = q.popleft()
                cnt += 1
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < m and 0 <= ny < m:
                        if a[nx][ny] > 0 and not check[nx][ny]:
                            check[nx][ny] = True
                            q.append((nx, ny))

            ans = max(ans, cnt)
print(ans)