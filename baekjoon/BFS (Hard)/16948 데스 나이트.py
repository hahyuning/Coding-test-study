from collections import deque

n = int(input())
sr, sc, er, ec = map(int, input().split())
dist = [[-1] * n for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = deque()
q.append((sr, sc))
dist[sr][sc] = 0

while q:
    r, c = q.popleft()

    for i in range(6):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < n:
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

print(dist[er][ec])