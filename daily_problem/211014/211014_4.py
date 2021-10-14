import heapq
import sys
input = sys.stdin.readline


def check(mid):
    q = []
    for _ in range(mid):
        heapq.heappush(q, 0)

    for t in a:
        min_t = heapq.heappop(q)
        if min_t + t > x:
            return False
        heapq.heappush(q, min_t + t)
    return True

n, x = map(int, input().split())
a = list(map(int, input().split()))

lt = 1
rt = n
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2

    if check(mid):
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)