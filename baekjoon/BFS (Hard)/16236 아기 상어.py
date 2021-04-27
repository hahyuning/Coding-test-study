from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 먹을 수 있는 물고기 중 가장 가까운 물고기까지의 거리와, 그 물고기의 위치 반환
def bfs(x, y, size):
    # 먹을 수 있는 모든 물고기까지의 거리와 위치 정보를 담은 배열
    ans = []
    d = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    d[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                # 이동 가능한지 확인
                move = False
                # 먹을 수 있는지 확인
                eat = False
                if maps[nx][ny] == 0:
                    move = True
                # 물고기가 있으면서, 이동할 수 있고, 먹을 수 있는 경우
                elif maps[nx][ny] < size:
                    move = True
                    eat = True
                # 물고기가 있으면서, 이동할 수는 있지만, 먹을 수는 없는 경우
                elif maps[nx][ny] == size:
                    move = True

                if move == True:
                    # 이동 가능하면 큐에 삽입
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    # 먹을 수 있으면 ans 에 삽입
                    if eat == True:
                        ans.append((d[nx][ny], nx, ny))

    if not ans:
        return None
    ans.sort()
    return ans[0]

# --------------------------------------------------------------------
n = int(input())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 상어의 위치
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            sx, sy = i, j
            maps[i][j] = 0

time = 0 # 걸린 시간
size = 2 # 상어의 크기
eat_num = 0 # 먹은 물고기의 개수

# 물고기를 한 번 먹을 때마다 bfs 반복
while True:
    p = bfs(sx, sy, size)
    # 먹을 수 있는 물고기가 없다면 break
    if p is None:
        break

    # 물고기까지의 거리, 물고기의 위치
    dist, nx, ny = p
    # 물고기를 먹었으므로 빈칸 처리
    maps[nx][ny] = 0
    # 이동 시간 더하기
    time += dist
    # 먹은 갯수 늘리기
    eat_num += 1

    # 먹은 갯수가 현재 크기와 같아진 경우
    if size == eat_num:
        # 크기를 1 늘리고 먹은 갯수 초기화
        size += 1
        eat_num = 0

    # 상어의 위치 좌표 갱신
    sx, sy = nx, ny

print(time)