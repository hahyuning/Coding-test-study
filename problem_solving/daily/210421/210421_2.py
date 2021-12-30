dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color):
    global cnt
    check[x][y] = True
    cnt += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == False:
            if a[nx][ny] == color:
                dfs(nx, ny, color)

m, n = map(int, input().split())
a = [input() for _ in range(n)]
w = 0
b = 0
check = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if check[i][j] == False:
            cnt = 0
            dfs(i, j, a[i][j])

            cnt = cnt ** 2
            if a[i][j] == "W":
                w += cnt
            else:
                b += cnt

print(str(w) + " " + str(b))