dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def make_cluster(i, j):
    cluster[i][j] = c
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == "x" and cluster[nx][ny] == 0:
                make_cluster(nx, ny)


def move(ch):
    down = n
    for j in range(m):
        for i in range(n):
            if cluster[i][j] == ch:
                tmp = n
                for k in range(i + 1, n):
                    if cluster[k][j] != ch and cluster[k][j] != 0:
                        tmp = k
                        break
                down = min(down, tmp - i - 1)

    for j in range(m):
        for i in range(n - 1, -1, -1):
            if cluster[i][j] == ch:
                cluster[i + down][j] = cluster[i][j]
                cluster[i][j] = 0
                a[i + down][j] = a[i][j]
                a[i][j] = "."


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
k = int(input())
order = list(map(int, input().split()))
dir = 0

cluster = [[0] * m for _ in range(n)]
c = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == "x" and cluster[i][j] == 0:
            c += 1
            make_cluster(i, j)

for x in order:
    y = 0
    if dir == 0:
        for j in range(m):
            if a[n - x][j] == "x":
                y = j
                a[n - x][j] = "."
                cluster[n - x][j] = 0
                break
    else:
        for j in range(m - 1, -1, -1):
            if a[n - x][j] == "x":
                y = j
                a[n - x][j] = "."
                cluster[n - x][j] = 0
                break

    cluster = [[0] * m for _ in range(n)]
    c = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == "x" and cluster[i][j] == 0:
                c += 1
                make_cluster(i, j)

    check = set()
    for k in range(4):
        nx, ny = n - x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if cluster[nx][ny] != 0:
                check.add(cluster[nx][ny])

    for ch in check:
        if ch not in cluster[n - 1]:
            move(ch)
    dir = 1 - dir

for row in a:
    print("".join(row))

