from collections import deque

n, m = map(int, input().split())
a = [input() for _ in range(n)]

d = [[[[-1] * 4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
sx, sy = 0, 0
x1, y1, x2, y2 = -1, -1, -1, -1

for i in range(n):
    for j in range(m):
        if a[i][j] == "S":
            sx, sy = i, j

        if a[i][j] == "C":
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j

q = deque()
for k in range(4):
    q.append((sx, sy, k, 0))
    d[sx][sy][k][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = -1
while q:
    x, y, dir, s = q.popleft()

    if s == 3:
        ans = d[x][y][dir][s]
        break

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if dir == k:
            continue

        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] != "#":
                ns = s
                if a[nx][ny] == "C":
                    if nx == x1 and ny == y1:
                        # 1이면 그대로, 1이 아니면 +1
                        ns |= 1
                    else:
                        # 2면 그대로, 2가 아니면 +2
                        ns |= 2

                if d[nx][ny][k][ns] == -1:
                    d[nx][ny][k][ns] = d[x][y][dir][s] + 1
                    q.append((nx, ny, k, ns))

print(ans)


