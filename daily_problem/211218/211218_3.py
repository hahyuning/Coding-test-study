import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global ans, blank

    if cnt >= ans:
        return
    if blank == 0:
        ans = min(ans, cnt)

    for k in range(4):
        tmp = []
        nx, ny = x + dx[k], y + dy[k]
        moved = False

        while 0 <= nx < n and 0 <= ny < m and a[nx][ny] == "." and not visited[nx][ny]:
            tmp.append((nx, ny))
            moved = True
            blank -= 1
            visited[nx][ny] = True
            nx += dx[k]
            ny += dy[k]

        if moved:
            dfs(nx - dx[k], ny - dy[k], cnt + 1)

        for i, j in tmp:
            visited[i][j] = False
            blank += 1

case = 1
while True:
    try:
        n, m = map(int, input().split())
        a = [list(input().rstrip()) for _ in range(n)]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        blank = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == ".":
                    blank += 1

        ans = 1000001
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if a[i][j] == ".":
                    visited[i][j] = True
                    blank -= 1
                    dfs(i, j, 0)
                    blank += 1
                    visited[i][j] = False

        if ans == 1000001:
            ans = -1

        print("Case {}: {}".format(case, ans))
        case += 1
    except:
        break