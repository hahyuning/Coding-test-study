INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0

    # 간선 개수만큼 반복
    for i in range(v):
        for j in range(e):
            node = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if dist[node] != INF and dist[nxt] > dist[node] + cost:
                dist[nxt] = dist[node] + cost
                if i == v - 1:
                    return True
    return False

v, e = map(int, input().split())
edges = []
dist = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

cycle = bellman_ford(1)
if cycle:
    print(-1)
else:
    for i in range(2, v + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])