import heapq
def solution(n, works):
    if n >= sum(works):
        return 0

    q = []
    for w in works:
        heapq.heappush(q, -w)
    while n > 0:
        w = heapq.heappop(q)
        heapq.heappush(q, w + 1)
        n -= 1

    return sum([w ** 2 for w in q])

print(solution(4, [4, 3, 3]))