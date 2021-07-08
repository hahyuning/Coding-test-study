import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(root):
    sub[root] = 1
    for nxt in graph[root]:
        if sub[nxt] == 0:
            dfs(nxt)
            sub[root] += sub[nxt]

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

sub = [0] * (n + 1)
dfs(r)

for _ in range(q):
    x = int(input())
    print(sub[x])