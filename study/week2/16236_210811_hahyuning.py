from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, size):
    # 모든 물고기까지의 거리와 위치 정보를 담은 배열
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
                move = False
                eat = False
                if maps[nx][ny] == 0:
                    move = True
                elif maps[nx][ny] < size:
                    move = True
                    eat = True
                elif maps[nx][ny] == size:
                    move = True

                if move == True:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat == True:
                        ans.append((d[nx][ny], nx, ny))

    if not ans:
        return None
    ans.sort()
    return ans[0]

n = int(input())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

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

while True:
    p = bfs(sx, sy, size)
    # 먹을 수 있는 물고기가 없다면 break
    if p is None:
        break

    # 물고기까지의 거리, 물고기의 위치
    dist, nx, ny = p
    maps[nx][ny] = 0
    time += dist
    eat_num += 1

    if size == eat_num:
        size += 1
        eat_num = 0

    sx, sy = nx, ny

print(time)