from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 각 방의 크기 반환
def bfs(x, y):
    q = deque()
    q.append((x, y))
    d[x][y] = room_num
    # 현재 방의 크기
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if d[nx][ny] != 0:
                    continue
                # 비트마스크
                # 0, 1, 2, 3 번 방향에 벽이 있는지 확인
                if (a[x][y] & (1 << i)) > 0:
                    continue
                q.append((nx, ny))
                d[nx][ny] = room_num
    return cnt


# ----------------------------------------------------------------
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 각각의 위치가 어떤 방에 속하는지 기록 (방문 여부 확인도 처리)
d = [[0] * m for _ in range(n)]
# 전체 방의 개수
room_num = 0
# 각 방들의 크기 기록 (1번부터 시작)
room_size = [0]

for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            room_num += 1
            room_size.append(bfs(i, j))

max_size = 0
for i in range(1, room_num + 1):
    max_size = max(max_size, room_size[i])

print(room_num)
print(max_size)
# ---------------------------------------------------------------
# 벽을 허물었을 때 만들 수 있는 방의 최대 크기
ans = 0
for i in range(n):
    for j in range(m):
        x, y = i, j
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                # 같은 방에 속한다면 continue
                if d[nx][ny] == d[x][y]:
                    continue
                # 벽이 있으면서 벽 너머가 다른 방인 경우
                if (a[x][y] & (1 << k)) > 0:
                    ans = max(ans, room_size[d[x][y]] + room_size[d[nx][ny]])

print(ans)
