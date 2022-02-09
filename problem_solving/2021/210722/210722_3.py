import heapq
n = int(input())
q = []
# 각 컴퓨터의 종료시간
last_time = [0] * n
# 각 컴퓨터의 사용횟수
cnt = [0] * n
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
            cnt[i] += 1
            break
print(ans)
print(*cnt[:ans])