def check(num):
    x = num // 5
    y = num % 5

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny]:
            if (nx * 5 + ny) in tmp:
                visit[nx][ny] = True
                check(nx * 5 + ny)

def dfs(cnt, idx, ycnt):
    global res, visit
    # 임도연파가 우위에 있는 경우
    if ycnt >= 4:
        return
    # 남은 인원으로 7명을 못채우는 경우
    if 25 - idx < 7 - cnt:
        return

    if cnt == 7:
        check(tmp[0])

        ch = 0
        for i in range(5):
            for j in range(5):
                if visit[i][j]:
                    ch += 1
        if ch == 7:
            res += 1

        visit = [[False] * 5 for _ in range(5)]
        return

    tmp.append(idx)
    x = idx // 5
    y = idx % 5

    if a[x][y] == "S":
        dfs(cnt + 1, idx + 1, ycnt)
    else:
        dfs(cnt + 1, idx + 1, ycnt + 1)

    tmp.pop()
    dfs(cnt, idx + 1, ycnt)


a = [input() for _ in range(5)]
visit = [[False] * 5 for _ in range(5)]
tmp = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
dfs(0, 0, 0)
print(res)