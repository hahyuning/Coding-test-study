from collections import deque

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans += 1
if ans == 0:
    print(cnt)
    print(ans)
else:
    while True:
        cnt += 1
        q = deque()
        d = [[0] * m for _ in range(n)]

        for j in range(1, m - 1):
            q.append((0, j))
            q.append((n - 1, j))
            d[0][j] = 1
            d[n - 1][j] = 1
        for i in range(1, n - 1):
            q.append((i, 0))
            q.append((i, m - 1))
            d[i][0] = 1
            d[i][m - 1] = 1

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == 0:
                    if a[nx][ny] == 1:
                        d[nx][ny] = 2
                    else:
                        d[nx][ny] = 1
                        q.append((nx, ny))

        x = 0
        for i in range(n):
            for j in range(m):
                if d[i][j] == 2:
                    a[i][j] = 0
                elif a[i][j] == 1:
                    x += 1
        if x == 0:
            break
        ans = x

    print(cnt)
    print(ans)



