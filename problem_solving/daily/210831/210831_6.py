import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    q = []

    for i in range(n):
        heapq.heappush(q, a[i])

    while len(q) > 1:
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        ans += (x + y)
        heapq.heappush(q, x + y)

    print(ans)