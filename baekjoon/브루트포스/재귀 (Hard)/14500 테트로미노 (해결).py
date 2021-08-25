def tetromino(x, y, sum, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
            check[nx][ny] = True
            tetromino(nx, ny, sum + a[nx][ny], cnt + 1)
            check[nx][ny] = False
        else:
            return

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
for i in range(n):
    for j in range(m):
        check[i][j] = True
        tetromino(i, j, 0, 0)
        check[i][j] = False

        if j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2]
            if i - 1 >= 0:
                temp2 = temp + a[i - 1][j + 1]
                answer = max(answer, temp2)
            if i + 1 < n:
                temp2 = temp + a[i + 1][j + 1]
                answer = max(answer, temp2)
        if i + 2 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j]
            if j + 1 < m:
                temp2 = temp + a[i + 1][j + 1]
                answer = max(answer, temp2)
            if j - 1 >= 0:
                temp2 = temp + a[i + 1][j - 1]
                answer = max(answer, temp2)

print(answer)