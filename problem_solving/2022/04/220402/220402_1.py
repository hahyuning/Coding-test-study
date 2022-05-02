from copy import deepcopy
from collections import deque

def dfs(now, grid):
    global ans

    if now == len(grid) * len(grid[0]):
        if check(grid):
            ans += 1
        return

    i = now // len(grid[0])
    j = now % len(grid[0])
    if grid[i][j] == "?":
        for x in ["a", "b", "c"]:
            grid[i][j] = x
            dfs(now + 1, grid)
            grid[i][j] = "?"
    else:
        dfs(now + 1, grid)

def check(grid):
    abc_check = dict()
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j]:
                if grid[i][j] in abc_check:
                    return False
                visited[i][j] = True
                abc_check[grid[i][j]] = True
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                            if not visited[nx][ny] and grid[nx][ny] == grid[i][j]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j]:
                return False

    ans_str = ""
    for x in grid:
        ans_str += "".join(x)
    if ans_str in res:
        return False

    res.append(ans_str)
    return True

ans = 0
res = []
def solution(grid):
    new_grid = []
    for i in range(len(grid)):
        tmp = grid[i]
        new_grid.append(list(tmp))

    dfs(0, new_grid)
    return ans

solution(["??b", "abc", "cc?"])