import sys

sys.setrecursionlimit(10 ** 6)

ans = 0


def dfs(graph, a, now, prev):
    global ans

    for nxt in graph[now]:
        if nxt == prev:
            continue
        dfs(graph, a, nxt, now)

    a[prev] += a[now]
    ans += abs(a[now])


def solution(a, edges):
    graph = [[] for _ in range(len(a))]

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    dfs(graph, a, 0, -1)
    if a[0] == 0:
        return ans
    return -1