from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, dir, check, grid):
    n = len(grid)
    m = len(grid[0])

    q = deque()
    q.append((x, y, dir))
    check[x][y][dir] = 0

    while q:
        x, y, dir = q.popleft()

        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0:
            nx = n - 1
        elif nx >= n:
            nx = 0
        if ny < 0:
            ny = m - 1
        elif ny >= m:
            ny = 0

        if grid[nx][ny] == "R":
            ndir = (dir + 1) % 4
        elif grid[nx][ny] == "L":
            ndir = (dir + 3) % 4
        else:
            ndir = dir

        if check[nx][ny][ndir] != -1:
            return check[x][y][dir] + 1

        check[nx][ny][ndir] = check[x][y][dir] + 1
        q.append((nx, ny, ndir))


def solution(grid):
    n = len(grid)
    m = len(grid[0])
    ans = []
    check = [[[-1 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                if check[i][j][k] == -1:
                    ans.append(bfs(i, j, k, check, grid))

    return sorted(ans)

solution(["SL","LR"])
solution(["S"])
solution(["R","R"])