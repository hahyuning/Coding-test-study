dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, x, y, p):
    global ans

    # 종료 조건: i = n이 된 경우
    if i == n:
        ans += p
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if (nx, ny) not in check:
            check.add((nx, ny))
            dfs(i + 1, nx, ny, p * prop[k])
            check.remove((nx, ny))

n, *prop = map(int, input().split())
check = set()
ans = 0

check.add((0, 0))
dfs(0, 0, 0, 1)
print(ans / (100 ** n))