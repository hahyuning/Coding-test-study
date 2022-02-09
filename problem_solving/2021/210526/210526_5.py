from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
light = [[False] * n for _ in range(n)]
check = [[False] * n for _ in range(n)]
switch = defaultdict(list)

for _ in range(m):
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1
    switch[(x, y)].append((a, b))

q = deque()
q.append((0, 0))
light[0][0] = True
check[0][0] = True

while q:
    x, y = q.popleft()
    for a, b in switch[(x, y)]:
        light[a][b] = True
        for k in range(4):
            na, nb = a + dx[k], b + dy[k]
            if 0 <= na < n and 0 <= nb < n and not check[a][b] and check[na][nb]:
                check[a][b] = True
                q.append((a, b))
                break

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and light[nx][ny] and not check[nx][ny]:
            q.append((nx, ny))
            check[nx][ny] = True

ans = 0
for i in range(n):
    for j in range(n):
        if light[i][j]:
            ans += 1
print(ans)
