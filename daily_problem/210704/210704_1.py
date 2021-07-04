from copy import deepcopy

def dfs(cnt, arr):
    global ans
    if cnt == cctv_num:
        tmp = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    tmp += 1
        if ans == -1 or tmp < ans:
            ans = tmp
        return

    x, y, d = cctv_loc[cnt]
    for dir in cctv[d]:
        tmp = deepcopy(arr)
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < m:
                if tmp[nx][ny] == 6:
                    break
                if tmp[nx][ny] not in [1, 2, 3, 4, 5]:
                    tmp[nx][ny] = -1
                nx += dx
                ny += dy
        dfs(cnt + 1, tmp)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cctv = {1: [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]], 2: [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]],
        3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        4: [[(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)],
            [(0, -1), (-1, 0), (0, 1)]],
        5: [[(-1, 0), (0, 1), (1, 0), (0, -1)]]}

cctv_num = 0
cctv_loc = []
for i in range(n):
    for j in range(m):
        if a[i][j] in [1, 2, 3, 4, 5]:
            cctv_num += 1
            cctv_loc.append((i, j, a[i][j]))
ans = -1
dfs(0, a)
print(ans)