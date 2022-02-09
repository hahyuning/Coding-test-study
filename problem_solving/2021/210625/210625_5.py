from collections import deque

n, w = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

check = [False] * (n + 1)
q = deque()
q.append(1)
check[1] = True

cnt = 0
while q:
    now = q.popleft()
    ch = False
    for nxt in tree[now]:
        if not check[nxt]:
            ch = True
            check[nxt] = True
            q.append(nxt)
    if not ch:
        cnt += 1

print(w / cnt)