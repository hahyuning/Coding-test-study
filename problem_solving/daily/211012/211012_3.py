from collections import deque

n, m = map(int, input().split())
do_not_jump = [int(input()) for _ in range(m)]

check = dict()
check[(2, 1)] = 1
q = deque()
q.append((2, 1, 1))

while q:
    now, cnt, k = q.popleft()

    for diff in [k - 1, k, k + 1]:
        if diff > 0:
            nxt = now + diff
            if nxt in do_not_jump:
                continue

            if nxt <= n:
                if (nxt, diff) not in check:
                    check[(nxt, diff)] = cnt + 1
                    q.append((nxt, cnt + 1, diff))
ans = -1
for x, y in check:
    if x == n:
        if ans == -1 or check[(x, y)] < ans:
            ans = check[(x, y)]
print(ans)