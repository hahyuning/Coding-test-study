import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 continue
        if dist[now] != -1 and dist[now] < cost:
            continue

        for nxt, nxt_cost in graph[now]:
            nxt_cost += cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if nxt_cost < dist[nxt] or dist[nxt] == -1:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))


n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n + 1):
    if dist[i] == -1:
        continue
    print(dist[i])