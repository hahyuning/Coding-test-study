import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
ans = [["."] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sx, sy, ex, ey = n, m, 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == "X":
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == ".":
                        cnt += 1
                else:
                    cnt += 1

            if cnt < 3:
                sx = min(sx, i)
                sy = min(sy, j)
                ex = max(ex, i)
                ey = max(ey, j)
                ans[i][j] = "X"

for row in ans[sx: ex + 1]:
    print("".join(row[sy: ey + 1]))

