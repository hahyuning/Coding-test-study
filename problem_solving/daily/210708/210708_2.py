from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
indegree = dict()
graph = [set() for _ in range(n + 1)]
for _ in range(m):
    k, *recipe, r = map(int, input().split())
    # 시간초과
    recipe.sort()
    if r in indegree:
        indegree[r].append([set(recipe), k])
    else:
        indegree[r] = [[set(recipe), k]]

    for i in range(k):
        graph[recipe[i]].add(r)

l = int(input())
y = list(map(int, input().split()))
check = [False] * (n + 1)
ans = set()
for yy in y:
    check[yy] = True
    ans.add(yy)
q = deque(y)

while q:
    now = q.popleft()

    for nxt in graph[now]:
        if nxt in ans:
            continue
        for i in range(len(indegree[nxt])):
            cnt = indegree[nxt][i][1]
            if now in indegree[nxt][i][0]:
                indegree[nxt][i][0].remove(now)
                cnt -= 1
                indegree[nxt][i][1] = cnt

                if cnt == 0:
                    check[nxt] = True
                    ans.add(nxt)
                    q.append(nxt)

print(len(ans))
ans = sorted(list(ans))
print(*ans)
