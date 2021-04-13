from collections import deque
n, k = map(int, input().split())
time = [-1] * 200001
time[n] = 0

q = deque()
q.append(n)

while q:
    now = q.popleft()
    for next in [now + 1, now - 1, 2 * now]:
        if 0 <= next <= 200000 and time[next] == -1:
            time[next] = time[now] + 1
            q.append(next)

print(time[k])

