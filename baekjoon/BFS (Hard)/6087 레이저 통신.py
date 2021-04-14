from collections import deque
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(h)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sx = sy = ex = ey = -1
for i in range(h):
    for j in range(w):
        if maps[i][j] == "C":
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

# 직선의 개수를 담을 배열
lines = [[-1] * w for _ in range(h)]
q = deque()
lines[sx][sy] = 0
q.append((sx, sy))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # maps 안에서 갈수 있을 때까지 계속 직진
        while 0 <= nx < h and 0 <= ny < w:
            if maps[nx][ny] == "*":
                break
            if lines[nx][ny] == -1:
                lines[nx][ny] = lines[x][y] + 1
                q.append((nx, ny))

            nx += dx[i]
            ny += dy[i]

# 거울의 개수는 직선의 개수보다 1개 작으므로 -1 해준다.
print(lines[ex][ey] - 1)