from bisect import bisect_right
import heapq, sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    deadline, benefit = map(int, input().split())
    heapq.heappush(q, (-benefit, deadline))

remain = [i for i in range(1, n + 1)]

ans = 0
while q:
    benefit, deadline = heapq.heappop(q)

    idx = bisect_right(remain, deadline)
    idx -= 1
    if idx < 0:
        continue

    remain.pop(idx)
    ans -= benefit

print(ans)
