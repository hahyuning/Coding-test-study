from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and maps[nx][ny] != "*":
                # 이동하려는 칸이 문인 경우
                if maps[nx][ny] == "#":
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 이동하려는 칸이 문이 아닌 경우
                else:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
    return dist


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # 지도를 상하좌우로 한칸씩 확대 (테두리에서는 이동하는데 가중치가 모두 0)
    maps = ["." + input() + "." for _ in range(n)]
    n += 2
    m += 2
    maps = ["." * m] + maps + ["." * m]

    # 바깥에서 부터 bfs, 죄수 1부터 시작하는 bfs, 죄수 2부터 시작하는 bfs
    # 총 bfs 를 세번 계산해야 한다.
    dist0 = bfs(0, 0)

    x1 = y1 = x2 = y2 = -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "$":
                if x1 == -1:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
    dist1 = bfs(x1, y1)
    dist2 = bfs(x2, y2)

    ans = n * m
    # 바깥, 죄수1, 죄수2 가 만나는 곳 찾기
    for i in range(n):
        for j in range(m):
            # 만나는 곳이 벽인 경우
            if maps[i][j] == "*":
                continue
            # 세명 중 하나라도 그곳에 도달하지 못하는 경우
            if dist0[i][j] == -1 or dist1[i][j] == -1 or dist2[i][j] == -1:
                continue

            res = dist0[i][j] + dist1[i][j] + dist2[i][j]
            # 세명이 만나는 곳이 문인 경우는 -2
            if maps[i][j] == "#":
                res -= 2

            ans = min(ans, res)
    print(ans)



