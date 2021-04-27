from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
# 토마토가 익는 시간을 기록할 리스트
time = [[0] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(m):
    for j in range(n):
        # 토마토들이 동시에 익시 시작 -> 익은 토마토가 들어있는 칸을 모두 큐에 삽입
        if board[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < m and 0 <= ny < n:
            # 익지 않은 토마토가 들어 있으면
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                time[nx][ny] = time[x][y] + 1
                queue.append((nx, ny))

# --------------------------------------------------------------------
# 모든 토마토가 익었는지 확인
flg = False
# 모든 토마토가 익는데 걸리는 시간
res = 0
for i in range(m):
    for j in range(n):
        res = max(res, time[i][j])
        # 익지 않은 토마토가 존재하면
        if board[i][j] == 0:
            flg = True
print(-1 if flg else res)
