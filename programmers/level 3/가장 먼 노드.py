import heapq
def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] > dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
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
