from collections import deque
n, k = map(int, input().split())
time = [-1] * 200001
time[n] = 0

q = deque()
q.append(n)

while q:
    now = q.popleft()
    if 0 <= 2 * now <= 200000 and time[2 * now] == -1:
        time[2 * now] = time[now]
        q.appendleft(2 * now)
    if 0 <= now + 1 <= 200000 and time[now + 1] == -1:
        time[now + 1] = time[now] + 1
        q.append(now + 1)
    if 0 <= now - 1 <= 200000 and time[now - 1] == -1:
        time[now - 1] = time[now] + 1
        q.append(now - 1)

print(time[k])

