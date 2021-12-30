from collections import deque
import sys

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

sx, sy = 0, 0
ex, ey = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == "0":
            sx, sy = i, j
            a[i][j] = "."

# dist[i][j][k]: 열쇠 소지 상태가 k일때 (i, j)까지의 최단 거리
# 열쇠가 6개이므로 비트마스크를 사용하면 64가지의 경우가 나온다.
dist = [[[-1] * 64 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((sx, sy, 0))
dist[sx][sy][0] = 0

while q:
    x, y, key = q.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != "#":
            # 도착지에 도착한 경우
            if a[nx][ny] == "1":
                dist[nx][ny][key] = dist[x][y][key] + 1
                print(dist[nx][ny][key])
                sys.exit(0)

            # 빈칸인 경우
            elif a[nx][ny] == "." and dist[nx][ny][key] == -1:
                q.append((nx, ny, key))
                dist[nx][ny][key] = dist[x][y][key] + 1

            # 문에 도착한 경우
            elif a[nx][ny].isupper() and dist[nx][ny][key] == -1:
                # 가지고 있는 열쇠 중 문에 해당하는 키가 있는지 확인
                if key & (1 << (ord(a[nx][ny]) - 65)) > 0:
                    dist[nx][ny][key] = dist[x][y][key] + 1
                    q.append((nx, ny, key))

            # 열쇠에 도착한 경우
            elif a[nx][ny].islower():
                # 키 추가
                nkey = key | (1 << (ord(a[nx][ny]) - 97))
                if dist[nx][ny][nkey] == -1:
                    dist[nx][ny][nkey] = dist[x][y][key] + 1
                    q.append((nx, ny, nkey))

print(-1)