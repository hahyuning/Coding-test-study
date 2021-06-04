from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    n, *a = list(map(int, input().split()))
    for i in range(n - 1):
        graph[a[i]].append(a[i + 1])
        indegree[a[i + 1]] += 1

res = []
q = deque()

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    res.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

if len(res) == v:
    for x in res:
        print(x)
else:
    print(0)