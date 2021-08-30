from collections import deque
from itertools import permutations

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# (sx, sy)부터 다른 모든 점까지의 거리 반환
def bfs(sx, sy):
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1 and maps[nx][ny] != "x":
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


# -----------------------------------------------------------------------
# 더러운 칸을 방문할 순서 정하기 -> 거리의 합 구하기
while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break

    maps = [input() for _ in range(n)]
    # 맨 앞에 시작 위치, 그 뒤로 먼지의 위치 저장
    dust = [(-1, -1)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "o":
                dust[0] = (i, j)
            elif maps[i][j] == "*":
                dust.append((i, j))

    # 1. 모든 먼지를 청소 가능한지 확인
    flg = True

    # i번째 먼지에서 j번째 먼지까지의 거리
    d = [[0] * len(dust) for _ in range(len(dust))]
    for i in range(len(dust)):
        # i 번째 먼지에서 다른 위치까지의 거리
        # d[a][b]: i번째 먼지에서 (a, b) 위치까지의 거리
        dist = bfs(dust[i][0], dust[i][1])

        for j in range(len(dust)):
            # i 번째 먼지에서 j 번째 먼지까지의 거리
            d[i][j] = dist[dust[j][0]][dust[j][1]]

            if d[i][j] == -1:
                flg = False

    if flg == False:
        print(-1)
        continue

    # 2. 청소 가능한 경우, 청소할 순서 정하기
    # 미리 구해놓은 d 배열을 통해 매번 거리 계산을 하지 않아도 된다.
    permutation = permutations([i + 1 for i in range(len(dust) - 1)])
    ans = -1
    # p에는 순열 중 하나가 들어 있다.
    for p in permutation:
        # 시작 위치 ~ 첫 번째 먼지
        now = d[0][p[0]]
        # 순서대로 거리 더하기
        for i in range(len(dust) - 2):
            now += d[p[i]][p[i + 1]]

        if ans == -1 or ans > now:
            ans = now
    print(ans)
