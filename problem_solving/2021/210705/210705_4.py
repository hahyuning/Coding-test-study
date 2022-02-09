from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cheese = 0
for row in a:
    cheese += sum(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
while True:
    if cheese == 0:
        break
    ans += 1

    # 0: 검사 안함, 1: 빈칸, 2: 치즈
    check = [[0] * m for _ in range(n)]
    check[0][0] = 1
    q = deque()
    q.append((0, 0))
    tmp = []
    remove = []
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 0:
                if a[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append((nx, ny))
                elif a[nx][ny] == 1:
                    check[nx][ny] = 2
                    tmp.append((nx, ny))

    for x, y in tmp:
        cnt = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == 1:
                cnt += 1
        if cnt >= 2:
            remove.append((x, y))

    cheese -= len(remove)
    for x, y in remove:
        a[x][y] = 0

print(ans)