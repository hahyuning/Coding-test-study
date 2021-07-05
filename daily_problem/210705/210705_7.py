from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

check = dict()
q = deque()
for x in a:
    q.append(x)
    check[x] = 0

while q:
    if len(check.keys()) >= k + n:
        break
    now = q.popleft()
    for nxt in [now + 1, now - 1]:
        if nxt not in check:
            check[nxt] = check[now] + 1
            q.append(nxt)

ans = list(sorted(check.items(), key=lambda x:x[1]))
s = 0
for i in range(n + k):
    s += ans[i][1]
print(s)