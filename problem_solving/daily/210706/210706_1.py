import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())
costs = defaultdict()
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[(a, b)] = c
dist = [-1] * n

q = []
heapq.heappush(q, (0, y))
dist[y] = 0

while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    for i in range(n):
        nxt_cost = 0
        if (i, now) in costs:
            nxt_cost = costs[(i, now)]
        elif (now, i) in costs:
            nxt_cost = costs[(now, i)]

        if nxt_cost != 0:
            nxt_cost += cost
            if dist[i] == -1 or nxt_cost < dist[i]:
                dist[i] = nxt_cost
                heapq.heappush(q, (nxt_cost, i))

dist.sort()
if dist[0] == -1:
    print(-1)
else:
    ans = 1
    sum = 0
    for d in dist:
        if 2 * d > x:
            print(-1)
            break

        if 2 * (sum + d) <= x:
            sum += d
        else:
            ans += 1
            sum = d
    else:
        print(ans)