INF = int(1e9)

def bellman_ford():
    for i in range(n):
        for j in range(2 * m + w):
            node = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if dist[nxt] > dist[node] + cost:
                dist[nxt] = dist[node] + cost
                if i == n - 1:
                    return True
    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    dist = [INF] * (n + 1)
    cycle = bellman_ford()

    if cycle:
        print("YES")
    else:
        print("NO")