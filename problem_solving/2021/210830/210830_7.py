import heapq

n = int(input())
a = []
for _ in range(n):
    num, s, e = map(int, input().split())
    heapq.heappush(a, (s, e))

q = []
s, e = heapq.heappop(a)
heapq.heappush(q, e)

while a:
    s, e = heapq.heappop(a)
    if q[0] <= s:
        heapq.heappop(q)
    heapq.heappush(q, e)

print(len(q))