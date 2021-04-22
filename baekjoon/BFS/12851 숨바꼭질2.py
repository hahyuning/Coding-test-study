from collections import deque

a, b = map(int, input().split())

q = deque()
q.append(a)

time = [-1] * 100001
cnt = [0] * 100001
time[a] = 0
cnt[a] = 1

while q:
    now = q.popleft()
    for nxt in [2 * now, now - 1, now + 1]:
        if 0 <= nxt < 100001:
            # 처음 방문인 경우
            if time[nxt] == -1:
                q.append(nxt)
                time[nxt] = time[now] + 1
                cnt[nxt] = cnt[now]

            else:
                # 이동 횟수가 최솟값인지 확인
                if time[nxt] == time[now] + 1:
                    cnt[nxt] += cnt[now]
print(time[b])
print(cnt[b])
