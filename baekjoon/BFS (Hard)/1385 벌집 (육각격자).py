from collections import deque

# 1.  육각 격자 채우기

# 규칙: 시작하면 위로 한칸, d[0] 방향으로 level - 1 번, d[1] 부터 level + 1 번씩 이동
dx = [-1, 0, 1, 1, 0, -1]
dy = [1, 1, 0, -1, -1, 0]

a = [[0] * 2001 for _ in range(2001)]
# 1의 좌표를 (1000, 1000)으로 설정
x, y = 1000, 1000
a[x][y] = 1

cnt = 2
for level in range(1, 1001):
    # 위로 한칸 이동
    x += dx[5]
    y += dy[5]
    a[x][y] = cnt
    cnt += 1

    # 규칙에 따라 이동
    for k in range(6):
        tmp = level
        if k == 0:
            tmp -= 1

        for _ in range(tmp):
            x += dx[k]
            y += dy[k]
            a[x][y] = cnt
            cnt += 1

# 2. 좌표 저장

# 숫자 k가 쓰여져 있는 칸의 좌표 기록
c = [None] * 3003002

for i in range(2001):
    for j in range(2001):
        if a[i][j] != 0 and a[i][j] <= 3003001:
            c[a[i][j]] = (i, j)

# 3. bfs 수행

# 경로 탐색을 위해 시작점과 끝점 위치 교환
e, s = map(int, input().split())

dist = [-1] * 3003002
path = [-1] * 3003002

q = deque()
q.append(s)
dist[s] = 0
path[s] = -1

while q:
    now = q.popleft()
    x, y = c[now]

    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < 2001 and 0 <= ny < 2001:
            if a[nx][ny] != 0:
                nxt = a[nx][ny]
                if dist[nxt] == -1:
                    q.append(nxt)
                    dist[nxt] = dist[now] + 1
                    path[nxt] = now

# 4. 경로 출력
print(e, end=" ")
while s != e:
    e = path[e]
    print(e, end=" ")