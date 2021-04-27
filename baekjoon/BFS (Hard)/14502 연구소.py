from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 2. 바이러스 확산
def bfs():
    global ans
    # 매 시행마다 a가 변하기 때문에 maps 를 복사해서 사용
    a = copy.deepcopy(maps)
    q = deque()

    # 바이러스가 있는 곳 전체를 큐에 삽입
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    a[nx][ny] = 2
                    q.append((nx, ny))

    # bfs 가 끝난 후 바이러스가 점염되지 않은 곳의 수를 세어 ans 를 최대값으로 갱신
    birus = 0
    for i in a:
        birus += i.count(0)
    ans = max(ans, birus)

# --------------------------------------------------------
# 1. 벽을 3개 세우는 함수 (조합)
# 벽이 3개 세워질 때마다 bfs 호출 -> bfs 가 ans 를 최대값으로 갱신
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(cnt + 1)
                maps[i][j] = 0

# ---------------------------------------------------------
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0
wall(0)
print(ans)