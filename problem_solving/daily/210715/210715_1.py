import sys
input = sys.stdin.readline

def dfs(x, y):
    # 탈출 확인
    if x >= n or x < 0 or y >= m or y < 0:
        return True
    # 이전에 확인했던 경로인 경우
    if maps[x][y] == "T":
        return True
    elif maps[x][y] == "F":
        return False

    if visit[x][y]:
        return False
    visit[x][y] = True
    nx, ny = x + d[maps[x][y]][0], y + d[maps[x][y]][1]
    res = dfs(nx, ny)

    if res:
        maps[x][y] = "T"
    else:
        maps[x][y] = "F"
    return res

n, m = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]
d = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
ans = 0
visit = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ans += 1
print(ans)