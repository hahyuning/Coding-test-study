from collections import deque

a, b = map(int, input().split())
dist = dict()

q = deque()
q.append(a)
dist[a] = 1

while q:
    now = q.popleft()
    for nxt in [2 * now, int(str(now) + "1")]:
        if 1 <= nxt <= b and not nxt in dist:
            q.append(nxt)
            dist[nxt] = dist[now] + 1

if b in dist:
    print(dist[b])
else:
    print(-1)