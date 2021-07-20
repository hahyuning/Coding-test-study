from collections import deque

dx = [-1, -1, 0, 0, 1, 1]
dy1 = [-1, 0, -1, 1, -1, 0]
dy2 = [0, 1, -1, 1, 0, 1]

m, n = map(int, input().split())
a = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
a.insert(0, [0] * (m + 2))
a.append([0] * (m + 2))
q = deque()
cnt  = [[0] * (m + 2) for _ in range(n + 2)]
q.append((0, 0))
cnt[0][0] = -1

while q:
    x, y = q.popleft()
    if x % 2 == 0:
        for k in range(6):
            nx, ny = x + dx[k], y + dy1[k]
            if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                if a[nx][ny] == 0 and cnt[nx][ny] == 0:
                    cnt[nx][ny] = -1
                    q.append((nx, ny))
                elif a[nx][ny] == 1:
                    cnt[nx][ny] += 1
    else:
        for k in range(6):
            nx, ny = x + dx[k], y + dy2[k]
            if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                if a[nx][ny] == 0 and cnt[nx][ny] == 0:
                    cnt[nx][ny] = -1
                    q.append((nx, ny))
                elif a[nx][ny] == 1:
                    cnt[nx][ny] += 1

ans = 0
for i in range(n + 2):
    for j in range(m + 2):
        if cnt[i][j] != -1:
            ans += cnt[i][j]
print(ans)
