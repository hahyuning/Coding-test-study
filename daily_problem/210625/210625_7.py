from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

check = [False] * (n + 1)
q = deque()
q.append((1, 0))
check[1] = True

depth = [0] * (n + 1)
res = []
while q:
    now, d = q.popleft()
    ch = False
    for nxt in tree[now]:
        if not check[nxt]:
            ch = True
            check[nxt] = True
            depth[nxt] = d + 1
            q.append((nxt, d + 1))
    if not ch:
        res.append(now)

s = 0
for x in res:
    s += depth[x]
if s % 2 == 0:
    print("No")
else:
    print("Yes")