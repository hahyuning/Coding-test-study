from collections import deque

a, b = map(int, input().split())

q = deque()
q.append(a)

time = [-1] * 100001
time[a] = 0

while q:
    now = q.popleft()
    if 0 <= 2 * now < 100001 and time[2 * now] == -1:
        q.appendleft(2 * now)
        time[2 * now] = time[now]

    for nxt in [now - 1, now + 1]:
        if 0 <= nxt < 100001 and time[nxt] == -1:
            q.append(nxt)
            time[nxt] = time[now] + 1

print(time[b])
