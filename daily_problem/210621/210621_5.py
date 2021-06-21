from collections import deque

n, m = map(int, input().split())
ss, ee = map(int, input().split())

teleport = dict()
for _ in range(m):
    s, e = map(int, input().split())
    if s in teleport:
        teleport[s].append(e)
    else:
        teleport[s] = [e]

    if e in teleport:
        teleport[e].append(s)
    else:
        teleport[e] = [s]

check = dict()
q = deque()
q.append(ss)
check[ss] = 0

while q:
    now = q.popleft()
    if now == ee:
        print(check[ee])
        break

    a = [now + 1, now - 1]
    if now in teleport:
        a += teleport[now]

    for nxt in a:
        if 1 <= nxt <= n and nxt not in check:
            q.append(nxt)
            check[nxt] = check[now] + 1
