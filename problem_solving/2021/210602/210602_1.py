from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(x):
    check = [False] * (n + 1)
    check[x] = True
    q = deque()
    q.append(x)
    cnt = 1

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not check[nxt]:
                cnt += 1
                check[nxt] = True
                q.append(nxt)
    return cnt


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = []
for i in range(1, n + 1):
    res = bfs(i)
    ans.append(res)

max_val = max(ans)
for i, x in enumerate(ans, start=1):
    if x == max_val:
        print(i, end=" ")