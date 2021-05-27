import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    dist = [[-1] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (a[0][0], 0, 0))
    dist[0][0] = a[0][0]

    while q:
        cost, x, y = heapq.heappop(q)
        if dist[x][y] != -1 and dist[x][y] < cost:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                nxt_cost = a[nx][ny] + cost
                if dist[nx][ny] == -1 or nxt_cost < dist[nx][ny]:
                    dist[nx][ny] = nxt_cost
                    heapq.heappush(q, (nxt_cost, nx, ny))
    return dist[n - 1][n - 1]

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = [list(map(int, input().split())) for _ in range(n)]
    print("Problem " + str(t) + ": " + str(dijkstra()))
    t += 1

