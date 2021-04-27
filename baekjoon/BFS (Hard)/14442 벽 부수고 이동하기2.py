from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m, k = map(int, input().split())
maps = [list(map(int, list(input()))) for _ in range(n)]
# 벽을 몇번 부수고 (i, j)까지 왔는지를 기록하기 위해 3차원 배열 사용
# (i, j, k) : k는 벽을 부순 횟수, k가 0이면 벽을 부순적이 없음
dist = [[[0] * 11 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

while q:
    x, y, z = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 이동하려는 칸이 벽이 아니면서 이전에 방문한 적이 없는 경우
            if maps[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            # 이전에 벽을 k번 보다 적게 부쉈고, 이동하려는 칸이 벽이면서 이전에 방문한 적이 없는 경우
            if z + 1 <= k and maps[nx][ny] == 1 and dist[nx][ny][z + 1] == 0:
                dist[nx][ny][z + 1] = dist[x][y][z] + 1
                q.append((nx, ny, z + 1))

ans = -1
for i in range(k + 1):
    if dist[n - 1][m - 1][i] == 0:
        continue
    if ans == -1 or ans > dist[n - 1][m - 1][i]:
        ans = dist[n - 1][m - 1][i]
print(ans)
