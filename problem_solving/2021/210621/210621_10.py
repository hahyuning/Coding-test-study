from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

q = deque()
q.append((0, 0))
dist[0][0] = 0

dx = [1, 0]
dy = [0, 1]

while q:
    x, y = q.popleft()
    num = a[x][y]

    for k in range(2):
        nx, ny = x + dx[k] * num, y + dy[k] * num
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

if dist[-1][-1] != -1:
    print("HaruHaru")
else:
    print("Hing")