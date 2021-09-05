import heapq

n, k = map(int, input().split())
j = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(j, (m, v))

b = []
for _ in range(k):
    x = int(input())
    heapq.heappush(b, x)

ans = 0
tmp = []
while b:
    now = heapq.heappop(b)
    while j and j[0][0] <= now:
        m, v = heapq.heappop(j)
        heapq.heappush(tmp, -v)

    if tmp:
        max_v = heapq.heappop(tmp)
        ans -= max_v
    if not tmp and not j:
        break

print(ans)
