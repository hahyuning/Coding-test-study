from collections import deque

n, m, x = map(int, input().split())
out_graph = [[] for _ in range(n + 1)]
in_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    out_graph[a].append(b)
    in_graph[b].append(a)

q = deque()
q.append(x)
check1 = [False] * (n + 1)
check1[x] = True
out_order = []

while q:
    now = q.popleft()
    out_order.append(now)
    for nxt in out_graph[now]:
        if not check1[nxt]:
            check1[nxt] = True
            q.append(nxt)

q = deque()
q.append(x)
check2 = [False] * (n + 1)
check2[x] = True
in_order = []

while q:
    now = q.popleft()
    in_order.append(now)
    for nxt in in_graph[now]:
        if not check2[nxt]:
            check2[nxt] = True
            q.append(nxt)

cnt = 0
for i in range(1, n + 1):
    if not check1[i] and not check2[i]:
        cnt += 1
print(len(in_order), end=" ")
print(len(in_order) + cnt)
