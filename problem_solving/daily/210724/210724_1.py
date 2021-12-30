import heapq
n = int(input())
q = []
last_time = [0] * n
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(q, (s, e))

ans = 0
while q:
    s, e = heapq.heappop(q)
    for i in range(n):
        if last_time[i] <= s:
            # 새로운 자리가 필요한 경우
            if last_time[i] == 0:
                ans += 1

            last_time[i] = e
            break
print(ans)

