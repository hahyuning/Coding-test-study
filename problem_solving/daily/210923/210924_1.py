from collections import defaultdict, deque

graph = defaultdict(list)
while True:
    try:
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    except:
        break

if len(graph.keys()) == 0:
    print(0)
else:
    q = deque()
    dist = [-1] * (len(graph.keys()) + 1)
    q.append(1)
    dist[1] = 0

    max_val = 0
    max_node = 0
    while q:
        now = q.popleft()
        for nxt, cost in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + cost
                if dist[nxt] > max_val:
                    max_node = nxt
                    max_val = dist[nxt]
                q.append(nxt)

    q = deque()
    dist = [-1] * (len(graph.keys()) + 1)
    q.append(max_node)
    dist[max_node] = 0

    ans = 0
    while q:
        now = q.popleft()
        for nxt, cost in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + cost
                ans = max(ans, dist[nxt])
                q.append(nxt)
    print(ans)