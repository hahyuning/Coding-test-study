import heapq

n = int(input())
study = [list(map(int, input().split())) for _ in range(n)]
study.sort()

ans = 0
# 우선순위 큐에 강의가 끝나는 시간을 삽입
q = []
heapq.heappush(q, study[0][1])

for i in range(1, n):
    if study[i][0] >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, study[i][1])
    else:
        heapq.heappush(q, study[i][1])
    ans = max(ans, len(q))
print(ans)