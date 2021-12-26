from collections import deque

def change_direction(type, dir):
    if type == 1:
        if dir == 0 or dir == 2:
            return dir
        else:
            return (dir + 2) % 4
    elif type == 2:
        if dir == 1 or dir == 3:
            return dir
        else:
            return (dir + 2) % 4
    elif type == 3:
        if dir == 1 or dir == 3:
            return dir - 1
        else:
            return  dir + 1
    elif type == 4:
        if dir == 0 or dir == 2:
            return (dir + 3) % 4
        else:
            return (dir + 1) % 4
    else:
        return dir

def bfs(x, y, dir):
    q = deque()
    check[x][y][dir] = True
    q.append((x, y, dir))

    while q:
        x, y, dir = q.popleft()
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m:
            ndir = change_direction(a[nx][ny], dir)

            if not check[nx][ny][ndir]:
                check[nx][ny][ndir] = True
                q.append((nx, ny, ndir))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 북:0, 동:1, 남:2, 서:3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = [[[False] * 4 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 9:
            for k in range(4):
                if not check[i][j][k]:
                    bfs(i, j, k)

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(4):
            if check[i][j][k]:
                ans += 1
                break
print(ans)
