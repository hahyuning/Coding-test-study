from collections import deque

def calculate(x1, y1, x2, y2):
    return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]


n, m = map(int, input().split())
a = [[0] * (m + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))
h, w, x1, y1, x2, y2 = map(int, input().split())

# 거리
d = [[-1] * (m + 1) for _ in range(n + 1)]
# 누적합
s = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]

# bfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((x1, y1))
d[x1][y1] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 1 <= nx <= n - h + 1 and 1 <= ny <= m - w + 1:
            if calculate(nx, ny, nx + h - 1, ny + w - 1) == 0:
                if d[nx][ny] == -1:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1

print(d[x2][y2])