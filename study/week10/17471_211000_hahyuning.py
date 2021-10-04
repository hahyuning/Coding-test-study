from itertools import combinations
from collections import deque

def bfs(start, x):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if nxt in x and not check[nxt]:
                check[nxt] = True
                q.append(nxt)
    return check

n = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    m, *a = map(int, input().split())
    for j in a:
        graph[i].append(j)

total = sum(people)
ans = -1
for m in range(1, n // 2 + 1):
    all_set = combinations([i for i in range(1, n + 1)], m)

    for x1 in all_set:
        ch = True
        x2 = []
        for i in range(1, n + 1):
            if i not in x1:
                x2.append(i)

        check = bfs(x1[0], x1)
        s1 = 0
        for y in x1:
            if not check[y]:
                ch = False
                break
            s1 += people[y]

        check = bfs(x2[0], x2)
        s2 = 0
        for i in range(1, n + 1):
            if i not in x1:
                if not check[i]:
                    ch = False
                    break
                s2 += people[i]
        if ch:
            if ans == -1 or abs(s1 - s2) < ans:
                ans = abs(s1 - s2)

print(ans)