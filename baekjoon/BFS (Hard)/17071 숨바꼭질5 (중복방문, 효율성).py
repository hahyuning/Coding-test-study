from collections import deque

# 문제 아이디어: 수빈이가 한 위치에 도착했다면, 2초마다 같은 위치로 이동 가능
# 홀수/짝수 시간에 어떤 칸에 도착했고, 동생이 홀수/짝수 시간만에 그 위치로 왔다면 찾을 수 있음
n, k = map(int, input().split())
q = deque()
q.append((n, 0))

# dist[i][j]: i에 도착한 최소 시간, j = 0이면 짝수시간, j = 1이면 홀수시간
dist = [[-1] * 2 for _ in range(500001)]
dist[n][0] = 0

while q:
    now, t = q.popleft()
    for nxt in [now - 1, now + 1, 2 * now]:
        if 0 <= nxt <= 500000 and not dist[nxt][1 - t]:
            dist[nxt][1 - t] = dist[now][t] + 1
            q.append((nxt, 1 - t))

ans = -1
t = 0
while True:
    k += t
    if k > 500000:
        break

    # 수빈이가 동생보다 먼저 도착했는지 확인
    if dist[k][t % 2] <= t:
        ans = t
        break
    t += 1
print(ans)