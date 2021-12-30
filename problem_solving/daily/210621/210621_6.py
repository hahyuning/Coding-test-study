from collections import deque
import sys

a, b = map(int, input().split())
n, m = map(int, input().split())
transf = dict()
for _ in range(m):
    aa, bb = map(int, input().split())
    if aa in transf:
        transf[aa].append(bb)
    else:
        transf[aa] = [bb]
    if bb in transf:
        transf[bb].append(aa)
    else:
        transf[bb] = [aa]

q = deque()
check = dict()
q.append(a)
check[a] = 0

while q:
    now = q.popleft()
    if now == b:
        print(check[b])
        sys.exit(0)

    if now in transf:
        for nxt in transf[now]:
            if 1 <= nxt <= 1000 and nxt not in check:
                check[nxt] = check[now] + 1
                q.append(nxt)

print(-1)