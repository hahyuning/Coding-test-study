from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j, color):
    q = deque()

    q.append((i, j))
    check.add((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if a[nx][ny] == color and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    check.add((nx, ny))

def down():
    for j in range(6):
        tmp = []
        for i in range(11, -1, -1):
            if a[i][j] != ".":
                tmp.append(a[i][j])

        while len(tmp) < 12:
            tmp.append(".")

        for i in range(12):
            a[i][j] = tmp[11 - i]


# -----------------------------------------------------
a = [list(input()) for _ in range(12)]
ans = 0

while True:
    flg = False
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if a[i][j] != "." and visited[i][j] == 0:
                check = set()
                bfs(i, j, a[i][j])

                if len(check) >= 4:
                    flg = True
                    for x, y in check:
                        a[x][y] = "."

    if flg == False:
        break

    down()
    ans += 1

print(ans)