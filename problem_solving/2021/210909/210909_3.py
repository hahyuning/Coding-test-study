import sys
sys.setrecursionlimit(10 ** 6)

# 현재 노드부터 해당 노드의 리프 노드까지의 거리의 최댓값 찾기
def dfs(now, fro):
    max_d = 0
    for nxt in tree[now]:
        if nxt != fro:
            max_d = max(max_d, dfs(nxt, now) + 1)

    dist[now] = max_d
    return dist[now]

# 리프노드까지의 거리가 d 이상인 노드들은 방문해야 함
def search(now, fro):
    global ans

    for nxt in tree[now]:
        if nxt != fro:
            if dist[nxt] >= d:
                ans += 1
                search(nxt, now)
                ans += 1
    return

n, s, d = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = 0
dist = [-1] * (n + 1)
dfs(s, 0)
search(s, 0)
print(ans)