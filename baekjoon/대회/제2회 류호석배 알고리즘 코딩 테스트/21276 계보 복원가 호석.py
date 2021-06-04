from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def recursion(x):
    if x not in res:
        ans.append(x + " 0")
        return

    res[x].sort()
    ans.append(x + " " + str(len(res[x])) + " " + " ".join(res[x]))
    for y in res[x]:
        recursion(y)

n = int(input())
all = input().split()
m = int(input())
graph = defaultdict(list)
indegree = dict()

for x in all:
    indegree[x] = 0

for _ in range(m):
    a, b = input().rstrip().split()
    graph[b].append(a)
    indegree[a] += 1

q = deque()
res = defaultdict(list)
parents = []
for x, y in indegree.items():
    if y == 0:
        q.append((x, x))
        parents.append(x)

while q:
    now, parent = q.popleft()
    if now != parent:
        res[parent].append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append((nxt, now))

print(len(parents))
parents.sort()
print(" ".join(parents))
ans = []
for x in parents:
    recursion(x)
ans.sort()
for x in ans:
    print(x)
