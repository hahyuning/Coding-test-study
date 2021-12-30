from collections import deque

s = int(input())
dist = [[-1] * 1001 for _ in range(1001)]
dist[1][0] = 0

q = deque()
q.append((1, 0))

while q:
    screen, clipboard = q.popleft()
    if dist[screen][screen] == -1:
        dist[screen][screen] = dist[screen][clipboard] + 1
        q.append((screen, screen))

    if screen + clipboard < 1001 and dist[screen + clipboard][clipboard] == -1:
        dist[screen + clipboard][clipboard] = dist[screen][clipboard] + 1
        q.append((screen + clipboard, clipboard))

    if 0 <= screen - 1 and dist[screen - 1][clipboard] == -1:
        dist[screen - 1][clipboard] = dist[screen][clipboard] + 1
        q.append((screen - 1, clipboard))

ans = -1
for x in dist[s]:
    if x != -1:
        if ans == -1 or ans > x:
            ans = x
print(ans)
