from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)
ans = [0] * (n + 1)
check = [False] * (n + 1)
check[1] = True

while q:
    parent = q.popleft()
    for x in graph[parent]:
        if not check[x]:
            ans[x] = parent
            q.append(x)
            check[x] = True

for i in range(2, n + 1):
    print(ans[i])