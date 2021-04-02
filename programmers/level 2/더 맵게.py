import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    for s in scoville:
        heapq.heappush(hq, s)

    while len(hq) > 1:
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        if a >= K:
            break
        heapq.heappush(hq, a + 2 * b)
        answer += 1

    if len(hq) == 1 and hq[0] < K:
        return -1
    return answer