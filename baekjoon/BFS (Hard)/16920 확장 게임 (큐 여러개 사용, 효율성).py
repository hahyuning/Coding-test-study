from collections import deque

n, m, p = map(int, input().split())
s = [0] + list(map(int, input().split()))
a = [[0] * m for _ in range(n)]

# -1은 벽, 0은 빈칸, 나머지는 플레이어의 숫자
for i in range(n):
    tmp = input()
    for j in range(m):
        if tmp[j] == ".":
            a[i][j] = 0
        elif tmp[j] == "#":
            a[i][j] = -1
        else:
            a[i][j] = int(tmp[j])

# 각 플레이어마다 큐 따로 사용
q = [deque() for _ in range(p + 1)]
# 다음 턴의 시작점 저장
nxt_q = [deque() for _ in range(p + 1)]

for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            q[a[i][j]].append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    ch = False

    # 플레이어 순서대로 진행
    for i in range(1, p + 1):
        d = [[0] * m for _ in range(n)]

        while q[i]:
            ch = True
            x, y = q[i].popleft()

            # 다음 턴에 확장할 칸 저장
            if d[x][y] == s[i]:
                nxt_q[i].append((x, y))

            # 확장하려고 하는 칸이 이미 다른 플레이어가 확장한 경우
            if a[x][y] > 0 and a[x][y] != i:
                continue

            # 칸 확장
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        d[nx][ny] = d[x][y] + 1
                        if d[nx][ny] <= s[i]:
                            a[nx][ny] = i
                            q[i].append((nx, ny))
        q[i] = nxt_q[i]
        nxt_q[i] = deque()
    # 더 이상 확장이 불가능하면 종료
    if not ch:
        break

ans = [0] * (p + 1)
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            ans[a[i][j]] += 1

print(*ans[1:])