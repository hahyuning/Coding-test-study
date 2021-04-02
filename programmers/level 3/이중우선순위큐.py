import heapq
def solution(operations):
    q = []
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(q, int(operation.split(" ")[-1]))
        else:
            if len(q) == 0:
                continue
            # 큐에서 최솟값 삭제
            if operation.split(" ")[1] == "-1":
                heapq.heappop(q)
            # 큐에서 최댓값 삭제
            else:
                q.pop(q.index(heapq.nlargest(1, q)[0]))
    if len(q) > 0:
        return [heapq.nlargest(1, q)[0], heapq.nsmallest(1, q)[0]]
    return [0, 0]