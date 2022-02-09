from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
back_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    back_graph[b].append((a, c))
    indegree[b] += 1
s, e = map(int, input().split())

res = [0] * (n + 1)
q = deque()
q.append(s)

while q:
    now = q.popleft()
    for nxt, nxt_cost in graph[now]:
        indegree[nxt] -= 1
        res[nxt] = max(res[nxt], res[now] + nxt_cost)
        if indegree[nxt] == 0:
            q.append(nxt)

check = [False] * (n + 1)
check[e] = True
cnt = 0
q.append(e)
while q:
    now = q.popleft()
    for nxt, nxt_cost in back_graph[now]:
        if res[now] - res[nxt] == nxt_cost:
            cnt += 1
            if not check[nxt]:
                check[nxt] = True
                q.append(nxt)

print(res[e])
print(cnt)