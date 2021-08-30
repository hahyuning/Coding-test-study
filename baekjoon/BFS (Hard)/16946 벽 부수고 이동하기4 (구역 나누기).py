from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    group[x][y] = group_cnt
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and group[nx][ny] == -1:
                if a[nx][ny] == 0:
                    group[nx][ny] = group_cnt
                    q.append((nx, ny))
    return cnt

# -----------------------------------------------------------------
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

# 빈칸이 어떤 그룹에 속하는지 기록
group = [[-1] * m for _ in range(n)]
# 각 그룹의 사이즈 기록
group_size = [0]
group_cnt = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and group[i][j] == -1:
            group_cnt += 1
            group_size.append(bfs(i, j))

# --------------------------------------------------------------
ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            tmp = 1
            check_list = []
            x, y = i, j
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if group[nx][ny] != -1 and group[nx][ny] not in check_list:
                        tmp += group_size[group[nx][ny]]
                        check_list.append(group[nx][ny])
            ans[i][j] = tmp % 10

for x in ans:
    print("".join(map(str, x)))

