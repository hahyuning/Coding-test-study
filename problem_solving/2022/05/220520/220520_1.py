from collections import defaultdict, deque

n, k = map(int, input().split())
m = len(str(n))

check = defaultdict(bool)
q = deque()
q.append((str(n), 0))
check[(str(n), 0)] = True

ans = -1
while q:
    now, cnt = q.popleft()

    if cnt == k:
        ans = max(ans, int(now))
        continue

    for i in range(m - 1):
        for j in range(i + 1, m):
            x, y = now[i], now[j]

            if i == 0 and int(y) == 0:
                continue

            nxt = now[:i] + now[j] + now[i + 1:j] + now[i] + now[j + 1:]
            if not check[(nxt, cnt + 1)]:
                check[(nxt,cnt + 1)] = True
                q.append((nxt, cnt + 1))

print(ans)
