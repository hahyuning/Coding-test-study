import heapq
k, n = map(int, input().split())
a = list(map(int, input().split()))
q = []
for x in a:
    heapq.heappush(q, x)

ans = 0
for _ in range(n):
    now = heapq.heappop(q)
    ans = now
    for x in a:
        heapq.heappush(q, x * now)
        
        if now % x == 0:
            break
print(ans)
