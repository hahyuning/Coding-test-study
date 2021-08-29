import heapq


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


def solution(N, road):
    graph = [[] for _ in range(N + 1)]

    distance = [50001] * (N + 1)
    for x in road:
        a, b = x
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    result = dijkstra(1, graph, distance)
    max_val = 0
    for x in result:
        if x != 50001 and x > max_val:
            max_val = x

    return result.count(max_val)