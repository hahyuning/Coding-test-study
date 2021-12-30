import heapq

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
q = []
for i in range(n):
    for j in range(n):
        heapq.heappush(q, num[i][j])

        if len(q) > n:
            heapq.heappop(q)
print(heapq.heappop(q))