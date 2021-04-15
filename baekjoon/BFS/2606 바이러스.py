from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False] * (n + 1)
q = deque()
q.append(1)
check[1] = True

ans = 0
while q:
    now = q.popleft()
    for next in graph[now]:
        if check[next] == False:
            ans += 1
            q.append(next)
            check[next] = True

print(ans)