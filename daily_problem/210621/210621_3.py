from collections import deque
import sys

a, b, n, m = map(int, input().split())
check = dict()
q = deque()
q.append(n)
check[n] = 0

while q:
    now = q.popleft()
    for nxt in [now - 1, now + 1, now + a, now + b, now - a, now - b, a * now, b * now]:
        if 0 <= nxt <= 100000 and nxt not in check:
            q.append(nxt)
            check[nxt] = check[now] + 1
            if nxt == m:
                print(check[nxt])
                sys.exit(0)