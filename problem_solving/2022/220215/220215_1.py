import heapq

n = int(input())
a = []
for _ in range(n):
    s, e = map(int, input().split())
    if s > e:
        s, e = e, s
    a.append((s, e))

d = int(input())
b = [(s, e) for s, e in a if e - s <= d]
b.sort(key=lambda x:x[1])

ans = 0
q = []
for s, e in b:
    if not q:
        heapq.heappush(q, (s, e))
    else:
        while q and e - q[0][0] > d:
            heapq.heappop(q)
        heapq.heappush(q, (s, e))

    ans = max(ans, len(q))
print(ans)