dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
rooms = [[0] * n for _ in range(n)]
priority = [[] for _ in range(n ** 2 + 1)]

for _ in range(n ** 2):
    a, *b = map(int, input().split())
    priority[a] = b

    friends = dict()
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            if rooms[i][j] == 0:
                cnt = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if rooms[nx][ny] in b:
                            cnt += 1
                        elif rooms[nx][ny] == 0:
                            blank += 1
                friends[(i, j)] = (cnt, blank)
                max_cnt = max(cnt, max_cnt)

    tmp_list = []
    for i in range(n):
        for j in range(n):
            if (i, j ) in friends and friends[(i, j)][0] == max_cnt:
                tmp_list.append((friends[(i, j)][1], i, j))
    tmp_list.sort(key=lambda x:(-x[0], x[1], x[2]))

    rooms[tmp_list[0][1]][tmp_list[0][2]] = a


ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n and rooms[nx][ny] in priority[rooms[i][j]]:
                    cnt += 1
        if cnt != 0:
            ans += 10 ** (cnt - 1)
print(ans)

