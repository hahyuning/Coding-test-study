from collections import deque
t = int(input())
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, 2, 1, 1, 2, -2, -1]

for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    dist = [[-1] * n for _ in range(n)]
    dist[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    print(dist[target_x][target_y])


