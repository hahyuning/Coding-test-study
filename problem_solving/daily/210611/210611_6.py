dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    global cnt
    cnt += 1

    room[i][j] = room_num
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and a[nx][ny] == 1:
            dfs(nx, ny)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

room = [[0] * m for _ in range(n)]
room_size = dict()

room_num = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and room[i][j] == 0:
            room_num += 1
            cnt = 0
            dfs(i, j)

            room_size[room_num] = cnt

ans = 0
for i in range(n):
    for j in range(m):
        if room[i][j] == 0:
            beside = []
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and room[nx][ny] != 0:
                    x = room[nx][ny]
                    if x not in beside:
                        beside.append(x)

            if not beside:
                continue

            tmp = 1
            for x in beside:
                tmp += room_size[x]
            ans = max(ans, tmp)
print(ans)