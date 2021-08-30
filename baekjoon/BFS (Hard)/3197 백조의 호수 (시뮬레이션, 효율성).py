from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def water_move():
    while water1:
        x, y = water1.popleft()
        a[x][y] = "."
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not water_check[nx][ny]:
                water_check[nx][ny] = True
                if a[nx][ny] == ".":
                    water1.append((nx, ny))
                else:
                    water2.append((nx, ny))

def swan_move():
    while swan1:
        x, y = swan1.popleft()
        if x == ex and y == ey:
            return True

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not swan_check[nx][ny]:
                swan_check[nx][ny] = True
                if a[nx][ny] == ".":
                    swan1.append((nx, ny))
                else:
                    swan2.append((nx, ny))
    return False

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
water_check = [[False] * m for _ in range(n)]
swan_check = [[False] * m for _ in range(n)]
water1 = deque()
water2 = deque()
swan1 = deque()
swan2 = deque()

sx, sy, ex, ey = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        # 백조가 있던 자리도 물로 처리해야 하므로 백조먼저 확인
        if a[i][j] == "L":
            if sx == -1 and sy == -1:
                sx, sy = i, j
                swan1.append((sx, sy))
                swan_check[sx][sy] = True
            else:
                ex, ey = i, j
            a[i][j] = "."

        if a[i][j] == ".":
            water1.append((i, j))
            water_check[i][j] = True

ans = 0
while True:
    water_move()
    if swan_move():
        break

    water1 = water2
    swan1 = swan2
    water2 = deque()
    swan2 = deque()
    ans += 1
print(ans)