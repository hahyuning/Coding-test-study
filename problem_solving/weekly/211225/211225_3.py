from collections import deque
import sys

n, m = map(int, input().split())
do_not_jump = [int(input()) for _ in range(m)]

if 2 in do_not_jump:
    print(-1)
    sys.exit(0)

check = dict()
check[(2, 1)] = 1
q = deque()
q.append((2, 1, 1))

while q:
    now, jump, cnt = q.popleft()

    for nxt_jump in [jump - 1, jump, jump + 1]:
        if nxt_jump >= 1:
            nxt = now + nxt_jump
            if nxt in do_not_jump:
                continue

            if nxt <= n:
                if (nxt, nxt_jump) not in check:
                    check[(nxt, nxt_jump)] = cnt + 1
                    q.append((nxt, nxt_jump, cnt + 1))
ans = -1
for x, y in check:
    if x == n:
        if ans == -1 or check[(x, y)] < ans:
            ans = check[(x, y)]
print(ans)